def final_score(match, interest, growth, risk):
    
    if match > 75:
        weight = 0.7   # strong skill match → prioritize match
    elif match > 50:
        weight = 0.5   # balanced
    else:
        weight = 0.3   # weak match → consider growth more

    growth_boost = 0
    if growth > 70:
        growth_boost = 5

    risk_penalty = risk * 0.2

    score = (
        weight * match +
        0.2 * interest +
        0.2 * growth +
        growth_boost -
        risk_penalty
    )

    return round(score, 2)