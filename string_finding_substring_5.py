## program 5 - to find the first occurrence of sub string in a given string using index() method 

# to find first occurrence of sub string in a main string 
str = input('Enter main string: ')
sub = input('Enter sub string: ')

# find position of sub in str
# search from 0th to last characters in str 

try:
    n = str.index(sub, 0, len(str))
except ValueError:
    print('Sub string not found')
else:
    print('Sub string found at position :', (n+1))
  
    
'''
F:\PY>py string_finding_substring_5.py
Enter main string: This is a boook
Enter sub string: s
Sub string found at position : 4

F:\PY>
'''

