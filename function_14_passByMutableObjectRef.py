## Program 14 - to pass a list to function and modify it 

## integer, float, string, tuple --> immutable (unmodifiable)
## list, dictionary --> mutable (modifiable)

## Pass by Object Reference 

def modify(lst):
    """ to add a new element to list """
    lst.append(9)               # same list will get modified which was passed as object reference ; no new list object will get created since List object is mutable 
    print('Inside function : ', end='')
    print(lst, id(lst))
    
# call modify() and pass lst 
lst = [1,2,3,4]
modify(lst)                 # i.e. modify(Reference name(lst) of object '1,2,3,4')
print('Outside function : ', end='')
print(lst, id(lst))

    
# Output:
'''
F:\PY>py function_14_passByMutableObjectRef.py
Inside function : [1, 2, 3, 4, 9] 2417677441856
Outside function : [1, 2, 3, 4, 9] 2417677441856

'''