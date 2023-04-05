import requests
import json

url = "https://api.edenai.run/v2/translation/automatic_translation"
txtinput = "how are you?"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "providers": "google",
    "text": txtinput ,
    "target_language": "fa",
    "source_language": "en"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMmNmY2U1OTUtY2Y0MC00YmFlLWFmODItNzYyOTE2MjFmYTdlIiwidHlwZSI6ImFwaV90b2tlbiJ9.3GEi53rxfTLBlgcNb_FqhELs6Yu3eDq2aBD-ZJvcAXE"
}

response = requests.post(url, json=payload, headers=headers)

result = response.text
print('>>>>>', json.loads(str(result)) ['google']['text'])