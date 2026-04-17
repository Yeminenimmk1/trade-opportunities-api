from fastapi import FastAPI
from api.routes import router
from dotenv import load_dotenv

# Load our API keys
load_dotenv()

app = FastAPI(title="Trade Opportunities API")

# Plug in the routes we made
app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running. Try sending a GET request to /analyze/pharmaceuticals"}