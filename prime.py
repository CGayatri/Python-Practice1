# program to display prime numbers between range 

#Take the input from the user:   
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
           

        
"""
F:\PY>py prime.py
Enter lower range: 1
Enter upper range: 10
2
3
5
7

F:\PY>py prime.py
Enter lower range: 10
Enter upper range: 50
11
13
17
19
23
29
31
37
41
43
47

F:\PY>
"""