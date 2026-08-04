#Requests library and working with APIs
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout= 30)
    if response.status_code == 200:
        print("Success!")
    else:
        print(f"Something went wrong: {response.status_code}")
    data = response.json()
    name = data.get('name', 'N/A')
    email = data.get('email', 'N/A')
    print(f"username: {name}, user email: {email}")
    city = data.get('address', {}).get('city', 'N/A')
    print(f"user city: {city}")
    company = data.get('company', {}).get('name', 'N/A')
    print(f"user company: {company}")
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")