# program to understand bytearray type array

# create a list of elements - byte numbers
elements = [10, 20, 0, 40, 15]      #this is a list of byte numbers 

# convert the list into bytearray type array  
x = bytearray(elements)

# before modification 
print('before modification array :')
for i in x : print(i)


#before modification array :
#10
#20
#0
#40
#15


# modify first two elements of x 
x[0] = 88
x[1] = 99

# after modification 
print('after modification array :')
for i in x : print(i)


#Output:
#after modification array :
#88
#99
#0
#40
#15



print(type(x))
#<class 'bytearray'>