#!c:/python27 python

def pr(n):
	l = []
	for i in range(n):
		l.append(i)
	return l

#print pr(10)
#print pr(100)

def ispalindrome(s):
	t=s.lower()
	return (t==t[::-1])

#print ispalindrome('malayalaM')
#print ispalindrome('abcd')

def mysum1(a=0,b=0):
	return a+b

#print mysum1(a=10,b=20) #keyword arguments
#print mysum1(b=20)
#print mysum1(50)

def mysum2(*args):
	s=0
	for i in args:
		s=s+i
	return s
#print mysum2(10,20,30)
#print mysum2(10,20,30,40)

def mysum(*args,**kwargs):
	#print args
	#print kwargs
	s=0
	for i in args:
		s=s+i
	for k,v in kwargs.items():
		s=s+v
	return s
#print mysum(10,20,30)
#print mysum(10,20,30,40)
#print mysum(10,20,30,40,a=100,b=200)

########################################

def mycounter(n):
	i=0
	while i<n:
		yield i
		i=i+1
	return

for i in mycounter(10):
	print i
