#This program will count the no. of charecters,words,lines and occurences.
#open file 
file = open("Talking_Idiots.txt", "r")
#Set the no. of lines,words and charecters to zero.
Number_of_lines = 0
Number_of_words = 0
Number_of_characters = 0

for line in file:
  #The strip() method returns a copy of the string by
  #removing both the leading and the trailing characters.
  #By default, it removes leading whitespaces if no argument passed.
  line = line.strip("\n") 
  #The split() method splits a string into a list(Lists are used to store
  #multiple items in a single variable). You can specify the
  #separator, default separator is any whitespace.
  words = line.split()
#+= operator is used to add two values and assign the final value to a variable.
  Number_of_lines += 1
  Number_of_words += len(words)
  Number_of_characters += len(line)
print("The number of lines are:",Number_of_lines)
print("The number of words are:",Number_of_words)
print("The number of charecters are:",Number_of_characters)
 
file.close()
# Open the file in read mode
text = open("Talking_Idiots.txt", "r")
  
# Create an empty dictionary
#Dictionaries are Python's implementation of a data structure that is more
#generally known as an associative array. A dictionary consists of a
#collection of key-value pairs. Each key-value pair maps the key to its
#associated value.
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split()
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
 print(key, ":", d[key])
#Print the repeated words and their no. of occurences
print("The repeated words and their occurences are:")
for key in list(d.keys()):
      if int(d[key])>1:
        print(key, ":", d[key])
