import requests

# pegando token com o id do usuario
r = requests.post('http://127.0.0.1:8000/rest_auth/login/', data={
    "username": "admin",
    "email": "admin@gmail.com",
    "password": "admin"
})
print(r.json())

t = requests.get('http://127.0.0.1:8000/api/frases/')
print(t.json())

# print(r.json()['key'])

# t = requests.post('http://127.0.0.1:8000/api/frases/', headers={'Authorization':'token '+r.json()['key']},data={
#     'title': 'oraçaõ',
#     'content': 'klalaskdkansdkasd6g54ds54g45a6',
#     'user_id': 1
# })
# print(t.json())
