
from commands_list.commands_list import CommandsList

class CommandsText:
    def textFor(command: CommandsList):
        if command == CommandsList.Start:
            return """
          Дорогой гость, если ты тут, значит, мы будем рады разделить наш особенный день именно с тобой 🥰

В этом чате будет появляться вся необходимая информация для твоего удобства. Так что оставайся тут, чтобы быть в курсе всех новостей)

Чтобы посмотреть информацию о мероприятии, в любое время нажми кнопку «Меню» и выбери «Информация о мероприятии».

Уже ждем встречи с тобой 💃🏻💃🏻

Катюша & Ильюша
        """ 
        elif command == CommandsList.Info:
            return  """
            Дата: 
20 августа 2022 (суббота)

Место: 
Усадьба Royal Hall
(Логойский р-н, д. Чуденичи, ул. Лесная 2А)

Время:
15:00 - трансфер
15:45 - фуршет
16:30 - регистрация
            """
        if command == CommandsList.SendMessageForAllUsers:
            return "Введите текст:"
        
    def textForOldCommand(command: CommandsList):
        if command == CommandsList.SendMessageForAllUsers:
            return "Ваш текст будет выглядить:"
            
            
        