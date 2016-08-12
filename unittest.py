#!/usr/bin/env python

def mult(a,b):
	"""
	>>> mult(2,3)
	6
	>>> mult('a',3)
	'aaa'
	"""
	return a*b


if __name__=='__main__':
	import doctest
	doctest.testmod()