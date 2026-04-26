# 🚀 TalentSense-AI-Powered Talent Scouting & Engagement Agent


## 🧠 Overview

TalentSense AI is an AI-powered recruitment assistant that automates candidate screening by analyzing job descriptions and resumes.

It evaluates candidates based on:

* Skill Match
* Growth Potential
* Interest Level
* Hiring Risk

and produces a ranked shortlist with explainable insights.

---

## 🎯 Problem Statement

Recruiters spend significant time manually reviewing resumes and identifying suitable candidates.

Traditional systems rely on keyword matching, which lacks contextual understanding and explainability.

---

## 💡 Solution

TalentSense AI:

* Parses job descriptions and resumes (PDF)
* Extracts structured data (skills, experience)
* Computes similarity using TF-IDF + cosine similarity
* Evaluates candidates using multi-factor scoring
* Generates a ranked shortlist with explanations

---

## 🏗️ Architecture

```
User Input (JD + Resumes)
        ↓
Parsing Layer (PDF + Text)
        ↓
Feature Extraction (Skills, Experience)
        ↓
Matching Engine (TF-IDF + Cosine Similarity)
        ↓
Scoring Engine (Match + Growth + Risk + Interest)
        ↓
Explainability Layer
        ↓
Dashboard Output (Streamlit)
```

---

## ⚙️ Scoring Logic

Dynamic scoring model:

* Match Score → Skill similarity
* Growth Score → Future potential
* Risk Score → Missing critical skills
* Interest Score → Candidate engagement

### Final Score:

```
Adaptive Weighting:

If Match > 75 → Weight = 0.7  
If Match > 50 → Weight = 0.5  
Else → Weight = 0.3  

Final Score =
    (Weight × Match)
  + (0.2 × Interest)
  + (0.2 × Growth)
  - (0.2 × Risk)
```

---

## 🧪 Sample Input

### Job Description

AI Engineer with Python, NLP, AWS

### Candidates

* Candidate A → Strong AI background
* Candidate B → Partial match
* Candidate C → Unrelated skills

---

## 📊 Sample Output

| Name | Match  | Growth | Risk   | Final | Decision    |
| ---- | ------ | ------ | ------ | ----- | ----------- |
| A    | High   | High   | Low    | 82    | Strong Hire |
| B    | Medium | Medium | Medium | 58    | Consider    |
| C    | Low    | Low    | High   | 18    | Reject      |

---

## 🚀 Features

* 📄 PDF Resume Parsing
* 🔍 Skill Extraction
* 📊 AI-based Matching
* 📈 Growth & Risk Analysis
* 🎯 Hiring Decision Output
* 🧠 Explainable Results
* 🖥️ Interactive Dashboard

---

## 🛠️ Installation

cd talentsense-ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Usage

1. Enter Job Description
2. Upload resumes (PDF)
3. Click Analyze
4. View ranked candidates

---

## 🏆 Why This Project Stands Out

* Goes beyond keyword matching
* Uses multi-factor decision logic
* Provides explainable hiring insights
* Simulates real recruiter workflow

---

## 🚀 Future Improvements

* Real-time candidate chat interaction
* Integration with LinkedIn API
* Resume keyword highlighting
* Bias detection in hiring

---

## 👨‍💻 Author

Sudhan Rajamani


---
##🏗️ 🚀 Architecture Diagram

                ┌────────────────────────────┐
                │        User (Recruiter)    │
                │  - Enter Job Description   │
                │  - Upload Resume PDFs      │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │     Streamlit Frontend     │
                │  - UI Dashboard            │
                │  - Controls & Visualization│
                └─────────────┬──────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ JD Parser    │     │ Resume Parser│     │ Chat/Interest│
│ (Regex/NLP)  │     │ (PyMuPDF)    │     │ Scoring      │
│ Extract:     │     │ Extract Text │     │ Simulated    │
│ Skills, Exp  │     │ → Structured │     │ Interaction  │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       └──────────┬─────────┴─────────┬──────────┘
                  ▼                   ▼
           ┌──────────────┐   ┌──────────────┐
           │ Matching     │   │ Advanced     │
           │ Engine       │   │ Scoring      │
           │ TF-IDF +     │   │ Growth & Risk│
           │ Cosine Sim   │   │ Analysis     │
           └──────┬───────┘   └──────┬───────┘
                  │                  │
                  └──────────┬───────┘
                             ▼
                 ┌──────────────────────┐
                 │ Final Scoring Engine │
                 │ Dynamic Weight Logic │
                 └──────────┬───────────┘
                            ▼
                 ┌──────────────────────┐
                 │ Explainability Layer │
                 │ - Skill Match        │
                 │ - Skill Gap          │
                 │ - Risk Insights      │
                 └──────────┬───────────┘
                            ▼
                 ┌──────────────────────┐
                 │   Output Dashboard   │
                 │ Ranking + Decisions  │
                 └──────────────────────┘

