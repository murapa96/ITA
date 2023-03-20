"""
Brain of the chatbot.
In the constructor it saves a ROLE, a Generator and a id of the messager
It also has a messages array
"""

import json


class Brain:
    bot = "bot"
    human = "human"
    messages = []  #

    def __init__(self, bot, role, messages, generator, id, user_name):
        self.role = role
        self.generator = generator
        self.id = id
        self.messages = messages
        self.bot = bot
        self.human = user_name

    def answer(self, message):
        text = "{}\n{}\n{}:{}\n{}:".format(self.role, ''.join(self.messages[-12:]),self.human , message , self.bot)
        answer = self.generator.generate(text)
        self.messages.append(self.human + ":" + message + "\n" + self.bot+":" + answer)
        return answer

    def save(self):
        with open('{}.json'.format(self.id), 'w') as f:
            json.dump(self.__dict__, f)

    def load(self):
        with open('{}.json'.format(self.id), 'r') as f:
            self.__dict__ = json.load(f)

    def reset(self):
        self.messages = []
        self.save()
