from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend import uploader, query, voice_agent

rag_voice_agent_api = FastAPI()

rag_voice_agent_api.include_router(uploader.routes.router)
rag_voice_agent_api.include_router(query.routes.router)
rag_voice_agent_api.include_router(voice_agent.routes.router)

@rag_voice_agent_api.get("/")
async def main():
    content = """
<body>
<form action="/files/upload" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)