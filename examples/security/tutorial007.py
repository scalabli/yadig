import secrets
import citus

from citus.security import HTTPBasic, HTTPBasicCredentials

app = citus.App()

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = citus.Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "123456")
    if not (correct_username and correct_password):
        raise citus.HTTPException(
            status_code=citus.status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/users/me")
def read_current_user(username: str = citus.Depends(get_current_username)):
    return {"username": username}
