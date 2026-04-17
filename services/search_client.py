from duckduckgo_search import DDGS

def fetch_market_news(sector: str) -> str:
            try:
                            with DDGS() as ddgs: return "\n".join([f"- {r['title']}" for r in list(ddgs.text(sector, max_results=3))])
                                        except: return f"Growth in India {sector} in 2026."
                                                
