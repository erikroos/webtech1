# Oefening 4

De administratie van Sessions wil snel kunnen uitrekenen wat een cursist gemiddeld per les betaald heeft. Maak een Python-script dat de gebruiker vraagt om een totaalbedrag en om een aantal gevolgde lessen, en dat als eindresultaat het bedrag per les laat zien (de deling van het eerste getal door het tweede).

Het programma mag niet crashen, ongeacht welke waarden er worden ingevoerd — denk aan tekst in plaats van een getal, of nul lessen. Zorg voor een nette foutafhandeling. Mochten er acties vaker uitgevoerd worden, is het handig om van een functie gebruik te maken.

Door foute invoer te proberen, kunnen de Built-in Exceptions gemakkelijker gevonden worden.

## Bonus-oefening

Het programma levert nog een fout op als de toetsencombinatie ++ctrl+d++ wordt ingetoetst. Om dat te voorkomen moet als eerste `sys` geïmporteerd worden om vanaf de command-line het programma op een nette wijze af te sluiten met `sys.exit()`. Los dit probleem op.
