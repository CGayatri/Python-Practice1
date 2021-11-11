## program 27 - to retrieve only negative numbers from a list of numbers 

# Retrieving only negative numbers from a list 
num = [1,2, 3, -4, -5, -6, -7, 8, 9]

for i in num :
    if (i>0):
        pass            # we are not interested 
    else :
        print(i)        # this is what we need 
        

'''
F:\PY>py control_27.py
-4
-5
-6
-7

'''