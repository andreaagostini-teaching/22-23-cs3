## nested cycles
# cicli annidati

# generare accordo
import random

for accordo in range(10):
    nota = random.randint(45, 56)
    for notaAccordo in range(6):
        nota = nota + random.randint(3, 4)
        print(nota, end=' ')
    print('')





