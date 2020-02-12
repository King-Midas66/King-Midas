n1=int(input())
n2=int(input())

n3=n1/100
n4=n2/n3/n3

print(round(n4,2))
if n4>=35:
    print("Obese Class III")
if 30<=n4<35:
    print("Obese Class II")
if 27<=n4<30:
    print("Obese Class I")
if 24<=n4<27:
    print("Overweight")
if 18.5<=n4<24:
    print("Normal")
if n4<18.5:
    print("Underweight")
