import requests

cityname = 'Jaffna'

url = 'https://wttr.in/{}'.format(cityname)

res = requests.get(url)

print(res.text)
