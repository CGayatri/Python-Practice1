## Strings are Immutable 

str = 'abcd'
print(str[0])

'''
F:\PY>python string_immutable.py
a
'''

# try to modify, you should get error - TypeError
str[0] = 'x'

'''
F:\PY>python string_immutable.py
a
Traceback (most recent call last):
  File "string_immutable.py", line 12, in <module>
    str[0] = 'x'
TypeError: 'str' object does not support item assignment
'''