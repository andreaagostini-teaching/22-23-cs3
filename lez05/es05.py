n = [64, 74, 57, 90] # note MIDI: mi, re, sol, fa#
# voglio riordinarle in ordine di pitch class
# -> [74, 64, 90, 57]: re, mi, fa#, sol

def midi2pitch(m):
    print(m)
    return m % 12

print(sorted(n, key = midi2pitch)) # stampa la lista ordinata senza modificare n
print(n)

