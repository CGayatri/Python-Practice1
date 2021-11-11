# program to create a bytes type array, read and display the elements of the array 

# program to understand bytes type array

# create a list of byte numbers
elements = [10, 20, 0, 40, 15]

# convert the list into bytes type array 
xArr = bytes(elements)

# retrieve elements from xArr using for loop and display
for i in xArr : print(i)

#NameError: name 'x' is not defined



print(type(xArr))
#<class 'bytes'>