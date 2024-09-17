# Getting Weather Data Without Scraping
import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

citydata = data['city']
print("Current Location:", citydata)

url = 'https://wttr.in/{}'.format(citydata)
res = requests.get(url)

print(res.text)