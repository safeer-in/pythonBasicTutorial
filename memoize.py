#!/usr/bin/env python

class Memoize:
	def __init__(self,fun):
		self.fun=fun
		self.memory={}

	def __call__(self,*args):
		try:
			return self.memory[args]
		except KeyError:
			self.memory[args]=self.fun(*args)
			return self.memory[args]

@Memoize
def fib(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def fib_seq(n):
	seq=[]
	if n>0:
		seq.extend(fib_seq(n-1))
	seq.append(fib(n))
	return seq

print fib_seq(40)