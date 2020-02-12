h=int(input())
num=1
for i in range(h):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
        #印完num後令num內容加一
    print()
