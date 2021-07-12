from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from . import schema, completer, crud



app = FastAPI()

@app.get('/')
def hello():
    return {
        "greet": "Welcome to the IEEE Techloop Registration Portal."
    }

@app.post("/user_info")
async def user_info(payload: schema.Information): #check schema for payload
    # Completion
    completed_api = completer.user_info_completer(payload) #will be used for future validation

    # CRUD Function.
    crud_response = await crud.user_info_crud(completed_api) #crud to make further changes in the database
    print(crud_response)

    # Returning response
    return crud_response 
