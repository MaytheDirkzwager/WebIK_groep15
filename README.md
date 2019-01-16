# Projectvoorstel Groep 15
*Gemaakt door Julian, Maythe & Soufian*
 1. Samenvatting
 2. Schets
 3. Features
 4. Afhankelijkheden
## 1. Samenvatting
Het doel van de webapplicatie is om twee of meer spelers gelijktijdig vragen te laten beantwoorden en hiermee punten te scoren. Als een bepaalde hoeveelheid punten is behaald, kunnen er kaarten met speciale bonussen worden ingezet. Als een vooraf ingesteld puntenaantal wordt behaald, dan heeft deze speler het spel gewonnen. Het spel is gebaseerd op een niet volledig uitgewerkte versie van een spel dat wordt geïntroduceerd in aflevering 20 van seizoen 8 van Friends.
## 2. Schets
**![](https://lh3.googleusercontent.com/9UGE30yYgStNI4zzRLshat7MBUZgP-lspmVD7h4tnyTMZ4IQqmqaSao5nugyGMl45TRFOteql5uhca9t-AyXxE3IVtpWR7pfDoNkaqWLz-QlScSjBhi-wMyU1wAjqfse-WtJvoYr)**
## 3. Features
1.  **Gebruikers kunnen een spel aanmaken en hier minimaal twee spelers aan toevoegen en een maximaal puntenaantal instellen**
2. **Gebruikers kunnen om beurten vragen beantwoorden**
        - Er is bovenaan de pagina een vraag te zien
        - Onderaan kan er een antwoord worden gekozen
3. **Gebruikers kunnen na iedere vraag:**
        - **zien of de beantwoorde vraag juist of onjuist was**
        - **hun totaal behaalde punten zien**
        - de punten van alle spelers zien
4. Gebruikers kunnen bij een bepaald puntenaantal kiezen voor speciale kaarten om nog meer punten te verdienen
5. **Gebruikers kunnen zien wanneer ze gewonnen hebben**
6. Gebruikers kunnen zien wie de meeste spellen heeft gewonnen
Dikgedrukte punten behoren tot de *minimum viable product*.
## 4. Afhankelijkheden
 - **Benodigdheden**: Voor de triviavragen gebruiken we een triviadatabase: [http://jservice.io](http://jservice.io/).  <br> De API die nuttig lijkt voor onze website is [Qriusity](https://www.programmableweb.com/api/qriusity), een API dat gespecialiseerd voor triviawebsites/-apps.<br>
 - **Externe componenten**: Voor de opmaak van de website zullen we gebruik moeten maken van Bootstrap en SVG (gemaakt om figuren te maken, handig voor optiebalken, wellicht).
 - **Concurrerende bestaande websites**: Ons spel zal elementen bevatten die geïnspireerd zijn door apps als Kahoot, Trivia Crack Piccolo, maar met andere doeleinden.
 - **Moeilijkste delen**: Een uitdaging die we waarschijnlijk tegemoet zullen komen is hoe we precies de unieke kaarten met speciale bonussen zullen moeten coderen. Die moeten we namelijk zelf bedenken, uitwerken en implementeren.