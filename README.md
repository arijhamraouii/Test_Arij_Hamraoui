# 📊 Calcul de la somme d'étalonnage

## 📝 Description du problème

Le document d'étalonnage nouvellement amélioré se compose de lignes de texte. Chaque ligne contient une **valeur d'étalonnage spécifique** que les lutins doivent récupérer.  
Sur chaque ligne, la valeur d'étalonnage peut être trouvée en **combinant le premier chiffre et le dernier chiffre** (dans cet ordre) pour former un nombre à deux chiffres.

### 🔍 Exemple

Pour les lignes suivantes :

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet


Les valeurs d'étalonnage sont :  
- `12` (ligne 1 : premier chiffre = 1, dernier chiffre = 2)  
- `38` (ligne 2 : premier chiffre = 3, dernier chiffre = 8)  
- `15` (ligne 3 : premier chiffre = 1, dernier chiffre = 5)  
- `77` (ligne 4 : premier chiffre = 7, dernier chiffre = 7)  

La **somme totale des valeurs d'étalonnage** est :  
`12 + 38 + 15 + 77 = 142`.

---

## 📂 Fichiers dans le projet

Ce projet contient des solutions dans les langages suivants :
- **`question1.js`** : Solution en JavaScript (Node.js). 🟦  
- **`question1.php`** : Solution en PHP. 🟪  
- **`question1.py`** : Solution en Python. 🟨  

---

## 🚀 Instructions générales

1. Téléchargez ou clonez ce dépôt.  
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DEPOT>

2. Assurez-vous que le fichier contenant les données d'étalonnage (par exemple, document.txt) est correctement placé dans le chemin spécifié dans les fichiers de code.
Vous pouvez modifier le chemin directement dans les scripts si nécessaire.

---

🛠️ Vérification du chemin du fichier
Modifiez la variable contenant le chemin du fichier dans le code, si nécessaire.

---

Exemple pour question1.py :
python

chemin_fichier = "C:/Users/arijh/Desktop/Test_Arij_Hamraoui/document.txt"
Assurez-vous que le fichier existe dans ce chemin avant d'exécuter le script.

---

⚙️ Commandes pour exécuter chaque fichier

---

JavaScript (Node.js) 🟦
Installez Node.js sur votre machine (si ce n'est pas déjà fait).

Ouvrez un terminal dans le dossier contenant question1.js.

Exécutez la commande suivante :

node question1.js

---

PHP 🟪
Installez PHP sur votre machine (si ce n'est pas déjà fait).

Ouvrez un terminal dans le dossier contenant question1.php.

Exécutez la commande suivante :

php question1.php

---

Python 🟨
Installez Python sur votre machine (si ce n'est pas déjà fait).

Ouvrez un terminal dans le dossier contenant question1.py.

Exécutez la commande suivante :

python question1.py

---
