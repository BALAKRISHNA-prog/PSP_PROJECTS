#Slicing
subject1="Problem"
subject2="solving"
subject3="and"
subject4="Programming"
subject5="My head"
subject=subject1+subject2+subject3+subject4
print(subject[0:7])
print(subject[7:14])

#in operator---membership

#Raw string operator

print(r"prints\n")

#%s string format
sub="Maths "
part= 1
print("%s%d"%(sub,part))
print("we have part %d of subject %s in first semester"%(part,sub))

#repeat(*)operator
print(subject1*3,subject2*3,subject3*3,subject5*5)
print((subject1+"")*3)
print(subject1.upper())
sentence="PSP is my favourite subject"
print(sentence)
print(sentence.split(' '))
