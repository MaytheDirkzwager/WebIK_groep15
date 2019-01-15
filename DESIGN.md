# Technisch Ontwerp Groep 15
*Gemaakt door Julian, Maythe & Soufian*
1. Controllers
2. Views
3. Models/helpers
4. Plugins/frameworks

## 1. Controllers
De volgende functies willen wij gaan gebruiken in application.py:
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

