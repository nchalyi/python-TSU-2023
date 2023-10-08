import funcs #все функции расположены в файле funcs.py, решение задачи 2 расположено там (см. check() функцию)

dice = input("Roll the dices (print in a NdM form) >> ")
print("All possible sums probabilities for",dice,"roll :")
funcs.chances(funcs.check(dice)[0],funcs.check(dice)[1])