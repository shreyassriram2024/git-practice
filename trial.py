import requests

print("Testing virtual environment...")

r = requests.get("https://api.github.com")
print("Status:", r.status_code)
