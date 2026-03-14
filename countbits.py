n=5
index=[]

for i in range(n+1):
    index.append(bin(i).count('1'))
print(index)