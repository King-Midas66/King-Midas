n=int(input())

n1=n//12
n2=n%12

if n2>0:
    print(n1,"dozen","and",n2)
else:
    print(n1,"dozen")
