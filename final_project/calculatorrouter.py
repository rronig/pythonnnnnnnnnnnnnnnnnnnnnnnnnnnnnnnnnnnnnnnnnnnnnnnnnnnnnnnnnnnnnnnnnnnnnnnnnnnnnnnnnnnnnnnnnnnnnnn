from fastapi import APIRouter, Depends, HTTPException, Header
from models import CalcRequest
from auth import authenticate_user_by_username
from fastapi import Header

router = APIRouter()

# Use username token without re-checking password
def get_current_user(token: str = Header(...)):
    # Get user by username only
    user = authenticate_user_by_username(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user

@router.post("/calculate")
def calculate(data: CalcRequest, user=Depends(get_current_user)):
    membership = user["membership"]
    op = data.operation.lower()
    a, b = data.a, data.b

    # Permission logic
    if membership == "Quid" and op != "add":
        raise HTTPException(403, "Quid members can only do addition")
    if membership == "Pro" and op not in ["add", "subtract"]:
        raise HTTPException(403, "Pro members can only do addition and subtraction")
    # Quo can do anything

    # Perform operation
    try:
        if op == "add":
            result = a + b
        elif op == "subtract":
            result = a - b
        elif op == "multiply":
            result = a * b
        elif op == "divide":
            result = a / b
        else:
            raise HTTPException(400, "Operation not supported")
        return {"result": result}
    except Exception as e:
        raise HTTPException(400, str(e))