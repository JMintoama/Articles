#include <stdio.h>

int main() {
    int num1, num2, somme;

    // Demander à l'utilisateur d'entrer les deux entiers
    printf("Entrez le premier entier : ");
    scanf("%d", &num1);

    printf("Entrez le deuxième entier : ");
    scanf("%d", &num2);

    // Calculer la somme
    somme = num1 + num2;

    // Afficher le résultat
    printf("La somme de %d et %d est %d.\n", num1, num2, somme);

    return 0;
}
