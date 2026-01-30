import requests
import uuid

url = "http://127.0.0.1:8002/api/hrm/api/v1/employees/"
data = {
    "employee_number": f"EMP{uuid.uuid4().hex[:6].upper()}",
    "first_name": "Test",
    "last_name": "Employee",
    "date_of_birth": "1990-01-01",
    "gender": "MALE",
    "hire_date": "2023-01-01",
    "employment_status": "ACTIVE",
    "employment_type": "FULL_TIME",
    "work_email": f"test_{uuid.uuid4().hex[:6]}@example.com",
    "username": f"testuser_{uuid.uuid4().hex[:6]}",
    "marital_status": "SINGLE",
    "pay_frequency": "MONTHLY",
    "department_name": "IT",
    "position_title": "Developer",
    "hierarchy_level": 0
}

response = requests.post(url, json=data)
print(f"Status: {response.status_code}")
