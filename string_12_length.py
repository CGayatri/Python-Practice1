## Program 12 - to find teh length of a string without using len() method 
## Finding Number of Characters and Words

# to find a no. of characters in a string 
str = input('Enter a string: ')

i = 0
for s in str:
    print(str[i], end='')
    
    i+=1
    
print('\nNo. of characters :', i)

'''
F:\PY>py string_12_length.py
Enter a string: This is a book
This is a book
No. of characters : 14

F:\PY>py string_12_length.py
Enter a string: Kindly let me survive you morons
Kindly let me survive you morons
No. of characters : 32

'''