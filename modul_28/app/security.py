from fastapi import Depends, status, HTTPException
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_NAME='api-key'
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
def get_api_ley(api_key: str = Depends(api_key_header)):
    allowed_api_keys = os.getenv("API_KEYS", "").split(",")
    print("Recieved API key from env variables: {}".format(api_key))
    print("Allowed API keys: {}".format(allowed_api_keys))
    if api_key not in allowed_api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    print("Allowed")
    return api_key