from fastapi import FastAPI, HTTPException
import calculatorrouter as calculator
from database import init_db, save_user_with_payment, get_user_payment_info
from models import UserCreate, UserLogin
from auth import register_user, authenticate_user
from datetime import datetime

app = FastAPI(title="Membership Calculator")

# Ensure DB exists
init_db()

# Include calculator router
app.include_router(calculator.router, prefix="/api")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# --------------------
# Auth Endpoints
# --------------------

@app.post("/register")
def register(user: UserCreate):
    """
    Original register endpoint - keeps backward compatibility
    """
    success = register_user(user.username, user.password, user.membership)
    if not success:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"message": f"User {user.username} registered successfully"}

@app.post("/register-with-payment")
def register_with_payment(user_data: dict):
    """
    New endpoint that handles registration with payment information
    """
    try:
        username = user_data.get("username")
        password = user_data.get("password")
        membership = user_data.get("membership")
        payment_data = user_data.get("payment_data", {})

        # Validate required fields
        if not all([username, password, membership]):
            raise HTTPException(status_code=400, detail="Missing required user fields")

        required_payment_fields = [
            "card_number", "cardholder_name", "expiry_month",
            "expiry_year", "cvv", "street_address", "city",
            "state", "zip_code"
        ]

        missing_fields = [field for field in required_payment_fields if field not in payment_data]
        if missing_fields:
            raise HTTPException(status_code=400, detail=f"Missing payment fields: {missing_fields}")

        # Save user with payment information
        user_id, error = save_user_with_payment(username, password, membership, payment_data)

        if not user_id:
            raise HTTPException(status_code=400, detail=error or "Registration failed")

        return {
            "message": f"User {username} registered successfully with payment",
            "user_id": user_id
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/login")
def login(user: UserLogin):
    auth_user = authenticate_user(user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Get payment info for the user (optional)
    payment_info = get_user_payment_info(user.username)

    return {
        "token": auth_user["username"],
        "membership": auth_user["membership"],
        "has_payment_info": payment_info is not None
    }

@app.get("/user/{username}/payment-info")
def get_payment_info(username: str):
    """
    Get payment information for a specific user
    """
    payment_info = get_user_payment_info(username)
    if not payment_info:
        raise HTTPException(status_code=404, detail="No payment information found")

    # Mask sensitive information for security
    if payment_info:
        # Mask card number (show only last 4 digits)
        card_number = payment_info.get('card_number', '')
        if len(card_number) >= 4:
            payment_info['card_number'] = '**** **** **** ' + card_number[-4:]
        # Remove CVV from response
        payment_info.pop('cvv', None)

    return payment_info
@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}