import unittest
from generator import GeneratorFactory

class TestGeneratorFactory(unittest.TestCase):
    def test_get_generator(self):
        generator = GeneratorFactory.get_generator('echo')
        self.assertEqual(generator.generate('test'), 'test')

    def test_get_generator_with_logger(self):
        generator = GeneratorFactory.get_generator_with_logger('echo')
        self.assertEqual(generator.generate('test'), 'test')

    def test_get_generator_with_logger_openai(self):
        generator = GeneratorFactory.get_generator('openai')
        #Assert that the generator is not None
        self.assertIsNotNone(generator)
        #Print a list of available engines
        print(generator.get_available_engines())


    def test_list_available_generators(self):
        generators = GeneratorFactory.list_available_generators()
        self.assertEqual(generators, ['echo', 'openai'])
if __name__ == '__main__':
    unittest.main()
