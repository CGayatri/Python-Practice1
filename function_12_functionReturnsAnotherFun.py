## Program 12 - to know how a function can return another function 

# functions can return other functions 

def display():
    def message():
        return 'How are you?'
        
    return message
    
    
# call display() function and it returns message() function 

# in following code, 'fun' refers to the name : 'message' @ line:9

fun = display()
print(fun())


#Output:
'''
F:\PY>py function_12_functionReturnsAnotherFun.py
How are you?
'''