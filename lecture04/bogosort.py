from random import randint, shuffle

N=int(input("Enter a number of elements in your random list >> "))
rl = [randint(0,99) for x in range(N)] # для простоты используем только целые числа до 99
print('Non-sorted list >> ',rl)

while rl != sorted(rl):
    shuffle(rl)

print('Sorted list >> ',rl)