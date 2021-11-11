## program - 15 : to accept a list and display it 

#accepting a list from a keyboard 

lst = eval(input('Enter a list : '))
print("List= ", lst)

"""
F:\PY>py input15.py
Enter a list : ["Ajay", "Allu Arjun", "Vijay Kumar", "Gabru"]
List=  ['Ajay', 'Allu Arjun', 'Vijay Kumar', 'Gabru']
"""


'''
F:\PY>py input15.py
Enter a list : 10,20,30
List=  (10, 20, 30)
'''

"""
F:\PY>py input15.py
Enter a list : [10, 20, 30]
List=  [10, 20, 30]
"""

'''
F:\PY>py input15.py
Enter a list : 23,  "gayatri", 6.8
List=  (23, 'gayatri', 6.8)
'''

"""
F:\PY>py input15.py
Enter a list : [23, "gayatri", 6.78]
List=  [23, 'gayatri', 6.78]
"""