def get_real_estate_portfolio():
    """
    Returns mock data for the Real Estate portfolio (Fractional ownership & REITs).
    """
    return [
        {
            "id": "RE-001",
            "name": "Dubai Marina Apartment (Fractional)",
            "location": "Dubai, UAE",
            "type": "Fractional Real Estate",
            "risk": "Low",
            "expected_yield": "7.5% Annual",
            "status": "Generating Passive Income"
        },
        {
            "id": "RE-002",
            "name": "Madrid Tourist Flat",
            "location": "Madrid, Spain",
            "type": "Direct Investment",
            "risk": "Minimal",
            "expected_yield": "8.2% Annual",
            "status": "Fully Booked (High Demand)"
        },
        {
            "id": "REIT-001",
            "name": "Global Healthcare Properties REIT",
            "location": "Global",
            "type": "REIT",
            "risk": "Low",
            "expected_yield": "5.1% Annual",
            "status": "Stable Dividend Payouts"
        }
    ]

def get_startup_opportunities():
    """
    Returns mock data for Startups and Venture Capital opportunities.
    """
    return [
        {
            "id": "VC-001",
            "name": "EcoTech Solutions AI",
            "sector": "Green Energy / AI",
            "stage": "Seed",
            "risk": "High",
            "potential_return": "10x - 50x",
            "integrity_check": "Founders Verified. Solid MVP."
        },
        {
            "id": "VC-002",
            "name": "DeFi lending Protocol X",
            "sector": "Web3 / Finance",
            "stage": "Series A",
            "risk": "Extreme",
            "potential_return": "100x",
            "integrity_check": "Smart Contracts Audited. High competition."
        },
        {
            "id": "VC-003",
            "name": "MedBotics",
            "sector": "Healthcare Robotics",
            "stage": "Pre-IPO",
            "risk": "Medium",
            "potential_return": "2x - 3x on IPO",
            "integrity_check": "FDA Pending. Strong institutional backing."
        }
    ]
