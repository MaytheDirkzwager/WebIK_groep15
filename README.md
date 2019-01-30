# Boombazled
## Projectvoorstel Groep 15
*Gemaakt door Julian El-Fasih, Maythe Dirkzwager & Soufian el Ouaâzizi*
 1. Samenvatting
 2. Schets
 3. Features
 4. Repository
 5. Taakverdeling

## 1. Samenvatting
Het doel van de webapplicatie is om twee of meer spelers gelijktijdig vragen te laten beantwoorden en hiermee punten te scoren. Als een bepaalde hoeveelheid punten is behaald, kunnen er kaarten met speciale bonussen worden ingezet. Als een vooraf ingesteld puntenaantal wordt behaald, dan heeft deze speler het spel gewonnen. Het spel is gebaseerd op een niet volledig uitgewerkte versie van een spel dat wordt geïntroduceerd in aflevering 20 van seizoen 8 van Friends.
## 2. Schets
**![](https://lh6.googleusercontent.com/RjUfnCriIrnfD28RRzgKcneKv7BnyZwl2mJDPhPDGcHZQ8y17v8JCHKG6ulj9Z-QxbILJSItqH5Tu1xMouoEfrKNG46LjFNEUyLtn0uRnKykehM2DLHpgNU0HPo7eM1G9ynFfhrK)**
Bovenstaande afbeelding geeft een impressie van de verschillende schermen die in onze webapplicatie te vinden zijn.
De hele presentatie met de losse schermen is te vinden via deze [link](https://prezi.com/kegmqcrojm20/welcome-to-bamboozled/?utm_campaign=share&utm_medium=copy).

## 3. Features
1. **Gebruikers kunnen een spel aanmaken en hier minimaal twee spelers aan toevoegen en een maximaal aantal ronden instellen**
2. **Gebruikers kunnen om beurten vragen beantwoorden**
    - Er is bovenaan de pagina een vraag te zien
    - Onderaan kan er een antwoord worden gekozen
    - Bij iedere vraag kan worden gekozen uit vier antwoordopties
3. **Gebruikers na iedere vraag:**
    - **zien of de beantwoorde vraag juist of onjuist was**
    - **hun totaal behaalde punten zien**
    - de punten van alle spelers zien
    - het aantal gespeelde ronden zien
4. Gebruikers krijgen na iedere goed beantwoorde vraag één van de vier kaarten:
    - Ladder of Chance to the Golden Mud Hut: Kies een getal tussen 1 en 10, bij goed antwoord heeft de speler meteen gewonnen.
    - Googl Card: Je krijgt twee gratis punten.
    - Hungry Monkey: Je krijgt alle punten van de speler met de meeste punten.
    - Banana turn: De eerstvolgende speler moet een beurt overslaan.
    
5. **Gebruikers kunnen zien wanneer ze gewonnen hebben**

Dikgedrukte punten behoren tot de *minimum viable product*.

## 4. Repository
 - **application.py**: routes voor de index, de gamepagina, de kaarten en voor het winscherm.
 - **helpers.py**: functies voor het genereren van een vraag met antwoorden, voor het genereren van een spelcode, voor het verkrijgen van één van de vier kaarten en voor het kiezen van de categorieën.
 - **boombazled.db**: database met één tabel waarin van iedere speler de nickname, score en de spelcode wordt opgeslagen.
 - **static/**: map met CSS bestand.
 - **templates/**: map met de vier html pagina's (card, game, index en lobbyWin).
 
 ## 5. Taakverdeling
 In dit project hebben alle groepsgenoten ongeveer evenveel bijgedragen aan het eindproduct. Iedereen heeft bijgedragen aan application.py en aan de html pagina's. Soufian is vooral bezig geweest met de trivia API, Julian heeft zich gefocust op de vragen en de opmaak hiervan en Maythe is bezig geweest met het implementeren van de kaarten. Gezamenlijk is er een eindproduct geleverd dat voldoet aan de hierboven genoemde eisen. 

