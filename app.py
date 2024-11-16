from flask import Flask, render_template, request, jsonify
from wordsegment import load, segment
import re

app = Flask(__name__)
load()  # Load wordsegment dictionary

def space_text(text):
    """Process text and add spaces"""
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    if not cleaned_text:
        return ""
    return " ".join(segment(cleaned_text))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.json.get('text', '')
    result = space_text(text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
