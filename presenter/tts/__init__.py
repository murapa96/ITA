'''
Text to speech implementation of the AbstractPresenter
'''

import sys
import os
import time
import threading
import queue
from ..abstract import AbstractPresenter
from gtts import gTTS
import pygame

class TTSPresenter(AbstractPresenter):

        def __init__(self):
            self.queue = queue.Queue()
            self.thread = threading.Thread(target=self.message_handler)
            self.thread.start()

        def message_handler(self):
            while True:
                message = self.queue.get()
                if message == 'quit':
                    break
                tts = gTTS(text=message, lang='en')
                tts.save('temp.mp3')
                pygame.mixer.init()
                pygame.mixer.music.load('temp.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

        def run(self):
            self.message_handler()

        def ask_user(self, message):
            print(message)
            return input()

        def __str__(self):
            return 'TTSPresenter'
