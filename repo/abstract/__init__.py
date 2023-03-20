
import abc

class AbstractRepo(abc.ABC):
    @abc.abstractmethod
    def save(self, key, value):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def delete(self, key):
        pass

    @abc.abstractmethod
    def update(self, key, value):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def delete_all(self):
        pass

    @abc.abstractmethod
    def get_all_keys(self):
        pass

