from random import randint

N=int(input("Enter a number of elements in your random list >> "))
rl = [randint(0,99) for x in range(N)] # для простоты используем только целые числа до 99
print('Non-sorted list >> ',rl)

for i in range(0,len(rl)-1):
    for j in range(0,len(rl)-1):
        if rl[j] > rl[j+1]:
            rl[j],rl[j+1]=rl[j+1],rl[j]
print('Sorted list >> ',rl)