def pchOct(n):
    p = n % 12
    o = int(n/12) # middle C in oct 5
    return p, o # tupla composta da p e o: (p, o) ma senza parentesi
    # perché non c'è ambiguità

nota = int(input("che nota? "))

p = 'cavallo'
pitch, ottava = pchOct(nota)
# la funzione restituisce una tupla
# che assegno a una tupla di variabili

# posso scriverla anche esplicitando la tupla:
# (pitch, ottava) = pchOct(nota)

print(pitch, ottava)

print("e siamo a ", p)



