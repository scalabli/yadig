import citus

from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = citus.App()


security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = citus.Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
