from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI
import pickle as pkl
import uvicorn


class Items(BaseModel):
    main_branch: str
    employment: str
    remote_work: str
    years_code: str
    org_size: str
    country: str
    age: str
    gender: str
    trans: Optional[str]
    sexuality: Optional[str]
    ethnicity: str
    accessibility: Optional[str]
    work_exp: str


def load_model():
    with open("model/model.pkl", "rb") as model_file:
        model = pkl.load(model_file)
    return model


app = FastAPI()


@app.get("/predict")
def predict(items: Items):
    return {"salary": 100000}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
