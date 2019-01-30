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
    - Spel maken
    - Spelers toevoegen
    - Categorieën kiezen
    - Aantal rondes kiezen
    - HTML pagina's
        * index.html
+ def game (POST request)
    - Triviavraag
    - Antwoord opties (4 opties, A/B/C/D)
    - Scorebord
    - Spel verlaten
    - HTML pagina's
        * game.html
+ def card (POST request)
    - Kaart (na een goed antwoord)
    - Beschrijving van de kaart
    - Toepassen effect kaart op score
    - Terug naar game-pagina
        * card.html

## 2. Views
**![](https://lh6.googleusercontent.com/RjUfnCriIrnfD28RRzgKcneKv7BnyZwl2mJDPhPDGcHZQ8y17v8JCHKG6ulj9Z-QxbILJSItqH5Tu1xMouoEfrKNG46LjFNEUyLtn0uRnKykehM2DLHpgNU0HPo7eM1G9ynFfhrK)**
Bovenstaande afbeelding geeft een impressie van de verschillende schermen die in onze webapplicatie te vinden zijn.
De hele presentatie met de losse schermen is te vinden via deze [link](https://prezi.com/kegmqcrojm20/welcome-to-bamboozled/?utm_campaign=share&utm_medium=copy).


## 3. Models/helpers
De volgende functies willen wij gaan implementeren in helpers.py:
+ def getQuestion(categories)
    - Input categorieën levert vraag, antwoord en verkeerde opties
+ def get_password()
    - Genereert wachtwoord van vier tekens, letters en cijfers
+ def get_card()
    - Kiest een willekeurige kaart en geeft deze terug
+ def get_categories()
    - returnt alle geselecteerde categorieën uit het index-scherm in een lijst

## 4. Plugins/frameworks
+ **Open Trivia Database**: Database vol met vragen met de mogelijkheid tot multiplechoice, onderverdeeld in zowel moeilijkheidsgraad als thema.
        Door middel van de een helpers-functie kunnen we makkelijk een vraag aanroepen uit de API voor het triviaspel.
+ **Bootstrap**: Functies voor html-pagina’s. Biedt allerlei extra’s voor het opmaken van de website-pagina’s.

