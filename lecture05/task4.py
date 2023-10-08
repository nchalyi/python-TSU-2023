import funcs #все функции расположены в файле funcs.py
from random import randint

dice = input("Roll the dices (print in a NdM form) >> ")
print("All possible sums probabilities for",dice,"roll :")
funcs.chances(funcs.check(dice)[0],funcs.check(dice)[1])

print("Generating a",dice,"roll...")
rolls=funcs.check(dice)[0]
sides=funcs.check(dice)[1]
for i in range(1,rolls+1):
    print("On",i,"dice you have",randint(1,sides))
