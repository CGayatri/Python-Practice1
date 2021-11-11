## program 7 - to display all positions of a sub string in a given main string - v2.0

# to find all occurrences of sub string in a main string 

main = input('Enter main string : ')
sub = input('Enter sub string : ')

flag = False

n = len(main)
pos = -1 

while True :        # repeat forever till True 
    pos = main.find(sub, pos+1, n)
    if pos == -1:
        break
    
    print('Found at position :', (pos+1))
    flag=True
    
if flag==False:
    print('Not found')
    
    
'''
F:\PY>py string_finding_substring_7.py
Enter main string : This is a book
Enter sub string : is
Found at position : 3
Found at position : 6

F:\PY>py string_finding_substring_7.py
Enter main string : This is a book
Enter sub string : notebook
Not found

F:\PY>
'''