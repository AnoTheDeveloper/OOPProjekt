from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev):
        self.__nev = nev
        self.__autok = []
        self.__berlesek = []

    def auto_hozzaadas(self, auto):
        self.__autok.append(auto)

    def berles_hozzaadas(self, berles):
        self.__berlesek.append(berles)

    def autok_listazasa(self):
        for auto in self.__autok:
            print(auto)

    def berlesek_listazasa(self):
        if not self.__berlesek:
            print("Nincsenek aktív bérlések.")
            return

        for index, berles in enumerate(self.__berlesek, start=1):
            print(f"{index}. {berles}")

    def auto_berlese(self, rendszam, datum):
        for berles in self.__berlesek:
            if (
                berles.get_auto().get_rendszam() == rendszam
                and berles.get_datum() == datum
            ):
                raise Exception("Az autó már foglalt ezen a napon!")

        for auto in self.__autok:
            if auto.get_rendszam() == rendszam:
                uj_berles = Berles(auto, datum)
                self.__berlesek.append(uj_berles)

                print(
                    f"Sikeres bérlés! Fizetendő: "
                    f"{auto.get_berletiDij()} Ft"
                )
                return

        raise Exception("Nincs ilyen rendszámú autó!")

    def berles_lemondasa(self, rendszam, datum):
        for berles in self.__berlesek:
            if (
                berles.get_auto().get_rendszam() == rendszam
                and berles.get_datum() == datum
            ):
                self.__berlesek.remove(berles)
                print("Bérlés sikeresen lemondva!")
                return

        raise Exception("Nem található ilyen bérlés!")