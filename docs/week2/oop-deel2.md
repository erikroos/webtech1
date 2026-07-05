# OOP Python – Inkapseling en properties

Inkapseling (Engels: *encapsulation*) is één van de fundamenten van object-georiënteerd programmeren. Het wordt gebruikt om onbevoegden niet de gelegenheid te bieden de kenmerken van een object zomaar aan te passen. Als dat mogelijk moet zijn, dienen zij toegang te krijgen tot zogenaamde *getters* en *setters*, waarover zo dadelijk meer.

Aan het eind van deze tekst maken we [oefening nummer 1](oefeningen/oop-oefening1.md).

!!! Info "zichtbaarheid"
    Python wijkt nadrukkelijk af van het idee van inkapseling zoals het bijvoorbeeld gedaan wordt bij Java. Python gebruikt niet de sleutelwoorden `private` of `protected` om de zichtbaarheid van een methode aan te geven.

## Het voorbeeld: lestegoed

Cursisten van Sessions betalen hun lessen vanuit een *lestegoed*: ze storten een bedrag, en de kosten van elke les gaan daar vanaf. Zo'n tegoed is bij uitstek iets wat je niet zomaar van buitenaf wilt laten aanpassen — een cursist die zijn eigen tegoed op €1.000.000 zet, daar wordt alleen de cursist zelf beter van. We bouwen daarom een klasse `Cursist` waarin het tegoed netjes is ingekapseld, inclusief een geschiedenis van alle betalingen, met tijdstip.

De code wordt in stapjes opgebouwd; we slaan deze uiteindelijk op in het bestand [`cursist.py`](bestanden/muziekschool/cursist.py).

## Klasse en methoden

Stap 1: de klasse

```python
class Cursist:
```

Stap 2: het importeren van de huidige tijd

```python
import datetime
```

Stap 3: een functie om het tijdstip van de betaling vast te leggen.

```python
@staticmethod
def _current_time():
    now = datetime.datetime.now()
    return f"{now:%Y-%m-%d %H:%M:%S}"
```

De functie `_current_time()` retourneert het tijdstip van de mutatie in het opgegeven formaat, tot op de seconde nauwkeurig. De `@staticmethod` decorator geeft aan dat dit een functie is die bij de klasse hoort maar niet afhankelijk is van een specifieke instantie.

## De constructor

Stap 4: de constructor

```python
def __init__(self, naam, email, tegoed=0.0):
    self._naam = naam
    self._email = email
    self.__tegoed = tegoed
    self._betalingsgeschiedenis = []
    print(f"Cursist {self._naam} ingeschreven bij Sessions")
```

Bij het inschrijven van een nieuwe cursist wordt gevraagd om een naam en een e-mailadres; een begintegoed is optioneel. De variabele `_betalingsgeschiedenis` is een lijst (`[]`) waarin alle mutaties worden vastgelegd. Let op de underscores voor de attribuutnamen — daarover zo meer.

## Storten en betalen

Stap 5: de methode `stort()`

```python
def stort(self, bedrag):
    if bedrag > 0:
        self.__tegoed += bedrag
        self._betalingsgeschiedenis.append((Cursist._current_time(), bedrag))
        self.toon_tegoed()
```

Indien het te storten bedrag groter dan nul (`0`) is, wordt het tegoed aangepast en wordt de mutatie toegevoegd aan de lijst `_betalingsgeschiedenis` (zie je wat het datatype is van dat wat er aan de lijst wordt toegevoegd?). Ook het actuele tegoed wordt nu getoond.

Stap 6: de methode `betaal_les()`

```python
def betaal_les(self, bedrag):
    if 0 < bedrag <= self.__tegoed:
        self.__tegoed -= bedrag
        self._betalingsgeschiedenis.append((Cursist._current_time(), -bedrag))
    else:
        print("Het bedrag dient groter dan nul (0) en maximaal gelijk aan het tegoed te zijn")
    self.toon_tegoed()
```

Er vindt een controle plaats of het tegoed toereikend is voor de les. Zo niet, volgt er een passende mededeling. Zo ja, wordt het tegoed bijgewerkt en de mutatie weer in de lijst vastgelegd.

Stap 7: de methode `toon_tegoed()`

```python
def toon_tegoed(self):
    print(f"Tegoed van {self._naam} bedraagt €{self.__tegoed:.2f}")
```

## Betalingsoverzicht

Stap 8: het betalingsoverzicht

```python
def toon_betalingen(self):
    print(f"\nBetalingsgeschiedenis van {self._naam}:")
    for datum, bedrag in self._betalingsgeschiedenis:
        if bedrag > 0:
            mutatie_type = "gestort"
        else:
            mutatie_type = "les betaald"
            bedrag = abs(bedrag)
        print(f"  {datum}: €{bedrag:.2f} {mutatie_type}")
```

In een lus wordt de volledige lijst van mutaties doorlopen en wordt de informatie naar het scherm geschreven.

## Testen

Nu is het tijd om het tegoed te testen!

```python
joyce = Cursist("Joyce", "joyce@email.nl")
joyce.stort(100.0)
joyce.betaal_les(35.0)
joyce.betaal_les(80.0)
joyce.stort(50.0)
joyce.toon_betalingen()
```

Dit geeft de volgende uitvoer:

```console
Cursist Joyce ingeschreven bij Sessions
Tegoed van Joyce bedraagt €100.00
Tegoed van Joyce bedraagt €65.00
Het bedrag dient groter dan nul (0) en maximaal gelijk aan het tegoed te zijn
Tegoed van Joyce bedraagt €65.00
Tegoed van Joyce bedraagt €115.00

Betalingsgeschiedenis van Joyce:
  2026-02-02 14:23:15: €100.00 gestort
  2026-02-02 14:23:15: €35.00 les betaald
  2026-02-02 14:23:16: €50.00 gestort
```

## Private versus Protected attributen

Je ziet in de code dat we twee soorten underscores gebruiken:

- **Enkele underscore** (`_naam`): Dit is een *conventie* in Python om aan te geven dat een attribuut "protected" is. Het is bedoeld voor intern gebruik maar is nog steeds toegankelijk van buitenaf.
- **Dubbele underscore** (`__tegoed`): Dit triggert Python's *name mangling* mechanisme, waardoor het attribuut moeilijker direct toegankelijk wordt van buitenaf.

Laten we dit demonstreren:

```python
joyce = Cursist("Joyce", "joyce@email.nl", 100.0)

# Dit werkt (protected met enkele underscore):
print(joyce._naam)  # Output: Joyce

# Dit werkt NIET (private met dubbele underscore):
print(joyce.__tegoed)  # AttributeError!
```

Het tweede voorbeeld geeft een foutmelding:

```console
AttributeError: 'Cursist' object has no attribute '__tegoed'
```

Python heeft het attribuut `__tegoed` hernoemd naar `_Cursist__tegoed` (name mangling) om directe toegang te voorkomen. Dit is Python's manier om attributen meer "private" te maken, hoewel ze technisch gezien nog steeds toegankelijk zijn via `joyce._Cursist__tegoed`.

## Getters, setters en de @property decorator

Hoe kan de buitenwereld nu tóch op een nette manier bij het tegoed? Daarvoor gebruiken we een *getter* (waarde opvragen) en een *setter* (waarde aanpassen). In veel programmeertalen schrijf je daarvoor methoden als `get_tegoed()` en `set_tegoed()`. Python biedt een elegantere manier: de `@property` decorator.

```python
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
```

Met de `@property` decorator kunnen we het tegoed gebruiken alsof het een gewoon attribuut is, maar achter de schermen worden wel de getter en setter aangeroepen — inclusief de validatie in de setter:

```python
joyce = Cursist("Joyce", "joyce@email.nl", 100.0)

# Gebruik als gewoon attribuut (maar de getter wordt aangeroepen)
print(f"Tegoed: €{joyce.tegoed:.2f}")

# De setter wordt automatisch aangeroepen
joyce.tegoed = 150.0
print(f"Nieuw tegoed: €{joyce.tegoed:.2f}")

# Validatie werkt nog steeds
joyce.tegoed = -10  # Dit wordt afgewezen
```

Uitkomst:

```console
Tegoed: €100.00
Nieuw tegoed: €150.00
Tegoed kan geen negatieve waarde krijgen
```

Je gebruikt dus `joyce.tegoed` in plaats van `joyce.get_tegoed()`, maar de validatie gebeurt nog steeds. Een property zonder setter is ook mogelijk; het attribuut is dan van buitenaf *read-only*:

```python
@property
def volledige_naam(self):
    """Read-only property"""
    return f"{self._naam} ({self._email})"
```

## Waarom inkapseling?

Inkapseling heeft verschillende voordelen:

1. **Controle**: Je kunt validatie toevoegen (zoals in `betaal_les()` waar we checken of het tegoed toereikend is)
2. **Flexibiliteit**: Je kunt later de interne implementatie aanpassen zonder de interface te wijzigen
3. **Beveiliging**: Je voorkomt dat gebruikers per ongeluk of opzettelijk ongeldige waarden instellen

## Samenvatting

In dit deel hebben we geleerd over:

- Inkapseling als OOP-principe
- Het verschil tussen `_` (protected) en `__` (private) attributen
- Het gebruik van `@staticmethod` voor functies die bij de klasse horen
- Het bijhouden van een geschiedenis met tijdstempels
- Getters en setters met de `@property` decorator, inclusief validatie

In het volgende deel gaan we kijken naar overerving: klassen die eigenschappen van andere klassen overnemen.

Maak nu [oefening nummer 1](oefeningen/oop-oefening1.md).
