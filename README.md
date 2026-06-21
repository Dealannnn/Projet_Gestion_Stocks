📦 Solution Intelligente de Gestion de Stocks

Ce projet a été réalisé dans le cadre du Master Informatique - Big Data (Université Paris 8) pour le module Projet Innovant 1 (DNF1ED12) et Conception, Spécification, Test (DNF2ED12).

📝 Description

Cette application est une solution de logistique intelligente permettant de :

Importer des données historiques de ventes.

Prédire la demande future via une approche de séries temporelles (moyenne mobile).

Générer des recommandations de commande automatiques.

Visualiser les résultats via une interface interactive.

🛠️ Stack Technique

Langage : Python 3.9

Interface : Streamlit

Analyse de données : Pandas, NumPy

Conteneurisation : Docker / Docker Compose

Qualité : PyTest (Tests unitaires)

🚀 Installation & Lancement

Prérequis : Avoir Docker et Docker Compose installés sur votre machine.

Clonez le dépôt ou téléchargez le dossier.

Placez-vous à la racine du projet dans un terminal.

Lancez l'application avec la commande suivante :

docker-compose up --build


Une fois le conteneur lancé, accédez à l'application dans votre navigateur à l'adresse suivante : http://localhost:8501

🧪 Tests & Validation

Le projet inclut une suite de tests unitaires pour valider la logique métier. Pour exécuter les tests au sein du conteneur, utilisez la commande :

docker-compose run gestion_stock pytest test_app.py


🎓 Contextes Académiques

DNF1ED12 (Projet tuteuré) : Développement de la solution et mise en place de la stack technique.

DNF2ED12 (Conception, Spécification, Test) : Respect de la méthodologie de conception (UML), spécification des besoins et mise en place d'une stratégie de tests automatisés.

Projet réalisé par Dylan Waziri
