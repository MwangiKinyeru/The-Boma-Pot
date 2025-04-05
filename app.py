from flask import Flask, request, jsonify, render_template
import pandas as pd
from joblib import load
from sklearn.metrics.pairwise import cosine_similarity
import os
import re

app = Flask(__name__)

# Load models and data
try:
    combined_df = pd.read_csv("Model/combined_df.csv")
    tfidf_vectorizer = load("Model/tfidf_vectorizer.joblib")
    tfidf_matrix = load("Model/tfidf_matrix.joblib")
    print("All models loaded successfully!")
except Exception as e:
    print(f"Error loading files: {str(e)}")
    print("Current directory:", os.getcwd())
    print("Model directory contents:", os.listdir('Model'))
    raise

def format_ingredients(ingredients):
    """Format ingredients into clean bullet points"""
    if pd.isna(ingredients):
        return ""
    # Remove brackets and quotes, then split
    cleaned = re.sub(r"[\[\]']", "", str(ingredients))
    items = [item.strip() for item in cleaned.split(",") if item.strip()]
    return "• " + "\n• ".join(items)

def format_instructions(instructions):
    """Improved instruction formatting that handles cooking times and multi-step paragraphs"""
    if pd.isna(instructions):
        return ""
    
    text = str(instructions).strip()
    
    # Case 1: Already has proper numbered steps (1. 2. 3.)
    if re.search(r'^\d+\.|\n\d+\.', text):
        steps = re.split(r'\d+\.', text)
        steps = [step.strip() for step in steps if step.strip()]
        return "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))
    
    # Case 2: Handle cooking time headers (like "Preparation 20 minutes...")
    time_match = re.match(r'^((?:Preparation|Cook|Serves).*?(?:minutes|hours|hour|minute))', text, re.IGNORECASE)
    if time_match:
        header = time_match.group(1).strip()
        remaining = text[len(header):].strip()
        return f"1. {header}\n" + format_instructions(remaining)
    
    # Case 3: Split at sentence endings but preserve cooking times
    sentences = re.split(r'\.(?=\s|$)(?!\d)', text)  # Split at periods followed by space or end
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Number the steps
    formatted = []
    current_num = 1
    for sentence in sentences:
        # Handle sub-steps separated by semicolons
        if ';' in sentence:
            parts = [p.strip() for p in sentence.split(';') if p.strip()]
            formatted.append(f"{current_num}. {parts[0]}")
            for part in parts[1:]:
                current_num += 1
                formatted.append(f"{current_num}. {part}")
        else:
            formatted.append(f"{current_num}. {sentence}")
        current_num += 1
    
    return "\n".join(formatted)

def recommend_recipe(user_input, combined_df, tfidf_vectorizer, tfidf_matrix, top_n=5):
    """Recommend top N recipes based on user input."""
    user_tfidf = tfidf_vectorizer.transform([user_input])
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]
    
    recommendations = combined_df.iloc[top_indices][["Title", "Ingredients", "Instructions"]].copy()
    recommendations["Ingredients"] = recommendations["Ingredients"].apply(format_ingredients)
    recommendations["Instructions"] = recommendations["Instructions"].apply(format_instructions)
    
    return recommendations.to_dict(orient="records")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get("query", "")
    recommendations = recommend_recipe(user_input, combined_df, tfidf_vectorizer, tfidf_matrix)
    return render_template("results.html", recipes=recommendations)

if __name__ == '__main__':
    app.run(debug=True)