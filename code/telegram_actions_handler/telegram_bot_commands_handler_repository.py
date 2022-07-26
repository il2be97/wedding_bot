from enum import Enum
import telebot
from data_storage_manager.data_storage_manager import DataStorage
from converter.message_to_user_dict_converter import MessageToUserDictConvert

class CommandsList(Enum):
    Start = 'start'
    Help = 'help'
    Users = 'admin_get_all_users'
    Info = 'info'

    def allComands():
        return [CommandsList.Start.value, CommandsList.Help.value, CommandsList.Users.value, CommandsList.Info.value]


class TelegramCommandsHandler:

    def handle_command(bot: telebot.TeleBot):
        @bot.message_handler(commands=CommandsList.allComands())
        def send_welcome(message):
            dictionary = MessageToUserDictConvert.convert(message=message)
            identifer = MessageToUserDictConvert.get_identifier(dictionary=dictionary)
            name = MessageToUserDictConvert.get_user_name(dictionary=dictionary)
            DataStorage.save(userDict=dictionary)
        
            if message.text == "/" + CommandsList.Start.value:
                bot.send_message(identifer, "Привет, " + name)
            if message.text == "/" + CommandsList.Start.value + " hello":
                bot.send_message(identifer, "Привет, " + name)
            elif message.text == "/" + CommandsList.Help.value:
                bot.send_message(identifer, "Помощь")
            elif message.text == "/" + CommandsList.Users.value:
                allUsers = DataStorage.load()
                bot.send_message(identifer, repr(allUsers), parse_mode='html')
            elif message.text == "/" + CommandsList.Info.value:
                bot.send_message(identifer)