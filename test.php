<?php
function extraireSommeEtalonnage($cheminFichier) {
    $sommeEtalonnage = 0; // Initialiser la somme

    // Vérifier si le fichier existe
    if (!file_exists($cheminFichier)) {
        die("Erreur : Le fichier spécifié n'existe pas.\n");
    }

    // Lire le fichier ligne par ligne
    $fichier = fopen($cheminFichier, "r");
    while (($ligne = fgets($fichier)) !== false) {
        $ligne = trim($ligne); // Supprimer les espaces inutiles
        $premierChiffre = '';
        $dernierChiffre = '';

        // Trouver le premier chiffre
        for ($i = 0; $i < strlen($ligne); $i++) {
            if (ctype_digit($ligne[$i])) {
                $premierChiffre = $ligne[$i];
                break;
            }
        }

        // Trouver le dernier chiffre
        for ($i = strlen($ligne) - 1; $i >= 0; $i--) {
            if (ctype_digit($ligne[$i])) {
                $dernierChiffre = $ligne[$i];
                break;
            }
        }

        // Former le nombre et l'ajouter à la somme
        if ($premierChiffre !== '' || $dernierChiffre !== '') {
            $nombreForme = (int) ($premierChiffre . $dernierChiffre);
            $sommeEtalonnage += $nombreForme;
        }
    }
    fclose($fichier);

    // Afficher la somme totale
    echo "La somme des valeurs d'étalonnage est : $sommeEtalonnage\n";
}

// Définir le chemin du fichier
$cheminFichier = "C:/Users/arijh/Desktop/Test_Arij_Hamraoui/document.txt";

// Appeler la fonction pour calculer et afficher la somme
extraireSommeEtalonnage($cheminFichier);
?>
