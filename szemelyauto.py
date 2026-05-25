from auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij, szemelyautoAdatok):
        super().__init__(rendszam, tipus, berletiDij)
        self.__szemelyautoAdatok = szemelyautoAdatok

    def get_szemelyautoAdatok(self):
        return self.szemelyautoAdatok