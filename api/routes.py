from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from core.security import verify_token
from core.rate_limiter import check_rate_limit
from services.orchestrator import run_sector_analysis

router = APIRouter()

@router.get("/analyze/{sector}")
def analyze_sector(sector: str, token: str = Depends(verify_token)):
    # 1. Run the rate limit check
    check_rate_limit(token)
    
    # 2. Clean up the user input (lowercase it and remove extra spaces)
    clean_sector = sector.strip().lower()
    
    # Basic validation so they don't send a massive string
    if len(clean_sector) > 30:
        raise HTTPException(status_code=400, detail="Sector name is too long.")
        
    # 3. Run the analysis
    try:
        report = run_sector_analysis(clean_sector)
        # Return as plain text markdown so it looks right in the browser
        return PlainTextResponse(content=report, media_type="text/markdown")
        
    except ValueError as e:
        # Triggers if the search engine found zero results
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        # Triggers if Gemini or DuckDuckGo crashes completely
        print(f"Failed to process request: {e}")
        raise HTTPException(status_code=500, detail="Server error. Please try again later.")