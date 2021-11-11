## Program 13 - to find the number of words in a string 
# as many number of spaces; +1 wuld be no of words

# to find no. of words in a string 

str = input('Enter a string : ')

i=0
count=0

flag = True             # this becomes False when no space is found 

for s in str:
    # Count only when there is no space previously
    if (flag==False and str[i]==' '):
        count+=1
        
    # If a space is found, make flag as True 
    if (str[i]==' '):
        flag = True
    else :
        flag = False
        
    i=i+1

print('No. of words :', (count+1))

'''
F:\PY>py string_13_noOfWords.py
Enter a string : You are a sweet girl baby
No. of words : 6

'''