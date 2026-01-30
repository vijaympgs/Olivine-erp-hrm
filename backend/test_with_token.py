import requests

headers = {
    'Authorization': 'Token a0e9c4cbf05d82e6a5c43ebd44c7f3f901d1e979',
    'Content-Type': 'application/json'
}

try:
    r = requests.get('http://localhost:8000/api/uoms/', headers=headers)
    print(f'Status Code: {r.status_code}')
    if r.status_code == 200:
        print('SUCCESS with token!')
    else:
        print(f'Error: {r.text}')
except Exception as e:
    print(f'Exception: {e}')




