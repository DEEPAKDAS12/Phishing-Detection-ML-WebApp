from flask import Flask, request, jsonify, render_template
import joblib
import requests
import numpy as np
from bs4 import BeautifulSoup
from scipy.sparse import hstack

app = Flask(__name__)

# ✅ Load Pretrained Models
vectorizer = joblib.load("vectorizer/tfidf_vectorizer.pkl")
voting_model = joblib.load("models/voting_classifier.pkl")

# ✅ Function to Extract Webpage Text & HTML Length
def extract_text_and_length(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "lxml")
        
        # Extract text content
        text = " ".join([p.text for p in soup.find_all("p")])
        html_length = len(response.text)  # HTML length as additional feature
        
        return text if text else "No content", html_length
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return "Error", 0

# ✅ Function to Preprocess Text for ML Model
def preprocess_text(text):
    text_vectorized = vectorizer.transform([text])  # ✅ Apply TF-IDF Transformation
    return text_vectorized

# ✅ Flask Route to Serve Frontend
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Flask API Endpoint for Prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # ✅ Extract webpage content and HTML length
    webpage_text, html_length = extract_text_and_length(url)
    
    if webpage_text == "Error":
        return jsonify({"error": "Unable to fetch webpage content"}), 500

    # ✅ Preprocess Text (TF-IDF Transformation)
    processed_text = preprocess_text(webpage_text)
    
    # ✅ Combine TF-IDF features with HTML length
    X_combined = hstack([processed_text, np.array([[html_length]])])
    
    # ✅ Predict using Voting Model
    pred_proba = voting_model.predict_proba(X_combined)[:, 1][0]  # Extract probability score

    # ✅ Apply Threshold = `0.38`
    threshold = 0.38
    final_prediction = "Phishing" if pred_proba > threshold else "Legitimate"

    return jsonify({"prediction": final_prediction, "score": float(pred_proba)})

# ✅ Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)
