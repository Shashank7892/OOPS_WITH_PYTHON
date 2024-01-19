f1=open("hanuman.jpg",'rb')
f2=open("hanuman1.jpg",'w+b')
for i in f1:
    f2.write(i)
print(f2.tell())
f2.seek(0)
print(f2.read())