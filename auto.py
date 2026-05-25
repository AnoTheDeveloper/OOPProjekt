from abc import ABC


class Auto(ABC):
    def __init__(self, rendszam, tipus, berletiDij):
        self.__rendszam = rendszam
        self.__tipus = tipus
        self.__berletiDij = berletiDij

    def get_rendszam(self):
        return self.__rendszam

    def get_tipus(self):
        return self.__tipus

    def get_berletiDij(self):
        return self.__berletiDij
    
    def __str__(self):
        return f"{self.__tipus} - {self.__rendszam} - {self.__berletiDij} Ft/nap"