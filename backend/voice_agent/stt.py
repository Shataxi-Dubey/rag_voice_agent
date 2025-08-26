# receive the audio file and convert it into text 
# send this text for querying
# get the text response

import os
import tempfile
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

async def speech_to_text(audio_file):

    transcription = elevenlabs.speech_to_text.convert(
        file=audio_file.file,
        model_id="scribe_v1", # Model to use, for now only "scribe_v1" is supported
        tag_audio_events=True, # Tag audio events like laughter, applause, etc.
        language_code="eng", # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True, # Whether to annotate who is speaking
    )


    return transcription.text