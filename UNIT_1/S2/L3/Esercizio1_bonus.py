def media_mobile(lista, n):

    # Creo una lista vuota dove andremo a mettere tutte le medie che calcoliamo
    risultati = []

    # Ciclo su tutti gli indici degli elementi della lista che andra' da 0 
    # a len(lista)-1
    for i in range(len(lista)):

        # Prendo tutti gli elementi della lista da 0 a i incluso (i + 1)
        finestra = lista[0 : i + 1]

        # Inserisco un controllo dove se la lunghezza di finestra e' maggiore di
        # n allora entro nell'if
        if len(finestra) > n:

            # Prendo solo gli ultimi n elementi della lista finestra
            finestra = finestra[-n:]

        # Calcolo la media
        media = sum(finestra) / len(finestra)

        # Aggiungo la media appena ottenuta alla lista risultati
        risultati.append(media)

    return risultati

print("Calcolatore di media mobile\n")

# Chiedo all'utente la lista dei numeri, in stringa, da analizzare
lista_numeri_utente = input("Inserisci la lista dei numeri separati da una virgola (es: 5,1,4,9,34,27):\n")

# Trasformo la stringa di numeri dell'utente in una lista di numeri
lista_numeri_trasformata = [float(x) for x in lista_numeri_utente.split(",")]

# Chiedo la dimensione della finestra n
dimensione_finestra = int(input("\nInserisci il valore della dimensione della finestra n (max numeri media):\n"))

# Chiamo la funzione
risultato = media_mobile(lista_numeri_trasformata, dimensione_finestra)

# Stampo il risultato
print("\nLa media mobile calcolata e':")
print(risultato)