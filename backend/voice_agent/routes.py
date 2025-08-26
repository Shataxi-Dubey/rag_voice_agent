# temporary record audio file
# send it to the stt endpoint

# get the text response
# send the text to the tts endpoint


from typing import Annotated

from fastapi import File, UploadFile, APIRouter
from fastapi.responses import StreamingResponse

from .stt import speech_to_text
from .tts import text_to_speech

router = APIRouter(
    prefix="/audio",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)

@router.post("/upload")
async def upload_files(
    audio_file: Annotated[
        UploadFile, File(description="Audio file as UploadFile")
    ],
):
    # call stt

    text = await speech_to_text(audio_file)
    return {"message": text, 'status_code': 200}

@router.post('/generate_speech')
def generate_speech(text: str):
    # call tts
    audio = text_to_speech(text)
    return StreamingResponse(audio, media_type="audio/mpeg")
