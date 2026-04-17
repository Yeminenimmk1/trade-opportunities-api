from fastapi import HTTPException
import time

# Storing sessions in memory. Format: {"token": {"count": 1, "start_time": 17000000}}
SESSION_STORE = {}

def check_rate_limit(token: str):
    current_time = time.time()
    
    # If this is a new user, add them to our dictionary
    if token not in SESSION_STORE:
        SESSION_STORE[token] = {"count": 1, "start_time": current_time}
        return

    user_data = SESSION_STORE[token]
    
    # Reset their limit if a full minute (60 seconds) has passed
    if current_time - user_data["start_time"] > 60:
        user_data["count"] = 1
        user_data["start_time"] = current_time
    else:
        # Increase their request count
        user_data["count"] += 1
        
        # Block them if they hit the endpoint more than 5 times in a minute
        if user_data["count"] > 5:
            raise HTTPException(
                status_code=429, 
                detail="Too many requests. Please wait a minute."
            )