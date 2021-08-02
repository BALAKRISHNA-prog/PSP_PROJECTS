'''
Tuples are identical to lists in all respect except for the following properties:
1.Tuples are defined by enclosing the elements in parenthesis(()).
2.Tuples are immutable.
'''
#Defining a tuple
studient=("Chandu","Ramesh","Ramu","Tarak","Tejas")
print(type(studient))
for i in studient:
    print(i)

studient=("Chandu","Ramesh","Ramu","Tarak","Tejas")
print(studient[3])
print(studient[0:3])

# What are the benifits of using tuples instead of lists in python

studient=("Chandu","Ramesh","Ramu","Tarak","Tejas")#tuple packing
(s1,s2,s3,s4,s5)=studient#Tuple unpacking
print(s1)
print(studient)
print(s2)
print(s3)
print(s4)
print(s5)
#(s1,s2,s3)=studient
#print(s1) ValueError: too many values to unpack (expected 3)

studient=("Chandu","Ramesh","Ramu","Tarak","Tejas")
(s2,s1,s3,s4,s5)=studient
print(s1)
studient_1=("Chandu","Ramesh",("Ramu","Tarak"),"Tejas")
print(type(studient_1))
print(studient_1)
print(studient_1[2][0])
print(len(studient_1))
print(len(studient))
print(len(studient_1[2]))
