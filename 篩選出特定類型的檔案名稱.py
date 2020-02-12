st=['apple.txt', 'banana.py', 'andy.txt', 'may.py', 'john.txt', 'pine.apple.py']

p=["P00_"+f.rpartition(".")[0].upper() for f in st if f.endswith(".py")]
print(p)
