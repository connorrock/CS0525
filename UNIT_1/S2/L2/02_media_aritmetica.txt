#include <stdio.h>

/*
Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro
media aritmetica.
*/

int main()
{
    int a; // Dichiarazione della prima variabile che conterra' il primo numero
    int b; // Dichiarazione della seconda variabile che conterra' il secondo numero
    float media_aritmetica; // Creazione della variabile in virgola mobile per la media

    printf("Calcolo media aritmetica di due numeri interi\n");

    printf("Inserire il primo numero intero: ");
    scanf("%d", &a); // Chiedo il primo numero e viene salvato nella variabile a

    printf("Inserire il secondo numero intero: ");
    scanf("%d", &b); // Chiedo il secondo numero e viene salvato nella variabile b

    media_aritmetica = (a + b) / 2.0; // Calcolo della media tra due interi

    /*
    In C se in una operazione e' presente almeno un decimale, il risultato viene calcolato 
    come decimale
    */

    printf("La media aritmetica tra %d e %d e': %.2f", a, b, media_aritmetica); // Stampa del risultato

    return 0;

}