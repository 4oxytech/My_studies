
import requests
import json
from config import open_weather_token
from pprint import pprint
def get_weather(city, open_weather_token):
    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Моросящий дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B',
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        pprint(data)
        city = data['name']
        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не понимаю, что там за погода такая, как там ещё живы люди?'
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        print(f'''Погода в городе {city}
Температура: {cur_weather}°C {wd}
Ветер: {wind}м/с
Влажность: {humidity}
Хорошо Вам провести свой день!''')


    except Exception as ex:
        print(ex)
        print('Название введено неверно. Проверьте название города, пожалуйста.')

def main():
    city = input('Введите, пожалуйста, название города. Сейчас помотрим как там делишки.')
    get_weather(city,open_weather_token)

if __name__ == '__main__':
    main()
