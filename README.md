Overview
Google API Toolkit is a Python library I created to simplify interactions with various Google APIs, such as Search (Custom Search JSON API), Maps, Sheets, and Drive. It handles OAuth2 authentication, request throttling, and data parsing for seamless integration into apps or scripts. This project is ideal for tasks like automated search queries, location-based services, or spreadsheet automation, showcasing my experience with REST APIs, error handling, and secure credential management.

Disclaimer: Requires a Google Cloud project and API keys. Respect rate limits and terms of service—use for educational or personal projects only.

Features
Multi-API Support: Easy wrappers for Google Search, Maps Geocoding, Sheets CRUD, and more.
OAuth2 & API Key Handling: Secure token management with refresh support.
Batch Requests: Queue multiple calls to optimize against quotas.
Data Parsing: Returns structured JSON/Pandas DataFrames for easy analysis.
CLI Interface: Quick commands for testing API endpoints.
Extensible: Modular design for adding new Google APIs (e.g., YouTube or Gmail).
Tech Stack
Language: Python 3.9+
Key Libraries:
google-api-python-client and google-auth for official SDKs.
requests for custom HTTP handling.
pandas for data export and manipulation.
python-dotenv for secure env vars.
No heavy dependencies—runs in most environments.
Getting Started
Prerequisites
Python 3.9 or higher.
A Google Cloud project with enabled APIs (e.g., Custom Search Engine for search).
Credentials: API key or OAuth2 client ID/secret (download as JSON).
Git for cloning.
Installation
Clone the repository:
bash
git clone https://github.com/abd0o0/googleApi.git
cd googleApi
Create a virtual environment and install dependencies:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Set up credentials (create .env in the root):
text
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
CUSTOM_SEARCH_ENGINE_ID=your_cse_id  # For search API
Usage
CLI Example (Search Query):
bash
python google_cli.py search --query "python tutorials 2025" --num_results 5 --output results.json
This queries Google Search API and saves top results as JSON (e.g., [{"title": "...", "link": "...", "snippet": "..."}]).
Programmatic Use (in a Python script):
python
from google_api.client import GoogleAPIClient
import json

# Initialize client (loads from .env)
client = GoogleAPIClient(api_type="search")  # Or "maps", "sheets"

# Perform a search
results = client.query("machine learning trends", num_results=10)

# Print or process results
print(json.dumps(results, indent=2))
Sheets Example (Read/Write):
python
from google_api.client import GoogleAPIClient

client = GoogleAPIClient(api_type="sheets")
sheet_id = "your_spreadsheet_id"

# Read data
data = client.read_range(sheet_id, "Sheet1!A1:C10")
print(data)  # List of rows

# Write data
client.write_range(sheet_id, "Sheet1!D1", [["New Data", 42]])
Run python google_cli.py --help for all commands. Examples in /examples folder; auth setup in /docs.
