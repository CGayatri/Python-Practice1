## Replacing a string with another string - replace() method 

str = 'That is a beautiful girl'

s1 = 'girl'
s2 = 'flower'

str1 = str.replace(s1, s2)

print('Original string :', str)

print('Replaced string :', str1)

"""
F:\PY>py string_replace.py
Original string : That is a beautiful girl
Replaced string : That is a beautiful flower
"""