import requests

# Register a new user
# response = requests.post('http://127.0.0.1:8000/api/register/', json={"username": "testuser", "password": "password"})
# print(response.json())

# # Login to get a JWT token
response = requests.post('http://127.0.0.1:8000/api/login/', json={"username": "testuser", "password": "password"})
tokens = response.json()
print(tokens)

# # Access a protected route
headers = {"Authorization": f"Bearer {tokens['access']}"}
response = requests.get('http://127.0.0.1:8000/api/protected/', headers=headers)
print(response.json())