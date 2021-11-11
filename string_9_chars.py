## Working with Characters -- get a string --> get chars using indexing or slicing 

## program 9 - to know the type of character entered by the user 

str = input('Enter a character : ')
ch = str[0]         # take only 0th character niito ch

# test ch 
if (ch.isalnum()):
    print("It is an alphabet or numeric character")
    
    if (ch.isalpha()):
        print("It is an alphabet")
        
        if (ch.isupper()):
            print("It is capital letter")
        else :
            print("It is lowercase letter")
    else :
        print("It is a numeric digit")

elif (ch.isspace()):
    print("It is a space")

else : 
    print("It may be a special character")
    
'''
F:\PY>py string_9_chars.py
Enter a character : a
It is an alphabet or numeric character
It is an alphabet
It is lowercase letter

F:\PY>py string_9_chars.py
Enter a character : &
It may be a special character

F:\PY>py string_9_chars.py
Enter a character : 5
It is an alphabet or numeric character
It is a numeric digit

'''