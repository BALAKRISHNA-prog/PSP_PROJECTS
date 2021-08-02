#A dictionary in python is the unordered and changable collection of data values
#that holds key_value pairs.
#A Dictionary in python is declared by enclosing a comma-seperated list of key-value pairs using curly
#braces({}).
#Syntax for python Dictionary:
'''
student1={'Name':'Balakrishna','Branch':'ECE','Section':'A7','Roll_No':7001}
print(type(student1))
print(student1)

student1={'Name':'Balakrishna','Branch':'ECE','Section':'A7','Roll_No':7001,'Name':'Kittu'}
print(student1)

student1={'Name':'Balakrishna','Branch':'ECE','Section':'A7','Roll_No':7001}
print("Before updating")
print(student1)
#'Member':NCC
student1.update({'Member':'NCC'})
print("After updating")
print(student1)

#Delete keys from the dictionary
student1={'Name': 'Balakrishna', 'Branch': 'ECE', 'Section': 'A7', 'Roll_No': 7001, 'Member': 'NCC'}
print("Before deleting")
print(student1)
del student1['Name']
print("After deleting")
print(student1)

#items() gives list of tuple pairs
print(student1.items())
'''
#printing the keys
student1={'Name':'Balakrishna','Branch':'ECE','Section':'A7','Roll_No':7001}
print("Keys of student1 are")
print(student1.keys())
print("values of student1 are")
print(student1.values())
for i in student1.keys():
    print(student1[i])

