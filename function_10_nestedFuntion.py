## Program 10 - to define a function inside a function 

# define a function inside another function 
def display(str):
    def message():
        return 'How are you?'
        
    result = message() + str 
    
    return result 
    

# call display() function 
print(display("Gayatri"))


'''
F:\PY>py function_10_nestedFuntion.py
How are you?Gayatri
'''