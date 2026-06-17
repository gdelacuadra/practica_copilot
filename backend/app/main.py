from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .auth import authenticate_user, create_access_token, refresh_access_token
from .models import Token

app = FastAPI(title="JWT Auth API", version="1.0.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token", response_model=Token, summary="Obtain a JWT access token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate with **username** and **password** and receive a JWT token
    valid for 300 seconds.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return Token(access_token=access_token, token_type="bearer")


@app.post("/token/refresh", response_model=Token, summary="Refresh an existing JWT access token")
async def refresh_token(token: str = Depends(oauth2_scheme)):
    """
    Provide a valid JWT token and receive a new one with a fresh 300-second
    expiration window.
    """
    new_token = refresh_access_token(token)
    if not new_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=new_token, token_type="bearer")
