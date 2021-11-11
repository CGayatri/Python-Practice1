## Program 20 - keyword variable arguments --> **kwargs --> dictionary (mutable)

def display(farg, **kwargs):                # **kwargs can take 0 or more values 
    """ to display given values """
    print('Formal argument =', farg)
    
    for x, y in kwargs.items():              # items() will give pairs of items 
    
        print('key = {}, value = {}'.format(x, y))
        
        
# pass 1 formal argument and 2 keyword arguments
display(5, rno=10)

print()

# pass 1 formal argument and 4 keyword arguments 
display(5, rno=10, name="Gayatri") 



#Output:
'''
F:\PY>py function_20_keywordVariableArg.py
Formal argument = 5
key = rno, value = 10

Formal argument = 5
key = rno, value = 10
key = name, value = Gayatri

F:\PY>
'''

print()
# pass 1 formal argument and 0 keyword arguments 
display(5) 
'''
Formal argument = 5
'''
