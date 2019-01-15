# Technisch Ontwerp Groep 15
*Gemaakt door Julian, Maythe & Soufian*
1. Controllers
2. Views
3. Models/helpers
4. Plugins/frameworks

## 1. Controllers
De volgende functies willen wij gaan implementeren in application.py:
+ def index (POST request)
    - Nickname invullen
    - Spel maken (dit maakt de gebruiker een host, waarmee anderen kunnen verbinden)
    - Spel joinen (door geheime code in te vullen die een host heeft gekregen)
    - HTML pagina's
        * index.html
        * index_invalid_id.html (als er niet is ingevuld in het nickname veld, run pagina met extra informatie)
+ def lobby (POST request)
    - Wachtruimte tot alle spelers aanwezig zijn
    - Spel beginnen (alleen voor host)
    - Instellingen (alleen voor host)
        * Thema kiezen
    - Spel verlaten
    - Na afloop spel wordt definitie gebruiker met andere opties:
        * Resultatenoverzicht
        * Optie om opnieuw een spel te spelen
    - HTML pagina's
        * lobby_host.html
        * lobby_player.html
        * newlobby.html (inclusief winstscherm)
        * gamesettings.html
+ def game (POST request)
    - Triviavraag
    - Antwoord opties (4 opties, A/B/C/D)
    - Scorebord
    - Instellingen
        * Voor host: sessie stoppen
        * Voor spelers: spel verlaten
    - Kaart (bij goed antwoord)
    - HTML pagina's
        * game.html
        * sessionsettings.html

## 2. Views
**![](https://lh6.googleusercontent.com/RjUfnCriIrnfD28RRzgKcneKv7BnyZwl2mJDPhPDGcHZQ8y17v8JCHKG6ulj9Z-QxbILJSItqH5Tu1xMouoEfrKNG46LjFNEUyLtn0uRnKykehM2DLHpgNU0HPo7eM1G9ynFfhrK)**

## 3. Models/helpers
De volgende functies willen wij gaan implementeren in helpers.py:
+ def apology()
    - Geef de html pagina waar je eerder op was, maar met een balk bovenin die zegt dat het niet gelukt is
+ def get_questin(amount = 1, type = multiple, category, difficulty)
    - Geeft een random vraag terug uit de volgende API: [Open Trivia Database](https://opentdb.com)

## 4. Plugins/frameworks
+ **Open Trivia Database**: Database vol met vragen met de mogelijkheid tot multiplechoice, onderverdeeld in zowel moeilijkheidsgraad als thema.
        Door middel van de een helpers-functie kunnen we makkelijk een vraag aanroepen uit de API voor het triviaspel.
+ **Bootstrap**: Functies voor html-pagina’s. Biedt allerlei extra’s voor het opmaken van de website-pagina’s.

