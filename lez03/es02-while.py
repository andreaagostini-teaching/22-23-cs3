import random
somma = 0

while somma < 100: # esegui il blocco finché somma < 100
    step = random.randint(1, 10)
    # somma = somma + step #- equivalente a:
    somma += step
    # ci sono anche -= *= /=
    if somma < 100:
        print(somma)

# calcolare Fibonacci fino a N
# calcolare 100 numeri casuali da 1 a 10 senza ripetizioni consecutive

# scrivete i numeri da 1 a 100 senza usare il ciclo for
# e senza fare come Zangarini

# calcolare una sequenza di numeri 
# compresi tra 1 e 10,
# che cresca in maniera irregolare,
# che non arrivi a superare il 100
# e che non contenga più di 15 numeri
