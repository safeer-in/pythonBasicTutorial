#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person(object):
	__fn="" #name mangling
	__ln=""
	__age=0

	def __init__(self,fn,ln,age):
		self.__fn=fn
		self.__ln=ln
		self.__age=age	

	def get_name(self):
		return self.__fn+" "+self.__ln

	def set_name(self,fn,ln):
		self.__fn=fn
		self.__ln=ln
		return

	def get_age(self):
		return self.__age

	def set_age(self,age):
		self.__age=age
		return