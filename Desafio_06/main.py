import requests

jsonData = {
            "email": "rodrigolima82@gmail.com",
            "assistantId": "723cb291-2dcf-4bad-a189-e62ef5c8df11",
            "url": "https://api.au-syd.assistant.watson.cloud.ibm.com/instances/fedbc1bb-9da2-4984-bb46-003ab1187152",
            "skillId": "fa2821bf-2888-4555-8ff3-735da33261c3",
            "apiKey": "gTer0zmg9bn01defPFC6RO5G7Hytm65tbSdDvZmEt_f8",
            "submitConfirmation": 'true'
        }

URL = "http://172.21.188.211:3000/submit"
r = requests.post(URL, json=jsonData)
print(r.status_code)
print(r.text)