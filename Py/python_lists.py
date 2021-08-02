
studients=["Kittu","Suman","Surya","Praveen","Arsh","Ash"]
studient_info=["Kittu",10,9.4,"ECE",["Chem","PSP","Maths"]]
print(type(studients))
print(studients)
print(type(studient_info))
print(studient_info)

#List Slicing
print(studients[0:4])
print(studients[:4])
print(studients[2:-1])
print(studient_info)
print(studient_info[-1])
print(studient_info[-1][1])
#Appending list elements
studients.append("Venkat")
print(studients)
studients[1]="Anil"
print(studients)
#Length of a list
print(len(studients))
#Find the index value of an element in the list
Surya_index=studients.index("Surya")
print(Surya_index)
for element in studients:
    print(element)
