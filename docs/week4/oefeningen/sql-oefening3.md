# Oefening 3

In week 2 hield de klasse `Cursist` het lestegoed en de betalingsgeschiedenis nog bij in het geheugen — weg programma, weg gegevens. Bij Sessions staat die informatie inmiddels in een database: de tabel `cursisten` (naam en actueel tegoed) en de tabel `betalingen` (tijdstip, cursist en bedrag).

Download de bestanden [`checkdb.py`](checkdb.py) en [`sessions.sqlite`](sessions.sqlite) en zet ze samen in een projectmap. Run `checkdb.py` en bekijk wat er gebeurt: alle betalingen worden getoond, met zowel de UTC-tijd als de lokale tijd.

Pas `checkdb.py` vervolgens zo aan dat:

1. er aan de gebruiker gevraagd wordt om de naam van één van de cursisten (bijvoorbeeld Joyce),
2. alleen de betalingen van díe cursist naar het scherm geschreven worden,
3. tot slot ook het actuele tegoed van deze cursist uit de tabel `cursisten` getoond wordt.

Maak uiteraard gebruik van placeholders en parameter substitution — na het deel over SQL-injectie weet je waarom!
