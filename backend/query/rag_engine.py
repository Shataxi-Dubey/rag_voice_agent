from backend.db.vector_db import vector_store

from google import genai
from google.genai import types

from dotenv import load_dotenv

load_dotenv()

def search_query(query):
    results = vector_store.similarity_search(query=query,k=3)
    if len(results) == 0:
        return {"message": f'No results found for {query}', 'status_code': 400}
    else:
        documents = [doc.page_content for doc in results]
        return generate_answer(query,documents)

def generate_answer(query, documents):

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= f"Answer the question: {query} based only on the following context: \
                                    {documents} \
                                    Provide a detailed answer. \
                                    Dont justify your answers. \
                                    Dont give information not mentioned in the CONTEXT INFORMATION. \
                                    Do not say 'according to the context'or 'mentioned in the context' or similar.",
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)) # Disables thinking
    )

    return {"message": response.text, 'status_code': 200 }