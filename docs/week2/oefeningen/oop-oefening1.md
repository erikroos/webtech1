# OOP Python – Oefening 1

Bekijk nogmaals het bestand [`cursist.py`](../bestanden/muziekschool/cursist.py). Het programma is nog niet helemaal perfect. Kijk naar de volgende coderegels voor een nieuwe cursist, die bij inschrijving direct een begintegoed meekrijgt:

```ipython
In [1]: run "cursist"

In [2]: bram = Cursist("Bram", "bram@email.nl", 250.0)
Cursist Bram ingeschreven bij Sessions

In [3]: bram.stort(50.0)
Tegoed van Bram bedraagt €300.00

In [4]: bram.betaal_les(35.0)
Tegoed van Bram bedraagt €265.00

In [5]: bram.toon_betalingen()
Betalingsgeschiedenis van Bram:
  2026-02-02 14:23:15: €50.00 gestort
  2026-02-02 14:23:15: €35.00 les betaald
```

Er is iets nog niet helemaal goed gegaan. De eerste mutatie, het begintegoed van €250,00, is niet in de betalingsgeschiedenis te zien. Graag een oplossing hiervoor.

**Extra:** voeg ook een property `email` toe (getter én setter). De setter mag alleen waarden accepteren waar een `@` in voorkomt — anders volgt een nette melding en blijft het oude e-mailadres staan.
