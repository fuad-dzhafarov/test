import telebot
import random
import requests

TOKEN = '807039933:AAHHQSnUdDgV4yUW66QpdCNZapD43gMbUI8'

bot = telebot.TeleBot(TOKEN)
STICKER_ID = 'CAADAgADswgAAgi3GQLZ3ZInK5ngPAI'

@bot.message_handler(content_types=['location'])
def send_location(message):
    lon = int(message.location.longitude)
    lat = int(message.location.latitude)
    response = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lon={lon}&lat={lat}')
    info = response.json()
    description = info['weather'][0]['description']
    temp = info['main']['temp']
    pressure = info['main']['pressure']
    humidity = info['main']['humidity']
    wind = info['wind']['speed']
    sendtxt = f'There is a {description} today. The temperature is {temp}. Pressure is {pressure}. The humidity is {humidity}. The speed of window is {wind}'
    bot.send_message(message.chat.id, sendtxt)

    
    
bot.polling()
