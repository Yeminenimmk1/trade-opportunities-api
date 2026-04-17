from fastapi import Header, HTTPException
import os

def verify_token(authorization: str = Header(None)):
    # Check if they even sent a token
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    
    # Get the expected token from the .env file
    expected_token = f"Bearer {os.getenv('AUTH_TOKEN', 'secret123')}"
    
    # Kick them out if it doesn't match
    if authorization != expected_token:
        raise HTTPException(status_code=401, detail="Invalid token")
        
    return authorization