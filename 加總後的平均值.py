sum1=0
ct=0

n = int(input())
while n!=-1:
    #print(n)
    sum1 += n
    ct+=1
    n=int(input())
else:
    print(sum1)
    print(sum1/ct)
