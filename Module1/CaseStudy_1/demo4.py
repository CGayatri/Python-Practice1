# Write a for loop that prints all elements of a list and their position in the list.
# a = [4,7,3,2,5,9] 

# Hint: Use Loop to iterate through list elements.

pos = 0 

a = [4,7,3,2,5,9]

for i in a:
    print('element at {} : {}'.format(pos, i) )
    pos+=1
    
    
'''
F:\PY\Module1\CaseStudy_1>py demo4.py
element at 0 : 4
element at 1 : 7
element at 2 : 3
element at 3 : 2
element at 4 : 5
element at 5 : 9

F:\PY\Module1\CaseStudy_1>
'''
