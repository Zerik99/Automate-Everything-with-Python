import requests
import json

url = "https://api.languagetool.org/v2/check"
data = {
    "text": "This is an test.",
    "language": "en-US",
}

response = requests.post(url, data=data)
result = json.loads(response.text)

print(result)
