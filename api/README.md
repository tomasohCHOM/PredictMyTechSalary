# PredictMyTechSalary API

The `api/` directory contains code for both the FastAPI server and developing 
the model. The API code consists of `main.py`, which loads `model/model.pkl` at 
runtime to have access to the predictor model.

You can open this directory via `cd api`.

The scripts `clean.py` and `model.py` are used for cleaning the `data/datcopy.csv` 
file and developing the predictor model. You can run them one after the other:

```bash
python3 clean.py
python3 model.py
```

(The `data/datcopy.csv` file was ignored from the repository because of its size, 
but it should be included if running `clean.py`).

You should end up with a `model.pkl` file inside the `model/` directory, as well 
as a `mappings.json` for the factorization for each column value in the csv.

## Setup / Development

To start a local FastAPI server, run the following in the terminal:

```bash
pip install -r requirements.txt
python3 main.py
```

(Note: a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) 
is recommended, though not required).

The API will be available at `localhost:8000`. You can access the 
self-generated documentation via `localhost:8000/docs`.

## Resources

- [FastAPI](https://fastapi.tiangolo.com/)
