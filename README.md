# 🏦 Analyse de Sentiment pour les Agences Bancaires 📊

Ce projet vise à développer un système d'analyse de sentiment automatisé pour les agences bancaires en utilisant des techniques de data mining. 
L'objectif est de collecter des commentaires des clients afin de comprendre leurs sentiments à l'égard des services bancaires et de fournir des informations précieuses pour améliorer la satisfaction des clients.

## 🌐 Contexte général du projet

### 🔑 Concepts clés liés à l'analyse de sentiment et au data mining

- **Analyse de sentiment :** L'analyse de sentiment, également connue sous le nom d'opinion mining, est une technique qui permet d'extraire et d'interpréter les sentiments, les émotions et les opinions exprimés dans des textes. Elle utilise des méthodes automatiques pour évaluer si un sentiment est positif, négatif ou neutre, afin de comprendre la perception des individus à l'égard d'un produit, d'un service ou d'une entité donnée.

- **Data mining :** Le data mining, également appelé fouille de données, est un processus d'extraction de connaissances utiles à partir de grandes quantités de données. Il utilise des techniques statistiques, mathématiques et d'apprentissage automatique pour découvrir des modèles, des relations et des tendances cachées dans les données.

## 📋 Méthodologie du travail

### 🛠️ Outils et technologies utilisés

- **Apify :** Plateforme de collecte de données en ligne.
- **Airflow :** Cadre de travail pour la gestion des flux de travail.
- **BERT :** Modèle de langage pré-entraîné pour le traitement du langage naturel.
- **PostgreSQL :** Système de gestion de base de données relationnelle.
- **Power BI :** Outil de visualisation des données.

### 🔄 Processus ETL (Extract, Transform, Load)

Le processus ETL comprend les étapes d'extraction des données, de filtrage, de transformation et de chargement dans la base de données. Airflow est utilisé pour automatiser ce processus.

## 📦 Collecte de données avec Apify

Apify est une plateforme puissante qui permet de collecter et de gérer des données provenant de diverses sources en ligne. Elle offre une interface conviviale et des fonctionnalités avancées pour automatiser la collecte de données à grande échelle.

<img src="https://github.com/FatimaEzzahraElAyadi/DataMining_Project_SentimentAnalysis/blob/master/Images/Apify.PNG">

### 🌐 Sources de données utilisées

Nous avons utilisé le Google Map Scraper d'Apify pour collecter les données des agences bancaires. Google Maps fournit des informations essentielles, y compris l'emplacement, les horaires d'ouverture, les évaluations et les commentaires des clients.

## 🧹 Filtrage des données

Le filtrage des données est une étape cruciale pour nettoyer les commentaires des clients en éliminant les données non pertinentes ou redondantes. Nous avons appliqué des techniques de prétraitement des données, y compris le filtrage des emojis.

## 📊 Transformation des données avec BERT

C'est une bibliothèque puissante pour le traitement du langage naturel.

## 📊 Visualisation
<img src="https://github.com/FatimaEzzahraElAyadi/DataMining_Project_SentimentAnalysis/blob/master/Images/V1.PNG">
<img src="https://github.com/FatimaEzzahraElAyadi/DataMining_Project_SentimentAnalysis/blob/master/Images/V2.PNG">
<img src="https://github.com/FatimaEzzahraElAyadi/DataMining_Project_SentimentAnalysis/blob/master/Images/V3.PNG">
<img src="https://github.com/FatimaEzzahraElAyadi/DataMining_Project_SentimentAnalysis/blob/master/Images/V4.PNG">

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/FatimaEzzahraElAyadi/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fatima-ezzahra-el-ayadi-977bb5196/)
