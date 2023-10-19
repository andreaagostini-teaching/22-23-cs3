def listIter(l, depth = 1):
    print("entro in", depth)
    for e in l:
        if type(e) == list:
            listIter(e, depth + 1)
        else:
            print('*' * depth, e)
    print("esco da ", depth)
    return


l = [1, 2, [3, 4], 5, 6]
#l = [1, 2, 3]
i = listIter(l)
print(i) ### i non è niente perché listIter non ha valore di ritorno


    