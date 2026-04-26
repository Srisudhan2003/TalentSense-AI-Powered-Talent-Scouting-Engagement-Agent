def growth_score(candidate):
    score = 50
    if candidate["experience"] < 3:
        score += 20
    if len(candidate["skills"]) > 5:
        score += 10
    return min(score,100)

def risk_score(candidate, jd):
    missing = set(jd["skills"]) - set(candidate["skills"])
    return min(len(missing)*10,100)
