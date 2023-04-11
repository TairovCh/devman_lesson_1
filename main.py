import requests

locations = ["/svo", "/london", "/череповца"]

url_template = 'https://wttr.in/{}?n&lang=ru&T&Q&M&m'

for location in locations:
    url = url_template.format(location)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
