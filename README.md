# Authorization and Authentication for FastAPI Applications

This repository provides an example package that facilitates token-based authentication and authorization within your FastAPI application.

## Overview

This package enhances your FastAPI application by incorporating token-based authentication and authorization mechanisms.

**Key Features**:

- Addition of two endpoints, `/login` and `/callback`, implementing the standard OAuth / OpenID connect flow via a web browser.

- Users authenticate through the `/login` endpoint, which redirects them to the Identity Provider (IdP), such as Keycloak, for login.

- Upon successful login, users are returned to the FastAPI app with an access token obtained from the IdP.

With the obtained access token, your FastAPI app gains the ability to access protected endpoints. This token remains valid for machine-to-machine communication until its expiration.

## Implementation Steps

To integrate this package into your FastAPI app, follow these steps:

1. Configure OAuth settings by setting the necessary environment variables. Refer to the [example.env](example.env) file. For testing purposes, update settings in that, and run FastAPI using the command: `sh ./run.sh`.

2. Incorporate the login endpoints into your code:

```python
from mvv.auth.fastapi import auth_router, verify_token
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI
import secrets

app = FastAPI(

    title="Your App Name",
    version="1.0.0",
    description="Description of your app.",
    openapi_tags={},
)

# Integrate the login endpoints
app.add_middleware(SessionMiddleware, secret_key=secrets.token_urlsafe(16))
app.include_router(auth_router)

```

3. Secure your endpoints using the access token:

```python
from mvv.auth.fastapi import auth_router, verify_token
from fastapi import Depends, FastAPI
import secrets
from starlette.middleware.sessions import SessionMiddleware
app = FastAPI(
    title="Your App Name",
    version="1.0.0",
    description="Description of your app.",
    openapi_tags={},

)

# Integrate the login endpoints
app.add_middleware(SessionMiddleware, secret_key=secrets.token_urlsafe(16))
app.include_router(auth_router)

@app.get("/protected_endpoint")
def doSomething(profile= Depends(verify_token(roles=["admin"]))):
    """
    Docstring...
    """

    return "OK"

```

Note: It's crucial to declare the 'SessionMiddleware'. This declaration enables FastAPI app to extract the Bearer token from the incoming request.

## Keycloak Configuration

Before proceeding, ensure you've configured a client in Keycloak. Assuming this is done, follow these steps to extend token lifetime:

1. **Realm Settings**: Navigate to the realm settings in the Keycloak administration console. Access the "Sessions" tab and extend the session lifetime as shown:

![Realm Settings](img/realm_settings.png)

2. **Adjust Client Settings**: Next, extend the token lifetime for the specific client. Select the client and head to the "Advanced" settings tab:

![Client Settings 1](img/client_settings_1.png)
![Client Settings 2](img/client_settings_2.png)

## Accessing Protected Endpoints

To access protected endpoints, include the `Authorization` header in your 
requests. Provide the Bearer token obtained after login:

```http

GET /protected_endpoint HTTP/1.1

Host: your-api-host

Authorization: Bearer ey...

```

## Log Level

This package uses Loguru for logging. To adjust its loglevel, use the environment variable ``LOG_LEVEL``.



# how to start the project

1. step:    python -m venv ./venv   ( maybe you need the current version like python3 -m venv ./venv )
2. step:    source venv/bin/activate
3. step:    pip install -r requirements.txt  (you can ignore the pip version)
4. step:    sh ./run.sh
5. step:    copy the URL / klick on the URL
6. step:    then add the following http://127.0.0.1:8000/login
7. step:    you will have to type in your name and password and then you go!!! 