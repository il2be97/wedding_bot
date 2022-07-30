from auth_token import token
import telebot
from telegram_bot_text_handler_repository.telegram_text_handler_repository import TelegramTextCommandHandlerRepository
from telegram_bot_commands_handler_repository.telegram_bot_commands_handler_repository import TelegramCommandsHandler

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    TelegramCommandsHandler.handle_command(bot=bot)
    TelegramTextCommandHandlerRepository.handle_text(bot=bot)

    bot.infinity_polling()
    bot.polling(none_stop=True)


if __name__ == '__main__':
    telegram_bot(token)
