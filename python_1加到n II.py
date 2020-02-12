sum1=0 #初始值設為零

n=int(input()) #從一加到n時所需用到的n

for i in range(1,n+1): #我們想從1開始加，一直加到n+1
    sum1 += i
    print(i,end='') #先將一串數字串起來
    if i< n:
     print('+',end='') #後面再規定後面所有添加的數字加上的型態會是+x
else:
    print(' =',sum1)
