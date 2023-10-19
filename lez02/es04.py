midinote = int(input("che nota? "))

if midinote < 21 or midinote > 108:
    print("fuori estensione")
else:
    print("ok")



if midinote < 21:
    print("troppo grave")

if midinote > 108:
    print("tropppo acuto")

if midinote >= 21 and midinote <= 108:
    print("ok")



if midinote < 21:
    print("troppo grave")
else:
    if midinote > 108:
        print("troppo acuto")
    else:
        print("ok")


if midinote < 21:
    print("troppo grave")
elif midinote > 108:
    print("troppo acuto")
else:
    print("ok")





pitchclass = midinote % 12

if midinote < 21 or midinote > 108:
    print("fuori estensione")
elif pitchclass == 0 or pitchclass == 4 or pitchclass == 7:
    print("è in do maggiore, non mi piace")
elif pitchclass == 2 or pitchclass == 5 or pitchclass == 9:
    print("è in re minore, mi viene da piangere")
else:
    print("ok")







