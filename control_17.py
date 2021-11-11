## program 17 - to display and find the sum of a list of numbers using for loop 

# take a list of numbers 
list = [10, 20, 30, 40, 50]

sum = 0

#retrieve one by one elements and add to sum 
for i in list :
    print(i)
    sum+=i

print("Sum =", sum)


'''
F:\PY>py control_17.py
10
20
30
40
50
Sum = 150
'''