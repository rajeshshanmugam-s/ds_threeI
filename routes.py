import uvicorn
from fastapi import UploadFile
from fastapi import FastAPI, File, UploadFile
import aiofiles

from ds_clinet import main

app = FastAPI()

@app.post("/")
async def post_endpoint(in_file: UploadFile=File(...)):
    # ...
    async with aiofiles.open('data/sample.wav', 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write
    response = main('data/sample.wav')
    return {"transcript": response}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

