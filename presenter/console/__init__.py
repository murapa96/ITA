'''
An inplementation of the AbstractPresenter using the console.
'''

import sys
import os
import time
import threading
import queue
from ..abstract import AbstractPresenter

class ConsolePresenter(AbstractPresenter):

    def __init__(self):
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.message_handler)
        self.thread.start()

    def message_handler(self):
        while True:
            message = self.queue.get()
            if message == 'quit':
                break
            print(message)

    def run(self):
        self.message_handler()

    def ask_user(self, message):
        print(message)
        return input()

    def __str__(self):
        return 'ConsolePresenter'


