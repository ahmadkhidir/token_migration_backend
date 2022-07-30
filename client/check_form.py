from django.db import DatabaseError
import requests


URL = 'http://192.168.43.121:8000/v1/form/'
DATA = {
    'type': 'phrase',
    'token': 'wetyuhghfgiuytty'
}

response = requests.post(URL, json=DATA)
print(response.content)