import openai
import os
from ..abstract import AbstractGenerator
"""
OPENAI CODEX GENERATOR

Generator specialiced on generate text from OpenAi Codex
Uses OpenAi API
"""


class GeneratorOpenAi(AbstractGenerator):
    def __init__(self, config=None):
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key
        self.config = {
            'engine': 'davinci',
            'temperature': 0.9,
            'max_tokens': 150,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'stop': ['\n', ' Human:', ' AI:']
        }
    def generate(self, text):
        return openai.Completion.create(
            engine=self.config['engine'] ,
            prompt=text,
            temperature=self.config['temperature'],
            max_tokens=self.config['max_tokens'],
            top_p=self.config['top_p'],
            frequency_penalty=self.config['frequency_penalty'],
            presence_penalty=self.config['presence_penalty'],
            stop=self.config['stop']
        )['choices'][0]['text']

    def get_config(self):
        return self.config

    def set_config(self, config):
        self.config = config

    def get_api_key(self):
        return self.api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def get_available_engines(self):
        return openai.Engine.list()


