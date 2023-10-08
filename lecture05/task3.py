import funcs #все функции расположены в файле funcs.py

dices = input("Roll the dices (print list of your dices in a NdM form, divided by 'space'. Example: 2d4 5d6 d8) >> ")
dslist = dices.split()
for a in range(0,len(dslist)):
    print("All possible sums probabilities for",dslist[a],"roll :")
    funcs.chances(funcs.check(dslist[a])[0],funcs.check(dslist[a])[1])

