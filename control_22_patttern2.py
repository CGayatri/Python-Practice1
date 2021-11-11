## program 22 - to display numbers from 1 to 100 in a proper format 

# displaying numbers from 1 to 100 in 10 rows and 10 cols 

for x in range(1, 11):      # 1 to 10 
    for y in range(1,11):
        #print(x * y, end=' ')
        print('{:5}'.format(x*y), end='')   
    print()
    
    
#Output:
'''  
F:\PY>py control_22_patttern2.py         ======== print(x * y, end='')
1234567891024681012141618203691215182124273048121620242832364051015202530354045506121824303642485460714212835424956637081624324048566472809182736455463728190102030405060708090100
F:\PY>py control_22_patttern2.py         =========== print(x * y, end=' ')
12345678910
2468101214161820
36912151821242730
481216202428323640
5101520253035404550
6121824303642485460
7142128354249566370
8162432404856647280
9182736455463728190
102030405060708090100

F:\PY>py control_22_patttern2.py        ========== end=' '
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100

F:\PY>py control_22_patttern2.py
  File "control_22_patttern2.py", line 9
    print()
    ^
IndentationError: expected an indented block

F:\PY>py control_22_patttern2.py
Traceback (most recent call last):
  File "control_22_patttern2.py", line 8, in <module>
    print('{1}'.format(x*y), end='')
IndexError: Replacement index 1 out of range for positional args tuple

F:\PY>py control_22_patttern2.py        ========== {:1}
12345678910
2468101214161820
36912151821242730
481216202428323640
5101520253035404550
6121824303642485460
7142128354249566370
8162432404856647280
9182736455463728190
102030405060708090100

F:\PY>py control_22_patttern2.py        ========== {:2}
 1 2 3 4 5 6 7 8 910
 2 4 6 8101214161820
 3 6 912151821242730
 4 81216202428323640
 5101520253035404550
 6121824303642485460
 7142128354249566370
 8162432404856647280
 9182736455463728190
102030405060708090100

F:\PY>py control_22_patttern2.py        ========== {:3}
  1  2  3  4  5  6  7  8  9 10
  2  4  6  8 10 12 14 16 18 20
  3  6  9 12 15 18 21 24 27 30
  4  8 12 16 20 24 28 32 36 40
  5 10 15 20 25 30 35 40 45 50
  6 12 18 24 30 36 42 48 54 60
  7 14 21 28 35 42 49 56 63 70
  8 16 24 32 40 48 56 64 72 80
  9 18 27 36 45 54 63 72 81 90
 10 20 30 40 50 60 70 80 90100

F:\PY>
F:\PY>py control_22_patttern2.py            ========== {:4}
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100

F:\PY>py control_22_patttern2.py            ========== {:5}
    1    2    3    4    5    6    7    8    9   10
    2    4    6    8   10   12   14   16   18   20
    3    6    9   12   15   18   21   24   27   30
    4    8   12   16   20   24   28   32   36   40
    5   10   15   20   25   30   35   40   45   50
    6   12   18   24   30   36   42   48   54   60
    7   14   21   28   35   42   49   56   63   70
    8   16   24   32   40   48   56   64   72   80
    9   18   27   36   45   54   63   72   81   90
   10   20   30   40   50   60   70   80   90  100
   
'''