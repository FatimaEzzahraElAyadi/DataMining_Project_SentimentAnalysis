# Analyse de Sentiment pour les Agences Bancaires

Ce projet vise à développer un système d'analyse de sentiment automatisé pour les agences bancaires en utilisant des techniques de data mining. 
L'objectif est de collecter des commentaires des clients afin de comprendre leurs sentiments à l'égard des services bancaires et de fournir des informations précieuses pour améliorer la satisfaction des clients.

## Introduction

Le secteur bancaire est en constante évolution, avec une concurrence accrue et des attentes croissantes des clients. Dans ce contexte, comprendre les sentiments et les opinions des clients est essentiel pour les agences bancaires. L'analyse de sentiment est une approche puissante qui permet de capturer et d'interpréter les émotions exprimées dans les commentaires des clients. Cela offre aux agences bancaires une opportunité unique d'identifier les domaines à améliorer, de mieux répondre aux besoins des clients et d'accroître leur satisfaction.

## Contexte général du projet

### Concepts clés liés à l'analyse de sentiment et au data mining

- **Analyse de sentiment :** L'analyse de sentiment, également connue sous le nom d'opinion mining, est une technique qui permet d'extraire et d'interpréter les sentiments, les émotions et les opinions exprimés dans des textes. Elle utilise des méthodes automatiques pour évaluer si un sentiment est positif, négatif ou neutre, afin de comprendre la perception des individus à l'égard d'un produit, d'un service ou d'une entité donnée.

- **Data mining :** Le data mining, également appelé fouille de données, est un processus d'extraction de connaissances utiles à partir de grandes quantités de données. Il utilise des techniques statistiques, mathématiques et d'apprentissage automatique pour découvrir des modèles, des relations et des tendances cachées dans les données.

## Méthodologie du travail

### Outils et technologies utilisés

- **Apify :** Plateforme de collecte de données en ligne.
- **Airflow :** Cadre de travail pour la gestion des flux de travail.
- **BERT :** Modèle de langage pré-entraîné pour le traitement du langage naturel.
- **PostgreSQL :** Système de gestion de base de données relationnelle.
- **Power BI :** Outil de visualisation des données.

### Processus ETL (Extract, Transform, Load)

Le processus ETL comprend les étapes d'extraction des données, de filtrage, de transformation et de chargement dans la base de données. Airflow est utilisé pour automatiser ce processus.

## Collecte de données avec Apify

Apify est une plateforme puissante qui permet de collecter et de gérer des données provenant de diverses sources en ligne. Elle offre une interface conviviale et des fonctionnalités avancées pour automatiser la collecte de données à grande échelle.

### Sources de données utilisées

Nous avons utilisé le Google Map Scraper d'Apify pour collecter les données des agences bancaires. Google Maps fournit des informations essentielles, y compris l'emplacement, les horaires d'ouverture, les évaluations et les commentaires des clients.

### Méthodes de collecte de données

Nous avons utilisé une approche basée sur la pagination pour extraire les informations de différentes pages des résultats de recherche Google Maps. Le Google Map Scraper d'Apify nous a permis de spécifier des critères de recherche pour cibler spécifiquement les agences bancaires.

## Filtrage des données

Le filtrage des données est une étape cruciale pour nettoyer les commentaires des clients en éliminant les données non pertinentes ou redondantes. Nous avons appliqué des techniques de prétraitement des données, y compris le filtrage des emojis.

## Transformation des données avec BERT

Dans cette section, nous explorons la transformation des données avec BERT, une bibliothèque puissante pour le traitement du langage naturel.
