from ast import Str
import telebot

class MessageToUserDictConvert:
    def convert(message: telebot.types.Message):
         return {'chat_identifier' : message.chat.id, 'user_name' : message.chat.first_name }

    def get_user_name(dictionary: dict):
        return dictionary['user_name']

    def get_identifier(dictionary: dict):
        return dictionary['chat_identifier']