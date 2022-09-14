import datetime
import config.settings as config

# Docs https://yandex.ru/dev/weather/doc/dg/concepts/forecast-info.html
class YandexWeather():
    def __init__(self, json):
        self.url = json['info']['url']
        self.timestamp = json['now']
        self.date = datetime.datetime.fromtimestamp(json['now']).strftime(config.time_format)
        self.week = json['forecast']['week']
        self.temperature = json['fact']['temp']
        self.icon = json['fact']['icon']
        self.condition = json['fact']['condition']
        self.wind = {
            'dir' : json['fact']['wind_dir'],
            'speed' : json['fact']['wind_speed'],
            'gust' : json['fact']['wind_gust']
        }
        self.pressure = json['fact']['pressure_mm']
        self.humidity = json['fact']['humidity']
