# techloop-reg-portal
## Set up a virtual environment for the project:
```
python3 -m venv virtualenv
```
## Activate the environment:
```
source virtualenv/bin/activate
```
## Install the dependencies:
```
pip install -r req.txt
```
## Run the API with Uvicorn:
```
uvicorn src.main:app --reload
```
## Use either swagger UI or postman to your convenience to test

* http://127.0.0.1:8000/docs go to your local host 8000/docs or 8000/redoc to access swagger
* All the post requests  are being stored in my personal mongo db as of now, once testing is done, it will be shifted to a public one
