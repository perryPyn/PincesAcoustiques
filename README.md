# Pinces Acoustiques : Manipulation de particules par ultrasons

Ce dépôt contient les travaux de recherche, de modélisation et d'implémentation d'un système de manipulation de particules sans contact en 1D.

<p align="center">
    <img src="assets/pincesacoustiques.png" width = 300>
</p>

## 1. Problématique et Enjeux
L'objectif est d'étudier la manipulation de micro-objets par forces de rayonnement acoustique. Des applications médicales autour de se système sont déjà envisagées dans la médecine douce comme pour le traitement des caillots sainguins.

## 2. Modélisation Théorique
Le principe du piège repose sur la création d'ondes stationnaires et la création d'un **potentiel de Gor'kov** ($U$).

### Équations Fondamentales
La force acoustique $F$ créée dérive du potentiel :
$$F = -\nabla U$$
$$U = K_1(|p|^2) - K_2(|p_x|^2 + |p_y|^2 + |p_z|^2)$$

* **$K_1, K_2$** : Constantes dépendant du volume de la bille et des masses volumiques (air vs polystyrène).
* **$p$** : Pression acoustique complexe résultant de la somme des pressions de chaque transducteur.

### Algorithme de Contrôle
Pour piéger et déplacer la particule, on peut faire une simulation afin de visualiser les noeuds de stabilité :

<p align="center">
    <img src="assets/gorkov_plot.png" width = 50%>
</p>

## 3. Dispositif Expérimental (Hardware)
Le montage consiste en deux transducteurs ultrasonores face à face, créant un champ 1D.

- **Microcontrôleur :** Arduino (ATMega328P).
- **Transducteurs :** Murata MA40S4S de fréquence centrale 40 kHz.
- **Amplification :** Montage amplificateur non-inverseur simple.

### Implémentation du déphasage
Le contrôle de la phase se fait via les registres de comparaison :
- `OCR1A` et `OCR1B` définissent les fronts du signal PWM.
- La fonction `SetPhase()` permet une mise à jour dynamique sans arrêt du signal. Elle assure une précision du déphasage inférieur à 1° soit une précision spatiale inférieure à 0.39 mm

<p align="center">
    <img src="assets/schema.png" width = 45%>
    <img src="assets/schema_montage.jpg" width = 45%>
</p>

## 4. Analyse et Résultats


## 5. Structure du Dépôt
- `/src` : Firmware Arduino (gestion des registres et modulation).
- `/scripts` : Modèles mathématiques et scripts d'analyse vidéo.
- `/docs` : Fiches techniques et schémas électroniques détaillés.

---
*Projet réalisé dans le cadre d'une étude sur la manipulation physique sans contact.*