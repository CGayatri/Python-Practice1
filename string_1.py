## program 1 - to access each element of a string in forward and reverse orders using while loop

# indexing on strings
str = 'Core Python'

# access each character using whie loop 
i = 0                   # i  = 0, 1, 2, 3, ... (n-1)
n = len(str)
while i<n:              # 0 to n-1
    print(str[i], end=' ')
    i+=1
    
print()

# access in reverse order 
i=-1                    # i = -1, -2, -3, ... (-n)
while i>=-n:            # -1 to -n
    print(str[i], end=' ')      #str[i]
    i-=1

print()

# access in reverse order using negative index
i=1                     # i = 1, 2, 3, ... n
#n = len(str)
while i<=n:            # 1 to n
    print(str[-i], end=' ')     #str[-i]
    i+=1
    
'''
F:\PY>py string_1.py
C o r e   P y t h o n
n o h t y P   e r o C
n o h t y P   e r o C
F:\PY>
'''