from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij, teherautoAdatok):
        super().__init__(rendszam, tipus, berletiDij)
        self.__teherautoAdatok = teherautoAdatok

    def get_teherautoAdatok(self):
        return self.__teherautoAdatok