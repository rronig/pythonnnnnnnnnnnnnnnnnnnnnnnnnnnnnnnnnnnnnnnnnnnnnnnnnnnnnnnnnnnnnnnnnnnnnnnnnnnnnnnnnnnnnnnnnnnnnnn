# models.py - Add this new model
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    membership: str

class UserLogin(BaseModel):
    username: str
    password: str

class PaymentInfo(BaseModel):
    card_number: str
    cardholder_name: str
    expiry_month: str
    expiry_year: str
    cvv: str
    street_address: str
    city: str
    state: str
    zip_code: str

class UserWithPayment(UserCreate):
    payment_data: PaymentInfo

class CalcRequest(BaseModel):
    operation: str
    a: float
    b: float