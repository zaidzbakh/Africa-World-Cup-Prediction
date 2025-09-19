# Prédiction du Vainqueur de la Coupe d’Afrique des Nations 2025

## Description du projet
Ce projet a pour objectif de prédire la nation qui remportera la Coupe d’Afrique des Nations (CAN) 2025 en utilisant des modèles de Machine Learning.  
L’approche repose sur l’analyse des données historiques des précédentes éditions de la CAN et des performances des équipes africaines, combinée à des algorithmes de classification.

---

## Fonctionnalités
- Analyse des données : exploration et visualisation des performances des nations.  
- Prétraitement : nettoyage, normalisation et feature engineering.  
- Entraînement de plusieurs modèles de Machine Learning.  
- Évaluation et comparaison des modèles à l’aide de métriques (accuracy, F1-score, etc.).  
- Prédiction finale : identification de la nation la plus probable gagnante de la CAN 2025.  

---

## Données utilisées
- Résultats historiques des éditions précédentes de la CAN.  
- Statistiques des équipes : buts marqués/encaissés, tirs, possession, passes, etc.  
- Classements FIFA/CAF des nations africaines.  
- Historique des confrontations directes entre nations.  

---

## Modèles de Machine Learning
Plusieurs algorithmes ont été testés :  
- RandomForestClassifier  
- XGBoostClassifier  
- Logistic Regression  
- (optionnel) Neural Networks  

Le meilleur modèle est sélectionné selon ses performances sur les données de test.

---

## Méthodologie
1. Prétraitement des données :  
   - Nettoyage (gestion des valeurs manquantes et doublons).  
   - Normalisation des variables numériques.  
   - Création de nouvelles features pertinentes.  

2. Entraînement des modèles :  
   - Séparation en train/test.  
   - Entraînement avec validation croisée.  
   - Optimisation des hyperparamètres.  

3. Évaluation :  
   - Accuracy, F1-score, matrice de confusion.  
   - Importance des features.  

4. Prédiction finale :  
   - Génération de probabilités de victoire pour chaque nation.  
   - Affichage de la nation prédite gagnante de la CAN 2025.  
