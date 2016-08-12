#!/usr/bin/env python
def mkinc(x):
	def inc(y):
		return x+y
	return inc

p=mkinc(10)
q=mkinc(20)

print p(1)
print q(1)

