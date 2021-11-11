## program 6 - to display all positions of a sub string in a given main string 

main = input('Enter main string : ')
sub = input('Enter sub string : ')

i=0
flag = False            # becomes true if substring is found 
count = 0

n = len(main)

while i<n:
    pos = main.find(sub, i, n)
    if (pos != -1):          # if found, display its position
        count+=1            # no. of times sub string occurred
        print(sub+ ' found at position :', (pos+1))
        i=(pos+1)           # search from (pos+1) position onwards
        flag = True
    else:
        i=i+1               # search from next character onwards 

if (flag == False):
    print('Sub string not found')
else:
    print('Sub string found {} times'.format(count))
    
    
'''
F:\PY>py string_finding_substring_6.py
Enter main string : This is a book
Enter sub string : is
is found at position : 3
is found at position : 6
Sub string found 2 times

F:\PY>
'''