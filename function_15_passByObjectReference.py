## Program 15 - to create a new object inside the function does not modify outside object 

# passing a list to a function 

def modify(lst):
    """ to create a new list """
    lst = [10, 11, 12]                  # a new list object '10,20,30' would get created with tag 'lst', won't be accessible outside function
    print('Inside function: ', end='')
    print(lst, id(lst))                 # ths newly created object would get considered here
    
    
# call modify() and pass lst 
lst = [1, 2, 3, 4]
modify(lst)
print('Outside function: ', end='')
print(lst, id(lst))                     # object '1,2,3,4' gets considered here        



# Output : 
'''
F:\PY>py function_15_passByObjectReference.py
Inside function: [10, 11, 12] 2063981230656
Outside function: [1, 2, 3, 4] 2063981222720

F:\PY>
'''