from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI
import pandas as pd
import pickle as pkl
import uvicorn


class Items(BaseModel):
    MainBranch: str
    Employment: str
    RemoteWork: str
    EdLevel: str
    YearsCode: str
    OrgSize: str
    Country: str
    Age: str
    Gender: str
    Trans: Optional[str] = Field(None)
    Sexuality: Optional[str] = Field(None)
    Ethnicity: str
    Accessibility: Optional[str] = Field(None)
    WorkExp: str


def load_model():
    with open("model/model.pkl", "rb") as model_file:
        model = pkl.load(model_file)
    return model


model = load_model()

input_df = pd.DataFrame(
    {
        "MainBranch": [2],
        "Employment": [1],
        "RemoteWork": [1],
        "EdLevel": [1],
        "YearsCode": [2],
        "OrgSize": [1],
        "Country": [4],
        "Age": [2],
        "Gender": [1],
        "Trans": [1],
        "Sexuality": [2],
        "Ethnicity": [1],
        "Accessibility": [1],
        "WorkExp": [1],
    }
)

predicted_salary = model.predict(input_df.values)

app = FastAPI()


@app.post("/predict")
def predict(items: Items):
    return {"salary": predicted_salary[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
