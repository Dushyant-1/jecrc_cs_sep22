Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=print('Hi how are u')
Hi how are u
a
print(a)
None
#### for defining a function def is used#####
def myfun():
    print('this is first fun')

    
myfun()
this is first fun
a=myfun()
this is first fun
print(a)
None
def second():
    return 'abcd'
second()
SyntaxError: invalid syntax
 second()
 
SyntaxError: unexpected indent
second()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    second()
NameError: name 'second' is not defined
second()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    second()
NameError: name 'second' is not defined
def sec
SyntaxError: invalid syntax

def second():
    return 'abcd'
second()
SyntaxError: invalid syntax
def second():
    return 'abcd'

second()
'abcd'
#### input but no output
def third(x)
SyntaxError: expected ':'
def third(x);
SyntaxError: expected ':'
def third(x):
    print('Hello')

    
third()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
####### input with output
third('abc')
Hello
def fourth(x)
SyntaxError: expected ':'
def fourth(x):
    return c*10

fourth(5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    fourth(5)
  File "<pyshell#35>", line 2, in fourth
    return c*10
NameError: name 'c' is not defined
def fourth(x):
    return x*10

fourth(4)
40
def fourth(x):
    print("hi")
    print('hello')
    print('how are you')
    return x*10

fourth(10)
hi
hello
how are you
100
third('f')
Hello

def fourth(x)
SyntaxError: expected ':'
def fourth(x):
    print('hi')
    return x**2
    print('hello')
    print('world')

    
fourth(3)
hi
9
## in the above code the statements below return will not be
##executed

def five(x,y,z):
    return x+y+z

five(1,2,3)
6

##### multiple return functions
def six(x,y,z):
    return x+y+z

six(x=5,y=4,z=2)
11
six(5,4,2)
11

six(4,3)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    six(4,3)
TypeError: six() missing 1 required positional argument: 'z'
def seven(x,y,z=1):
    return x+y+z

seven(4,8,7)
19
seven(4,8)
13
### in the above code error is not shown as z is a default
# argument and the code will run even with 2 parameters .
def seven(x=1,y,z=1):
    
SyntaxError: non-default argument follows default argument
def seven(x,y=1,z=2):
    return x+y

seven(1)
2
### args always returns a tuple
def eight(*x):
    return x

eight ()
()
eight(2)
(2,)
eight(2,4,5)
(2, 4, 5)

def nine(**x):
    return x

nine()
{}
nine(name='Bipul',email='Bipul@gmail.com')
{'name': 'Bipul', 'email': 'Bipul@gmail.com'}
nine(n1=0,n2=[11,10,20],n3=['ab','xy'])
{'n1': 0, 'n2': [11, 10, 20], 'n3': ['ab', 'xy']}
def name(x):
    return 'happy birthday'

name('Dushyant')
'happy birthday'
def name(x):
    return 'happy birthday ',x


name("L")
('happy birthday ', 'L')
def name(x):
    return print('happy birthday',x)

name('g')
happy birthday g
def name(x):
    return print('happy birthday',x,'to you')

name("FCUK")
happy birthday FCUK to you

def myfun(x,y,z):
    return x+y+z

myfun(2,4,6)
12
myadd = lambda x,y,z:x+y+z
myadd(5,9,7)
21

import math
math.pi
3.141592653589793
math.sqrt(81)
9.0
math.pow(2,3)
8.0
math.factorial(5)
120
import math as m
m.pi
3.141592653589793
m.sqrt(81)
9.0
from math import sqrt
sqrt(81)
9.0
import datetime as dt
aaj ki date=aaj.date.today()
SyntaxError: invalid syntax
import datetime as dt
aajkidate=aaj.date.today()
SyntaxError: multiple statements found while compiling a single statement
import datetime as dt
aajkidate=dt.date.today()
print(aajkidate)
2022-09-19
import calendar
print
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

