from bot.configuration.config import bot
import telebot


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! This ia a parser for YouTube. "
                                      "you can use /get_videos to enter the title of video u want to download;"
                                      "/search to search video u mentioned and "
                                      "/help to find out which formats are available")

@bot.message_handler(commands=['search_videos'])
def get_videos(message):
    msg = bot.send_message(message.chat.id, "enter the title of video you want to find")
    bot.register_next_step_handler(msg, search)

@bot.message_handler(commands=['help'])
def help(message):
   bot.send_message(message.chat.id, "You can download videous in 2 formats: MP3 and MP4. To download in "
                                     "type u want type MP3 or MP4")


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == ("mp3"):
        bot.send_message(message.chat.id, "aboba mp3")
    elif message.text == ("mp4"):
        bot.send_message(message.chat.id, "boba mp4")


@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, "Parsing started")
    video_link = "https://www.youtube.com/results?search_query=" + message.text


bot.polling(none_stop=True)







