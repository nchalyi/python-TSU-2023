
first_9=["zero","one","two","three","four","five","six","seven","eight","nine"]
from_10_to_19=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decimal=["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

numberInput = str(input('Input a number from 0 to 99 >> '))
listN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
if numberInput in ','.join(map(str,listN)):
    numInt = int(numberInput)
    if numInt < 10:
        print(first_9[numInt])
    elif numInt < 20 and numInt > 9:
        print(from_10_to_19[numInt-10])
    else:
        decN = int(numberInput[0])
        edN = int(numberInput[1])
        if edN == 0:
            print(decimal[decN-2])
        else:
            print(decimal[decN-2]+' '+first_9[edN-1])
else:
    print('not a number bruh')