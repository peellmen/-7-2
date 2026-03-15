import telebot 
from logect import detect_bird
bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "привет ")

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    bot.send_message(message.chat.id, "ваше фото")
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image/" + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    name, acc = detect_bird("image/" + file_name)
    bot.send_message(message.chat.id, f'ваше фото:{name}')

bot.polling()