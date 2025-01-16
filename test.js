const fs = require('fs'); // Module pour gérer les fichiers

// Fonction pour calculer la somme des valeurs d'étalonnage
function extraireSommeEtalonnage(cheminFichier) {
    let sommeEtalonnage = 0; // Initialiser la somme

    // Lire le fichier en mode synchrone
    const data = fs.readFileSync(cheminFichier, 'utf8');
    const lignes = data.split('\n'); // Diviser le contenu en lignes

    // Parcourir chaque ligne
    lignes.forEach((ligne) => {
        ligne = ligne.trim(); // Supprimer les espaces inutiles
        let premierChiffre = '';
        let dernierChiffre = '';

        // Trouver le premier chiffre
        for (const char of ligne) {
            if (/\d/.test(char)) {
                premierChiffre = char;
                break;
            }
        }

        // Trouver le dernier chiffre
        for (let i = ligne.length - 1; i >= 0; i--) {
            if (/\d/.test(ligne[i])) {
                dernierChiffre = ligne[i];
                break;
            }
        }

        // Former le nombre et l'ajouter à la somme
        if (premierChiffre || dernierChiffre) {
            const nombreForme = parseInt(premierChiffre + dernierChiffre, 10);
            sommeEtalonnage += nombreForme;
        }
    });

    // Afficher la somme totale
    console.log(`La somme des valeurs d'étalonnage est : ${sommeEtalonnage}`);
}

// Définir le chemin du fichier
const cheminFichier = 'C:/Users/arijh/Desktop/Test_Arij_Hamraoui/document.txt';

// Appeler la fonction pour calculer la somme
extraireSommeEtalonnage(cheminFichier);
