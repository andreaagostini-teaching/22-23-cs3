l = [[[10, 20, 30], [100, 200, 300]],
     [[345, 567, 789], [123456, 34567]]]

# esercizio svolto:
# esprimere gli indirizzi di liste annidate così:
#
# la maniera normale sarebbe l[1][0][2]
indirizzo = [1, 0, 2]

e = l
for i in indirizzo:
    print(e)
    e = e[i]

print(e)

