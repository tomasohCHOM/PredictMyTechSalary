# ds-project

## Setup / Development

Open two terminal windows, in one of them, open the `api/` directory that contains the server code:

```bash
cd api
pip freeze > requirements.txt
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

## License

MIT License
