## Program 24 - to accept a group of numbers and find their total average 

def calc(lst):              # passing a group of elements 
    """ to find total and average """
    n = len(lst)
    
    sum = 0
    for i in lst :
        sum+=i
    
    avg = sum/n
    
    return sum, avg
    
    
# take a group of integers from keyboard
print('Enter numbers separated by space : ')
lst = [int(x) for x in input().split()]

# call calc() and pass the list 
x, y = calc(lst)

print('Total : ', x)
print('Average : ', y)


# Output:
'''
F:\PY>py function_24.py
Enter numbers separated by space :
10 20 30 40 51
Total :  151
Average :  30.2

F:\PY>
'''