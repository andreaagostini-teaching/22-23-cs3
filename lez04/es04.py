def incrementa(x):
    x = x + 1
    return x

def aggiungiElemento(l):
    l.append(1)

n = int(input("dimmi un numero: "))

x = 1000

p = incrementa(n)
#la variabile n non viene cambiata

print("ora x vale ", x)

print ("il numero dopo è ", p)
print("n ora vale", n)

q = incrementa(p)

print ("e quello ancora dopo è ", q)

a = [10, 20, 30]
aggiungiElemento(a)
#la variabile a viene cambiata perché contiene una lista, che è mutabile
print("ora a vale ", a)


