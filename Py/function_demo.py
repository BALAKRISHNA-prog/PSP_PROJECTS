'''#A function in python is a piece of code which runs when it is referenced.
#It is used to utilize the code in more than one place in a program.,
#in-built functions,user defined functions print(),input()

def add(x,y):
    return x+y
x=3
y=4

#z=add(x,y)
#print("z=",z)
#print(add(x,y))
#print(add(30,40))
def square(x):
    return x*x
#print(square(20))
#Lambda function:It is an anonymous function or a function having no name.
#It a small and restricted function having no more than one line.
#lambda p1,p2:expression

adder=lambda x,y:x+y
print(adder(1,2))
multiplier=lambda q,w,e:q*w*e
print(multiplier(1,2,3))
import math
Euclidian_distance=lambda x,y:math.sqrt((x**2)+(y**2))
print(Euclidian_distance(3,4))

#map()-->It is used to apply a particular operation to every element in a
#sequence
even_list=[2,4,6,8,10]
squared_even_list=map(lambda x:x*x,even_list)
print(list(squared_even_list))

#Temperature conversion C to F using lambda function
Temperature_in_C=[39.2,36.5,37.3,38,37.8]
Temperature_in_F=map(lambda x:((x*9/5)+32),Temperature_in_C)
print(list(Temperature_in_F))
'''
#lambdas in reduce()
from functools import reduce
even_list=[2,4,6,8,10]
product=reduce(lambda x,y:x*y,even_list)
print(product)
