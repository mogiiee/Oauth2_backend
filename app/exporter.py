from dotenv import load_dotenv
import os

load_dotenv()   

# MONGO_DETAILS = "mongodb+srv://mogiiee:mogiiee@cluster0.f8mil.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGO_DETAILS = os.environ["MONGO_DETAILS"]