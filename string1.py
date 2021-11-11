
s1 = 'Welcome to "Core Python" learning'
print(s1)

s2 = "Welcome to 'Core Python' learning"
print(s2)

'''
F:\PY>py string1.py
Welcome to "Core Python" learning
Welcome to 'Core Python' learning
'''

s3 = "Welcome to \tCore Python \nlearning"
print(s3)

'''
F:\PY>py string1.py
Welcome to "Core Python" learning
Welcome to 'Core Python' learning
Welcome to      Core Python
learning
'''

s4 = "Welcome to \aCore Python \alearning"
print(s4)

s5 = "Welcome to \bCore Python \blearning"
print(s5)

'''
F:\PY>py string1.py
Welcome to "Core Python" learning
Welcome to 'Core Python' learning
Welcome to      Core Python
learning
Welcome to Core Python learning     # alert tone rings
Welcome toCore Pythonlearning
'''

s6 = "Welcome to \nCore Python \nlearning"
print(s6)

'''
F:\PY>py string1.py
Welcome to "Core Python" learning
Welcome to 'Core Python' learning
Welcome to      Core Python
learning
Welcome to Core Python learning
Welcome toCore Pythonlearning
Welcome to
Core Python
learning
'''

s7 = "Welcome to \vCore Python \vlearning"
print(s7)

'''
F:\PY>py string1.py
Welcome to "Core Python" learning
Welcome to 'Core Python' learning
Welcome to      Core Python
learning
Welcome to Core Python learning
Welcome toCore Pythonlearning
Welcome to
Core Python
learning
Welcome to Core Python learning
'''

print()
s8 = "Welcome to \rCore Python \rlearning"
print(s8)

"""
F:\PY>py string1.py
Welcome to "Core Python" learning
Welcome to 'Core Python' learning
Welcome to      Core Python
learning
Welcome to Core Python learning
Welcome toCore Pythonlearning
Welcome to
Core Python
learning
Welcome to Core Python learning

learninghon

F:\PY>
"""

#s9 = "Welcome to \xCore Python \xlearning"
#print(s9)

#F:\PY>py string1.py
#  File "string1.py", line 97
#    s9 = "Welcome to \xCore Python \xlearning"
#         ^
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 11-13: truncated \xXX escape


s = r"Raw \tstring \nCore Python"
print(s)
#Raw \tstring \nCore Python

name = u'\u0915\u094b\u0930 \u092a\u0948\u0925\u0964\u0928'
print(name)

## core python (would type in hindi)

# length of string - len() function
str = 'Core Python'
length = len(str)
print('Length =', length)       # Length = 11



