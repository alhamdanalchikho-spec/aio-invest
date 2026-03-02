from market_data import get_live_crypto_prices

def run_sniper_algorithm():
    """
    The Alouch Sniper Algorithm V2.
    Monitors market data for significant dips to find optimal entry points.
    """
    market_data = get_live_crypto_prices()
    
    # Sniper Logic: Look for coins that have dropped significantly in the last 24h
    # In a real scenario, this would check order books and lower timeframes (e.g. 15m RSI)
    
    opportunities = []
    
    for asset, data in market_data.items():
        # Handle cases where the API returns None instead of a float/number
        change_24h = data.get("usd_24h_change")
        if change_24h is None:
            change_24h = 0.0
            
        current_price = data.get("usd", 0)
        
        # SNIPER TRIGGER: Drop of more than 5% or specific price levels
        if change_24h < -5.0:
            opportunities.append({
                "asset": asset.upper(),
                "price": current_price,
                "status": "🎯 SNIPER ALERT: Severe Dip",
                "action": "STRONG BUY",
                "drop_percentage": round(change_24h, 2)
            })
        elif change_24h < -2.0:
             opportunities.append({
                "asset": asset.upper(),
                "price": current_price,
                "status": "⚠️ WATCHING: Approaching Buy Zone",
                "action": "ACCUMULATE",
                "drop_percentage": round(change_24h, 2)
            })
             
    # Fallback if no dips found to show the scanning state
    if not opportunities:
        return {
            "status": "Scanning Market (No major dips detected)",
            "best_opportunity": "Waiting for Volatility",
            "active_alerts": []
        }
        
    # Sort by the biggest drop
    opportunities.sort(key=lambda x: x["drop_percentage"])
    
    return {
        "status": f"Sniper Active! Found {len(opportunities)} opportunities.",
        "best_opportunity": f"{opportunities[0]['asset']} @ ${opportunities[0]['price']:,.2f}",
        "active_alerts": opportunities
    }
