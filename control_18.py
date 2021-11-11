## program 18 - to display and sum of a list of numbers using while loop 

list = [10, 20, 30, 40 , 50]

sum = 0 
i=0

while ( i<len(list) ) :
    print(list[i])
    sum = sum + list[i]
    i+=1                    # if not mentioned, it is called "infinite loop"
print("Sum =", sum)


'''
F:\PY>py control_18.py
10
20
30
40
50
Sum = 150
'''