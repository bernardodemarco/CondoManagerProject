import pickle
import os

from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource) -> None:
        self.__cache = []
        self.__datasource = os.path.join(os.path.dirname(__file__), f'..\\pickle_files\\{datasource}')
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, obj):
        self.__cache.append(obj)
        self.__dump()

    def update(self, obj):
        if obj in self.__cache:
            index = self.__cache.index(obj)
            self.__cache[index] = obj
            self.__dump()

    def remove(self, obj):
        try:
            self.__cache.remove(obj)
            self.__dump()
        except ValueError:
            pass

    def get_all(self):
        return self.__cache
