import requests
import json

url = 'http://localhost:5000/restapi'
data = {'text' : "hi",}
headers = {'Content-Type' : "application/json"}
response = requests.post(url, data = json.dumps(data), headers = headers)
print(response.json()['result'])