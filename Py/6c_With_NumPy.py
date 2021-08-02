#Write a program to perform multiplication of two square matrices

#) Write a program to perform addition of two square matrices(With NumPy)
import numpy as np
  
R1 = 3
C1 = 3
  
  
print("Enter the entries of 3*3 matrix in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries1 = list(map(int, input().split()))
  
# For printing the matrix
matrix1 = np.array(entries1).reshape(R1, C1)
print(matrix1)

R2 = 3
C2 = 3
  
  
print("Enter the entries of second  3*3 matrix in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries2 = list(map(int, input().split()))
  
# For printing the matrix
matrix2 = np.array(entries2).reshape(R2, C2)
print(matrix2)

print("The added matrix is:")
print(matrix1*matrix2)
