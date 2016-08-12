#!/usr/bin/env python
# -*- coding:utf-8 -*-

#function as first class object

def mymap(func,lst):
	n1=[]
	for i in lst:
		n1.append(func(i))
	return n1

def myfilter(func,lst):
	n1=[]
	for i in lst:
		if func(i):
			n1.append(i)
	return n1

def square(x):
	return x*x

#print mymap(square,range(10))

print mymap(lambda x:x*x*x,range(10))
print myfilter(lambda x:x%2==0,range(10))