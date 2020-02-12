n=int(input())

st=[]
for i in range(n,0,-1):
    print("data",i)
    st.append(i)

print()
for i in range(n,0,-1):
    print("data",st.pop())
