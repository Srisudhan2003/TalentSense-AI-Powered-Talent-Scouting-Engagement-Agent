def explain(candidate, jd):
    matched = set(candidate["skills"]) & set(jd["skills"])
    missing = set(jd["skills"]) - set(candidate["skills"])
    return f"Matched: {matched} | Missing: {missing} | Experience: {candidate['experience']} years"
