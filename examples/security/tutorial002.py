from typing import Optional

import citus
from citus.security import OAuth2PasswordBearer

app = citus.App()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(citus.Base):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = citus.Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = citus.Depends(get_current_user)):
    return current_user
