"""
This is a principal Module FastApi
"""

from fastapi import FastAPI
from routes.user import protected_route as user
from routes.material import protected_route as material
from routes.loans import protected_route as loan
from routes.auth import auth

app = FastAPI()

app.include_router(auth, prefix="/api/auth")
app.include_router(user, prefix="/api")
app.include_router(material, prefix="/api")
app.include_router(loan, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
