file = open("text.txt")   # open the file

# print(file.read())  #read all the contents of the file
#print(file.read(2))  #read n number of character by passing parameter

#print(file.readline())   #read one line at a time
#print(file.readline())

# print line by line using while loop, if it find blank it will come out
# line = file.readline()
# while line!="":
#     print(line)
#     line= file.readline()

#using realines() to store all data line by line in a list with index
#print(file.readlines())
i=0
#line= file.readlines()
for line in file.readlines():
    print(line)          # will read each line
file.close()   # close the file