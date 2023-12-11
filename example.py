from fastapi import FastAPI, Depends
from fastapi_oauth_client import verify_token, auth_router
from starlette.middleware.sessions import SessionMiddleware
import secrets


app = FastAPI(

    title="FastAPI",
    version="1.0.0",
    description="Description of your app.",
    openapi_tags={},
)

# Integrate the login endpoints
app.add_middleware(SessionMiddleware, secret_key=secrets.token_urlsafe(16))
app.include_router(auth_router)

@app.get("/protected_endpoint")
def doSomething(profile=Depends(verify_token(roles=["admin"]))):
    return profile