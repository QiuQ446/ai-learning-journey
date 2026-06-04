from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """上传单个文件，返回文件名和大小"""
    content = await file.read()
    return {
        "filename": file.filename,
        "size": len(content),
        "content_type": file.content_type
    }

@app.post("/upload-multiple")
async def upload_multiple(files: List[UploadFile] = File(...)):
    """上传多个文件"""
    result = []
    for file in files:
        content = await file.read()
        result.append({
            "filename": file.filename,
            "size": len(content)
        })
    return {"files": result}