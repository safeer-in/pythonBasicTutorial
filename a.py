#!/usr/bin/env python
# -*- coding:utf-8 -*-

from person import Person

class Employee(Person):
	def __init__(self,fn,ln,age,role):
		#Person.__init__(self,fn,ln,age) #old way

		super(Employee,self).__init__(fn,ln,age)
		self.role=role

	def set_role(self,role):
		self.role=role

	def get_role(self):
		return self.role