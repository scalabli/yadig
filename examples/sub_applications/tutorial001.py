import citus

app = citus.App()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


subapi = citus.App()


@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}


app.mount("/subapi", subapi)
