from datetime import datetime
from szalloda import Szalloda


class FelhasznaloiFelulet:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.futtat()

    def futtat(self):
        while True:
            print("\nVálasszon műveletet:")
            print("1. Foglalás")
            print("2. Lemondás")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Választás (1-4): ")

            if valasztas == "1":
                self.foglalas()
            elif valasztas == "2":
                self.lemondas()
            elif valasztas == "3":
                self.listaz_foglalasok()
            elif valasztas == "4":
                print("Kilépés. Viszontlátásra!")
                break
            else:
                print("Érvénytelen választás. Kérem, válasszon 1 és 4 között.")

    def foglalas(self):
        szobaszam = int(input("Adja meg a foglalni kívánt szobaszámot: "))
        ev = int(input("Adja meg az év(yyyy): "))
        honap = int(input("Adja meg a hónap(1-12): "))
        nap = int(input("Adja meg a nap(1-31): "))
        datum = datetime(ev, honap, nap)

        self.szalloda.foglalas(szobaszam, datum)

    def lemondas(self):
        self.szalloda.lemondas()

    def listaz_foglalasok(self):
        self.szalloda.listaz_foglalasok()


if __name__ == "__main__":
    szalloda = Szalloda("Python Hotel")
    felhasznaloi_interfesz = FelhasznaloiFelulet(szalloda)
