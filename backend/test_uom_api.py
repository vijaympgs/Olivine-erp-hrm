import requests
import json

try:
    r = requests.get('http://localhost:8000/api/uoms/')
    print(f'Status Code: {r.status_code}')
    if r.status_code == 200:
        data = r.json()
        print(f'Response type: {type(data)}')
        print(f'Response: {json.dumps(data, indent=2)[:500]}')
    else:
        print(f'Error: {r.text[:500]}')
except Exception as e:
    print(f'Exception: {e}')




