'''
Repo Module.

AbstractFactory that can create different implementations of the AbstractRepo interface.


'''

import pkgutil

from .abstract import AbstractRepo
from .sqlite import SQLiteRepo
from .json import JsonRepo

class RepoFactory(object):
    '''
    Factory class that can create different implementations of the AbstractRepo interface.
    '''
    def __init__(self, config=None):
        self.config = config
        self.repo = None

    def create_repo(self, repo_type):
        '''
        Create a repo object based on the repo_type passed in.
        '''
        if repo_type == 'sqlite':
            self.repo = SQLiteRepo(self.config)
        elif repo_type == 'json':
            self.repo = JsonRepo(self.config)
        else:
            raise Exception('Repo type: {} not supported'.format(repo_type))
        return self.repo

    def create_repo_with_logger(self, repo_type):
        '''
        Create a repo object with a logger.
        '''
        repo = RepoLogger(self.create_repo(repo_type))

        return repo

    def get_repo(self):
        '''
        Return the repo object.
        '''
        return self.repo

    def get_all_repo_types(self):
        '''
        Return a list of all the repo types supported.
        '''
        return [name for _, name, _ in pkgutil.iter_modules([os.path.dirname(__file__)])]


class RepoLogger(AbstractRepo):
    '''
    Decorator class that logs all the calls to the repo object.
    '''
    def __init__(self, repo: AbstractRepo):
        self.repo = repo

    def save(self, key, value):
        '''
        Log the save call and then call the save method on the repo object.
        '''
        print('Saving key: {} value: {}'.format(key, value))
        self.repo.save(key, value)

    def get(self, key):
        '''
        Log the get call and then call the get method on the repo object.
        '''
        print('Getting key: {}'.format(key))
        return self.repo.get(key)

    def delete(self, key):
        '''
        Log the delete call and then call the delete method on the repo object.
        '''
        print('Deleting key: {}'.format(key))
        self.repo.delete(key)

    def update(self, key, value):
        '''
        Log the update call and then call the update method on the repo object.
        '''
        print('Updating key: {} value: {}'.format(key, value))
        self.repo.update(key, value)

    def get_all(self):
        '''
        Log the get_all call and then call the get_all method on the repo object.
        '''
        print('Getting all')
        return self.repo.get_all()

    def delete_all(self):
        '''
        Log the delete_all call and then call the delete_all method on the repo object.
        '''
        print('Deleting all')
        self.repo.delete_all()

    def get_all_keys(self):
        '''
        Log the get_all_keys call and then call the get_all_keys method on the repo object.
        '''
        print('Getting all keys')
        return self.repo.get_all_keys()
