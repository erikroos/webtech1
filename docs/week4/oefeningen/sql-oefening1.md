# Oefening 1

## Opgave 1

Maak gebruik van sqlite om de database `sessions.sqlite` te maken.

## Opgave 2

Muziekschool Sessions wil haar docenten in een database bijhouden. Maak een tabel aan met de naam `docent`. Deze tabel moet de volgende attributen hebben:

kolomnaam | eigenschappen
---- | ----
`ID` | Integer primary key NOT NULL
`Naam` | Text NOT NULL
`Instrument` | Text NOT NULL
`Uurtarief` | Real NOT NULL

## Opgave 3

Voeg de volgende gegevens toe:

ID | Naam | Instrument | Uurtarief
---|---|---|---
1 | Bart | Gitaar | 40
2 | Ineke | Piano | 45
3 | Carla | Zang | 42.50
4 | Douwe | Drums | 38

## Opgave 4

Schrijf een query die alle gegevens uit de tabel `docent` afdrukt. Gebruik deze query om telkens de gegevens uit de tabel af te drukken nadat je de volgende wijzigingen hebt doorgevoerd:

- Wijzig het uurtarief van het record met ID 1. Het uurtarief wordt nu 42.50.
- Wijzig de naam van het record met ID 2 in Ineke-Marije.
- Verwijder het record met ID 4.

## Opgave 5

Sluit sqlite weer af. Merk op dat er nu een bestand `sessions.sqlite` op je filesystem is aangemaakt. Dit bestand komt in oefening 3 nog van pas.
