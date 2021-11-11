## program 11 - to display even numbers between m and n (minimum and maximum range)

m , n = [int(i) for i in input("Enter comma separated minimum and maximum range: ").split(',')]
# 1 to 10 ===> 

x = m   # start from m onwards
#x = 1 #  start from ths number

# make start as even so that adding 2 to it would give next even number
if(x%2 != 0):
    x = x + 1

while(x>=m and x<=n):
    print(x)
    x+=2

print("End")


"""
F:\PY>py control_11.py
Enter comma separated minimum and maximum range: 1, 10
2
4
6
8
10
End

F:\PY>
"""


'''
while(x>=m and x<=n):
    if(x%2 == 0):
        print(x)
    x+=2

print("End")


F:\PY>py control_11.py
Enter comma separated minimum and maximum range: 1, 10
End

'''
