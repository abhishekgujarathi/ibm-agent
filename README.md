# 🧠 Skill-Gap Analyzer & Coach

An AI-powered web app that identifies top in-demand skills based on your profile and recommends personalized learning resources using Google Gemini and LangGraph.

## 🚀 Features

* Collects your **current role**, **experience**, and **target industries**
* Analyzes 100+ mock job postings to surface **top 3 most demanded skills**
* Uses **Gemini** (Google Generative AI) to generate:

  * Personalized coaching advice
  * Curated learning links (e.g., Coursera, Codecademy)

## 🛠️ Tech Stack

* Python (Flask)
* LangGraph (StateGraph workflow)
* LangChain + Google Gemini API
* HTML/CSS frontend

## 📦 Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/skill-gap-analyzer.git
   cd skill-gap-analyzer
   ```

2. **Create virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API key:**

   ```bash
   export GOOGLE_API_KEY=your_api_key_here
   ```

5. **Run the app:**

   ```bash
   python app.py
   ```

6. **Visit in browser:**
   [http://localhost:5000](http://localhost:5000)

## 🧪 Example Use Case

**Input:**

* Role: Data Analyst
* Experience: 2
* Target Industries: Technology, Marketing

**Output:**

* Top Skills: Python, SQL, Public Speaking
* Gemini Coaching: Explanation + resource links to improve

## 📄 Folder Structure

```
.
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## 🧠 Credits

Built as part of the **IBM AI-ML Internship Project** using skills from:

* LangChain & LangGraph
* Google Gemini (Generative AI)
* Flask Web Framework

---

Let me know if you want badges, screenshots, or deployment instructions added!
