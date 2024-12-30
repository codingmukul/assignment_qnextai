# Earnings Transcript Summary API

## Overview
This API processes earnings call transcripts for companies and summarizes key points in five distinct categories:
- Financial Performance
- Market Dynamics
- Expansion Plans
- Environmental Risks
- Regulatory or Policy Changes

The API leverages Generative AI models to summarize and extract the relevant information from the earnings call transcripts and returns the results in a structured JSON format.

## Features
- **Summarization of Transcript**: The API takes in an earnings call transcript and provides concise summaries for each of the five categories.
- **Structured Output**: The output is formatted in JSON for easy integration and processing.
- **Error Handling**: The API gracefully handles missing or invalid fields in the request.

## Technologies Used
- **Flask**: A lightweight Python web framework to create the RESTful API.
- **Generative AI**: (e.g., Gemini 1.5 Flash) used to process and summarize the text.
- **Python 3.x**: The programming language used to implement the solution.

## Requirements
- Python 3.x
- Flask (for API development)
- Requests (for making API calls, if needed)
- A Generative AI model (Gemini 1.5 Flash or equivalent) integrated via its API
- Any other libraries required for text processing

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/codingmukul/assignment_qnextai.git
cd earnings-transcript-summary-api
```

### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
You'll need to set up the API key for the Generative AI model (e.g., Gemini 1.5 Flash). Store it in an `.env` file:
```env
GENAI_API_KEY=your_api_key_here
```

### 5. Run the Application
```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000//earnings_transcript_summary`.

## API Endpoints

### 1. POST /earnings_transcript_summary
#### Description:
This endpoint accepts a JSON request with a company name and an earnings call transcript, and returns a structured summary of the transcript.

#### Request Format:
```json
{
  "company_name": "Reliance Industries",
  "transcript_text": "YOUR TRANSCRIPT TEXT HERE"
}
```

- `company_name`: (string) Name of the company (e.g., "Reliance Industries").
- `transcript_text`: (string) The full earnings call transcript.

#### Response Format:
```json
{
  "company_name": "Reliance Industries",
  "financial_performance": "SHORT SUMMARY OF FINANCIAL PERFORMANCE HERE",
  "market_dynamics": "SHORT SUMMARY OF MARKET DYNAMICS HERE",
  "expansion_plans": "SHORT SUMMARY OF EXPANSION PLANS HERE",
  "environmental_risks": "SHORT SUMMARY OF ENVIRONMENTAL RISKS HERE",
  "regulatory_or_policy_changes": "SHORT SUMMARY OF REGULATORY OR POLICY CHANGES HERE"
}
```

Each field in the response represents a summary of the corresponding aspect of the earnings call transcript.

## Error Handling

The API ensures that errors are handled gracefully. If any field is missing or the input is invalid, the API will respond with a relevant error message and HTTP status code.

Example of error response:
```json
{
  "error": "Missing 'company_name' or 'transcript_text' in the input"
}
```


#### Error Responses:
- `400 Bad Request`: If the `company_name` or `transcript_text` is missing in the request.
- `400 Bad Request`: If the `transcript_text` is empty.
- `500 Internal Server Error`: If there is a failure with the Generative AI model or any other error.

## Example Usage

### Example 1: Valid Request
```bash
curl -X POST http://127.0.0.1:5000/earnings_transcript_summary \
-H "Content-Type: application/json" \
-d '{"company_name": "Reliance Industries", "transcript_text": "In Q4, Reliance reported a 10% revenue growth..."}'
```

### Example 2: Invalid Request (Missing Transcript)
```bash
curl -X POST http://127.0.0.1:5000/earnings_transcript_summary \
-H "Content-Type: application/json" \
-d '{"company_name": "Reliance Industries"}'
```

### Example 3: Successful Response
```json
{
  "company_name": "Reliance Industries",
  "financial_performance": "Reliance's Q4 revenue grew by 10% year-over-year, driven by strong performance in the telecom and retail sectors.",
  "market_dynamics": "Market demand for telecommunications has been increasing, with growing competition in the 5G space.",
  "expansion_plans": "Reliance plans to expand its retail footprint by opening 200 new stores in the next year.",
  "environmental_risks": "The company is focusing on reducing carbon emissions and enhancing its ESG initiatives.",
  "regulatory_or_policy_changes": "New regulations in the telecom sector are expected to impact pricing strategies in the coming quarter."
}
```

## Contact

For further inquiries, please contact For further inquiries, please drop an email at <a>mukulaggarwal360@gmail.com</a>s