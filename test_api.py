import requests

response = requests.post("http://127.0.0.1:8000/run", params={"task": "count wednesdays"})
print(response.json())
