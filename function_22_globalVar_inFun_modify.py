## Program 22 - to access global variable inside a function and modify it 

# 'global' keyword 

a = 1
def myfun():
    global a                # this is global var 
    
    print('Inside function before modify, global a =', a)       # displays global var 
    
    a = 2                   # modify global var value 
    print('Inside function after modify, modified a =', a)      # display new value 
    
    
myfun()
print('Outside function, global a =', a)      # display modified value 



# Output:
'''
F:\PY>py function_22_globalVar_inFun_modify.py
Inside function before modify, global a = 1
Inside function after modify, modified a = 2
Outside function, global a = 2

F:\PY>
'''