from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

#Intializing Gemini API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# Model for summarization
model = genai.GenerativeModel("gemini-1.5-flash-8b")

# Helper function to process the LLM output in required format
def process_llm_response(response_text):
    categories = {
        "financial_performance": "",
        "market_dynamics": "",
        "expansion_plans": "",
        "environmental_risks": "",
        "regulatory_or_policy_changes": ""
    }

    # Split the response into lines or sentences
    lines = response_text.split("\n")
    
    # Logic to extract each category from the response
    for line in lines:
        if "Financial Performance" in line:
            categories["financial_performance"] = line.split(":")[1].strip()
        elif "Market Dynamics" in line:
            categories["market_dynamics"] = line.split(":")[1].strip()
        elif "Expansion Plans" in line:
            categories["expansion_plans"] = line.split(":")[1].strip()
        elif "Environmental Risks" in line:
            categories["environmental_risks"] = line.split(":")[1].strip()
        elif "Regulatory or Policy Changes" in line:
            categories["regulatory_or_policy_changes"] = line.split(":")[1].strip()

    # If any category is empty, provide a default or error message
    for key, value in categories.items():
        if not value:
            categories[key] = f"No information available for {key.replace('_', ' ')}."

    return categories

# Helper function to Check for Invalid Responses and Handle Errors
def handle_empty_or_invalid_response(response_text):
    if not response_text or "error" in response_text.lower():
        return {"error": "Failed to generate valid summary from the transcript."}
    
    return process_llm_response(response_text)


# Helper function to create prompt
def generate_prompt(transcript_text):
    return f"""
    Please summarize the earnings call transcript below into the following categories:
    1. Financial Performance
    2. Market Dynamics
    3. Expansion Plans
    4. Environmental Risks
    5. Regulatory or Policy Changes

    Transcript: {transcript_text}

    Format your response like this:
    - Financial Performance: [summary]
    - Market Dynamics: [summary]
    - Expansion Plans: [summary]
    - Environmental Risks: [summary]
    - Regulatory or Policy Changes: [summary]
    """

# Helper function to summarize the earnings call transcript
def summarize_transcript(transcript_text):
    prompt = generate_prompt(transcript_text)
    
    response = model.generate_content(prompt)
    return handle_empty_or_invalid_response(response.text.strip())


# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Earnings Transcript Summary API!",
        "usage": {
            "endpoint": "/earnings_transcript_summary",
            "method": "POST",
            "example_input": {
                "company_name": "Reliance Industries",
                "transcript_text": "YOUR TRANSCRIPT TEXT HERE"
            }
        }
    })

# Route to summarize the earnings call transcript
@app.route('/earnings_transcript_summary', methods=['POST'])
def earnings_transcript_summary():
    data = request.get_json()

    if not data or 'company_name' not in data or 'transcript_text' not in data:
        return jsonify({"error": "Missing 'company_name' or 'transcript_text' in the input"}), 400
    
    company_name = data['company_name']
    transcript_text = data['transcript_text']

    if not transcript_text:
        return jsonify({"error": "Transcript text cannot be empty"}), 400

    # Call the summarization function
    try:
        formatted_summary = summarize_transcript(transcript_text)
        return jsonify({
            "company_name": company_name,
            "financial_performance": formatted_summary["financial_performance"],
            "market_dynamics": formatted_summary["market_dynamics"],
            "expansion_plans": formatted_summary["expansion_plans"],
            "environmental_risks": formatted_summary["environmental_risks"],
            "regulatory_or_policy_changes": formatted_summary["regulatory_or_policy_changes"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Main function
if __name__ == '__main__':
    app.run(debug=True)
