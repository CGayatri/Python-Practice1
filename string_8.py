## Splitting and Joining Strings
## Program 8 - to accept and display a group of numbers 

# string.split(seperator)
# separator.join(string)

str = input('Enter numbers separated by space : ')

# cut the string where a space is found 
lst = str.split(' ')


# display the numbers from teh list 
for i in lst :
    print(i)
    
'''
F:\PY>py string_8.py
Enter numbers separated by space : 10 20 30 40
10
20
30
40
'''