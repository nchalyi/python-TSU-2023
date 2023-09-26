
N=input("Enter 1st number >> ")
while not N.isdigit() or N == '0':
    N=input("Please, enter a nonzero integer number >> ")
N=int(N)
M=input("Enter 2nd number >> ")
while not M.isdigit() or M == '0':
    M=input("Please, enter a nonzero integer number >> ")
M=int(M)
i=max(N,M)
k=min(N,M)
while k != 0:
    i,k = k,i%k
print('Greatest common divisor >>',i)