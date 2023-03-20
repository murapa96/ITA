'''
AbstractPresenter is a abstract class that represents some kind of user iteration with the bot.
'''
import abc

class AbstractPresenter(abc.ABC):

    '''
    Handler for the messages that the user sends to the bot.
    '''
    @abc.abstractmethod
    def message_handler(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    '''
    Ask the user for some information, and wait for the response.
    '''
    @abc.abstractmethod
    def ask_user(self):
        pass

    '''
    Run a given command from the AI.
    '''

    @abc.abstractmethod
    def run_command(self):
        pass





