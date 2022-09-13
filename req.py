import config.settings as s
import requests
# GET https://api.weather.yandex.ru/v2/informers?
#  lat=<широта>
#  & lon=<долгота>
#  & [lang=<язык ответа>]
# X-Yandex-API-Key: <значение ключа>

payload = { 'lat': s.lat, 'lon': s.lon, 'lang' : s.lang}
headers = {
    'X-Yandex-API-Key': s.api_key,
    'user-agent': 'my-app/0.0.1'
}
r = requests.get('https://api.weather.yandex.ru/v2/informers', params=payload, headers=headers).json()
