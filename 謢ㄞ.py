h=int(input())
w=int(input())
for i in range(1,h+1):
    for j in range(1,w+1):
        print("%d"%(i),"*","%d"%(j),"=","%2d"%(i*j),sep="",end=" ")
    print()
 
