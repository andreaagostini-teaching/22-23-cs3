midinote = int(input("che nota? "))

pitchclass = midinote % 12

if pitchclass == 0 or pitchclass == 4 or pitchclass == 7:
    print("do maggiore")
else:
    print("no")

# ESERCIZI:
# data una nota MIDI:
# fa parte dell'accordo di re minore?
# fa parte della metà grave della tastiera?
# fa parte del registro centrale?
# fa parte dell'accordo di settima diminuita di DO nel registro grave?


# data una frequenza:
# fa parte dello spettro del la centrale?