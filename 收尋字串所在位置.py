s=input()
n=input()

pos = s.find(n)
while pos!=-1:
    print(pos)
    pos = s.find(n,pos+1)
