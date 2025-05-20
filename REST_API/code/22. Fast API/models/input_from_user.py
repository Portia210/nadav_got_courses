from pydantic import BaseModel

class InputFromUser(BaseModel):
    name: str
    age: int