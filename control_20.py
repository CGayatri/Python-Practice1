## program 20 - to display stars in right angled triangular form using a single loop 

# to display stars in right angled triangular form - v2.0

for i in range(1, 11):
    print('* ' * (i))       # repeat star (*) for i times
    

## v1.0 :
'''
for i in range(1, 11):
    for j in range(1, i+1):
        print('* ', end='')
    print() 

'''