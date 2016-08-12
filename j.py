#!/usr/bin/env python

def outer1(p,q):
	def outer(fun):
		def inner(x,y):
			if x<p: x=p
			if x>q: x=q
			if y<p: y=p
			if y>q: y=q
			return fun(x,y)
		return inner
	return outer

@outer1(0,100)    #syntactic sugar - decarative function
def add(x,y):
	return x+y


print add(10,20)
print add(-10,20)
print add(10,200)