
N=input("Enter any number >> ")
while not N.isdigit() or int(N)<2:
    N=input("Please, enter any integer number more than 1 >> ")
N=int(N)
out=[]
listN=set(range(2,N+1))
while listN:
    p=min(listN)
    out.append(p)
    listN -= set(range(p,N+1,p))
print('Prime numbers from 2 to your number >> ',out)
