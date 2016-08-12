#!/usr/bin/env python

from unittest import mult
import unittest

class MyTest(unittest.TestCase):
	def setup(self):
		pass

	def teardown(self):
		pass

	def test1(self):
		self.assertEqual(mult(2,3),6)
	def test2(self):
		self.assertEqual(mult('a',3),'aaa')

if __name__ == "__main__":
	unittest.main()