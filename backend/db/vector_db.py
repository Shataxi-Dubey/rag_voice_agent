import os
import io
import fitz  # PyMuPDF
import camelot
from dotenv import load_dotenv

from PIL import Image


from langchain.schema import Document
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from google import genai
from google.genai.types import HttpOptions



load_dotenv()

host = os.getenv("QDRANT_HOST", "localhost")
port = os.getenv("QDRANT_PORT", 6333)

url = f"http://{host}:{port}"
client = QdrantClient(url)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

client.recreate_collection(
    collection_name="rag_collection",
    vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="rag_collection",
    embedding=embeddings,
)

def extract_paragraphs(pdf_path):
    """Extract paragraph-like text blocks using PyMuPDF."""
    doc = fitz.open(pdf_path)
    paragraphs = []

    for page_num, page in enumerate(doc[:3], start=1):
        blocks = page.get_text("blocks")  # list of (x0, y0, x1, y1, text, block_no, block_type)
        for id, block in enumerate(blocks):
            text = block[4].strip()
            if len(text.split()) > 5:  # filter very short blocks (likely headers/labels)
                paragraphs.append(
                    Document(
                        page_content=text,
                        metadata={"type": "paragraph", "page": page_num, "para_num": id}
                    )
                )
    return paragraphs


def extract_figures(pdf_path):
    """Extract figure placeholders (images) using PyMuPDF."""
    doc = fitz.open(pdf_path)
    figures = []

    for page_num, page in enumerate(doc[:3], start=1):
        images = page.get_images(full=True)
        for img_index, img in enumerate(images, start=1):
            xref = img[0]  # reference id
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]  # raw image bytes
            image = Image.open(io.BytesIO(image_bytes))  # open image with PIL

            # generate description of the image
            
            client = genai.Client(http_options=HttpOptions(api_version="v1"))
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    image,
                    "Write the description of the image in plain text format in 20 words"
                ],
            )
            print(response.text)
        
            figures.append(
                Document(
                    page_content= response.text,
                    metadata={"type": "figure", "page": page_num, "image_index": img_index}
                )
            )
    return figures


def extract_tables(pdf_path):
    """Extract tables using Camelot."""
    tables = camelot.read_pdf(pdf_path, pages="all")
    docs = []

    for i, table in enumerate(tables):
        df = table.df 
        markdown_table = df.to_markdown(index=False)
        docs.append(
            Document(
                page_content=markdown_table,
                metadata={"type": "table", "table_index": i}
            )
        )
    return docs


def extract_pdf_content(pdf_path):
    paragraphs = extract_paragraphs(pdf_path)
    figures = extract_figures(pdf_path)
    tables = extract_tables(pdf_path)

    return paragraphs + figures + tables

# This function should handle the insertion of chunks into the database.
def insert_chunks(file_paths):

    total_pages = []
    for file_path in file_paths:

        if os.path.basename(file_path).endswith(".pdf"):
            total_pages += extract_pdf_content(file_path)

        if os.path.basename(file_path).endswith(".txt"):
            loader = TextLoader(file_path)
            pages = loader.load()
            total_pages += pages

        # pages is a list and pages[0].page_content contains the text of the page
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        chunks = text_splitter.split_documents(total_pages)

    num = 30
    documents = []
    for chunk in chunks[:num]:
        document = Document(page_content=chunk.page_content, metadata=chunk.metadata)
        documents.append(document)

    ids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=ids)

    # exception handling if documents could not be added in vector database

    return {"message": f"{len(chunks[:num])} Chunks inserted", "status_code": 200}