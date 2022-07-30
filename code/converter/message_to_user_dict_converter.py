from array import array
from ast import Str
import json
import telebot

class MessageToUserDictConvert:
    def convert(message: telebot.types.Message, textToSend: Str = None):
        return {'chat_identifier' : message.chat.id, 'user_name' : message.chat.first_name, 'previous_command' : message.text, 'text_to_send': textToSend} 

    def get_user_name(dictionary: dict):
        return dictionary['user_name']

    def get_identifier(dictionary: dict):
        return dictionary['chat_identifier']
    
    def get_text_to_send(dictionary: dict):
        return dictionary['text_to_send']
    
    def get_previous_command(usersInfo: list, user: int):
        for userInfo in usersInfo:
            dictionary = json.loads(userInfo)
            if dictionary['chat_identifier'] == user:
                return dictionary['previous_command']
            
    def get_user_info(usersInfo: list, user: int):
        for userInfo in usersInfo:
            dictionary = json.loads(userInfo)
            if dictionary['chat_identifier'] == user:
                return dictionary