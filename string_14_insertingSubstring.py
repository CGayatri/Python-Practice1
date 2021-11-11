## Program 14 - to insert a substring in a string in a particular position 

main = input('Enter a string : ')
sub = input('Enter a sub string : ')

n = int(input('Enter position no : '))

# decrease n by 1 to insert at correct position 
n = n-1

# find the number of characters in str, sub 
len_main = len(main)
len_sub = len(sub)

# take another string as a list 
str1= []

# apppend 0 to (n-1) characters from str to str1 
for i in range(n):
    str1.append(main[i])

# append sub string to str1 
for i in range(len_sub):
    str1.append(sub[i])
    
# append remaining characters from str to str1
for i in range(n, len_main):
    str1.append(main[i])
    
# convert the individual characters of list str1 into a string using join() method with empty string as separator
str1 = ''.join(str1)

# display the total string 
print(str1)

"""
F:\PY>py string_14_insertingSubstring.py
Enter a string : It is summer
Enter a sub string : hot
Enter position no : 7
It is hotsummer

F:\PY>
"""




