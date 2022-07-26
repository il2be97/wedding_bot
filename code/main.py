from auth_token import token
import telebot
from telegram_actions_handler.telegram_bot_commands_handler_repository import TelegramCommandsHandler

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    TelegramCommandsHandler.handle_command(bot=bot)

    bot.polling(none_stop=True)


if __name__ == '__main__':
    telegram_bot(token)
