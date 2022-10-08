Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list=[1,2,3]
list.append(2)
list
[1, 2, 3, 2]
list.extend(2,4)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list.extend(2,4)
TypeError: list.extend() takes exactly one argument (2 given)
list.extend([1,2])
list
[1, 2, 3, 2, 1, 2]
list+=[5]
list
[1, 2, 3, 2, 1, 2, 5]
tuple=(1,2,3)
Y=9,4,5
type(Y)
<class 'tuple'>
<class 'tuple'>
SyntaxError: invalid syntax
##dictionary is a unordered pair and index slicing is not possible in it.It has a key vlaue pair.
d1 = {'name':['akash','akshat','sunny'],'Age':[25,20,22],  }
type(d1) #above is the syntax of a dictionary
<class 'dict'>
len(d1)
2
d1[name] #to access the values stored in the first keyword
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d1[name] #to access the values stored in the first keyword
NameError: name 'name' is not defined
d1['name']
['akash', 'akshat', 'sunny']
d1['age']
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d1['age']
KeyError: 'age'
d1['Age']
[25, 20, 22]
d1.keys()
dict_keys(['name', 'Age'])
d1.vlaues()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d1.vlaues()
AttributeError: 'dict' object has no attribute 'vlaues'. Did you mean: 'values'?
d1.values()
dict_values([['akash', 'akshat', 'sunny'], [25, 20, 22]])
d1.items()
dict_items([('name', ['akash', 'akshat', 'sunny']), ('Age', [25, 20, 22])])
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
d1['phone number']=[222xxx,8888xxxx,741xxx]
SyntaxError: invalid decimal literal
d1['phone number']=[222,333,4444]
d1
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'phone number': [222, 333, 4444]}
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'phone number': [222, 333, 4444]}
d1['name']
['akash', 'akshat', 'sunny']
d1['name'][0]
'akash'
##in the above expression akash is treated as a list##
d1['name'][0][::-1]
'hsaka'
d1['name'][0]='aah' ##for changing the letter in the dictionary
d1
{'name': ['aah', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'phone number': [222, 333, 4444]}
d1['name'][3]='name'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d1['name'][3]='name'
IndexError: list assignment index out of range
########### To delete an element in a dictionary ###############
del d1['phone number']
print(d1)
{'name': ['aah', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
d1['name'].append('gfg')
print(d1)
{'name': ['aah', 'akshat', 'sunny', 'gfg'], 'Age': [25, 20, 22]}
################## To remove an element from the dictionary#############################
d1['name'].remove('gfg')
d1
{'name': ['aah', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
############################# To get the value from key existing in the dictionary but if the key is not present in the dictionary it will not show any error #############
d1.get('email')
d1.get('name')
['aah', 'akshat', 'sunny']

a=20
b='ML'
print(a,b)
20 ML
print9a,b,sep='          ')####used to separate two parameters
SyntaxError: unmatched ')'

print(a,b,sep='          ')
20          ML
print(a,b,sep='@')
20@ML
print(a)
20
print(b)
ML

=================== RESTART: E:/python4.py ===================
20###ML

=================== RESTART: E:/python4.py ===================
20###ML

=================== RESTART: E:/python4.py ===================
20
ML
a=input('Enter your name: ')
Enter your name: Dushyant
a
'Dushyant'
a = int(input('Enter first number : '))
Enter first number : 1
b=int(input("Enter second number : '))
            
SyntaxError: unterminated string literal (detected at line 1)

b=int(input('Enter second number : '))
            
Enter second number : 1
a+b
            
2
############ Above expression is used to take input input from user to add two number###
            
a=input('Enter your n1: ')
            
Enter your n1: 2
c=input('Enter your n2 ')
            
Enter your n2 3
a+c
            
'23'
print(a+c)
            
23
a=int(input('Enter the age : '))
            
Enter the age : 3
if a > 18
            
SyntaxError: expected ':'

=================== RESTART: E:/python4.py ===================
Enter the age : 56
A gift
Traceback (most recent call last):
  File "E:/python4.py", line 4, in <module>
    if age>=18 and age<=20:
NameError: name 'age' is not defined

=================== RESTART: E:/python4.py ===================
Enter the age : 43
A gift
Traceback (most recent call last):
  File "E:/python4.py", line 4, in <module>
    if age>=18 and age<=20:
NameError: name 'age' is not defined

=================== RESTART: E:/python4.py ===================
Enter the age : 54
Traceback (most recent call last):
  File "E:/python4.py", line 4, in <module>
    if age>=18 and age<=20:
NameError: name 'age' is not defined

=================== RESTART: E:/python4.py ===================
Enter the age : 54
Koi gift nahi hai


=================== RESTART: E:/python4.py ===================
Enter the age : 1
Traceback (most recent call last):
  File "E:/python4.py", line 1, in <module>
    age=int(input('Enter the age : '))
ValueError: invalid literal for int() with base 10: ''

=================== RESTART: E:/python4.py ===================
Enter the age : 5
A gift

=================== RESTART: E:/python4.py ===================
Enter the age : 1
A gift

=================== RESTART: E:/python4.py ===================
Enter the age : 1
A gift

=================== RESTART: E:/python4.py ===================
Enter the age : Saturday
Half day work

=================== RESTART: E:/python4.py ===================
Enter the age : Sunday
Traceback (most recent call last):
  File "E:/python4.py", line 4, in <module>
    elif today == 'Sunday':
NameError: name 'today' is not defined

=================== RESTART: E:/python4.py ===================
Enter the age : 
=================== RESTART: E:/python4.py ===================
Enter the age : Sunday
Traceback (most recent call last):
  File "E:/python4.py", line 5, in <module>
    if condition == 'sick':
NameError: name 'condition' is not defined

=================== RESTART: E:/python4.py ===================
Enter the age : Sunday
Enter the condition : sick
Take rest

=================== RESTART: E:/python4.py ===================
Enter the num: 1
Enter the num: 1
Enter the num: 2
C is the greatest
>>> 
=================== RESTART: E:/python4.py ===================
Enter the num: 2 
Enter the num: 3
Enter the num: 4
C is the greatest
>>> 
=================== RESTART: E:/python4.py ===================
Enter the num: 4
Enter the num: 3
Enter the num: 2
A is the greatest
>>> 
=================== RESTART: E:/python4.py ===================
Enter the num: 4
Enter the num: 5
Enter the num: 2
B is the greatest
>>> 
>>> 
>>> 
>>> ##### Function for printing number upto n#####
>>> range(0,8)
range(0, 8)
>>> list (range(0,8))
[0, 1, 2, 3, 4, 5, 6, 7]
>>> list (range(8))
[0, 1, 2, 3, 4, 5, 6, 7]
>>> list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
