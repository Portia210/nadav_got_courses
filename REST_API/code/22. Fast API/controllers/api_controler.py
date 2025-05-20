from fastapi import APIRouter, Request
from models.input_from_user import InputFromUser
from models.output_to_user import OutputToUser
router = APIRouter()



@router.get("/")
def home(request: Request):
    return "This is home page " + request.app.state.first_name

@router.get("/{name}")
def name(name):
    return "Your name is " + name


# how to take models to as input or output
@router.get("/inputfromuser", response_model=OutputToUser)
def input(input_from_user: InputFromUser):
    return "Input Page"