h=int(input())
w=int(input())
for i in range(h+1):
    for j in range(1,w+1):
        print(i,"*",j,"=",i*j,sep="",end="\t")
    print()
