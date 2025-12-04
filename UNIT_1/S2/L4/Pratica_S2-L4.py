import math

# Funzione per leggere i numeri
def leggi_numero(messaggio):

    while True:

        valore = input(messaggio).strip()

        try:

            return float(valore)
        
        except ValueError:

            print("Errore: inserisci un numero valido!")


# Funzione del perimetro del quadrato
def perimetro_quadrato():

    lato = leggi_numero("\nInserire la lunghezza del lato del quadrato: ")

    return lato * 4

# Funzione del perimetro del cerchio
def perimetro_cerchio():

    r = leggi_numero("\nInserire il valore del raggio del cerchio: ")

    return 2 * math.pi * r

# Funzione del perimetro del rettangolo
def perimetro_rettangolo():

    base = leggi_numero("\nInserire la lunghezza della base del rettangolo: ")
    altezza = leggi_numero("Inserire la lunghezza dell'altezza del rettangolo: ")

    return 2 * base + 2 * altezza

# Funzione interattiva del menu'
def menu():

    while True:

        print("\n --- Calcola il perimetro ---\n")
        print("\nScegliere una delle seguenti opzioni:\n")
        print("1 - Quadrato")
        print("2 - Cerchio")
        print("3 - Rettangolo")
        print("4 - Esci")

        scelta_utente = input("\nScegli la figura (1, 2 o 3) oppure esci (4): ").strip()

        if scelta_utente == "1":

            risultato = perimetro_quadrato()
            print("\nIl perimetro del quadrato e':", risultato)

        elif scelta_utente == "2":

            risultato = perimetro_cerchio()
            print("\nIl perimetro del cerchio e':", risultato)

        elif scelta_utente == "3":

            risultato = perimetro_rettangolo()
            print("\nIl perimetro del rettangolo e':", risultato)

        elif scelta_utente == "4":

            print("\nProgramma terminato.")
            break

        else:

            print("\n Valore inserito non valido! Valori ammessi 1, 2, 3, 4...Riprova.")

# Avvio del programma
menu()