############# Mathematial Functions #############3

'''
import math 
import math as m 
from math import sqrt
from math import factorial, sqrt
'''

import math
i = 16
x = math.sqrt(i)
print("Square root of i =", x)          #Square root of i = 4.0

from math import sqrt
j = 25
y = sqrt(j)
print("Square root of j =", y )         #Square root of j = 5.0

import math as m 
k = 5
fact = m.factorial(k)
print("Factorial of {0} =".format(k), fact)   #Factorial of 5 = 120


#ceil()
from math import ceil
print("ceil(4.5) is :", ceil(4.5))      #ceil(4.5) is : 5
print("ceil(4.4) is :", ceil(4.4))      #ceil(4.4) is : 5

#floor()
from math import floor
print("floor(4.5) is :", floor(4.5))    #floor(4.5) is : 4
print("floor(4.6) is :", floor(4.6))    #floor(4.6) is : 4

#radians()
from math import radians
print("90 degrees = ", radians(90), " radians")     #90 degrees =  1.5707963267948966  radians

#degrees()
from math import degrees
print("1.57 Radians = ", degrees(1.57), " degrees")     #1.57 Radians =  89.95437383553924  degrees

#sin()
from math import sin
print("sin(0.5) =", sin(0.5))           #sin(0.5) = 0.479425538604203

#cos()
from math import cos
print("cos(0.5) =", cos(0.5))           #cos(0.5) = 0.8775825618903728

#tan()
from math import tan 
print("tan(0.5) =", tan(0.5))           #tan(0.5) = 0.5463024898437905

## exponentiation
#exp()
from math import exp
print("e **10 : exp(10) =" , exp(10))       #e **10 : exp(10) = 22026.465794806718

## absolute value
from math import fabs 
print("absolute value of -4.56 =", fabs(-4.56))     #absolute value of -4.56 = 4.56
#ImportError: cannot import name 'abs' from 'math' (unknown location)

#abs() function - NOT from math module
print("absolute value of -4.56 =", abs(-4.56))      #absolute value of -4.56 = 4.56

## Factorial of a value 
#factorial()
from math import factorial 
print("Factorial of 4 =", factorial(4))     #Factorial of 4 = 24
#print("Factorial of -4 =", factorial(-4))   #ValueError: factorial() not defined for negative values


## modulus of float values; % module operator works only for integers 
#fmod(x,y)
from math import fmod
print("Float modulus of (14.5, 3) =", fmod(14.5, 3))        #Float modulus of (14.5, 3) = 2.5

#fsum(values)
## calculates acccurate sum of floating point values
from math import fsum
#print("sum of (1.5, 2.4, -3.3) =", fsum(1.5, 2.4, -3.3))    #TypeError: fsum() takes exactly one argument (3 given)
print("sum of (1.5, 2.4, -3.3) =", fsum([1.5, 2.4, -3.3]))      #sum of (1.5, 2.4, -3.3) = 0.6000000000000001


#modf(x)
## returns float and integral parts of x
from math import modf
print("modf(2.56) =", modf(2.56))       #modf(2.56) = (0.56, 2.0)


#calculating logs

#log10(x)
## returns base-10 log of x (log to the base 10)
from math import log10
print("log10(5.2345) =", log10(5.2345))     #log10(5.2345) = 0.7188752041406328

#log(x, [, base])
## returns the natural log of x to base 'base'
from math import log
print("log(5.5 , 2) =", log(5.5, 2))        #log(5.5 , 2) = 2.4594316186372973

## Square root of value 
#sqrt()
from math import sqrt
print("square root of 49, sqrt(49) =", sqrt(49))    #square root of 49, sqrt(49) = 7.0

## power of a to b 
# pow(x, y) === x**y
from math import pow
print("5 to the power 3 : pow(5,3)=", pow(5,3))     #5 to the power 3 : pow(5,3)= 125.0

# pow(x,y[, z]) ==== (x**y) %z
#print("pow(5,3,12) =", pow(5,3,12))        #TypeError: pow expected 2 arguments, got 3

## Greatest Common Divisor of x and y 
#gcd()
from math import gcd
print("gcd(25,30) =", gcd(25,30))           #gcd(25,30) = 5


## truncated value 
#trunc()
from math import trunc
print("trunc(15.5676) =", trunc(15.5676))   #trunc(15.5676) = 15
print("trunc(15.00) =", trunc(15.00))       #trunc(15.00) = 15
print("trunc(4) =", trunc(4))               #trunc(4) = 4

#isinf()
## returns true f value passed is +ve or -ve infinity
from math import isinf
num = float('inf')
print("num = ", num)                    #num =  inf
print("is num infinity :", isinf(num))  #is num infinity : True

#print("is 10/0 infinity ?:", isinf(10/0))   #ZeroDivisionError: division by zero

#num = 10/0  ##ZeroDivisionError: division by zero


#isnan
## check whether passed value is a Not a Number ;returns true is x is a Not a Number
from math import isnan
num1 = float('NaN')
print("num1 =", num1)       #num1 = nan
print("isnan(num1) =", isnan(num1))     #isnan(num1) = True

num2 = 15
print("isnan(num2) =", isnan(num2))     #isnan(num2) = False





###### constants in math module #########
print("pi = ", math.pi)         #pi =  3.141592653589793
print("e =", math.e)            #e = 2.718281828459045
print("inf =", math.inf)        #inf = inf
print("NaN =", math.nan)        #NaN = nan

