import datetime

from persoon import Docent, Cursist


class Les:
    """Klasse voor lessen bij muziekschool Sessions

    Een les is samengesteld uit:
    - Een docent
    - Een groep cursisten
    - Een lokaal en een tijdstip
    """

    def __init__(self, naam, docent, lokaal, max_cursisten=8):
        self.naam = naam
        self.docent = docent
        self.lokaal = lokaal
        self.max_cursisten = max_cursisten
        self.cursisten = []
        self.aangemaakt_op = datetime.datetime.now()

    def schrijf_in(self, cursist):
        """Schrijft een cursist in voor deze les

        Parameters:
            cursist (Cursist): De in te schrijven cursist
        """
        if len(self.cursisten) >= self.max_cursisten:
            print(f"De les {self.naam} zit vol!")
            return False
        self.cursisten.append(cursist)
        print(f"{cursist._naam} ingeschreven voor {self.naam}")
        return True

    def toon_deelnemers(self):
        """Toont alle deelnemers van deze les"""
        if not self.cursisten:
            print(f"Nog geen inschrijvingen voor {self.naam}")
        else:
            print(f"\nDeelnemers {self.naam} (docent: {self.docent._naam}, lokaal {self.lokaal}):")
            for cursist in self.cursisten:
                print(f"  - {cursist}")
            print(f"Aantal: {len(self.cursisten)} van maximaal {self.max_cursisten}")


class Muziekschool:
    """De muziekschool zelf: heeft docenten, cursisten en lessen"""

    def __init__(self, naam):
        self.naam = naam
        self.lessen = []

    def voeg_les_toe(self, les):
        self.lessen.append(les)
        print(f"Les {les.naam} toegevoegd aan het rooster van {self.naam}")

    def toon_rooster(self):
        print(f"\nRooster van {self.naam}:")
        for les in self.lessen:
            print(f"  - {les.naam} bij {les.docent._naam} in lokaal {les.lokaal} "
                  f"({len(les.cursisten)} inschrijvingen)")


if __name__ == "__main__":
    # Maak docenten aan
    bart = Docent("Bart", "bart@sessions.nl", "gitaar")
    ineke = Docent("Ineke", "ineke@sessions.nl", "piano")

    # Maak cursisten aan
    roos = Cursist("Roos", "roos@email.nl", 2007)
    bram = Cursist("Bram", "bram@email.nl", 2002)
    joyce = Cursist("Joyce", "joyce@email.nl", 1990)

    # Maak lessen aan (compositie!)
    gitaarles = Les("Gitaar voor beginners", bart, "A1.02", max_cursisten=2)
    pianoles = Les("Piano gevorderden", ineke, "B0.17")

    # Schrijf cursisten in
    gitaarles.schrijf_in(roos)
    gitaarles.schrijf_in(bram)
    gitaarles.schrijf_in(joyce)  # De les zit vol!
    pianoles.schrijf_in(joyce)

    gitaarles.toon_deelnemers()

    # En de school als geheel
    sessions = Muziekschool("Sessions")
    sessions.voeg_les_toe(gitaarles)
    sessions.voeg_les_toe(pianoles)
    sessions.toon_rooster()
