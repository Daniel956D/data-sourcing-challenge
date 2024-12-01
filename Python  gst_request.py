import requests
import json
import os
from dotenv import load_dotenv

# Load the NASA_API_KEY from the .env file
load_dotenv()
api_key = os.getenv('NASA_API_KEY')

# Check if API key is loaded correctly
if not api_key:
    raise ValueError("NASA_API_KEY not found. Please check your .env file.")

# Step 1: Set the base URL and parameters for GST
base_url = "https://api.nasa.gov/DONKI/"
GST = "GST"
startDate = "2013-05-01"
endDate = "2024-05-01"

# Step 2: Build the query URL for GST
gst_query_url = f"{base_url}{GST}?startDate={startDate}&endDate={endDate}&api_key={api_key}"

# Step 3: Make a "GET" request for the GST URL and store it in a variable named gst_response
gst_response = requests.get(gst_query_url)

# Print the status code to verify if the request was successful
print("Status Code:", gst_response.status_code)

# Step 4: Convert the response variable to JSON and store it as a variable named gst_json
if gst_response.status_code == 200:
    gst_json = gst_response.json()

    # Preview the first result in JSON format
    print("\nPreview of GST JSON data:")
    print(json.dumps(gst_json[:2], indent=4))  # Print the first two items to preview the structure
else:
    print(f"Error: Request failed with status code {gst_response.status_code}")
