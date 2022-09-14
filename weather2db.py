from re import I
from config.database import ins
import req
from parser import YandexWeather


a = YandexWeather(req.r)
ins(a.temperature, a.date)

