import schedule
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from threading import Thread
import requests
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

TOKEN = os.environ['telegram_token']
subscribers = set()
bot = telebot.TeleBot(TOKEN, skip_pending=True)

def default_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = KeyboardButton("/Subscribe")
    item2 = KeyboardButton("/Unsubscribe")
    item3 = KeyboardButton("/Help")
    markup.add(item1, item2, item3)
    return markup

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = default_markup()
    bot.send_message(
        message.chat.id,
        'Greetings! Subscribe to this bot to get notifications about the status of NinjaVan sorting facility.',
        reply_markup=markup)

@bot.message_handler(commands=['Subscribe'])
def subscribe_command(message):
    subscribers.add(message.chat.id)
    markup = default_markup()
    bot.send_message(message.chat.id, 'You have been subscribed to this bot.', reply_markup=markup)

@bot.message_handler(commands=['Unsubscribe'])
def unsubscribe_command(message):
    subscribers.remove(message.chat.id)
    markup = default_markup()
    bot.send_message(message.chat.id, 'You have been unsubscribed to this bot.', reply_markup=markup)

@bot.message_handler(commands=['Help'])
def help_command(message):
    markup = default_markup()
    bot.send_message(message.chat.id, 'Subscribe to this bot to get notifications about the status of NinjaVan sorting facility.', reply_markup=markup)

def get_request(url):
    try:
        response = requests.get(url)
        print(response)
        send_message()
        return response
    except Exception as e:
        print(e)
        return None

def send_message(message="There are too many vehicles in the sorting facility. Please wait for a while."):
    for subscriber in subscribers:
        bot.send_message(subscriber, message)

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

thread1 = Thread(target=schedule_checker)
thread1.start()

schedule.every().second.do(lambda: get_request("http://190.92.221.226:5000/health"))


print("bot is running...")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        sleep(5)