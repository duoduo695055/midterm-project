# -*- coding: 'utf-8' -*-
import requests
import re

while True:
    city=input('please input the city or exit:\n')
    if not city:
        break

    req=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s'%city)

    dic_city=req.json()
    #print(dic_city)
    city_data=dic_city.get('data')
    #print(city_data)
    if city_data:
        city_forecast=city_data['forecast'][0]#字典的值是一个列表
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        fengli=re.findall(r'\d',city_forecast.get('fengli'))
        print('wind:',''.join(fengli))
        print(city_forecast.get('fengxiang'))
        print(city_forecast.get('type'))
    else:
        print('no data')
