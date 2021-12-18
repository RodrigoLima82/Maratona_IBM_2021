# MARATONA BEHIND THE CODE 2021

# DESAFIO 6: FINAL

# Autor: Rodrigo Oliveira
# LinkedIn: https://www.linkedin.com/in/rodrigolima82/

import requests

jsonData = {
            "email": "",
            "assistantId": "",
            "url": "",
            "skillId": "",
            "apiKey": "",
            "submitConfirmation": ''
        }

URL = ""
r = requests.post(URL, json=jsonData)
print(r.status_code)
print(r.text)