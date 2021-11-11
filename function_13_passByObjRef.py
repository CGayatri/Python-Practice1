## Program 13 - to pass an integer to a function and modify it 

## integer, float, string, tuple --> immutable (unmodifiable)
## list, dictionary --> mutable (modifiable)


## Pass by Object Reference 

def modify(x):
    """ reassign a value to the variable """
    
    x = 15          # trying to modify immutable object,; new object will get created here and won't be available outside this function 
    print('Inside function : ', end='')
    print(x, id(x))
    
# call modify() and pass x
x = 10
modify(x)           #i.e. modify(object 10's reference name/tag)
print('Outside function : ', end='')
print(x, id(x))



#Output:
'''
F:\PY>py function_13_passByObjRef.py
Inside function : 15 140725215025248
Outside function : 10 140725215025088
'''

