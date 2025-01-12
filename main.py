from fastapi import FastAPI
from api import router as api_router

app = FastAPI()

# Include the centralized router
app.include_router(api_router)


@app.get("/")
def head_root():
    return {"message": "Welcome to the Library Management System API"}
