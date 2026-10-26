# Intro
```
Hey,

Je viens de recevoir le rapport de QA pour la phase 1 du projet. Il y a plusieurs bogues, dont un qui fait planter l'application !
Malheureusement, je ne suis pas au bureau pour les prochains jours (un de mes enfants est tombé malade ce week-end).
Je ne sais pas encore quand je pourrai être là dans la semaine. Pourriez-vous prendre en charge la mise en œuvre du projet ?
Vous devrez régler les bogues de la phase 1 et mettre en œuvre les éléments de la phase 2 (j'ai ajouté le travail de la phase 2 et les bogues de la section “issues” du repo).

Vous devrez cloner et forker le repo et le mettre en place sur votre machine locale (tout ce dont vous avez besoin se trouve dans le fichier README).
Ensuite, passez en revue les bogues dans la section des problèmes, puis essayez de reproduire les problèmes sur votre machine locale pour résoudre les bogues et ajouter la gestion des erreurs.
Pour gagner du temps de configuration, nous utilisons Flask et JSON pour éviter d'utiliser une base de données.
La plupart des outils dont vous aurez besoin se trouvent dans le fichier requirements.txt dans le repo,
mais vous devrez installer Flask et notre framework de test préféré, pytest, ainsi que notre outil de test de performance, Locust.

Vous devrez également préparer un rapport de test et un rapport de performances,
conformément au guide de développement à la fin des spécifications fonctionnelles ci-jointes.
Veillez à suivre toutes les directives, car le QA nous reproche de ne pas respecter les normes.
Vous devez tester de manière approfondie les résultats requis (à la fois les happy paths et les sad paths) pour toutes les fonctionnalités de l'application.
Je vous encourage également à adopter une approche de TDD, car cela vous aidera à rationaliser votre travail.

Une fois que vous aurez terminé, nous ferons un examen de ce que vous avez dans la branche QA du code.
Nous examinerons les rapports et la manière dont vous avez résolu les problèmes,
nous examinerons votre code et nous testerons la couverture de la nouvelle fonctionnalité.

Merci !
```

## 1. Why

This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

## 2. Getting Started

This project uses the following technologies:

* Python v3.x+
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

  Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need.

* [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

  This ensures you'll be able to install the correct packages without interfering with Python on your machine.

  Before you begin, please ensure you have this installed globally.

## 3. Installation

- After cloning, change into the directory and type `virtualenv .`. This will then set up a virtual python environment within that directory.
- Next, type `source bin/activate`. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting files outside. To deactivate, type `deactivate`.
- Rather than hunting around for the packages you need, you can install in one step. Type `pip install -r requirements.txt`. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is `pip freeze > requirements.txt`.
- Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be `server.py`. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details.
- You should now be ready to test the application. In the directory, type either `flask run` or `python -m flask run`. The app should respond with an address you should be able to go to using your browser.

Sous Windows (PowerShell), les commandes utilisées pour ce travail sont :

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
$env:FLASK_APP="server.py"
flask run
```

## 4. Current Setup

The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:

* competitions.json - list of competitions
* clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

## 5. Testing

You are free to use whatever testing framework you like - the main thing is that you can show what tests you are using.

Framework utilisé : **pytest**. Les tests sont dans le dossier `tests/`, séparés par type :

* `tests/unit/` : tests unitaires (`test_loaders.py`, `test_views.py`)
* `tests/integration/` : tests d'intégration (`test_routes.py`)
* `tests/performance/` : test de performance Locust (`locustfile.py`)

Répartition : 10 tests unitaires pour 5 tests d'intégration.

Lancer les tests (depuis la racine du projet) :

```powershell
python -m pytest -v
```

### Couverture

We also like to show how well we're testing, so there's a module called
[coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

Configuration : le fichier `.coveragerc` limite la mesure au code de l'application (`server.py`).

```powershell
python -m coverage run -m pytest
python -m coverage report -m
```

Résultat :

```
Name        Stmts   Miss  Cover   Missing
-----------------------------------------
server.py      40      2    95%   40-41
-----------------------------------------
TOTAL          40      2    95%
```

La couverture de `server.py` est de 95 %, au-dessus des 60 % demandés.

Remarque : ce résultat est mesuré sur le code de la branche `main`. Les corrections de bugs sont réparties dans des branches séparées (voir section 8).

## 6. Flake8 Report

Commande exécutée :

```powershell
python -m flake8 server.py tests
```

Résultat : aucun code F (aucune erreur de logique, par exemple variable non définie ou import inutile). Il reste uniquement des remarques de style :

* E231 : espace manquant après une virgule
* E111 / E117 : indentation
* E302 : lignes vides manquantes
* E501 : lignes de plus de 79 caractères
* W292 / W293 : fin de fichier et espaces en fin de ligne

Sortie complète de flake8 (coller ici l'affichage du terminal) :

```
(coller la sortie de : python -m flake8 server.py tests)
```

## 7. Performance Report

Outil : **Locust**, avec 6 utilisateurs (`tests/performance/locustfile.py`).

Objectifs de l'énoncé : moins de 5 secondes pour charger la page des compétitions, moins de 2 secondes pour une mise à jour.

Commande (le site doit tourner dans un autre terminal) :

```powershell
python -m locust -f tests/performance/locustfile.py -H http://127.0.0.1:5000 -u 6 -r 2 -t 30s --headless --html tests/performance/rapport_locust.html
```

Rapport généré : `tests/performance/rapport_locust.html`.

Résultats (coller ici le tableau affiché par Locust : `# reqs`, `# fails`, `Avg`, `Max`) :

```
(coller le tableau Locust)
```

## 8. Branches

Chaque bug et chaque fonctionnalité a sa propre branche, nommée `bug/nom` ou `feature/nom`.

Bugs corrigés (`bug/...`) :

| Branche | Problème corrigé |
|---|---|
| `bug/points-non-deduits` | Les points du club n'étaient pas déduits après une réservation |
| `bug/points-insuffisants` | Réservation acceptée sans assez de points |
| `bug/limite-12-places` | Plus de 12 places en une réservation |
| `bug/limite-12-cumulee` | Plus de 12 places cumulées par club et par compétition |
| `bug/places-insuffisantes` | Réservation au-delà des places restantes |
| `bug/email-inconnu` | Plantage avec un email inconnu |
| `bug/message-email-inconnu` | Aucun message d'erreur sur la page de connexion |
| `bug/places-invalides` | Réservation de 0 place ou d'un nombre négatif |
| `bug/champ-places-vide` | Plantage avec un champ vide |
| `bug/competition-inconnue` | Plantage avec un club ou une compétition inconnu dans l'adresse |
| `bug/competitions-passees` | Réservation possible sur une compétition passée |
| `bug/message-confirmation` | Le message de confirmation n'indiquait pas le nombre de places |

Fonctionnalités (`feature/...`) :

* `feature/page-points` : page publique `/points` avec les points de tous les clubs (phase 2)
* `feature/nouvelles-competitions` : nouvelles compétitions dans `competitions.json`
* `feature/bootstrap` : style Bootstrap sur les trois pages
* `feature/tests` : tests, couverture, Locust et rapports