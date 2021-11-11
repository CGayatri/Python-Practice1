## Program 18 - default arguments

def grocery(item, price = 40.00):
    """ to display the given arguments """
    print('Item = %s' % item)
    print('Price = %.2f' % price)
    
# call grocery() and pass arguments 
grocery(item='Sugar', price=50.75)      # pass 2 arguments
grocery(item='Sugar')                   # default value for price is used 


# Output:
'''
F:\PY>py function_18_defaultArg.py
Item = Sugar
Price = 50.75
Item = Sugar
Price = 40.00

F:\PY>
'''