# Это файл с функциями для Задач 2, 3 и 4. Сделано это для упрощения
from itertools import product
# Часть 1. Проверка ввода пользователя.
# Скорее всего можно всё это как-то сократить, так что буду рад получить совет :)
def check(dice):
    correct_dices = ['4','6','8','10','12','20']
    correct_rolls = ['1','2','3','4','5','6','7','8','9','10'] # число бросков дайса.
    # поскольку в реальной игре почти никогда не бросают больше 10 костей одного типа за раз,
    # я решил ограничить это число
    if dice in ['d4','d6','d8','d10','d12','d20']:
        dice = "1" + dice
    while "d" not in dice:
        dice = input("Invalid input (use NdM form, use 'd' once) >> ")
    dlist = dice.split('d')
    while len(dlist) != 2:
        dice = input("Invalid input (use NdM form, use 'd' once) >> ")
        dlist = dice.split('d')
    while dlist[0] not in correct_rolls or dlist[1] not in correct_dices:
        dice = input("Invalid input (use NdM form, where N and M is adequate digits and 'd' used once) >> ")
        dlist = dice.split('d')
        while len(dlist) != 2:
            dice = input("Invalid input (use NdM form, where N and M is adequate digits and 'd' used once) >> ")
            dlist = dice.split('d')
    return [int(dlist[0]),int(dlist[1])]

# Часть 2. Собственно, задача.
# Это не самый эффективный алгоритм (возможно, претендент на самый НЕ эффективный),
# поэтому лучше не бросать больше 7-8 дайсов с большим количеством граней
# Например, мой ноут не смог быстро посчитать уже: 9d8, 6d20, 8d12
def chances(N,M):
    x=[i for i in range(1,M+1)] # возможные числа на дайсе
    comb=list(product(x,repeat=N)) # всевозможные комбинации
    summs=[]
    for i in range(0,len(comb)):
        summs.append(sum(comb[i])) # список сумм всех комбинаций
    nums=[]
    probs=[]
    for i in range(N,N*M+1):
        nums.append(summs.count(i)) # число одинаковых элементов
        probs.append((summs.count(i))/(M**N)*100)
    for i in range(N,N*M+1):
        print(i,'=',round(probs[i-N],2),'%')

