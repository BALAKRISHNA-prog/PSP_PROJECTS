'''
#File handling in python
#When text file is in the same folder ,no need to mention entire path
f=open("G:\kittu\Raptor Files\Exp6.txt","r")
if f.mode =="r":
    contents=f.read()
    print(contents)

f1=f.readlines()
for line in f1:
    print(f1)

f=open("hello.txt","r")

if f.mode=="r":
    contents=f.read()
    print(contents)

f=open("hello.txt","a+")
f.write("How are you all")
f=open("hello.txt","r")
contents=f.read()
print(contents)
f.close()
'''
f = open("hello.txt","w")
if f.mode == "w":
    f.write("hello world!How are you doing?")
f.close()
   
