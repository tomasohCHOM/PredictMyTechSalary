from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI, HTTPException
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
    Trans: str
    Sexuality: str
    Ethnicity: str
    Accessibility: str
    WorkExp: str


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


def load_model():
    with open("model/model.pkl", "rb") as model_file:
        model = pkl.load(model_file)
    return model


def load_mappings():
    with open("mappings/mappings.json", "r") as fp:
        mappings = json.load(fp)
    return mappings


model = load_model()
mappings = load_mappings()

app = FastAPI()


@app.get("/")
def entry():
    return {"salary": 100000.0}


@app.post("/predict")
def predict(items: Items):
    converted_items = dict(items)
    inputs = {}

    for mapping_key in mappings.keys():
        if mapping_key in set(["YearsCode", "WorkExp"]):
            inputs[mapping_key] = [handleYears(converted_items[mapping_key])]
            continue
        if converted_items[mapping_key] not in mappings[mapping_key]:
            print(mapping_key, converted_items[mapping_key])
            return HTTPException(status_code=422, detail="Value not present")
        inputs[mapping_key] = [mappings[mapping_key][converted_items[mapping_key]]]

    input_values = [[input_value[0] for input_value in inputs.values()]]
    predicted_salary = model.predict(input_values)

    return {"salary": predicted_salary[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
