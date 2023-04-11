import requests


url = 'https://wttr.in/'

response = requests.get(url)
response.raise_for_status()

print(response.text)