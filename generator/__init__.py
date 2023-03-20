from .abstract import AbstractGenerator
from .openai import GeneratorOpenAi
"""
GENERATOR TEST IMPLEMENTATION

Interface for the class Generator
It must have a "generate" method with a string parameter.
"""


class GeneratorEcho(AbstractGenerator):
    def generate(self, text):
        return text


"""
GENERATOR LOGGER IMPLEMENTATION

Special generator that takes another generator as injection dependency
and logs the input and output of the generate method.
"""


class GeneratorLogger(AbstractGenerator):
    def __init__(self, generator):
        self.generator = generator

    def generate(self, text):
        print("\nInput: " + text)
        output = self.generator.generate(text)
        print("Output: " + output)
        return output


"""
FACTORY PATTERN CREATOR
"""


class GeneratorFactory:
    generators = {
        'echo': GeneratorEcho(),
        'openai': GeneratorOpenAi()
    }

    @classmethod
    def get_generator(cls, generator_name, config=None):
        return cls.generators[generator_name]

    @classmethod
    def get_generator_with_logger(cls, generator_name):
        return GeneratorLogger(cls.generators[generator_name])

    @classmethod
    def list_available_generators(cls):
        return list(cls.generators.keys())
