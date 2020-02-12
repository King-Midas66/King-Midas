sum1=0
ct=0

numbmax=0
numbpos=0


n=int(input())
while n!=-1:
    sum1+=n
    ct+=1
    if n>numbmax:
        #n=numbmax會變成numbmax給n
        #ct=numbpos會變成numbpos給n
        numbpos=ct
        numbmax=n
    n=int(input())

else:
    print(sum1)
    print(sum1/ct)
    print(numbmax)
    print(numbpos)
