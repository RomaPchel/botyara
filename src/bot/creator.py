from configuration import config as bot


class BotCreator:

    @staticmethod
    def create(token):
        return bot.Bot(token)
