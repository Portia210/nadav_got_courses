from pydantic import BaseModel

class OutputToUser(BaseModel):
    output: str