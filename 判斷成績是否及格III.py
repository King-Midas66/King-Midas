n1=int(input())

if(n1>2 or n1<1):
    print("roll error")
else:
    n2=int(input())

    if (n1==1 or n1==2):
        if(0<=n2<=100):
            if (n1==1):
                if n2>=60:
                    print("pass")
                else:
                    print("fail")
            if (n1==2):
                if n2>=70:
                    print("pass")
                else:
                    print("fail")
        else:
            print("score error")    
