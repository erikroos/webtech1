# OOP Python – Oefening 2

In deze oefening breiden we het verhuursysteem van Sessions uit met overerving. Vertrek vanuit de klasse `Instrument` uit [`instrument.py`](../bestanden/muziekschool/instrument.py).

## a. Subklassen maken

Maak twee subklassen van `Instrument`:

- `SnaarInstrument`, met een extra attribuut `_aantal_snaren`
- `Blaasinstrument`, met een extra attribuut `_materiaal` (bijvoorbeeld "koper" of "hout")

Geef beide klassen een eigen `__init__()` die met `super().__init__()` de constructor van `Instrument` aanroept. Test de klassen door een paar instanties aan te maken en te printen, bijvoorbeeld een westerngitaar (6 snaren) en een trompet (koper).

## b. Overriding

Bij Sessions geldt: wie een blaasinstrument huurt, betaalt eenmalig €25,00 reinigingskosten (hygiëne!). Override de methode `verhuur()` in de klasse `Blaasinstrument` zodanig dat:

- eerst een melding wordt getoond over de reinigingskosten,
- daarna via `super().verhuur(aantal)` de gewone verhuurlogica wordt uitgevoerd.

Verwachte uitvoer:

```console
Let op: voor Trompet geldt €25.00 reinigingskosten per verhuur
Verhuurd: 1x Trompet. Nog 3 beschikbaar
```

## c. Polymorfisme

Maak een lijst met verschillende instrumenten (minimaal één `Instrument`, één `SnaarInstrument` en één `Blaasinstrument`) en loop er met een `for`-lus doorheen waarbij je elk instrument print en er één exemplaar van verhuurt. Als het goed is zie je bij het blaasinstrument automatisch de reinigingsmelding verschijnen en bij de andere instrumenten niet — zonder dat de lus daar iets van hoeft te weten. Dat is polymorfisme!

## d. Extra uitdaging

Geef `SnaarInstrument` een methode `vervang_snaren()` die meldt dat de snaren vervangen zijn. Wat gebeurt er als je deze methode aanroept op een `Blaasinstrument`? Verklaar de foutmelding.
