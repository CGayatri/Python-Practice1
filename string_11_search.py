## program 11- Searching in the String - to search for the position of a string in a given group of strings 

# take an empty array
str = []

# accept how many strings
n = int(input('How many strings? : : '))

# append strings to str array : str.append(input())
for i in range(n):
    print('Enter string: ', end='')
    str.append(input())

    
# ask for the string to search 
s = input('Enter string to search: ')

# linear search or sequential search 
flag = False

for pos in range(len(str)):                 # repeat from 0th to n-1 th strings
    if (s==str[pos]):                       # if s is matching with str[pos] then found 
        print('Found @ position :' , (pos+1))
        flag = True
        
        
if flag == False:
    print('Not Found')

"""
F:\PY>py string_11_search.py
How many strings? : : 5
Enter string: Ramesh
Enter string: Kumar
Enter string: Sriya
Enter string: Vinod Kumar
Enter string: Ramesh
Enter string to search: Ramesh
Found @ position : 1
Found @ position : 5
"""

'''
  File "string_11_search.py", line 12, in <module>
    str.apppend(input())
AttributeError: 'list' object has no attribute 'apppend'
'''