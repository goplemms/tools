from typing import AnyStr, Callable
from os import path

class FileMonad:
    def __init__(self, file_descriptor, mode:str=''):
        self.__file_descriptor = file_descriptor
        self.__opened_file = None


    def __del__(self):
        if self.__opened_file is not None:
            self.__opened_file.close()


    def bind(self, f: Callable) -> 'FileMonad':
        if self.__opened_file is None:
            self.__opened_file = open(self.__file_descriptor)

        try:
            result = f(self.__opened_file)
            return
