Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\DELL\Desktop\training\program1.py =============
Hello world
>>> 'hello'+"lelo"
'hellolelo'
>>> 3*6
18
>>> 5<2and4<3
SyntaxError: invalid decimal literal
>>> 4 < 2 and 3 < 5
False
>>> 2<4 and 5<7
True
>>> 4<5 or 6>9
True
>>> hello*True
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hello*True
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> hello*8
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hello*8
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> 'hello'*8
'hellohellohellohellohellohellohellohello'
>>> 'hello '*8
'hello hello hello hello hello hello hello hello '
