from random import randint

N=int(input("Enter a number of elements in your random list >> "))
rand_list = [randint(0,99) for x in range(N)] # для простоты используем только целые числа до 99
print(rand_list)
