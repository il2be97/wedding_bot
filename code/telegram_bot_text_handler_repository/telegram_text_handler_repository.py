from cgitb import text
from email import message
import json
import types
import telebot
from telebot import types
from text_commands_list.text_commands_list import TextCommandsList
from commands_list.commands_list import CommandsList

from converter.message_to_user_dict_converter import MessageToUserDictConvert
from data_storage_manager.data_storage_manager import DataStorage

class TelegramTextCommandHandlerRepository:
    def handle_text(bot: telebot.TeleBot):
        @bot.message_handler()
        def handle_text(message: telebot.types.Message):
            identifer = message.chat.id
            name = message.chat.first_name
            list = DataStorage.load()
            previousCommand = MessageToUserDictConvert.get_previous_command(list, identifer)
            userDict = MessageToUserDictConvert.get_user_info(usersInfo=list, user=message.chat.id)
            textToSend = MessageToUserDictConvert.get_text_to_send(userDict)
            
            if previousCommand == "/" + CommandsList.SendMessageForAllUsers.value:
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                markup.add(types.KeyboardButton("Отправить"))
                markup.add(types.KeyboardButton("Отмена"))
                bot.send_message(identifer, "Ваш текст будет выглядить:\n" + message.text, reply_markup=markup)
                dictionary = MessageToUserDictConvert.convert(message=message, textToSend=message.text)
                DataStorage.save(dictionary)
            if message.text == TextCommandsList.Cancel.value:
                DataStorage.save(MessageToUserDictConvert.convert(message=message))
            if message.text == TextCommandsList.Send.value and textToSend != None:
                for user in list:
                    dictionary = json.loads(user)
                    userIdentifier = MessageToUserDictConvert.get_identifier(dictionary=dictionary)
                    bot.send_message(userIdentifier, text=textToSend)
                    DataStorage.save(MessageToUserDictConvert.convert(message=message))