from random import randint, shuffle

N=int(input("Enter a number of elements in your random list >> "))
rl = [randint(0,99) for x in range(N)] # для простоты используем только целые числа до 99
print('Non-sorted list >> ',rl)

while rl != sorted(rl):
    shuffle(rl)

# Альтернативный способ решения, без встроеной функции sorted():
# def is_sorted(list):
#     for i in range(0, len(list)-1):
#         if (list[i] > list[i+1] ):
#             return False
#     return True
# while (is_sorted(rl) == False):
#     shuffle(rl)

print('Sorted list >> ',rl)