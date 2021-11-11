## Program 16 - the positional arguments of a function 

def attach(s1, s2):
    """ to join s1 and s2 and display total string """
    s3 = s1 + s2 
    print('Total string: ' + s3)            # + : String 
    #print('Total string: ' , s3)            # , : int
    
# call attach() and pass 2 strings 
attach('New', 'York')           # positional arguments 

#attach(10, 20)                 #print('Total string: ' , s3)
#Total string:  30


# Output:
'''
F:\PY>py function_16_positionalArg.py
Total string: NewYork

F:\PY>
'''