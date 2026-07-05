class Persoon:
    """Superklasse voor alle personen bij muziekschool Sessions"""

    def __init__(self, naam, email):
        self._naam = naam
        self._email = email

    def stel_voor(self):
        print(f"Hallo, ik ben {self._naam}")

    def __str__(self):
        return f"{self._naam} ({self._email})"


class Docent(Persoon):
    """Een docent geeft les in een bepaald instrument"""

    def __init__(self, naam, email, instrument, uurtarief=40.0):
        super().__init__(naam=naam, email=email)
        self._instrument = instrument
        self._uurtarief = uurtarief

    def stel_voor(self):
        print(f"Hallo, ik ben {self._naam} en ik geef les in {self._instrument}")

    def bereken_lesprijs(self, minuten):
        prijs = self._uurtarief * minuten / 60
        print(f"Een les van {minuten} minuten bij {self._naam} kost €{prijs:.2f}")
        return prijs


class Cursist(Persoon):
    """Een cursist volgt lessen bij Sessions"""

    def __init__(self, naam, email, geboortejaar):
        super().__init__(naam=naam, email=email)
        self._geboortejaar = geboortejaar

    def stel_voor(self):
        print(f"Hallo, ik ben {self._naam} en ik ben cursist bij Sessions")


if __name__ == "__main__":
    bart = Docent("Bart", "bart@sessions.nl", "gitaar")
    roos = Cursist("Roos", "roos@email.nl", 2007)
    henk = Persoon("Henk", "henk@email.nl")

    # Polymorfisme: dezelfde aanroep, verschillend gedrag
    for persoon in [bart, roos, henk]:
        persoon.stel_voor()

    bart.bereken_lesprijs(45)
