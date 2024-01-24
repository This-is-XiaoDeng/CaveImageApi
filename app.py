from pathlib import Path
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

from fastapi.responses import FileResponse, JSONResponse

load_dotenv()
app = FastAPI()

@app.route("/")
async def index(request: Request) -> JSONResponse:
    data = {}
    for file in os.listdir(os.environ["SOURCE"]):
        data[file] = f"https://sgimg.thisisxd.top/{file}"
    return JSONResponse(data)

@app.route("/{file}")
async def get_file(request: Request) -> FileResponse:
    return FileResponse(Path(os.environ["SOURCE"]).joinpath(request.path_params.get("file")))

