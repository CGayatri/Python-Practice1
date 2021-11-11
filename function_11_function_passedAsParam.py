## Program 11 - to pass a function as parameter to another function 

# functions can be passed as parameters to other functions

def display(fun):
    return 'Hai ' + fun 
    
def message():
    return 'How are you? '
    
def sum():
    return 'added'

# call dispaly() function and pass message() function
print(display(message()))       # whichever function you pass 
print(display(sum()))           # whichever function you pass 


'''
F:\PY>py function_11_function_passedAsParam.py
Hai How are you?
'''

"""
F:\PY>py function_11_function_passedAsParam.py
Hai How are you?
Hai added
"""
