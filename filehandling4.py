f1=open("file.txt",'a+')
print(f1.tell())
f1.write("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
print(f1.tell())
f1.seek(0)
print(f1.read())

