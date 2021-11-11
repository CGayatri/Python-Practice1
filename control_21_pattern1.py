## program 21 - to display the stars in an equilateral triangular form using a single for loop


# to display stars in equilateral triangular form 

n=40
for i in range(1, 11):
    print(' '*n, end='')     #repeat space for n times
    print('* ' * (i))       #repeat star for i times 
    n=n-1
    
'''
F:\PY>py control_21_pattern1.py
                                        *
                                       * *
                                      * * *
                                     * * * *
                                    * * * * *
                                   * * * * * *
                                  * * * * * * *
                                 * * * * * * * *
                                * * * * * * * * *
                               * * * * * * * * * *
'''



k=1

for i in range(9, -1, -1):
    print(' '*i, end='')
    print('* '*k)
    k+=1
    
'''
F:\PY>py control_21_pattern1.py
                                        *
                                       * *
                                      * * *
                                     * * * *
                                    * * * * *
                                   * * * * * *
                                  * * * * * * *
                                 * * * * * * * *
                                * * * * * * * * *
                               * * * * * * * * * *
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *

'''

n = 40 
for i in range(1,11):
    print(' ' * (n-i) + '* ' * i)
    
    
'''
F:\PY>py control_21_pattern1.py
                                        *
                                       * *
                                      * * *
                                     * * * *
                                    * * * * *
                                   * * * * * *
                                  * * * * * * *
                                 * * * * * * * *
                                * * * * * * * * *
                               * * * * * * * * * *
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *
                                       *
                                      * *
                                     * * *
                                    * * * *
                                   * * * * *
                                  * * * * * *
                                 * * * * * * *
                                * * * * * * * *
                               * * * * * * * * *
                              * * * * * * * * * *

F:\PY>
'''                                       