#1.Looping over a range of numbers
#Normal method
for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)
    
#Better
print("\n")
for i in range(6):
    print(i**2)
    
#2.Using Generators Inside Functions
#Normal way using lists
print("\n")
total = 0
list1 = [1,2,3,4,5,6,7,8,9,10]
for element in range(0, len(list1)):
    total = total + list1[element]
 
print(total)
#Idiomatic approach
print(sum(i for i in range(11)))     

#3.Looping over a collection
#Normal method
print("\n")
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])
#Better
print("\n")
for color in colors:
    print(color)
#4.Looping a string backwards in the list form
print("\n")
colors = ['red', 'green', 'blue', 'yellow']
print(colors[::-1])

#Looping backwords line by line
print("\n")
for color in reversed(colors):
    print(color)
#5.Reversing Numbers
print("\n")
list2 = [1,3,6,4,2]
print(list2[::-1])
#6.Looping over a collection and indices
print("\n")
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print((i), colors[i])
#Better
print("\n")
for i, color in enumerate(colors):
    print((i), color)
#It's fast and beautiful and saves you from tracking the individual indices and incrementing them.

#7.Looping over two collections
names = ['Raj', 'Chintu', 'Mintu','Pintu']
colors = ['red', 'green', 'blue', 'yellow']
print("\n")
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], colors[i])
#Better
print("\n")
for name, color in zip(names, colors):
    print(name, color)

#8.Looping in sorted order


# Forward sorted order
print("\n")
numbers = [6, 9, 3, 1]
print("The numbers are:",numbers)
print(sorted(numbers))




# Backwards sorted order
print("\n")
print(sorted(numbers, reverse=True))
   



#9.Printing in any order
print("\n")
List = [1,2,3]
w, v, t = List
print(v, w, t )
print(t, v, w )

#10.Swap two numbers using a single line of code
print("\n")
x,y = 11, 34
print(x)
print(y)
x,y = y,x
print(x)
print(y)

#11.Print a string N Times
print("\n")
str ="Point"
print(str * 3)

#12. Find The Most Frequent Value In A List.
print("\n")
num = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(num), key = num.count))

#13.Converting lists into dictionary
print("\n")
user = ['Chintu', 'Mintu', 'Pintu']
age = [23,19,34]
dictionary = dict(zip(user, age))
print(dictionary)

#14.Multiple user input
#Normal method
print("\n")
x = input('Enter a number')
y = input ('Enter another number')
print(x)
print(y)
#Better
print("\n")
x, y = input("Enter two values with space between them: ").split() 
print("value of x ", x)
print("value of y: ", y)


#15.Using if and else as a short ternary operator replacement
#Normal Method:
print("\n")
x = True
value = 0
if x:
    value = 1
print(value)
#idiomatic
print("\n")
x = True
value = 1 if x else 0
print(value)

#16.Multiple assignment
#Normal method
print("\n")
x = 'ha'
y = 'ha'
z = 'ha'
print("x,y and z are:",x,y,z)
#idiomatic
print("\n")
x = y = z = 'ha'
print("x,y and z are:",x,y,z)
#Using Sets:
#Normal way
print("\n")
ls1 = [1, 2, 3, 4, 5]
ls2 = [4, 5, 6, 7, 8]
elements_in_both = []
for element in ls1:
  if element in ls2:
    elements_in_both.append(element)
print(elements_in_both)
#Idiomatic 
print("\n")
ls1 = [1, 2, 3, 4, 5]
ls2 = [4, 5, 6, 7, 8]
elements_in_both = list( set(ls1) & set(ls2) )
print(elements_in_both)

#17.Set Comprehension
#Normal way
print("\n")
elements = [1, 3, 5, 2, 3, 7, 9, 2, 7]
unique_elements = set()
for element in elements:
  unique_elements.add(element)
print(unique_elements)
#idiomatic
print("\n")
elements = [1, 3, 5, 2, 3, 7, 9, 2, 7]
unique_elements = {element for element in elements}
print(unique_elements)

#18.Updating Values in a List
#Normal way
# Add three to all list members.
print("\n")
a = [3, 4, 5]
b = a                     # a and b refer to the same list object

for i in range(len(a)):
    a[i] += 3             # b[i] also changes
    print(a)
    print(b)
#Idiomatic
print("\n")
a = [3, 4, 5]
b = a

# assign the variable "a" to a new list without changing "b"
a = [i + 3 for i in a]
b = a[:]  # even better way to copy a list   
print(a)
print(b)

#19.Internal squaring example in idiomatic way
#Normal way
print("\n")
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for idx in range(len(x)):
    if x[idx] % 2 == 0:
        result.append(x[idx] * 2)

    else:
        result.append(x[idx])

print(result)
#idiomatic
print("\n")
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=[(element * 2 if element % 2 == 0 else element) for element in x]
print(result)

#20.Quick Copy of the List
#Normal method:
print("\n")
list_a = [1,2,3,4,5]
list_b = [1,2,3,4,5]
print(list_a)
print(list_b)
#Idiomatic 
print("\n")
list_a = [1,2,3,4,5]
list_b = list_a[:]
print(list_a)
print(list_b)
  
