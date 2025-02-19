from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI(title="User Management API")

app.include_router(auth.router, tags=["authentication"])
app.include_router(users.router, tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API"}