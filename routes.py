from fastapi import UploadFile
from fastapi import FastAPI, File, UploadFile
import aiofiles

app = FastAPI()

@app.post("/")
async def post_endpoint(in_file: UploadFile=File(...)):
    # ...
    async with aiofiles.open('data/sample.wav', 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write

    return {"Result": "OK"}

