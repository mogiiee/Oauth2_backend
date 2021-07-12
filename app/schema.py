from pydantic import BaseModel

# Route schema for Item.
class Information(BaseModel):
    name: str
    email: str = None
    phone_number: int
    info: str = None