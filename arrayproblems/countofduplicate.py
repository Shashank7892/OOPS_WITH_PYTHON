l=[2,2,3,4,3,4,1,1]
d={}
c=0

for i in l:
    d[i]=l.count(i)
    
print(d)
# operation required to elinmate if duplicate is present and return -1 if not possible
for i in d:
    if d[i]!=1:
        c+=1
    else:
        c=-1
        break
print(c)