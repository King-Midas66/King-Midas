st=[]

n=int(input())
while n!=-1:
    st.append(n)
    n=int(input())

st.sort()
print(st)

st.insert(3,10)
print(st)

print(st.count(10))

st.sort()
st.reverse()
print(st)
