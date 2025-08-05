import telebot
import json
import requests

bot = telebot.TeleBot('YOUR_BOT_TOKEN') # TODO: !!!
API = 'YOUR_API_TOKEN' # TODO: !!!

@bot.message_handler(commands=['start'])
def start(message):
    cat = requests.get(f'https://api.thecatapi.com/v1/images/search?limit=1&breed_ids=beng&api_key={API}')
    if cat.status_code == 200:
        valid_cat = json.loads(cat.text)
        bot.send_message(message.chat.id, valid_cat[0]["url"])
    else:
        bot.send_message(message.chat.id, 'Something went wrong, please try again!')

@bot.message_handler()
def base(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn1 = telebot.types.InlineKeyboardButton('Tap here!', callback_data='restart')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Type /start or click the button below!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'restart')
def restart_callback(call):
    start(call.message)

if __name__ == "__main__":
    print('Bot launched')
    bot.polling(none_stop=True)
  
