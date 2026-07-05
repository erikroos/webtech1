# Flask – Installatie

Er zijn meerdere manieren om Flask te installeren en er gelijk mee te kunnen werken. Hier wordt de moderne wijze getoond, waarbij we gebruik maken van de tool [`uv`](https://docs.astral.sh/uv/) in combinatie met een Python *virtuele omgeving*.

## Wat is een virtuele omgeving?

In de kern is het belangrijkste doel van virtuele Python-omgevingen het creëren van een geïsoleerde omgeving voor Python-projecten. Dit betekent dat elk project zijn eigen afhankelijkheden kan hebben, ongeacht welke afhankelijkheden elk ander project heeft. Installeer je voor project A versie 3 van Flask, dan heeft project B daar geen last van. Het mooie hiervan is dat er geen limieten zijn aan het aantal omgevingen: een virtuele omgeving is uiteindelijk niets meer dan een map (directory) met daarin een eigen Python plus de voor dat project geïnstalleerde pakketten.

Onthoud dit concept goed — ook als straks een tool het meeste werk voor ons doet, blijft dit wat er onder de motorkap gebeurt.

## Wat is uv?

[`uv`](https://docs.astral.sh/uv/) is een moderne, zeer snelle tool voor het beheren van Python-projecten. Waar je vroeger losse commando's nodig had om een virtuele omgeving aan te maken (`python -m venv`), te activeren (`activate`) en pakketten te installeren (`pip install`), regelt `uv` dit allemaal in samenhang. In het werkveld zie je `uv` in hoog tempo de oudere werkwijze vervangen — maar die oudere commando's kom je in tutorials en documentatie nog volop tegen; verderop leggen we daarom uit hoe de twee zich tot elkaar verhouden.

## Stappenplan installatie

### Stap 1: open een command line

In thema 1.1 en 1.2 hebben we ook al gewerkt met een command line. Op macOS kun je eenvoudig het programma *Terminal* openen, op Windows gebruik je PowerShell. In alle gevallen kom je als je het programma opstart standaard in je *home directory* (`~/`) terecht.

!!! tip "Microsoft Windows Terminal"

    Op Windows 11 is [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701) de standaard terminal-applicatie; op oudere Windows-versies kun je deze via de Microsoft Store installeren.

    ![Voorbeeld van Windows Terminal](imgs/powershell.png)

Editors als bijvoorbeeld [VSCode](https://code.visualstudio.com/) of [PyCharm](https://www.jetbrains.com/pycharm/) hebben veelal een ingebouwde terminal; voor alle stappen die we nu gaan doorlopen kan je daar natuurlijk ook gebruik van maken.

### Stap 2: installeer uv

Installeer `uv` met één commando:

=== "macOS / Linux"

    ```console
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows (PowerShell)"

    ```console
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

Sluit hierna je terminal en open een nieuwe, zodat het commando `uv` bekend is. Controleer de installatie:

```console
~ $> uv --version
uv 0.7.13
```

(Het exacte versienummer kan afwijken; als er maar een versienummer verschijnt.)

!!! info "Python nog niet geïnstalleerd?"
    Geen probleem: `uv` kan ook Python zelf voor je installeren. Zodra je straks een project aanmaakt, haalt `uv` automatisch een passende Python-versie op als die nog ontbreekt.

### Stap 3: maak een project aan

Maak met `uv init` een nieuw project aan voor alles wat met webtechnologie te maken heeft, en stap er met `cd` (*change directory*) in:

```console
~ $> uv init webtech
Initialized project `webtech` at `/Users/student/webtech`
~ $> cd webtech
~/webtech $>
```

Bekijk met `ls` (*list directory contents*) wat er is aangemaakt:

```console
~/webtech $> ls
main.py  pyproject.toml  README.md
```

Het belangrijkste bestand hier is `pyproject.toml`: hierin houdt `uv` bij welke pakketten (*dependencies*) het project gebruikt. Vergelijkbaar met wat je in week 1 zag bij html: het is gewoon een leesbaar tekstbestand, neem gerust eens een kijkje.

### Stap 4: voeg Flask toe

Om Flask te installeren gebruiken we `uv add`:

```console
~/webtech $> uv add flask
Using CPython 3.13.1
Creating virtual environment at: .venv
Resolved 8 packages in 210ms
Installed 7 packages in 12ms
 + blinker==1.9.0
 + click==8.1.8
 + flask==3.1.0
 + itsdangerous==2.2.0
 + jinja2==3.1.5
 + markupsafe==3.0.2
 + werkzeug==3.1.3
```

Er gebeuren hier twee belangrijke dingen, kijk maar goed naar de output:

1. **`Creating virtual environment at: .venv`** — `uv` heeft automatisch een virtuele omgeving aangemaakt, in de (verborgen) map `.venv` binnen je project. Dáár wordt Flask geïnstalleerd, netjes geïsoleerd van de rest van je systeem.
2. Flask is geïnstalleerd, inclusief de pakketten waar Flask zelf weer van afhankelijk is (zoals `jinja2` en `werkzeug` — die namen gaan we nog vaak tegenkomen).

Bekijk de virtuele omgeving gerust eens van binnen:

=== "macOS / Linux"

    ```console
    ~/webtech $> ls .venv/bin
    activate      activate.csh  flask  pip  python  python3  ...
    ```

=== "Windows"

    ```console
    ~/webtech $> ls .venv\Scripts
    activate  activate.bat  Activate.ps1  flask.exe  python.exe  ...
    ```

Je ziet: een eigen `python`, een eigen `flask`-commando — een mini-Python-installatie speciaal voor dit project. Dit is de virtuele omgeving waar we het hierboven over hadden.

### Stap 5: testen

Met `uv run` voer je een commando uit *binnen* de virtuele omgeving van het project:

```console
~/webtech $> uv run flask --version
Python 3.13.1
Flask 3.1.0
Werkzeug 3.1.3
```

Als laatste test proberen we de Flask-*module* te importeren in de interactieve Python-shell:

```console hl_lines="4"
~/webtech $> uv run python
Python 3.13.1 (main, Dec  3 2024, 17:59:52)
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>> flask.__version__
'3.1.0'
>>>
```

Geen foutmelding: Flask is klaar voor gebruik! Een Python-bestand als `app.py` draai je straks op dezelfde manier: `uv run app.py`.

## Hoe verhoudt dit zich tot pip en activate?

Vóór `uv` (en nog steeds, in heel veel tutorials en documentatie) zag de werkwijze er zo uit:

1. virtuele omgeving aanmaken: `python -m venv webtech`
2. omgeving *activeren*: `source webtech/bin/activate` (macOS/Linux) of `.\webtech\Scripts\activate` (Windows)
3. pakketten installeren met [`pip`](https://pypi.org/project/pip/), de klassieke Python Package Installer: `pip install flask`

Na het activeren wordt de command prompt aangevuld met de naam van de virtuele omgeving tussen haakjes — het teken dat alle commando's (`python`, `pip`, `flask`) vanaf dat moment naar de virtuele omgeving verwijzen:

![Voorbeeld van een geactiveerde virtuele omgeving in Windows PowerShell](imgs/powershell_activate.png)

`uv` doet exact hetzelfde, alleen automatisch: `uv add` maakt de omgeving aan en installeert erin, `uv run` voert commando's erbinnen uit zonder dat je hoeft te activeren. Activeren kán overigens nog steeds — de scripts staan gewoon in `.venv` — en dat is handig om te weten als je editor of een tutorial erom vraagt:

=== "macOS / Linux"

    ```console
    ~/webtech $> source .venv/bin/activate
    (webtech) ~/webtech $> python app.py
    ```

=== "Windows"

    ```console
    ~/webtech $> .venv\Scripts\activate
    (webtech) ~/webtech $> python app.py
    ```

!!! notice "In het vervolg van deze module"
    In de lesstof gebruiken we `uv run` om Python-bestanden te draaien en `uv add` om pakketten toe te voegen. Kom je ergens `pip install <pakket>` tegen (bijvoorbeeld in externe documentatie), dan is het equivalent dus `uv add <pakket>`. Zie je in een voorbeeld `python bestand.py` staan, dan werkt dat na activeren van de virtuele omgeving, of je gebruikt `uv run bestand.py`.

!!! info "requirements.txt"
    Op [de startpagina](../index.md) staat een `requirements.txt`-bestand met de exacte versies waarmee al het lesmateriaal is getest. Zo'n bestand somt de dependencies van een project op, inclusief versienummers. Wil je precies die versies gebruiken, download het bestand dan naar je projectmap en voer uit:

    ```console
    ~/webtech $> uv add -r requirements.txt
    ```
