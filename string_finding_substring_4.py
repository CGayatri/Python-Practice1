## program 4 - to find the first occurance of substring in a give main string

# find(), index(), rfind(), rindex() - find() returns -1 if not found, index() returns ValueError exception if sub string is not found . 
# mainstring.find(substring, beginnning, ending)

# to find first occurrence of sub string in a main string
str = input('Enter main string: ')
sub = input('Enter sub string: ')

# find position of sub in str
# search from 0th to last characters in str 

n = str.find(sub, 0 , len(str))

# find() returns -1 if sub string is not found 
if n == -1:
    print('Sub string not found')
else:
    print('Sub string found at position :', (n+1))

'''
F:\PY>py string_finding_substring_4.py
Enter main string: This is a book
Enter sub string: is
Sub string found at position : 3

'''