## program 2 - to access the characters of a string using for loop 

# accessing elements of a string using for loop 
str = 'Core Python'

# access each letter using for loop
for i in str : 
    print(i, end=' ')
   
'''   
F:\PY>py string_2.py
C o r e   P y t h o n
F:\PY>
'''

print()

for i in str[ : : ]:
    print(i, end='')
    
'''
F:\PY>py string_2.py
C o r e   P y t h o n
Core Python
F:\PY>
'''

print()

for i in str[ : : -1]:
    print(i, end='')
    
    
'''
F:\PY>py string_2.py
C o r e   P y t h o n
Core Python
nohtyP eroC
F:\PY>
'''