import citus

app = citus.App()


@app.get("/headers-and-object/")
def get_headers(response: citus.Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}
