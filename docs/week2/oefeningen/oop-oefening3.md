# OOP Python – Oefening 3

In deze oefening gaan we de klasse `Les` uit deel 4 verder uitbreiden. Vertrek vanuit [`les.py`](../bestanden/muziekschool/les.py) en [`persoon.py`](../bestanden/muziekschool/persoon.py).

## a. Inschrijfnummer toevoegen

Pas de code van `les.py` zodanig aan dat elke les automatisch een uniek lesnummer krijgt. Je kunt hiervoor een class-attribuut gebruiken dat bij elke nieuwe les opgehoogd wordt.

**Tip:** een class-attribuut wordt gedefinieerd buiten de `__init__()`-methode en wordt aangeroepen met de klassenaam ervoor, bijvoorbeeld: `Les._volgend_nummer`.

## b. Lespakket toevoegen

Sessions biedt verschillende lespakketten aan: een losse les, een strippenkaart (10 lessen) of een jaarabonnement. Maak een nieuwe klasse `Lespakket` met de volgende eigenschappen:

- **type**: het soort pakket ("Losse les", "Strippenkaart", "Jaarabonnement")
- **prijs**: de prijs van het pakket
- **aantal_lessen**: het aantal lessen dat het pakket omvat

Pas vervolgens de klasse `Cursist` (uit `persoon.py`) aan zodat een cursist bij het inschrijven voor een les een `Lespakket`-object mee kan krijgen. Zorg ervoor dat het pakket ook getoond wordt bij `toon_deelnemers()`.

## c. Jeugdkorting toevoegen (optionele uitdaging)

Cursisten die jonger zijn dan 18 jaar krijgen 25% korting op hun lespakket. Voeg aan de klasse `Cursist` een methode `bereken_pakketprijs()` toe die op basis van het geboortejaar bepaalt of de korting van toepassing is, en de juiste prijs teruggeeft en toont.

Verwachte output:

```console
Lespakket Strippenkaart voor Roos: €297.50 (25% jeugdkorting toegepast)
Lespakket Strippenkaart voor Joyce: €350.00
```

## d. Instrumentverhuur koppelen (nog een optionele uitdaging)

Combineer dit met het verhuursysteem uit oefening 2: geef een `Cursist` een attribuut `gehuurde_instrumenten` (een lijst) en een methode `huur_instrument(instrument)` die het instrument verhuurt (via `instrument.verhuur(1)`) en aan de lijst toevoegt. Laat in een testscript een cursist een lespakket kiezen én een instrument huren, en print daarna een compleet overzicht van deze cursist.

Als dit gelukt is kun je jezelf feliciteren: je hebt het complete datamodel van een muziekschool gebouwd met overerving én compositie — precies de structuur die in week 5 terugkomt als database-model!
