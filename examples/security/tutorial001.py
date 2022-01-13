import citus

from citus.security import OAuth2PasswordBearer

app = citus.App()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = citus.Depends(oauth2_scheme)):
    return {"token": token}
