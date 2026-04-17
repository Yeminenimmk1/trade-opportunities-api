import os
from google import genai
from datetime import datetime  # <-- NEW: Import this to get the date

def generate_trade_report(market_data: str, sector: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from your .env file!")

    # 1. Get today's date in a nice format (e.g., April 17, 2026)
    current_date = datetime.now().strftime("%B %d, %Y") # <-- NEW: Calculate the date

    client = genai.Client(api_key=api_key)
    model_id = "gemini-flash-latest"
    
    # 2. Tell the AI what today's date is in the prompt
    prompt = f"""
    Today's Date: {current_date} 
    
    You are a professional healthcare and trade analyst. 
    Analyze the following recent data for the {sector} sector in India:
    
    {market_data}
    
    Write a detailed Market Analysis and Outbreak Prediction report.
    Ensure the report explicitly mentions today's date and reflects 2026 timelines.
    Format the response in clear Markdown with headings and bullet points.
    """
    
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini error: {e}")
        raise e