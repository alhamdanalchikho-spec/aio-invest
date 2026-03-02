from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

# Import our custom modules
from market_data import get_live_crypto_prices, get_gold_prices, get_forex_rates
from sniper_engine import run_sniper_algorithm
from portfolio import get_real_estate_portfolio, get_startup_opportunities
from integrity_engine import check_investment_integrity

app = FastAPI(title="AIO Invest - Alpha Command Center API")

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to AIO Invest Alpha Core"}

@app.get("/api/market")
def get_market_overview():
    """
    Returns a unified overview of all market sectors: Crypto, Gold, Forex.
    """
    crypto_data = get_live_crypto_prices()
    gold_data = get_gold_prices()
    forex_data = get_forex_rates()
    
    return {
        "timestamp": time.time(),
        "crypto": crypto_data,
        "gold": gold_data,
        "forex": forex_data
    }

@app.get("/api/sniper")
def get_sniper_status():
    """
    Runs the sniper algorithm to find market dips and opportunities.
    """
    return run_sniper_algorithm()


@app.get("/api/portfolio")
def get_portfolio_data():
    """
    Returns the alternative investment portfolio (Real Estate & Startups).
    """
    return {
        "real_estate": get_real_estate_portfolio(),
        "startups": get_startup_opportunities()
    }


@app.post("/api/integrity_check")
def verify_asset(asset_data: dict):
    """
    Runs the Sixth Sense Integrity Engine on provided asset data.
    """
    result = check_investment_integrity(asset_data)
    return result

if __name__ == "__main__":
    import uvicorn
    # Make sure to run the server from the `backend` directory
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
