'''
PRATICA S2/L3

GENERA UN NOME PER LA TUA BAND

Obiettivo

Scrivere un programma in Python che genera un nome per una band musicale utilizzando
due input forniti dall'utente: la citta' di origine e il nome del proprio animale 
domestico.

Descrizione dell'esercizio

In questo esercizio, dovrai creare un programma che esegue le seguenti operazioni:

1. Richiesta di input: Il programma deve chiedere all'utente di inserire:

    - il nome della citta' di origine.
    - il nome del proprio animale domestico.

2. Genenerazione del nome della band: Una volta ricevuti gli input, il programma deve
combinare il nome della citta' e il nome dell'animale in un unica stringa che rappresenta
il nome della band.

3. Output: Il programma deve stampare a video il nome generato per la band.

'''

print("================================================")
print("Benvenuto su Generatore di nomi per la tua band!")
print("================================================")

city = input("\nDigita la tua citta' di origine: ")
pet = input("Digita il nome del tuo animale domestico: ")

band_name = f"{city} {pet}"

print("\nIl nome della tua band potrebbe essere:", band_name)