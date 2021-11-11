## program 1 - to calculate the area of a circle 

# import math module for pi constant value 
import math 

r = float(input("Enter radius: "))
area = math.pi * r**2
print('Area of circle= ', area)
print('Area of circle= {:0.2f}'.format(area))

'''
F:\PY>py control_1.py
Enter radius: 15.5
Area of circle=  754.7676350249478
Area of circle= 754.77
'''