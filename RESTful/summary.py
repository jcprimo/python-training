# Summarize API
import os 
import requests

SMMR_API_KEY="FFDA4CDE15"
global_url="https://api.smmry.com"
api_url = "&SM_API_KEY=" + SMMR_API_KEY
target_url = "http://www.bbc.com/news/business-43298897"
summarize_url = "&SM_URL=" + 

params = {
		'SM_API_KEY' : SMMR_API_KEY,
		'sm_url': target_url    
         }
response = requests.get(global_url, params=params)

