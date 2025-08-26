import os
import tempfile


async def create_temporary_file(files):

    tmp_files = []
    for file in files:
        suffix = os.path.splitext(file.filename)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
            tmp_files.append(tmp_path)
    
    return tmp_files