Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2**64
18446744073709551616L
>>> 2**250
1809251394333065553493296640760748560207343510400633813116524750123642650624L
>>> print "Hello World"
Hello World
>>> a=4
>>> b=5
>>> a+b
9
>>> print a+b
9
>>> b-a
1
>>> b-c

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b-c
NameError: name 'c' is not defined
>>> b-a
1
>>> a/b
0
>>> b/a
1
>>> a*b
20
>>> a%b
4
>>> a==b
False
>>> a>b
False
>>> a<b
True
>>> a
4
>>> b
5
>>> a,b=10,20
>>> a
10
>>> b
20
>>> a,b=b,a
>>> a
20
>>> b
10
>>> c=30
>>> a,b,c=c,a,b
>>> c
10
>>> a
30
>>> b
20
>>> 1.0/3.0
0.3333333333333333
>>> a>b and b<c
False
>>> a>b and b<c
False
>>> a>b or b>c
True
>>> not a>b
False
>>> s='ol'
>>> print s
ol
>>> s="ol"
>>> print s
ol
>>> 'hello' + 'world'
'helloworld'
>>> a=10.0
>>> int
<type 'int'>
>>> 


>>> inta)
SyntaxError: invalid syntax
>>> int(a)
10
>>> clear

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> 
>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 


>>> 
>>> 


>>> 

>>> 
>>> b
20
>>> float(b)
20.0
>>> a
10.0
>>> int(a)
10
>>> round(a)
10.0
>>> double (b)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    double (b)
NameError: name 'double' is not defined
>>> 'a'
'a'
>>> "a"
'a'
>>> 'abcd'
'abcd'
>>> "abcd"
'abcd'
>>> "abcd's"
"abcd's"
>>> 'inapp"s'
'inapp"s'
>>> "inapp's"
"inapp's"
>>> a=[1,2,3,4,5]
>>> a=[1,2.3,'a','dsf']
>>> a
[1, 2.3, 'a', 'dsf']
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> a=range(10)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[4]
4
>>> a[9]
9
>>> a[2:7]
[2, 3, 4, 5, 6]
>>> a[:7]
[0, 1, 2, 3, 4, 5, 6]
>>> a[2:]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> del a
>>> a

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=range
>>> a
<built-in function range>
>>> a=range(10)
>>> del a[5]
>>> a
[0, 1, 2, 3, 4, 6, 7, 8, 9]
>>> a=range(10)
>>> a[-2]
8
>>> a[-2:4]
[]
>>> a[-4]
6
>>> a[-2:-4]
[]
>>> a[-1:1]
[]
>>> a[-3:-1]
[7, 8]
>>> a[1:10:2]
[1, 3, 5, 7, 9]
>>> range(1,10,2)
[1, 3, 5, 7, 9]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(0,10,2)
[0, 2, 4, 6, 8]
>>> c=a[1:10:2]
>>> c
[1, 3, 5, 7, 9]
>>> a[::2]
[0, 2, 4, 6, 8]
>>> a[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a=[1,2.4,'a','b',5.4,'ab']
>>> a[::-1]
['ab', 5.4, 'b', 'a', 2.4, 1]
>>> a
[1, 2.4, 'a', 'b', 5.4, 'ab']
>>> a[3]='c'
>>> a
[1, 2.4, 'a', 'c', 5.4, 'ab']
>>> b=a
>>> b
[1, 2.4, 'a', 'c', 5.4, 'ab']
>>> a[3]=1000
>>> a
[1, 2.4, 'a', 1000, 5.4, 'ab']
>>> b
[1, 2.4, 'a', 1000, 5.4, 'ab']
>>> print "it is shallow copy"
it is shallow copy
>>> x=10
>>> y=x
>>> x
10
>>> y
10
>>> x=20
>>> x
20
>>> y
10
>>> x="ab"
>>> x
'ab'
>>> y=x
>>> y
'ab'
>>> x="bc"
>>> x
'bc'
>>> y
'ab'
>>> s="abcdefghijklmnopqrstuvwxyz"
>>> s[1:10]
'bcdefghij'
>>> s[10]=45

Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    s[10]=45
TypeError: 'str' object does not support item assignment
>>> s="malayalam"
>>> s[::-1]
'malayalam'
>>> s==s[::-1]
True
>>> 
s=[1,2,3]
>>> a,b,c=s
>>> a
1
>>> b
2
>>> c
3
>>> a,b=s

Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    a,b=s
ValueError: too many values to unpack
>>> a=[]
>>> a=list()
>>> s='malayalam'
>>> a=list(s)
>>> a
['m', 'a', 'l', 'a', 'y', 'a', 'l', 'a', 'm']
>>> a[5]
'a'
>>> s[5]
'a'
>>> t=(1,2,3)
>>> print "tuple"
tuple
>>> t
(1, 2, 3)
>>> 
a=[];
>>> a
[]
>>> a.append(1)
>>> a
[1]
>>> a.append(2)
>>> a
[1, 2]
>>> a.extend([3,4,5,6])
>>> a
[1, 2, 3, 4, 5, 6]
>>> a+range(7,15)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> a
[1, 2, 3, 4, 5, 6]
>>> a=range(10)
>>> a[:4]+1000+a[:4]

Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    a[:4]+1000+a[:4]
TypeError: can only concatenate list (not "int") to list
>>> a[:4]+1000+a[4:]

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    a[:4]+1000+a[4:]
TypeError: can only concatenate list (not "int") to list
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> enumerate(a)
<enumerate object at 0x026CA1C0>
>>> b=enumerate(a)
>>> b
<enumerate object at 0x026CA918>
>>> s='malayalam'
>>> is s==s[::-1]:
	
SyntaxError: invalid syntax
>>> if s==s[::-1]:
	print s+"is a palindrome"
else:
	print s+"is not palindrome"

	
malayalamis a palindrome
>>> if s==s[::-1]:
	print s+"is a palindrome"
	else:
	print s+"is not palindrome"
	
SyntaxError: invalid syntax
>>> if s==s[::-1]:
	print s+"is a palindrome"
else:
	print s+"is not palindrome"

malayalamis a palindrome
>>> if s not s[::-1]:
	print s+"is a palindrome"
else:
	print s+"is not palindrome"
	
SyntaxError: invalid syntax
>>> if s!=s[::-1]:
	print s+"is a palindrome"
else:
	print s+"is not palindrome"

	
malayalamis not palindrome
>>> if s==s[::-1]:
	print s+"is a palindrome"
else:
	print s+"is not palindrome"

	
malayalamis a palindrome
>>> if s==s[::-1]:
	print "true"
elif s!=s[::-1]:
	print "false"
else:
	print 'i dont know'

	
true
>>> for i in range
SyntaxError: invalid syntax
>>> for i in range(10):
	print i

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(3,25,4):
	print i

	
3
7
11
15
19
23
>>> a=[1,2.9,4,'a','abc']
>>> for i in a:
	print i

	
1
2.9
4
a
abc
>>> for i,j in enumerate(a):
	print i,j

	
0 1
1 2.9
2 4
3 a
4 abc
>>> for i,j in enumerate(a):
	if i>2:break
	else:
	print i,j
	
  File "<pyshell#206>", line 5
    print i,j
        ^
IndentationError: expected an indented block
>>> for i,j in enumerate(a):
	if i>2:break
	else:
		print i,j

		
0 1
1 2.9
2 4
>>> a=45
>>> typeof(a)

Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    typeof(a)
NameError: name 'typeof' is not defined
>>> instanceof(a)

Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    instanceof(a)
NameError: name 'instanceof' is not defined
>>> instanceof(a,'int')

Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    instanceof(a,'int')
NameError: name 'instanceof' is not defined
>>> type(a)==int
True
>>> for i,j in a:
	if i>2:break
	else:
		print i,j

		

Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    for i,j in a:
TypeError: 'int' object is not iterable
>>> a=range(10)
>>> type(a)==list
True
>>> for i in  range(10):
	print i,

	
0 1 2 3 4 5 6 7 8 9
>>> while i<20:
	print i,
	i+=1

	
9 10 11 12 13 14 15 16 17 18 19
>>> i=0;
>>> while i<20:
	print i,
	i+=1

	
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
>>> 
