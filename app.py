# app.py (Flask version with LangGraph + Gemini)
import os
import random
from flask import Flask, render_template, request
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI

# Read Gemini API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY environment variable not set")
os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest", temperature=0.2)

# Simulated job postings
titles = ["Data Analyst", "Marketing Specialist", "Software Engineer", "Product Manager"]
industries = ["Technology", "Marketing", "Finance", "Education"]
skill_pool = [
    "Python", "SQL", "Tableau", "SEO", "Git", "AWS", "Excel",
    "Machine Learning", "Public Speaking", "Project Management"
]

job_postings = [
    {
        "title": random.choice(titles),
        "industry": random.choice(industries),
        "skills": random.sample(skill_pool, k=3)
    }
    for _ in range(100)
]

# Node: get_profile (handled by Flask input)
def get_profile(state):
    return state

# Node: analyze_skills
def analyze_skills(state):
    counts = {}
    for post in job_postings:
        if post['industry'] in state['industries']:
            for skill in post['skills']:
                counts[skill] = counts.get(skill, 0) + 1
    state['top_skills'] = [skill for skill, _ in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]]
    return state

# Node: generate_coaching
def generate_coaching(state):
    skills = ", ".join(state['top_skills'])
    prompt = (
        f"You are a career coach. The user has these top in-demand skills: {skills}. "
        "Explain briefly why these skills are valuable and suggest 2-3 specific learning resources (with URLs)."
    )
    response = llm.invoke(prompt)
    state['coaching'] = response.content.strip()
    return state

# Build the LangGraph
builder = StateGraph(dict)
builder.set_entry_point('get_profile')
builder.add_node('get_profile', get_profile)
builder.add_node('analyze_skills', analyze_skills)
builder.add_node('generate_coaching', generate_coaching)
builder.add_edge('get_profile', 'analyze_skills')
builder.add_edge('analyze_skills', 'generate_coaching')
builder.add_edge('generate_coaching', END)
graph = builder.compile()

# Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_state = {
        'role': request.form['role'],
        'experience': request.form['experience'],
        'industries': [i.strip() for i in request.form['industries'].split(',')]
    }
    final_state = graph.invoke(user_state)
    print(final_state)
    return render_template('index.html', result=final_state)

if __name__ == '__main__':
    app.run(debug=True)
