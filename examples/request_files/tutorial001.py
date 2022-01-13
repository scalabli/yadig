import citus

app = citus.App()


@app.post("/files/")
async def create_file(file: bytes = citus.File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: citus.UploadFile = citus.File(...)):
    return {"filename": file.filename}
