from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


@app.get("/")
def read():
    return {"salary": 100000}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
