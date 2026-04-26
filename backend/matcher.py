
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match_score(candidate, jd):
    t1 = " ".join(candidate.get("skills", []))
    t2 = " ".join(jd.get("skills", []))


    if not t1.strip() or not t2.strip():
        return 0.0

    try:
        vec = TfidfVectorizer().fit_transform([t1, t2]).toarray()
        score = cosine_similarity([vec[0]], [vec[1]])[0][0]
        return round(score * 100, 2)
    except:
        return 0.0