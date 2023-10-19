def sampstoms(s, sr=44100, tail=0):
    return s / sr + tail

# parametro posizionale accettando i default
print(sampstoms(100000))

# parametri posizionali
print(sampstoms(100000, 48000))
print(sampstoms(96000, 96000, 1))

# parametri per nome
print(sampstoms(882000, tail=2))

# parametri per nome
print(sampstoms(882000, tail=2, sr=48000))





