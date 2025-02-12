#include<stdio.h>

void main(){
    int N;
    printf("entrer la taille du tableau:\n");scanf("%d",&N);
    printf("remplir le tableau\n\n");
    int Tab[N],i;
    for (i=0;i<N;i++){
        printf("la valeur %d:\n",i+1);scanf("%d",&Tab[i]);
    }
    printf("\nLes elements du tableau:\n");
    for (i=0;i<N;i++){
        printf("%d\ ",Tab[i]); 
   }
}