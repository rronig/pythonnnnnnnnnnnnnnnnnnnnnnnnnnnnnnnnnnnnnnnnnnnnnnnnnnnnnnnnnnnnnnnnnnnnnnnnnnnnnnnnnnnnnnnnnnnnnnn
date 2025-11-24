import requests
url='http://127.0.0.1:8000/create_person'
person_data = {"name": "John", "age": 25}
r = requests.post(url, json=person_data)
print(r.json())
print(r.status_code)