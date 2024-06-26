# PredictMyTechSalary

Predict My Tech Salary is a data science project that focuses on the impact that demographic data 
has on the compensation of employees in the technical industry. The goal of this project is to develop 
a model that predicts a yearly salary given arbitrary parameters, such as ethnicity, gender, age, education 
level, and accessibility. This data science project is a part of the Project ACCESS Summer 2024 Research 
Program with the overarching goal of raising awareness of emerging social justice issues in STEM.

Please visit [this page](https://predictmytechsalary.vercel.app/about) for more info regarding this project!

## Setup / Development

Open two terminal windows, in one of them, open the `api/` directory that contains the server code:

```bash
pip install -r requirements.txt
cd api
python3 main.py
```

(Note: a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) 
is recommended, though not required).

In the other terminal, open the `frontend/` directory that contains the client-side code:

```bash
cd frontend
npm install
npm run dev
```

Make sure that you have Node.js installed on your machine.

(Before making requests to the server, ensure that you create a `.env` inside `frontend/` and 
it contains this value):

```
PUBLIC_API_URL="http://localhost:8000"
```

This will connect the frontend application with the API.

## License

MIT License
