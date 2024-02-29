import requests

URL = "http://127.0.0.1:8000/stuinfo/"

r = requests.get(url=URL)

# Use the json() method to get the parsed JSON content
data = r.json()

print(data)
