# to open file for read operation 
filev = open("firstfile.txt", "r")   # fixed typo (filke → file)

# to check file is open or not
if(filev):
    # to read data from file
    data = filev.read()
    print(data)
    print("-----------------------------")
    print("no of characters :", len(data))
    
    # closing file
    filev.close()
else:
    print("unable to open file")
