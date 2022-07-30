from enum import Enum


class CommandsList(Enum):
    Start = 'start'
    Help = 'help'
    Users = 'admin_get_all_users'
    Info = 'info'
    SendMessageForAllUsers = 'send_message_for_all_users'

    def allComands():
        return [CommandsList.Start.value, CommandsList.Help.value, CommandsList.Users.value, CommandsList.Info.value, CommandsList.SendMessageForAllUsers.value]
