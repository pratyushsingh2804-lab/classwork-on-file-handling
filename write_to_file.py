# program for writing data into file 

# opening file for write operation 
filev = open("firstfile.txt", "w")   # fixed file name

# writing five sentence into file 
sentences = []

# taking input from user
print("Enter any five sentences:")

for x in range(5):
    # input of data from user 
    sentence = input()
    
    # inserting sentence into the list (added newline)
    sentences.append(sentence + "\n")
    
    print("-----------------------------")
        
# writing data into file
filev.writelines(sentences)

# closing the file
filev.close()
