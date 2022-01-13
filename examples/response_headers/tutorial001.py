import citus


app = citus.App()


@app.get("/headers/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return citus.responses.JSONResponse(content=content, headers=headers)
