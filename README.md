# 📊 Calcul de la somme d'étalonnage

## 🎯 Objectif
Développer un système qui analyse un document texte ligne par ligne pour extraire et additionner les valeurs d'étalonnage, où chaque valeur est formée par la combinaison du premier et du dernier chiffre trouvés sur chaque ligne.

## 📝 Description du problème
Le document d'étalonnage nouvellement amélioré se compose de lignes de texte. Chaque ligne contient une **valeur d'étalonnage spécifique** que les lutins doivent récupérer.

Sur chaque ligne, la valeur d'étalonnage peut être trouvée en **combinant le premier chiffre et le dernier chiffre** (dans cet ordre) pour former un nombre à deux chiffres.

### 🔍 Exemple
Pour les lignes suivantes :
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

Les valeurs d'étalonnage sont :
- `12` (ligne 1 : premier chiffre = 1, dernier chiffre = 2)
- `38` (ligne 2 : premier chiffre = 3, dernier chiffre = 8)
- `15` (ligne 3 : premier chiffre = 1, dernier chiffre = 5)
- `77` (ligne 4 : premier chiffre = 7, dernier chiffre = 7)

La **somme totale des valeurs d'étalonnage** est : `12 + 38 + 15 + 77 = 142`

## 📦 Prérequis

Avant d'exécuter les solutions, assurez-vous d'avoir installé :

<div align="center">

| Langage | Version minimale | Site officiel |
|---------|-----------------|---------------|
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="20" height="20"/> JavaScript | Node.js 14+ | [nodejs.org](https://nodejs.org/) |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" width="20" height="20"/> PHP | PHP 7.4+ | [php.net](https://www.php.net/) |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20" height="20"/> Python | Python 3.8+ | [python.org](https://www.python.org/) |

</div>

## 📂 Structure du projet
```
.
├── README.md
├── question1.js    # Solution JavaScript
├── question1.php   # Solution PHP
├── question1.py    # Solution Python
└── document.txt    # Fichier d'entrée
```

## 🚀 Installation et utilisation

### 1. Cloner le dépôt
```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
```

### 2. Configuration du fichier d'entrée

#### 🛠️ Configuration du chemin
Si nécessaire, modifiez le chemin du fichier dans les scripts selon votre environnement :

<details>
<summary><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="20" height="20"/> JavaScript</summary>

```javascript
const filePath = './document.txt';
```
</details>

<details>
<summary><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" width="20" height="20"/> PHP</summary>

```php
$filePath = './document.txt';
```
</details>

<details>
<summary><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20" height="20"/> Python</summary>

```python
file_path = './document.txt'
```
</details>

### 3. Exécution des solutions

Choisissez votre langage préféré et exécutez la solution correspondante :

<details>
<summary><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="20" height="20"/> Solution JavaScript</summary>

```bash
node question1.js
```
</details>

<details>
<summary><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" width="20" height="20"/> Solution PHP</summary>

```bash
php question1.php
```
</details>

<details>
<summary><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20" height="20"/> Solution Python</summary>

```bash
python question1.py
```
</details>

## 📝 Format du fichier d'entrée

Le fichier `document.txt` doit contenir une série de lignes, où chaque ligne contient au moins un chiffre. Exemple :
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

## 📊 Format de sortie

Chaque solution affichera :
1. La somme totale des valeurs d'étalonnage

Exemple de sortie :
```
Somme totale des valeurs d'étalonnage : 142
```
