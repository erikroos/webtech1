import datetime


class Cursist:
    """Klasse voor cursisten van muziekschool Sessions

    Attributen:
        naam (str): De naam van de cursist.
        email (str): Het e-mailadres van de cursist.
        tegoed (float): Het lestegoed in euro's (private).
        betalingsgeschiedenis (list): Alle mutaties van het tegoed, met tijdstip.
    """

    @staticmethod
    def _current_time():
        now = datetime.datetime.now()
        return f"{now:%Y-%m-%d %H:%M:%S}"

    def __init__(self, naam, email, tegoed=0.0):
        self._naam = naam
        self._email = email
        self.__tegoed = tegoed
        self._betalingsgeschiedenis = []
        print(f"Cursist {self._naam} ingeschreven bij Sessions")

    def stort(self, bedrag):
        """Verhoog het lestegoed met een bedrag"""
        if bedrag > 0:
            self.__tegoed += bedrag
            self._betalingsgeschiedenis.append((Cursist._current_time(), bedrag))
            self.toon_tegoed()

    def betaal_les(self, bedrag):
        """Betaal een les vanuit het tegoed"""
        if 0 < bedrag <= self.__tegoed:
            self.__tegoed -= bedrag
            self._betalingsgeschiedenis.append((Cursist._current_time(), -bedrag))
        else:
            print("Het bedrag dient groter dan nul (0) en maximaal gelijk aan het tegoed te zijn")
        self.toon_tegoed()

    def toon_tegoed(self):
        print(f"Tegoed van {self._naam} bedraagt €{self.__tegoed:.2f}")

    def toon_betalingen(self):
        print(f"\nBetalingsgeschiedenis van {self._naam}:")
        for datum, bedrag in self._betalingsgeschiedenis:
            if bedrag > 0:
                mutatie_type = "gestort"
            else:
                mutatie_type = "les betaald"
                bedrag = abs(bedrag)
            print(f"  {datum}: €{bedrag:.2f} {mutatie_type}")

    @property
    def tegoed(self):
        """Getter voor tegoed"""
        return self.__tegoed

    @tegoed.setter
    def tegoed(self, waarde):
        """Setter voor tegoed"""
        if waarde >= 0:
            self.__tegoed = waarde
        else:
            print("Tegoed kan geen negatieve waarde krijgen")
            self.__tegoed = 0


if __name__ == "__main__":
    joyce = Cursist("Joyce", "joyce@email.nl")
    joyce.stort(100.0)
    joyce.betaal_les(35.0)
    joyce.betaal_les(80.0)
    joyce.stort(50.0)
    joyce.toon_betalingen()

    print(f"\nTegoed via property: €{joyce.tegoed:.2f}")
    joyce.tegoed = -10  # Wordt afgewezen
