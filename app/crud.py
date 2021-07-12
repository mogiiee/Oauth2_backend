from . import database

async def user_info_crud(payload):
    database_instance = database.Client.get_database("IEEE_phase1_db")
    collection = database_instance["test2"]
    try:
        inserted = await collection.insert_one(payload)
    except Exception as e:
        raise Exception(str(e))

    return {

        "status": True,
        "response": "Inserted.",
        "metadata": {
            "_id": str(payload["_id"])
        }
        
    }
