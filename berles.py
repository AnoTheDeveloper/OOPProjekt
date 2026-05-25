class Berles:
    def __init__(self, auto, datum):
        self.__auto = auto
        self.__datum = datum

    def get_auto(self):
        return self.__auto

    def get_datum(self):
        return self.__datum
    
    def __str__(self):
        return f"{self.__auto} | Dátum: {self.__datum}"