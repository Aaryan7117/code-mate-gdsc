from flask import Flask, request, jsonify, render_template
import subprocess
import json
import os

app = Flask(__name__)

FEEDBACK_FILE = "feedback.json"

def save_feedback(query, response, rating):
    """Save user feedback (query, response, rating) to a JSON file."""
    feedback_data = []
    
    # Load existing feedback if the file exists
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            feedback_data = json.load(file)

    # Append new feedback
    feedback_data.append({"query": query, "response": response, "rating": rating})

    # Save back to the file
    with open(FEEDBACK_FILE, "w") as file:
        json.dump(feedback_data, file, indent=4)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get('query')
    
    result = subprocess.run(['ollama', 'run', 'llama2'], input=query, capture_output=True, text=True)
    
    response = result.stdout.strip()
    
    return jsonify({'response': response})

@app.route('/submit_feedback', methods=['POST'])  
def submit_feedback():
    """Receive user feedback and store it."""
    data = request.json
    query = data.get("query")
    response = data.get("response")
    rating = data.get("rating") 

    if query and response and rating is not None:
        save_feedback(query, response, rating)
        return jsonify({"message": "Feedback saved successfully!"})
    return jsonify({"error": "Invalid feedback data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
