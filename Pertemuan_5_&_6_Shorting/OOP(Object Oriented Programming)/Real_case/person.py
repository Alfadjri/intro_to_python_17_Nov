from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self,nama,umur):
        self._name = nama
        self.__age = umur
    @abstractclassmethod
    def get_detail(self):
        pass
    
    def getUmur(self):
        return self.__age
    def set_umur(self,umur):
        if umur > 0 :
            self.__age = umur
        else :
            raise ValueError("umur harus bernilai positif")