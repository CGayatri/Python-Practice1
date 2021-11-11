## Program 17 - Keyword arguments of a function

def grocery(item, price):
    """ to display teh given arguments """
    print('Item = %s' % item)
    print('Price = %.2f' % price)
    

# call grocery() function and pass 2 arguments 
grocery(item = 'Sugar', price = 50.75)      # keyword arguments 
grocery(price = 88.00, item = 'Oil')        # keyword arguments 


#Output:
'''
F:\PY>py function_17_keywordArg.py
Item = Sugar
Price = 50.75
Item = Oil
Price = 88.00

F:\PY>
'''