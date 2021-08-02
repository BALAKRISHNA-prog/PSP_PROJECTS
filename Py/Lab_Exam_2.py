#2. Given an integer 'n' write a program to generate a dictionary with (i, i*i)
#such that i is  an integer between 1 and n (both included). The program should
#then print the dictionary. 
#                    Input and Output
#                    Enter a number 5
#                    {1:1, 2:4, 3:9, 4:16, 5:25}
#Making an empty dictionary
dict = {}
#We use try-except method, so as to prompt the user to get the intended(integer)
#input 
try:
    inp = int(input("Enter a number "))
except:
    print("Invalid input")
    quit()
for i in range(inp+1):#We take range (inp+1) as the index starts from '0'
    dict[i] = i*i     
dict.pop(0)  #pops the item present at index=0
print(dict)
