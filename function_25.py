## Program 25 - function to display a group of strings 

def display(lst):
    """ to display the strings """
    
    for i in lst:
        print(i)
        

# take a group of strings from keyboard 
print('Enter strings separated by comma : ')
lst = [x for x in input().split(',')]

# call display() and pass the list 
display(lst)



#Output:
'''
F:\PY>py function_25.py
Enter strings separated by comma :
Gaurav,Vinod,Vishal,Ankit
Gaurav
Vinod
Vishal
Ankit

F:\PY>
'''