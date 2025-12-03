import re

def analisi_parole(testo):

    # Converto il testo in minuscolo
    testo = testo.lower()

    # Rimuovo la punteggiatura
    testo = re.sub(r'[^\w\s]', '', testo)

    # Divido il testo in parole
    parole = testo.split()

    # Conteggio con dizionario
    conteggio = {}

    for parola in parole:
        
        if parola in conteggio:
            
            conteggio[parola] += 1

        else:

            conteggio[parola] = 1

    return conteggio


print("Benvenuto nel programma di analisi delle parole\n")

# Chiedo il testo all'utente
testo_utente = input("Inserisci una frase o un testo da analizzare:\n")

# Chiamo la funzione
risultato = analisi_parole(testo_utente)

# Stampo il risultato
print("\nRisultato dell'analisi (parola:conteggio):")
print(risultato)