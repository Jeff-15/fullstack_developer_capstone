# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = "http://localhost:3030"
sentiment_analyzer_url = "https://sentianalyzer.1l67mjw23e6y.us-south.codeengine.appdomain.cloud/"

def get_request(endpoint, **kwargs):
    if(kwargs):
        for key,value in kwargs.items():
            params = params + key + "="+value+"&"
        request_url = backend_url+endpoint+"?"+params
    else:
        request_url = backend_url+endpoint
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(url=request_url)
        return response.json()
    except Exception as e:
        print(e)
# Add code for get requests to back end

def analyze_review_sentiments(text):
    
    request_url = sentiment_analyzer_url+"analyze/"+text

    try:
        response = requests.get(url=request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    print(data_dict)
    try:
        response = requests.post(request_url,json=data_dict)
        return response.json()
    except Exception as e:
        print(e)

