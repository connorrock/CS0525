#include <stdio.h>


int main()
{
    int a;
    int b;
    int moltiplicazione;

    printf("Inserire il primo numero: ");
    scanf("%d", &a);

    printf("Inserire il secondo numero: ");
    scanf("%d", &b);

    moltiplicazione = a * b;

    printf("Il prodotto tra %d e %d e': %d", a, b, moltiplicazione);

    return 0;

}