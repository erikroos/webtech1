# OOP Python – Meerdere klassen en compositie

In dit laatste deel aandacht voor de wijze waarop meerdere klassen samenwerken. De belangrijkste techniek daarbij is *compositie* (Engels: *composition*): een object wordt *samengesteld* uit verschillende andere objecten. Het samengestelde object kan op die manier taken delegeren aan de samenstellende objecten. Compositie lijkt op het eerste gezicht wel wat op overerving, maar waar overerving een **is-een**-relatie beschrijft, beschrijft compositie een **heeft-een**-relatie.

Aan het eind van deze paragraaf maken we [oefening 3](oefeningen/oop-oefening3.md).

## Het voorbeeld: lessen bij Sessions

Een les bij muziekschool Sessions *heeft een* docent, *heeft* (een groep) cursisten en *heeft* een lokaal. De les zelf *is* geen docent en *is* geen cursist — vandaar compositie in plaats van overerving. We bouwen de klasse `Les` in het bestand [`les.py`](bestanden/muziekschool/les.py), en gebruiken daarbij de klassen `Docent` en `Cursist` uit het vorige deel.

Het is belangrijk om commentaar op te nemen binnen codeblokken. Zo is het voor iemand die de code niet ontwikkeld heeft, maar er wel mee verder moet, duidelijk wat de bedoeling is. In het commentaar van de klasse zetten we een korte beschrijving, gevolgd door een omschrijving van de attributen — dat doen we hier met een zogenaamde *docstring*:

```python
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
```

Let op de constructor: een `Les`-object krijgt een compleet `Docent`-object mee als parameter, en houdt een lijst van `Cursist`-objecten bij. Dat is compositie in de praktijk.

## Cursisten inschrijven

Aan de klasse `Les` voegen we een methode toe om een cursist in te schrijven, met een controle op het maximale aantal deelnemers:

```python
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
```

En een methode om alle deelnemers te tonen:

```python
def toon_deelnemers(self):
    """Toont alle deelnemers van deze les"""
    if not self.cursisten:
        print(f"Nog geen inschrijvingen voor {self.naam}")
    else:
        print(f"\nDeelnemers {self.naam} (docent: {self.docent._naam}, lokaal {self.lokaal}):")
        for cursist in self.cursisten:
            print(f"  - {cursist}")
        print(f"Aantal: {len(self.cursisten)} van maximaal {self.max_cursisten}")
```

In de lus wordt elke cursist geprint — en omdat `Persoon` een `__str__()`-methode heeft (die `Cursist` erft), verschijnt daar netjes de naam met het e-mailadres. Overerving en compositie werken hier dus vrolijk samen.

## De klasse `Muziekschool`

De school zelf is óók een compositie: een `Muziekschool` *heeft* lessen (en via die lessen docenten en cursisten):

```python
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
```

## Het geheel in actie

Nu alle klassen af zijn, kunnen we ze gebruiken:

```python
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
```

Dit geeft de volgende uitvoer:

```console
Roos ingeschreven voor Gitaar voor beginners
Bram ingeschreven voor Gitaar voor beginners
De les Gitaar voor beginners zit vol!
Joyce ingeschreven voor Piano gevorderden

Deelnemers Gitaar voor beginners (docent: Bart, lokaal A1.02):
  - Roos (roos@email.nl)
  - Bram (bram@email.nl)
Aantal: 2 van maximaal 2
Les Gitaar voor beginners toegevoegd aan het rooster van Sessions
Les Piano gevorderden toegevoegd aan het rooster van Sessions

Rooster van Sessions:
  - Gitaar voor beginners bij Bart in lokaal A1.02 (2 inschrijvingen)
  - Piano gevorderden bij Ineke in lokaal B0.17 (1 inschrijvingen)
```

## Compositie vs. overerving

Het verschil tussen compositie en overerving nog even op een rij:

**Overerving** (is-een relatie):

- Een `Docent` **is een** `Persoon`
- Een `Cursist` **is een** `Persoon`
- Gebruikt `super()` om functionaliteit over te nemen

**Compositie** (heeft-een relatie):

- Een `Les` **heeft een** `Docent`
- Een `Les` **heeft** `Cursisten`
- Een `Muziekschool` **heeft** `Lessen`
- Gebruikt instantievariabelen om andere objecten te bevatten

Gebruik compositie wanneer:

1. **Flexibiliteit belangrijk is**: je kunt tijdens runtime eenvoudig de samenstelling wijzigen (bijvoorbeeld een andere docent voor een les inplannen)
2. **Een object functionaliteit nodig heeft van meerdere verschillende klassen**
3. **Er geen "is-een"-relatie is**: de objecten zijn niet hetzelfde type, maar werken samen

## Vooruitblik: van klassen naar database

Kijk nog eens goed naar wat we deze week gebouwd hebben: cursisten, docenten, instrumenten en lessen, met relaties daartussen (een les heeft een docent, een les heeft cursisten). Dit is precies de structuur die we verderop in de module terug gaan zien:

- in week 4 slaan we dit soort gegevens op in databasetabellen,
- en in week 5 verbinden we de twee werelden: elke klasse wordt dan een *model* dat via SQLAlchemy aan een databasetabel gekoppeld is.

De tijd die je nu investeert in het begrijpen van klassen en relaties, betaalt zich dus dubbel en dwars uit.

## Samenvatting

In dit deel hebben we geleerd over:

- Het werken met meerdere klassen die elkaar gebruiken
- Het documenteren van klassen met docstrings
- Compositie: objecten samenstellen uit andere objecten ("heeft-een")
- Het verschil tussen compositie en overerving
- Het gebruik van lijsten om collecties van objecten op te slaan

## Afsluiting OOP

Je hebt nu alle belangrijke OOP-concepten in Python gezien:

1. **Klassen en objecten**: het maken van sjablonen en instanties
2. **Inkapseling**: het afschermen van data, met properties voor nette toegang
3. **Overerving**: het hergebruiken van code via superklassen
4. **Polymorfisme**: dezelfde interface, verschillende implementaties
5. **Compositie**: het samenstellen van objecten uit andere objecten

Deze concepten vormen de basis voor het datamodel van je project — en voor alles wat we vanaf week 3 met Flask gaan bouwen.

Maak nu [oefening 3](oefeningen/oop-oefening3.md).
