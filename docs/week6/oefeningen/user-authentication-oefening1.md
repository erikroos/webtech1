# User authentication - Oefening 1

In deze afsluitende oefening beveilig je een bestaande site met een inlogsysteem. Gebruik daarvoor de mentor-site die je in [oefening 1 van week 5](../../week5/oefeningen/flask-views-oefening1.md) hebt gebouwd — of, nog beter, het project waar je met je duo aan werkt.

Het is de bedoeling dat je de theorie van deze week toepast:

1. **Model**: voeg een model `User` toe met een gebruikersnaam/e-mailadres en een *gehashed* wachtwoord (dus nooit het wachtwoord zelf!). Gebruik `UserMixin` en een `user_loader`, zoals in de theorie.
2. **Formulieren**: maak een registratie- en een inlogformulier met `FlaskForm`.
3. **Views**: voeg routes toe voor `/register`, `/login` en `/logout`.
4. **Beveiliging**: scherm de pagina's waarop gegevens gewijzigd kunnen worden (toevoegen en verwijderen van studenten en docenten) af met `@login_required`. Het overzicht mag publiek blijven.
5. **Navigatie**: toon in de navigatiebalk 'Inloggen'/'Registreren' voor anonieme bezoekers en 'Uitloggen' voor ingelogde gebruikers. Gebruik hiervoor `current_user.is_authenticated` in je template.

Test het geheel: registreer een gebruiker, log in, wijzig gegevens, log uit en controleer dat de beveiligde pagina's daarna netjes naar de inlogpagina doorverwijzen.

**Extra uitdaging:** toon na het inloggen een flash-bericht met de naam van de gebruiker, en zorg ervoor dat een al ingelogde gebruiker die naar `/login` gaat direct wordt doorgestuurd naar de homepagina.

!!! Tip "Voor je project"
    Dit is exact het onderdeel "Geregistreerde bezoekers kunnen op de site inloggen" uit [de beoordeling](../../index.md#toetsing). Werk deze oefening dus meteen uit in je projectcode — twee vliegen in één klap.
