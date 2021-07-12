import motor.motor_asyncio 
from .exporter import MONGO_DETAILS

# Mongo Database
Client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Mongo DB Database Name
DB_NAME = "IEEE_phase1_db"
