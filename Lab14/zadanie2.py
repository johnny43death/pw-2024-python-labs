import requests

url = 'https://mapy.radiopolska.pl/api/programById/PL/6'
rozglosnia = requests.get(url)
json = rozglosnia.json()
#print(json)
data = json["data"]
data2 = data[0]
adres = data[0]["url"]
#print(adres)