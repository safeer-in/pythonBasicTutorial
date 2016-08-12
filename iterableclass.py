#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ICounter(object):
	def __init__(self,low,high):
		self.low=low
		self.high=high

	def __iter__(self):
		return self

	def next(self):
		l=self.low
		if l > self.high:
			raise StopIteration
		else:
			self.low+=1
			return l