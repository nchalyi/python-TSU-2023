f=open("lecture05/task1.txt","r")

list=[]
for line in f:
    list.append(int(line))
for i in range(0,len(list)):
    for j in range(0,len(list)):
        for k in range(0,len(list)):
            if list[i]+list[j]+list[k] == 2020:
                # print(list[i],list[j],list[k])
                result=list[i]*list[j]*list[k]
f.close()
nf=open("lecture05/output1.txt","w")
nf.write(str(result))
nf.close()

