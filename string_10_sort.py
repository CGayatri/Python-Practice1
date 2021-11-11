## Sorting String - sort(), sorted()

## program 10 - to sort a group of strings into alphabetical order .

# string.sort() - It sorts the oiginal array. So, the original order fo strings will be lost and we will have only one sorted array. 
# sorted(string) - To retain the original array even after even after sorting

# take an empty array 
str = []

# accept how many strings 
n = int(input('How many strings: : '))

# apppend each string to an empty array and make an array of strings : str.append(input())
for i in range(n):
    print('Enter string : ', end='')
    str.append(input())


# sort the array - sort()
str.sort()                      # sort() method 

# display the sorted arary 
print('Sorted list :')
for i in str:
    print(i)


'''
F:\PY>py string_10_sort.py
How many strings: : 5
Enter string : Pune
Enter string : Delhi
Enter string : Mumbai
Enter string : Chennai
Enter string : Bengaluru
Sorted list :
Bengaluru
Chennai
Delhi
Mumbai
Pune
'''

print()

# sort the array - sorted()
str1 = sorted(str)              # sorted() method
# display sorted array 
print('Sorted : ')
for i in str1:
    print(i)
    
"""

F:\PY>py string_10_sort.py
How many strings: : 5
Enter string : Pune
Enter string : Delhi
Enter string : Mumbai
Enter string : Chennai
Enter string : Bengaluru
Sorted list :
Bengaluru
Chennai
Delhi
Mumbai
Pune

Sorted :
Bengaluru
Chennai
Delhi
Mumbai
Pune

F:\PY>
"""    
    
