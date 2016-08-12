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

#for i in mycounter(10):
	#print i

#########################

def mycount():
	i=0
	while True:
		yield i
		i=i+1

k=0
#for i in mycount():
#	print i
#	k=k+1
#	if k>10:break

m=mycount()

k=0
#for j in m:
#	print j,
#	k=k+1
#	if k>20:break

#commandline argument


def fact1(n):
	if n<0:
		raise ValueError("Argument Negative",n)
	elif n==0:
		return 1
	else:
		return n*fact(n-1)


#inp=raw_input("Give input: ")

#try:
#	print fact(int(inp))
#except ValueError as e:
#	print e.args
#except IOError as e:
#	print e.args
#finally:
#	print "This will always be printed"

import sys
def fact(n):
	#print locals()
	if n<0:
		raise ValueError("Argument Negative",n)
	elif n==0:
		return 1
	else:
		return n*fact(n-1)

#print globals()
if __name__=="__main__":
	if len(sys.argv)>2:
		print "Too many values"
	elif len(sys.argv)<2:
		print "Too few values"
	else:
		inp=sys.argv[1]
		try:
			print fact(int(inp))
		except ValueError as e:
			print e.args
