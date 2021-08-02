#) Write a program to perform addition of two square matrices

R1 = 3
C1 = 3
  
# Initialize matrix
matrix1 = []
print("Enter the entries of the fist matrix rowwise:")
  
# For user input
for i in range(R1):          # A for loop for row entries
    a =[]
    for j in range(C1):      # A for loop for column entries
         a.append(int(input()))
    matrix1.append(a)
  
# For printing the matrix
for i in range(R1):
    for j in range(C1):
        print(matrix1[i][j], end = " ")
    print()
X=matrix1
###
R2 = 3
C2 = 3
  
# Initialize matrix
matrix2 = []
print("Enter the entries of the second matrix rowwise:")
  
# For user input
for i in range(R2):          # A for loop for row entries
    a =[]
    for j in range(C2):      # A for loop for column entries
         a.append(int(input()))
    matrix2.append(a)
  
# For printing the matrix
for i in range(R2):
    for j in range(C2):
        print(matrix2[i][j], end = " ")
    print()

Y=matrix2





 # Program to add two matrices using nested loop
 

 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print("The added matrix is:") 
for r in result:
    print(r)
