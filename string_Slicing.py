## slicing the strings - a slice represent a part or a piece of a string 

## stringname[start : stop : stepsize]

# if 'start' and 'stop' are not specified, then slicing is done from 0th to (n-1)th element.
# if 'stepsize' is not written, then it is  taken to be 1. 

str = 'Core Python'
print(str)      #Core Python
print(str[0:9:1])       # access string from 0th to 8th element in steps of 1 
#Core Pyth

print(str[0:9:2])       # access every other character from 1st char onwards , i.e. 0th, 2nd, 4th, 6th, chars and so on.
#Cr yh

print(str[::])          # access string from 0th to last character 
#Core Python

print(str[2:4:1])       # access from str[2] to str[3] in steps 1
#re

print(str[::2])         # access entire string in steps of 2 
#Cr yhn

print(str[2::])         # access string from str[2] to ending 
#re Python

print(str[:4:])         # access string from str[0] to str[3] in steps of 1 (default)
#Core

## reverse order : strinngname[-start:-stop]
#Core Python
#012345678910
#C o r e  P y t h o n
#-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(str[-4:-1])      # access string from str[-4] to str[-2] from left to right (cuz stepsize is NOT negative)
#tho

print(str[-6::])        # access from str[-6] till the end of the string 
#Python

print(str[-1:-4:-1])    # retrieve fromstr[-1] to str[-3] from right to left 
#noh

print(str[-1::-1])      # retrieve from str[-1] till first element from right to left 
#nohtyP eroC