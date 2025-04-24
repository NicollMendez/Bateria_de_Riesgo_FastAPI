import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {".xlsx", ".csv"}  # Extensiones permitidas

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_extension = os.path.splitext(file.filename)[1]  # Obtener la extensión del archivo

    # Validar la extensión del archivo
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed. Only .xlsx and .csv are accepted.")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return JSONResponse(content={"filename": file.filename, "path": file_path})

ALLOWED_EXTENSIONS = {".xlsx", ".csv"}  # Extensiones permitidas

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_extension = os.path.splitext(file.filename)[1]  # Obtener la extensión del archivo

    # Validar la extensión del archivo
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed. Only .xlsx and .csv are accepted.")

    # Guardar el archivo si es válido
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return JSONResponse(content={"filename": file.filename, "path": file_path})
