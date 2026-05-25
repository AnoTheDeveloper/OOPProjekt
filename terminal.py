from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto


def adatok_betoltese():
    kolcsonzo = Autokolcsonzo("SpeedCar")

    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 12000, 5)
    auto2 = Szemelyauto("XYZ-567", "Honda Civic", 15000, 5)
    auto3 = Teherauto("TRK-999", "Ford Transit", 20000, 1200)

    kolcsonzo.auto_hozzaadas(auto1)
    kolcsonzo.auto_hozzaadas(auto2)
    kolcsonzo.auto_hozzaadas(auto3)

    kolcsonzo.auto_berlese("ABC-123", "2026-05-25")
    kolcsonzo.auto_berlese("XYZ-567", "2026-05-26")
    kolcsonzo.auto_berlese("TRK-999", "2026-05-27")
    kolcsonzo.auto_berlese("ABC-123", "2026-05-28")

    return kolcsonzo


def menu():
    kolcsonzo = adatok_betoltese()

    while True:
        print("\n===== AUTÓKÖLCSÖNZŐ =====")
        print("1 - Autók listázása")
        print("2 - Autó bérlése")
        print("3 - Bérlés lemondása")
        print("4 - Bérlések listázása")
        print("0 - Kilépés")

        valasztas = input("Választás: ")

        try:
            if valasztas == "1":
                kolcsonzo.autok_listazasa()

            elif valasztas == "2":
                rendszam = input("Rendszám: ")
                datum = input("Dátum (YYYY-MM-DD): ")

                kolcsonzo.auto_berlese(rendszam, datum)

            elif valasztas == "3":
                rendszam = input("Rendszám: ")
                datum = input("Dátum (YYYY-MM-DD): ")

                kolcsonzo.berles_lemondasa(rendszam, datum)

            elif valasztas == "4":
                kolcsonzo.berlesek_listazasa()

            elif valasztas == "0":
                print("Kilépés...")
                break

            else:
                print("Érvénytelen menüpont!")

        except Exception as hiba:
            print(f"Hiba: {hiba}")


menu()