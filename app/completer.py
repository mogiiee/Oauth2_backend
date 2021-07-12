from fastapi.encoders import jsonable_encoder
from datetime import datetime

def user_info_completer(payload):
    encoded_payload = jsonable_encoder(payload)
    
    current_time_obj = datetime.now()

    encoded_payload["creation_timestamp"] = current_time_obj.timestamp()

    return encoded_payload

