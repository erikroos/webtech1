# HTML – Formulieren


Een erg belangrijke schakel tussen een bezoeker en een website of applicatie zijn *formulieren*. Formulieren stellen gebruikers in staat in te loggen, bestellingen te plaatsen, gericht te zoeken naar informatie met behulp van zoekschermen en nog veel meer.

HTML-formulieren worden op een webpagina geplaatst met behulp van de tag `<form>`. Een formulier kan aan een bestaand HTML-document toegevoegd worden. Een formulier begint met `<form>` en helemaal aan het einde van het formulier komt te tag `</form>`.te staan. 

```
<form>
  <!-- Hier komt het formulier te staan, -->
  <!-- Dat bestaat uit input-velden, maar ook labels en vragen. -->
  <!-- Helemaal aan het einde sluit je het formulier weer af. -->
</form>
```

## Input-tag
Het HTML-element `<input>` wordt gebruikt om interactieve besturingselementen te maken voor webgebaseerde formulieren. Dit element wordt gebruikt om gegevens van de gebruiker te accepteren en is één van de krachtigst, meest complexe en gevaarlijkste elementen in heel HTML vanwege het enorme aantal combinaties van invoertypen en attributen – én omdat je hiermee de bezoeker de mogelijkheid biedt om contact met de server te maken.

Alle `<input>`-tags kennen het attribuut `type`. Standaard is de waarde hiervan `text`, wat betekent dat er een tekstinput wordt weergegeven.

```
<form>  
  <h2>Hieronder een simpel inputelement</h2>
  <input type="text"> 
</form>
```

![`Een simpel inputelement](imgs/simpel_formulier.png)

!!! info "Tekst input"
    Door gebruik te maken van `type="text"` wordt er een tekstinput-element van één regel gegenereerd (*gerenderd*). Wanneer je een input van meerdere regels tekst wilt hebben, moet je gebruik maken van de tag `<textarea>`. Hier komen we later nog uitgebreid over te spreken. 

### input types 

Er is in een tekstveld in het formulier aangemaakt. We komen er later op terug wat daar exact de bedoeling van is en hoe je dit in je process kunt gebruiken. Er zijn nog veel meer input-types. In de tabel hieronder wordt een aantal veel gebruikte opgesomd.

input type | omschrijving
-----------|--------------
`text`       | voor teksten
`number`     | mag alleen getallen bevatten
`email`      | controleert of het e-mailadres geldig is
`password`   | vervangt de invoer door asterisk of bolletjes
`hidden`     | niet zichtbaar, wordt vaak gebruikt om gegeven in op te slaan die onnodig tot fouten kunnen leiden, bijv. huidige datum bij een order.
`color`      | opent een color-picker
`button`     | toont een knop
`submit`     | knop die de inhoud van het formulier doorstuurt naar de server

Bekijk [de documentatie op MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) voor een volledig overzicht van de `<input>`-tag en de bijhorende attributen.

Een eenvoudig inlogformulier zou door de volgende HTML-regels gebouwd kunnen worden. Het ziet er niet echt fraai uit, maar daar wordt in de volgende paragrafen uitgebreid aandacht aan besteed.

![Een eenvoudig html-formulier](imgs/simpel_form.png)

Het `<form>`-element bepaalt waar en hoe de gegevens verstuurd worden. Daarvoor zijn er nog twee attributen die voor deze tag opgevoerd moeten worden, `method` en `action`.

Met het attribuut `action` kan aangeven worden wáár de informatie uit het formulier naar toe moet worden verzonden (de url van de server die de het formulier verder gaat verwerken). Het attribuut `method` kent twee mogelijke opties: `GET` en `POST`. De `GET`-methode zal de inhoud van het formulier via een URL overbrengen naar de ontvangende partij. De andere methode, `POST`, komt veel beter van pas wanneer er met een database gewerkt wordt. Op het moment dat het werken met Flask besproken gaat worden, zullen we uitgebreid bij deze twee attributen stilstaan.

## Labels

Tijd om het formulier aan te passen. Een aantal verbeteringen zal worden doorgevoerd. Op de eerste plaats is het onduidelijk welk van de twee invoervelden bedoeld is voor het e-mailadres en welk voor het wachtwoord. Dat zijn *labels* voor ontwikkeld.

Met een `<label>` kan aangegeven worden welk element van het formulier een toegevoegde waarde gaat krijgen. Daarvoor moet bij het `<label>`-element het attribuut `for` ingevuld zijn met dezelfde waarde als het attribuut `id` van het beoogde tekstveld. Met deze aanpassingen komt de html van de pagina hierboven er als volgt uit te zien:

```
<form method="get" action="pagina1.html">
  <label for="email">E-mailadres :</label>
  <input type="email" id="email" name="email" placeholder="e-mailadres">
  
  <label for="password">Wachtwoord :</label>
  <input type="password" id="password" name="password" placeholder="wachtwoord">
  
  <input type="submit" value="Verstuur">
</form>
```

!!! info "Extra attributen"
    Zoals je ziet hebben we stiekem nog een paar meer attributen van het `input`-element ingevuld. Zo zie je `name`, `value` en `placeholder` terugkomen. Op de eerste van deze twee komen we later uitgebreid terug. De waarde die het attribuut `value` krijgt zorgt ervoor dat een element op het formulier een standaardwaarde krijgt toegewezen. 
    
    Waar `value` een min of meer vast waarde krijgt zoals bij de Verzend-knop, wordt `placeholder` meer gebruikt als tijdelijke invulling. Op het moment dat het tekstvak geactiveerd wordt, verdwijnt de inhoud en kunnen de gegevens ingevoerd worden.

Stel dat je het formulier zoals dat hierboven is weergegeven zou invullen met de volgende gegevens:

- email: henk@hanze.com
- password: supergeheim

Als je dan op 'Verstuur' zou klikken, zie je het volgende in de adresbalk van je browser staan:

![Niet echt veilig](imgs/niet_veilig.png)

De gegevens worden in de URL opgenomen en doorgestuurd naar de ontvanger. Duidelijk is wel dat er aan GET-methode een aantal nadelen kleven. Net echt fijne security. Later zullen we hier uitgebreid op terugkomen.

## Selecties

### Radio-buttons

Wanneer je wilt dat een bezoeker een keuze maakt uit verschillende opties, kun je gebruik maken van zogenaamde *radio-buttons*. De bezoeker krijgt dan een aantal opties voorgeschoteld met open bolletjes ervoor, en door op zo'n bolletje te klikken selecteert -ie één van deze opties.

```
<form>
         <h3>Bespeelt u al een instrument?</h3>
         <label for="ja">Ja :</label>
         <input type="radio" id="ja" name="janee" value="ja">
         <label for="nee">Nee :</label>
         <input type="radio" id="nee" name= "janee" value="nee">
</form>
```

![Bolletjes als selectie](imgs/bolletjes.png)

Let op het attribuut `name` van de verschillende opties. Doordat deze voor alle bolletjes hetzelfde is (`janee` in het voorbeeld) weet je browser dat de opties bij elkaar horen en dat er van deze opties maar één tegelijktijd geselecteerd mag worden.

### Checkboxes

Een andere vorm van selectie zijn de zogenaamde *selectboxes*. Deze lijken erg op de radio-buttons, maar hebben als belangrijk verschil dat je er *meerdere* tegelijkertijd kunt selecteren:

```
<form method="get">
         <h3>Wel instrument bespeelt u?</h3>
         <input type="checkbox" name="instrument[]" value="Piano">Piano
         <input type="checkbox" name="instrument[]" value="Gitaar">Gitaar
         <input type="checkbox" name="instrument[]" value="Trompet">Trompet
         <input type="checkbox" name="instrument[]" value="Viool">Viool
         <input type="checkbox" name="instrument[]" value="Kerkorgel">Kerkorgel
</form>
```

![Checkboxes als inputmethode](imgs/checkboxes.png)

### Dropdown

Een laatste mogelijkheid voor keuzelijsten die we bespreken is het *drop-down menu*. Het voordeel hiervan ten opzichte van keuzerondjes is dat het minder ruimte in beslag neemt. Maar dat is ook een nadeel, omdat gebruikers niet meteen alle opties kunnen zien. 

Iedere keuzelijst heeft twee elementen nodig: `select` en `option`. De eerste om aan te geven dat het om een keuzelijst handelt en met met de tweede geven we de verschillende opties van deze keuzelijst aan.

```
<form>
<p>Kunt u bladmuziek lezen?</p>
   <select name="bladmuziek">
            <option value="ja">Ja</option>
            <option value="beetje">Beetje</option>
            <option value="nee">Nee</option>
   </select>
</form>
```

![dropdown keuzemenu](imgs/dropdown.png)

De gebruikers zien de waardes Ja, Beetje en Nee opdoemen. Hun keuze wordt vastgelegd onder de naam ’bladmuziek’. En onder die naam kan de keuze naar een tweede pagina gestuurd worden.

## Textarea

Een `textarea` is een extra groot tekstveld dat geschikt is voor het invoeren van een grote hoeveelheid tekst door de gebruiker (de maximale grootte is bepaald door de server die het *request* afhandelt, maar in de regel kan er zo vijf megabyte in). Het kan aan een webpagina worden toegevoegd als een `<textarea>`-element. 

De grootte van het tekstvak kan worden bepaald door een aantal rijen en een aantal kolommen op te geven.

```
<form>
  <p>Heeft u nog opmerkingen?</p>
  <p>Noteer ze in de ruimte hieronder en verstuur de gegevens.</p>
  <textarea name="opmerking" rows="5" cols="60"></textarea>
  <input type="submit" value="Verstuur feedback">
</form>
```

![Textarea](imgs/textarea.png)















