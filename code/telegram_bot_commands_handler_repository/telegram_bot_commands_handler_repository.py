from ast import Str
from enum import Enum
import imp
import telebot
from commands_list.commands_list import CommandsList
from commands_text.commands_text import CommandsText
from data_storage_manager.data_storage_manager import DataStorage
from converter.message_to_user_dict_converter import MessageToUserDictConvert

class TelegramCommandsHandler:

    def handle_command(bot: telebot.TeleBot):
        @bot.message_handler(commands=CommandsList.allComands())
        def handle_command(message: telebot.types.Message):
            identifer = message.chat.id
            name = message.chat.first_name
            list = DataStorage.load()
        
            if message.text == "/" + CommandsList.Start.value or message.text == "/" + CommandsList.Start.value + " hello":
                photo = open('code/images/start.jpg', "rb")
                text = CommandsText.textFor(command=CommandsList.Start)
                bot.send_photo(identifer, photo= photo, caption=text)
            elif message.text == "/" + CommandsList.Help.value:
                bot.send_message(identifer, "Помощь")
            elif message.text == "/" + CommandsList.Users.value:
                allUsers = list
                bot.send_message(identifer, repr(allUsers), parse_mode='html')
            elif message.text == "/" + CommandsList.Info.value:
                bot.send_message(identifer, text=CommandsText.textFor(command=CommandsList.Info))
            elif message.text == "/" + CommandsList.SendMessageForAllUsers.value:
                bot.send_message(identifer, text=CommandsText.textFor(command=CommandsList.SendMessageForAllUsers))
            
            dictionary = MessageToUserDictConvert.convert(message=message)
            DataStorage.save(dictionary)
            