''' 
streamlit app with \
1. Add a button for File upload \
2. File upload will enter the chunks in the vector database \
3. Upload speech file and get its transcription \
4. Use the transcription as query and find the relevant chunks and generate the response\
5. Convert the response to audio \
6. Add a button for playing the audio \
'''

import os
import requests
import io

import streamlit as st

host = os.getenv("BACKEND_HOST", "localhost")
port = os.getenv("BACKEND_PORT", 8000)

url = f"http://{host}:{port}"

# Upload the PDF file and prepare its chunk
uploaded_files = st.file_uploader(
    "Choose a PDF file", accept_multiple_files=True
)
if uploaded_files and "db_ready" not in st.session_state:
    files = [("files", (f.name, f, "application/pdf")) for f in uploaded_files]

    msg = requests.post(f'{url}/files/upload', files=files)
    msg = msg.json()
    if msg['status_code'] == 200:
        st.success("Files uploaded and processed successfully!")
        st.session_state.db_ready = True


# Generate Query in Audio Format
if "db_ready" in st.session_state and len(uploaded_files):

    audio_file = st.file_uploader(
        "Ask question by uploading an audio file", accept_multiple_files=False
    )
        
    st.write("OR")

    audio_value = st.audio_input("Record a voice message")
        
    if audio_file is not None: 
        file_bytes = audio_file.read()
        file_bytes = io.BytesIO(file_bytes)
        file = {"audio_file": (audio_file.name, file_bytes, audio_file.type)}
        msg = requests.post(f'{url}/audio/upload', files=file)

    if audio_value is not None:
        file_bytes = audio_value
        file = {"audio_file": ("tmp.wav", file_bytes, audio_value.type)}
        msg = requests.post(f'{url}/audio/upload', files=file)



    if (audio_file is not None) or (audio_value is not None ):
        
        msg = msg.json()
        if msg['status_code'] == 200:
            st.success("Audio Files uploaded and processed successfully!")
            query = msg['message']
            st.write(f"Your Query is : {query}")

            answer = requests.get(f'{url}/user/query', params = {"q": query})
            answer = answer.json()
            if answer['status_code'] == 200:
                answer = answer['message']
                st.write(f"Answer is : {answer}")

                audio_response = requests.post(f'{url}/audio/generate_speech', params = {"text": answer})
                if audio_response.status_code == 200:
                    st.audio(audio_response.content, format="audio/mpeg")

                else:
                    st.write('Something is wrong in generating audio')
            else:
                st.write(f"Answer is : {answer['message']}")
        

        else:
            st.write('Something is wrong')

    else:
        st.warning("Please upload an audio file to ask a question.")




