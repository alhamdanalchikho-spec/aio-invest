def check_investment_integrity(asset_data):
    """
    The Alouch Integrity Engine - Sixth Sense.
    Analyzes asset data to determine its safety and trustworthiness.
    """
    integrity_score = 100
    details = []

    # 1. Transparency Check
    if not asset_data.get('founders_verified', True):
        integrity_score -= 30
        details.append("⚠️ Founders are not fully verified.")

    # 2. Vague or Unrealistic API/Promises check (Lie Detector)
    promises = asset_data.get('daily_return_promise', 0)
    if promises > 1.0: # Anything promising > 1% daily is highly suspicious
        integrity_score -= 50
        details.append("❌ Suspiciously high daily returns promised (>1%).")

    # 3. Liquidity/Distribution Check
    top_holder_share = asset_data.get('top_holder_share', 0)
    if top_holder_share > 40:
        integrity_score -= 20
        details.append("⚠️ Liquidity is too concentrated (Top holder > 40%).")

    if integrity_score < 50:
        status = "❌ REJECTED: Highly suspicious investment."
    elif integrity_score < 80:
        status = "⚠️ WARNING: High Risk, proceed with caution."
    else:
        status = "✅ VERIFIED: Asset meets AIO Invest standards."

    return {
        "score": integrity_score,
        "status": status,
        "details": details
    }
