f1=open("file2.txt","r+")
f1.read()
f1.write("hello")
print(f1.tell())
f1.seek(0)
print(f1.read())
