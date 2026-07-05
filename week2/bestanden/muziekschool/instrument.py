class Instrument:
    """Klasse voor huurinstrumenten van muziekschool Sessions

    Attributen:
        naam (str): De naam van het instrument.
        huurprijs (float): De huurprijs per maand in euro's.
        voorraad (int): Het aantal beschikbare exemplaren.
    """

    def __init__(self, naam, huurprijs, voorraad):
        self.naam = naam
        self.huurprijs = huurprijs
        self.voorraad = voorraad

    def verhuur(self, aantal):
        """Verhuur een aantal exemplaren van dit instrument"""
        nieuwe_voorraad = self.voorraad - aantal
        if nieuwe_voorraad >= 0:
            self.voorraad = nieuwe_voorraad
            print(f"Verhuurd: {aantal}x {self.naam}. Nog {self.voorraad} beschikbaar")
        else:
            print(f"Onvoldoende exemplaren. Nog maar {self.voorraad} beschikbaar")

    def __str__(self):
        return f"Instrument: {self.naam}, Huurprijs: €{self.huurprijs:.2f} p/m, Beschikbaar: {self.voorraad}"


if __name__ == "__main__":
    gitaar = Instrument("Elektrische gitaar", 17.50, 5)
    print(gitaar)

    gitaar.verhuur(2)
    print(gitaar)

    gitaar.verhuur(2)
    print(gitaar)

    gitaar.verhuur(2)  # Dit zal niet lukken - onvoldoende exemplaren!
    print(gitaar)
