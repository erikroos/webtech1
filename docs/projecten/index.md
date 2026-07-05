# Casuïstiek voor het project

Liefst zo snel mogelijk, in ieder geval vanaf week drie, werken studenten in duo's aan hun eigen project, waarbij de volgende onderdelen van belang zijn:

- Website heeft vormgeving en een koppeling met een database
- Op de site ingevulde data komt door sqlalchemy terecht in een sqlite-database
- Website maakt gebruik van verschillende views
- Geregistreerde bezoekers kunnen op de site inloggen

Wanneer studenten zelf geen project kunnen bedenken, is het prima één van de onderstaande projecten uit te voeren:

1. [Bungalowpark Bos en Duin](bungalowpark.md)
2. [Website Filmfan](filmfan.md)
3. [Programmeerles voor gepensioneerden](programmeerles.md)
4. [Stage lopen](stage.md)

Kies één van deze casussen en laat aan je practicumdocent weten welke casus je gaat doen en met wie. Het advies is om je practicumdocent geregeld om feedback te vragen. Het kan zijn dat je practicumdocent een klassikaal moment inplant waarop elk duo hun idee en eventueel begin van de uitwerking aan de gehele groep kort presenteert.

## Uitgebreide planning

### Week 1-2
Regel de IDE en de ontwikkelomgeving. Inventariseer welke bestanden nodig zijn (py en html) en bedenk het ontwerp en de vormgeving van de site.

### Week 3
Maak de belangrijkste bestanden `app.py` en de eerste templates aan: `base.html` en `home.html` in de folder templates (in `base.html` wordt de navigatiebalk opgezet, denk hier goed over na).
Maak ook templates en formulieren voor de andere pagina's uit je ontwerp.

Test de werking en met name de interactie van de site.

### Week 4
Ontwerp de databasestructuur voor je project: welke tabellen (modellen) zijn er nodig en hoe verhouden die zich tot elkaar?

### Week 5
Maak de bestanden `models.py`, `forms.py` en `views.py` aan en koppel de site aan de database.
Vul ook de folder templates aan met de specifiek voor elk model beschikbare html-bestanden. Zorg ervoor dat de betreffende data via de website benaderd en eventueel aangepast kan worden.

### Week 6
Zorg voor een inlogsysteem en zorg dat specifieke onderdelen alleen voor ingelogde bezoekers beschikbaar zijn.
