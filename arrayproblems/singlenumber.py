#single number

l=[1,2,1,2,4]
d=0

for x in range(0,len(l)):
    d^=l[x]
    
print(d)
    