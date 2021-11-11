# A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password :
    # 1. at least 1 letter between [a-z]
    # 2. at least 1 number between [0-9]
    # 3. at least 1 letter between [A-Z]
    # 4. at least 1 character from [$#@]
    # 5. Minimum length of transaction password : 6 
    # 6. Maximum length of transaction password : 12
    
# Hint : in case of input data being supplied to the question, it should be assumed to be a console input 

# Use of regular expression - import module re

import sys 
#import re 


# Password Validation 
'''
def pwd_check(passw):
    if (len(passw) >= 6 and len(passw) <=12):
            if (re.search("[a-z]".passw)):
                if (re.search("[A-Z]".passw)):
                    if (re.search("[0-9]".passw)):
                        if (not re.serach("[$#@]".passw)):
                            print("Invalid password; Need at lest one special character from $#@ ")
                    else :
                        print("Invalid password; Need at least one number")
                else :
                    print("Invalid password; Need at least one upper letter ")
            else :
                print("Invalid password; Need at least one lower letter ")
    else :
        print("Invalid password; Length of password should be minimum 6 and maximum 12")
        
'''


spsym = ['$', '#', '@']

def pwd_check(passwd):
    """ to validate value of entered password """
    if (len(passwd) < 6):
        print("length should be minimum 6")
    if (len(passwd) > 12):
        print("length should be maximum 12")

    if not any(char.isdigit() for char in passwd):
        print("password should have at least one number")

    if not any(char.isupper() for char in passwd):
        print("password should have at least one capital letter ")
        
    if not any(char.islower() for char in passwd):
        print("password should have at least one lower letter ")
        
    if not any(char in spsym for char in passwd):
        print("there should be at least one special character from $#@")


uname = input("Enter an username : ")
passwd = input("Enter a password : ")

pwd_check(passwd)


#Output:
'''
F:\PY\Module1\CaseStudy_1>py demo3.py
Enter an username : Gayatri
Enter a password : password
password should have at least one number
password should have at least one capital letter
there should be at least one special character from $#@

F:\PY\Module1\CaseStudy_1>py demo3.py
Enter an username : Gayatri
Enter a password : Password
password should have at least one number
there should be at least one special character from $#@

F:\PY\Module1\CaseStudy_1>py demo3.py
Enter an username : Gayatri
Enter a password : P@ssword
password should have at least one number

F:\PY\Module1\CaseStudy_1>py demo3.py
Enter an username : Gayatri
Enter a password : P@ssw0rdP@ssw0rd
length should be maximum 12

F:\PY\Module1\CaseStudy_1>py demo3.py
Enter an username : Gayatri
Enter a password : P@ss
length should be minimum 6
password should have at least one number

F:\PY\Module1\CaseStudy_1>py demo3.py
Enter an username : Gayatri
Enter a password : P@ssw0rd

F:\PY\Module1\CaseStudy_1>
'''






















