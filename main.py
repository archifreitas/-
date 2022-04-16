import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv(".env")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query/")
async def query_sql():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
