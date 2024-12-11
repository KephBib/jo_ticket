# Exercice "JO Tickets"

![Logo](../../assets/jo_paris.jpg)

👉 À réaliser après avoir lu le cours "Advanced 3"

## 📜 Situation

Cette année se déroule les **Jeux Olympiques** 2024 à Paris ! Le CIO (Comité International Olympique) décide donc de faire appel à une équipe Française pour s'occuper de la billetterie, et coup de chance vous êtes choisi !

Votre équipe décide de vous confier la génération de ticket des matchs de football de la compétition : 16 équipes, 7 stades et 32 matchs à prévoir. Les pays en compétition seront les suivants :

- France
- États-Unis
- Guinée
- Nouvelle-Zélande
- Argentine
- Maroc
- Indonésie
- Ukraine
- Ouzbékistan
- Espagne
- Égypte
- Rep. Dominicaine
- Japon
- Paraguay
- Mali
- Israël

Voici le calendrier des rencontres :

| Date            | Match                  | Affiche                                      |
| --------------- | ---------------------- | -------------------------------------------- |
| 24 Juillet 2024 | Match 1 Groupe C       | Espagne - Ouzbékistan                        |
| 24 Juillet 2024 | Match 1 Groupe B       | Argentine - Maroc                            |
| 24 Juillet 2024 | Match 1 Groupe A       | Guinée - Nouvelle-Zélande                    |
| 24 Juillet 2024 | Match 2 Groupe C       | Égypte - Rep. Dominicaine                    |
| 24 Juillet 2024 | Match 1 Groupe D       | Japon - Paraguay                             |
| 24 Juillet 2024 | Match 2 Groupe B       | Indonésie - Ukraine                          |
| 24 Juillet 2024 | Match 2 Groupe D       | Mali - Israël                                |
| 24 Juillet 2024 | Match 2 Groupe A       | France - États-Unis                          |
| --------------- | ---------------------- | -------------------------------------------- |
| 27 Juillet 2024 | Match 3 Groupe C       | Espagne - Rep. Dominicaine                   |
| 27 Juillet 2024 | Match 3 Groupe B       | Argentine - Indonésie                        |
| 27 Juillet 2024 | Match 4 Groupe B       | Ukraine - Maroc                              |
| 27 Juillet 2024 | Match 4 Groupe C       | Ouzbékistan - Égypte                         |
| 27 Juillet 2024 | Match 3 Groupe D       | Israël - Paraguay                            |
| 27 Juillet 2024 | Match 3 Groupe A       | Nouvelle-Zélande - États-Unis                |
| 27 Juillet 2024 | Match 1 Groupe D       | Japon - Mali                                 |
| 27 Juillet 2024 | Match 1 Groupe A       | France - Guinée                              |
| --------------- | ---------------------- | -------------------------------------------- |
| 30 Juillet 2024 | Match 5 Groupe C       | Rep. Dominicaine - Ouzbékistan               |
| 30 Juillet 2024 | Match 6 Groupe C       | Espagne - Égypte                             |
| 30 Juillet 2024 | Match 5 Groupe B       | Ukraine - Argentine                          |
| 30 Juillet 2024 | Match 6 Groupe B       | Maroc - Indonésie                            |
| 30 Juillet 2024 | Match 5 Groupe A       | États-Unis - Guinée                          |
| 30 Juillet 2024 | Match 6 Groupe A       | Nouvelle-Zélande - France                    |
| 30 Juillet 2024 | Match 5 Groupe D       | Paraguay - Mali                              |
| 30 Juillet 2024 | Match 6 Groupe D       | Israël - Japon                               |
| --------------- | ---------------------- | -------------------------------------------- |
| 02 Aout 2024    | Quart de final 1       | 1B - 2A                                      |
| 02 Aout 2024    | Quart de final 2       | 1D - 2C                                      |
| 02 Aout 2024    | Quart de final 3       | 1C - 2D                                      |
| 02 Aout 2024    | Quart de final 4       | 1A - 1B                                      |
| --------------- | ---------------------- | -------------------------------------------- |
| 05 Aout 2024    | Demi final 1           | ? - ?                                        |
| 05 Aout 2024    | Demi final 2           | ? - ?                                        |
| --------------- | ---------------------- | -------------------------------------------- |
| 09 Aout 2024    | Matche 3eme place      | ? - ?                                        |
| 09 Aout 2024    | Finale                 | ? - ?                                        |

Pour ce qui est des billets, ils seront vendus selon 3 catégories, et avec plusieurs choix de devises pour faciliter l'achat à l'international : euro (EUR) et dollar (USD).

| Catégorie            | Placement | Prix EUR | Prix USD |
| -------------------- | --------- | -------- | -------- |
| Catégorie "Silver"   | Libre     | 100 EUR  | 110 USD  |
| Catégorie "Gold"     | Attribué  | 150 EUR  | 165 USD  |
| Catégorie "Platinum" | Attribué  | 200 EUR  | 220 USD  |

## 🏁 Objectifs

Afficher la liste des billets (place, prix, équipes, stade et ville) disponible avec un numéro correspondant (1 pour le premier, 2 pour le deuxième)

Demandez à l'utilisateur combien de billet il souhaite imprimer, puis demandez lui de choisir lesquels. Pour éviter toute faute de frappe on lui demande de saisir le numéro du billet afficher au dessus

Vous êtes en charge de la génération des billets dans leur version française. Pour cela, l'entreprise qui s'occupe de la vente des billets en ligne vous a fourni plusieurs choses :

- Un export de leur base de données, avec 1 fichier JSON correspondant à 1 table
- L'image de fond à utiliser pour les billets

Vous devez créer un programme permettant de générer des billets à partir de la liste fourni en JSON. Ces billets devront être sauvegardé dans le dossier `tickets`

### Formatage des données

Vu que l'API permettant de récupérer ces informations en temps réel n'existe pas encore, on vous a fourni des extraits de la base de données sous forme de documents JSON, chaque fichier correspondant à une table :

- `stadiums.json` contient la liste des stades utilisés lors du tournoi
- `events.json` contient la liste des matchs
- `tickets.json` contient la liste des billets à éditer

Vous y retrouverez notamment les ID (clés étrangères) utilisés dans la base de données pour faire référence à d'autres tables. La valeur `event_id` présente sur un élément du fichier `tickets.json` fera donc référence à un match du fichier `events.json`, etc.

Pour identifier chaque ticket, utiliser un simple nombre qui s'auto-incrémente aurait été délicat car trop simple à deviner, facilitant ainsi la fraude aux faux billets. On utilise à la place des [**UUID**](https://fr.wikipedia.org/wiki/Universally_unique_identifier) quasi-uniques pour numéroter chaque billet, la base de donnée d'origine [(PostgreSQL)](https://www.postgresql.org/docs/current/datatype-uuid.html) s'occupant d'éviter l'insertion tout doublon.

### Écriture sur le billet

Votre tâche sera d'abord de lire les trois documents JSON, d'éventuellement ranger et recouper leurs données, puis il faudra ensuite boucler sur **chaque billet** pour écrire leurs informations et le QR Code sur l'image de fond, qui sera sauvegardée dans le dossier `tickets`.

Pour le texte à imprimer sur le billet, il faudra impérativement utiliser la police d'écriture de la charte graphique du tournoi, à savoir **Paris2024**. Le nom des équipes devront être écrits en **bleu** (le même que celui du ticket) noté (51, 19, 104) taille 36px, et le reste du texte en **blanc** taille 22px, avec la police **"Paris2024"**. L'entreprise vous a fourni les fichiers à utiliser, dans le dossier `fonts`.

Vous partez de données formatées en anglais (sauf pour le nom des équipes) et il faudra donc prendre en compte cela. Les dates sont stockées au format [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601) avec l'heure correspondant au fuseau horaire de Paris, et correspondant à +2 heures par rapport à UTC. Sur le billet, la date devra être affichée au format "jour/mois/année" et l'heure du match au format "heures:minutes", grâce à l'usage de la [bibliothèque standard datetime](https://docs.python.org/fr/3/library/datetime.html). Si un billet n'a pas de place définie (valeur "free"), on devra écrire "Libre".

Le code-barres bidimensionnel de type **QR Code** a été choisi pour assurer un scan rapide des billets, qu'ils soient imprimés ou présentés sur un smartphone. Son contenu devra simplement correspondre à l'ID du billet.

Pour cela, on vous propose d'installer et d'utiliser la bibliothèque Python `qrcode` dont la documentation est sur [PyPI](https://pypi.org/project/qrcode/). Son usage n'est pas très complexe, mais on vous a fourni un exemple fonctionnel dans le fichier `test_qr.py`.

Enfin, l'entreprise d'impression vous a envoyé les positions x,y de chaque texte ainsi que celles du QR Code :

* 126, 835 : QR Code
* 37, 426 : Équipe domicile (1ere ligne)
* 112, 503 : Équipe extérieur (2nde ligne)
* 60, 588 : Nom du stade + ville
* 60, 656 : Date & heure de début du match
* 20, 756 : Catégorie
* 200, 756 : Place
* 325, 756 : Prix du billet

## ⭕ Conditions de réussite

- ✔️ Chaque image générée correspond à un billet du fichier `tickets.json`
- ✔️ Toutes les informations du billet, du stade et du match sont écrites de façon lisible (format de date, devise...)
- ✔️ Le prix du billet est suivi d'un `$` ou d'un `€` selon la devise
- ✔️ Un billet sans place attribuée indique "Libre"

## ☝ Conseils

Faites attention, lors de l'écriture de votre code, à ne pas trop mélanger anglais et français, et à utiliser le bon lexique selon la langue : "billet" en français mais "ticket" en anglais, etc. Dans le cas présent, les données qui vous sont fournies sont en anglais, et il vaut mieux s'en tenir à l'anglais lorsque l'on travaille avec un partenaire international. (Vous pouvez garder les commentaires en français, ça reste un exercice !)

Faire un jeu de test peut aussi être une bonne idée, tester sur 1 ticket avant de tester sur l'ensemble des tickets
