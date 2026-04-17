from services.search_client import fetch_market_news
from services.llm_client import generate_trade_report

def run_sector_analysis(sector: str) -> str:
    # 1. Get the data from the internet
    news_data = fetch_market_news(sector)
    
    if not news_data:
        raise ValueError(f"Could not find any recent news for the '{sector}' sector.")
        
    # 2. Pass that data to Gemini to write the report
    markdown_report = generate_trade_report(news_data, sector)
    
    return markdown_report