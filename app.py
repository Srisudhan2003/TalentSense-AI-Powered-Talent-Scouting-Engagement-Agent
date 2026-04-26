import streamlit as st
import pandas as pd
from backend.parser import extract_text_from_pdf, parse_text
from backend.matcher import compute_match_score
from backend.advanced import growth_score, risk_score
from backend.scorer import final_score
from backend.explainer import explain

st.set_page_config(page_title="TalentSense AI", layout="wide")

st.title("TalentSense - AI-Powered Talent Scouting & Engagement Agent ")


# Input
jd_text = st.text_area("📄 Enter Job Description")
files = st.file_uploader("📂 Upload Resumes", type=["pdf"], accept_multiple_files=True)

# Color function
def get_color(score):
    if score > 75:
        return "🟢"
    elif score > 50:
        return "🟡"
    else:
        return "🔴"

# Decision logic
def decision(final):
    if final > 75:
        return "✅ Strong Hire"
    elif final > 55:
        return "⚠️ Consider"
    else:
        return "❌ Reject"

if st.button("Analyze Candidates"):

    jd = parse_text(jd_text)
    results = []

    for file in files:
        text = extract_text_from_pdf(file)
        candidate = parse_text(text)

        match = compute_match_score(candidate, jd)
        interest = 70 if candidate["experience"] > 2 else 50
        growth = growth_score(candidate)
        risk = risk_score(candidate, jd)

        final = final_score(match, interest, growth, risk)

        results.append({
            "name": file.name,
            "match": match,
            "interest": interest,
            "growth": growth,
            "risk": risk,
            "final": final,
            "candidate": candidate
        })

    # Sort
    results = sorted(results, key=lambda x: x["final"], reverse=True)

    st.subheader("Ranked Candidates")

    # Cards layout
    for r in results:
        with st.container():
            st.markdown("---")

            col1, col2, col3 = st.columns([2,1,1])

            with col1:
                st.subheader(f"{r['name']}")
                st.write(decision(r["final"]))

            with col2:
                st.metric("Final Score", f"{r['final']}", get_color(r["final"]))

            with col3:
                st.metric("Risk", r["risk"], get_color(100 - r["risk"]))

            # Score row
            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Match", r["match"])
            c2.metric("Interest", r["interest"])
            c3.metric("Growth", r["growth"])
            c4.metric("Risk", r["risk"])

            # Expand details
            with st.expander("🔍 View Details"):
                st.write(explain(r["candidate"], jd))