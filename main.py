import requests

location = ["/svo", "/london", "/череповца"]

url_template = 'https://wttr.in/{}?n&lang=ru&T&Q'

for x in location:
    url = url_template.format(x)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)