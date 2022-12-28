from app.bot.components.keyboards.buttons.buttons import Buttons
import telebot


class KeyBoard:
    @staticmethod
    def generate_keyboard():
        user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        user_markup.row(Buttons.MP3)
        user_markup.row(Buttons.MP4)

        return user_markup
