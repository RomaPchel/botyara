import config as bot


class BotCreator:

    @staticmethod
    def create(name, token):
        return bot.Bot(name, token)
