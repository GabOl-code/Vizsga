from datetime import datetime


class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)


def szamol_foglalas_ar(szoba, datum):
    nap = datum.weekday()
    if nap == 4 or nap == 5:
        return szoba.ar
    else:
        return szoba.ar // 2


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        szoba = next((s for s in self.szobak if s.szobaszam == szobaszam), None)
        if szoba:
            ar = szamol_foglalas_ar(szoba, datum)
            foglalas = Foglalas(szoba, datum, ar)
            self.foglalasok.append(foglalas)
            print(f"Foglalás sikeres. Az ár: {ar} Ft")
        else:
            print("Hiba: A megadott szobaszám nem létezik.")

    def lemondas(self):
        while True:
            szobaszam_input = input("Kérem adja meg a lemondani kívánt szobaszámot: ")
            try:
                szobaszam = int(szobaszam_input)
                foglalas = next((f for f in self.foglalasok if f.szoba.szobaszam == szobaszam), None)
                if foglalas:
                    self.foglalasok.remove(foglalas)
                    print("Lemondás sikeres.")
                    break
                else:
                    print("Hiba: A megadott szobaszámra nincs foglalás.")
            except ValueError:
                print("Hiba: Érvénytelen szobaszám. Kérjük, csak számot adjon meg.")

    def listaz_foglalasok(self):
        print("Összes foglalás:")
        for foglalas in self.foglalasok:
            print(f"{foglalas.szoba.szobaszam}: {foglalas.datum} - {foglalas.ar} Ft")


class Foglalas:
    def __init__(self, szoba, datum, ar):
        self.szoba = szoba
        self.datum = datum
        self.ar = ar


# Feltöltés:
szalloda = Szalloda("Python Hotel")
print(szalloda.nev)
szalloda.szoba_hozzaad(EgyagyasSzoba(101))
szalloda.szoba_hozzaad(EgyagyasSzoba(102))
szalloda.szoba_hozzaad(KetagyasSzoba(201))

datum = datetime(2023, 12, 1)  # Példa dátum: 2023.12.01
szalloda.foglalas(101, datum)
szalloda.foglalas(102, datum)
szalloda.foglalas(201, datum)
# Példa dátum: 2023.12.04 nem péntek, vagy szombat féláron
datum = datetime(2023, 12, 4)
szalloda.foglalas(101, datum)
szalloda.foglalas(201, datum)
szalloda.listaz_foglalasok()

szalloda.lemondas()
szalloda.listaz_foglalasok()
