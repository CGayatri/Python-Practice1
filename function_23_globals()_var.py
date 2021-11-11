## Program 23 - to get a copy of global variable into a function and work with it 
## globals()[key]

# same name for global and local variables 

a = 1           # this is global var a
def myfun():
    a = 2       # this is local var a
    
    x = globals()['a']      # get global var into x i.e. value of global var a =1 --> assign to x
    
    print('Inside function, global var a =', x)
    print('Inside function, local var a =', a)
    
    
myfun()
print('Outside function, global var a =', a)



#Output:
'''
F:\PY>py "function_23_globals()_var.py"
Inside function, global var a = 1
Inside function, local var a = 2
Outside function, global var a = 1

F:\PY>
'''
