latoTesto = input("dimmi il lato: ")
# questo restituisce una stringa

lato = eval(latoTesto) 
# lato è una variabile che contiene un float
perimetro = lato * 4

"""
questo
è
un
blocco
"""

area = lato * lato
volume = area * lato

print("perimetro", perimetro)
print("area", area)
print("volume del cubo", volume)

