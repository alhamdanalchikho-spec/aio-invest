import requests

def get_live_crypto_prices():
    """
    Fetches live cryptocurrency prices from CoinGecko.
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,apple&vs_currencies=usd,eur&include_24hr_change=true"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching crypto prices: {e}")
        # Return fallback data if API fails or rate limited
        return {
            "bitcoin": {"usd": 65000.0, "eur": 60000.0, "usd_24h_change": -2.5},
            "ethereum": {"usd": 3500.0, "eur": 3200.0, "usd_24h_change": 1.2},
            "solana": {"usd": 150.0, "eur": 138.0, "usd_24h_change": 5.0}
        }

def get_gold_prices():
    """
    Simulates or fetches live gold prices.
    Using simulated realistic data for now as free gold APIs are very limited.
    """
    # 1 Troy Ounce = 31.1034768 grams
    # 24k is pure gold
    # 21k is 21/24 purity
    base_ounce_usd = 2350.20
    eur_usd_rate = 1.08
    
    ounce_eur = base_ounce_usd / eur_usd_rate
    gram_24k_eur = ounce_eur / 31.1034768
    gram_21k_eur = gram_24k_eur * (21/24)
    
    return {
        "ounce_usd": round(base_ounce_usd, 2),
        "ounce_eur": round(ounce_eur, 2),
        "gram_24k_eur": round(gram_24k_eur, 2),
        "gram_21k_eur": round(gram_21k_eur, 2),
        "trend": "Bullish"
    }

def get_forex_rates():
    """
    Simulates live Forex rates.
    """
    return {
        "EUR_USD": {"rate": 1.0845, "change": "+0.12%"},
        "USD_JPY": {"rate": 151.20, "change": "-0.05%"},
        "GBP_USD": {"rate": 1.2630, "change": "+0.20%"}
    }
