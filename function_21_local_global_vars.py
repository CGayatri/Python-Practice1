## Program 21 - global and local variables 

# same name for global and local variables 

a = 1           # this is global var

def myfun():
    a=2         # this is local var
    print('Inside function, a =', a)    # displays local var i.e. a = 2
    
    
myfun()
print('Outside function, a =', a)       # displays global var i.e. a = 1
 


'''
F:\PY>py function_21_local_global_vars.py
Inside function, a = 2
Outside function, a = 1

'''