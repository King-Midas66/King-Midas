#st=[input()]


#while st!=-1:  
    #txt=["T00_"+st.capitalize() for f in st if f.endswith(".py")]
    #print(txt)
    #st=input()


st=[]

n=input()
while n!="-1":
    st.append(n)
    n=input()

t=["T00_"+f.capitalize() for f in st if f.endswith(".txt")]
print(t)

p=["P00_"+f.rpartition('.')[0].upper()+".py" for f in st if f.endswith(".py")]
print(p)
