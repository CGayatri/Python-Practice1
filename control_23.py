## program 23 - to search for an element in the list of elements

group1 = [1,2,3,4,5]
search = int(input('Enter element to search: '))

for element in group1:
    if search == element:
        print("Element found in group1")
        break   # come out of the loop 
else: 
    print("Element not found in group1")    # this is else suite
    
    
"""
F:\PY>py control_23.py
Enter element to search: 23
Element not found in group1

F:\PY>
F:\PY>py control_23.py
Enter element to search: 34
Element not found in group1

F:\PY>py control_23.py
Enter element to search: 3
Element found in group1

F:\PY>
"""