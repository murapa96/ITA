import telebot
import copy
import re


class Bot:
    brains = {}
    bot = telebot.TeleBot("")

    def __init__(self, template_brain):
        self.template_brain = template_brain

        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            # Aqui se crea el nuevo brain para el usuario
            self.bot.reply_to(message, "Hola {}! ¿Cómo estás?".format(
                message.user.first_name))
            self.brains[message.chat.id] = copy.copy(self.template_brain)
            self.brains[message.chat.id].id = message.chat.id

        @self.bot.message_handler(func=lambda message: True)
        def answer(message):
            if message.chat.id in self.brains:
                answer = self.brains[message.chat.id].answer(message.text)
                self.bot.reply_to(message, answer)
            else:
                if re.match("^\..*", message.text):
                    self.bot.send_message(message.chat.id, "Hola {}! ¿Cómo estás?".format(
                        message.user.first_name))
                    self.brains[message.chat.id] = copy.copy(self.template_brain)
                    self.brains[message.chat.id].id = message.chat.id
                    self.bot.send_message(message.chat.id, self.brains[message.chat.id].answer(message.text))

    def run(self):
        self.bot.polling()

