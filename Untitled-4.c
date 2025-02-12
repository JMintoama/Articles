#include<stdio.h>
#define Max 100
int Tab[Max],N,i,j,x;
void saisie(){
    do {printf("taille du tableau :");scanf("%d",&N);
    }while ((N<0)||(N>Max));
    printf("remplir le tableau\n\n");
    for (i=0;i<N;i++){
        printf("la valeur %d:\n",i+1);scanf("%d",&Tab[i]);
    }
}

void affichage(){
    printf("\n Les elements du tableau:\n");
    for (i=0;i<N;i++){
        printf("%d ",Tab[i]); 
   }
}

void tri(){
    for (i=0;i<N-1;i++){
        for(j=i+1;j<N;j++){
            if (Tab[i]>Tab[j]){
                x=Tab[j];Tab[j]=Tab[i];Tab[i]=x;
                }
        }
    }
    printf("\n Tableau tri:\n");
    for (i=0;i<N;i++){
        printf("%d ",Tab[i]); 
   }
    

}
void main(){
    saisie();
    affichage();
    tri();
}