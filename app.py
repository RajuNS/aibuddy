from flask import Flask, render_template, request, jsonify
from google import genai
import os

# Initialize Flask app
app = Flask(__name__)

# Set your API key (replace with your actual API key)
API_KEY = "AIzaSyA86DrqeNL9D-Fvd6ghIJsHlt5k1MrYnKM"  # Get it from https://ai.google.dev
client = genai.Client(api_key=API_KEY)

# Load the latest Gemini model
model = "gemini-2.0-flash"  # Use "gemini-1.5-pro" for more advanced responses

def get_gemini_response(prompt):
    """Generate AI response using Google Gemini API."""
    try:
        response = client.models.generate_content(model=model, contents=prompt)
        return response.text if response and hasattr(response, "text") else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        prompt = request.form.get("prompt", "").strip()
        if not prompt:
            return jsonify({'response': "Please enter a message."})

        response = get_gemini_response(prompt)
        return jsonify({'response': response})

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
