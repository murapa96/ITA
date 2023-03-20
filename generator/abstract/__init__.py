from abc import ABC, abstractmethod

"""
ABSTRACT GENERATOR

Interface for the class Generator
It must have a "generate" method with a string parameter.
"""


class AbstractGenerator(ABC):
    def generate(self, text):
        pass

