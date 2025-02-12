#include<stdio.h>
int plus(int x, int y);
main(){
    int x,y;
    printf("valeur1:\n");scanf("%d",&x);
    printf("valeur2:\n");scanf("%d",&y);
    printf("la somme=%d",plus(x,y));
}
int plus(int a, int b){
    int z;
    z=a+b;
    return z;
}
