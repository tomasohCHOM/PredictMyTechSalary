from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle as pkl
import uvicorn
import json


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


def load_mappings():
    with open("mappings.json", "r") as fp:
        mappings = json.load(fp)
    return mappings


# Helper function for handling a range of years
def handleYears(year_range):
    if year_range == "Less than 5 years":
        return 2
    if year_range == "From 5 to 10 years":
        return 7
    if year_range == "From 11 to 20 years":
        return 12
    if year_range == "From 21 to 40 years":
        return 25
    return 42


model = load_model()
mappings = load_mappings()

app = FastAPI()


@app.post("/predict")
def predict(items: Items):
    converted_items = dict(items)
    inputs = {}
    inputs["Trans"] = 1
    inputs["Sexuality"] = 1
    inputs["Accessibility"] = 1
    for model_input, v in converted_items.items():
        if model_input == "YearsCode" or model_input == "WorkExp":
            inputs[model_input] = [handleYears(v)]
            continue
        if model_input in set(["Trans", "Sexuality", "Accessibility"]):
            continue
        if v not in mappings[model_input]:
            print(model_input, v)
            return HTTPException(status_code=422, detail="Value not present")
        inputs[model_input] = [mappings[model_input][v]]
    input_df = pd.DataFrame(inputs)
    predicted_salary = model.predict(input_df.values)
    return {"salary": predicted_salary[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
