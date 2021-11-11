## Program 19 - to show variable length argument and its use ---> *args --> tuple (immutable)

def add(farg, *args):                       # *args can take 0 or more values
    """ to add given numbers """
    print('Formal argument = ', farg)
    
    sum = 0 
    for i in args:
        sum+=i
    print('Sum of all numbers =', (farg+sum))
    
# call add() function and pass arguments 
add(5)


'''
F:\PY>py function_19_variableLengthArg.py
Formal argument =  5
Sum of all numbers = 5
'''

add(5, 10)
'''
Formal argument =  5
Sum of all numbers = 15
'''

add(5, 10, 20, 30)
'''
Formal argument =  5
Sum of all numbers = 65
'''
