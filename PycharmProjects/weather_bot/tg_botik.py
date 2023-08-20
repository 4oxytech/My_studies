import requests
import datetime
import telebot
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token=tg_bot_token)

dp = Dispatcher(bot)
def telegram_bot(tg_bot_token):
 bot = telebot.TeleBot('6075612984:AAFrghK2k2IgGTD8vRUm7EpsQYhNVnsqujc')

@dp.message_handler(commands=['start','main','hello'])
async def start_message(message: types.Message):
  bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, у природы нет плохой погоды, верно? Напиши мне название города, и мы посмотрим, что там у нас с погодой.')
@dp.message_handler()
async def get_wather(message: types.Message):
    pass
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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        city = data['name']
        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не понимаю, что там за погода такая, как там ещё живы люди?'

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        await message.reply(f'''Погода в городе {city}
    Температура: {cur_weather}°C {wd}
    Ветер: {wind}м/с
    Влажность: {humidity}
    Хорошо Вам провести свой день!''')
    except:
     await message.reply('\U00002620 Название введено неверно. Проверьте название города, пожалуйста \U00002620')
def main():
 city = input('Введите, пожалуйста, название города. Сейчас помотрим как там делишки.')


if __name__ == '__main__':
 bot = telebot.TeleBot(tg_bot_token)
executor.start_polling(dp)
bot.polling(none_stop=True)


