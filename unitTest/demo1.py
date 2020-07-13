#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self,name,score,pram):
		self.name = name
		self.score = score
		self.pram = pram

	def get_grade(self):
		if self.score >= 80 and self.score <= 100:
			print('A')
		elif self.score >= 60 and self.score <= 79:
			print('B')
		elif self.score >= 0 and self.score <= 59:
			print('C')
		else:
			raise ValueError('value is not between 0 and 100')

	def hello(self):
		print('hello world')

	def hello_1(self):
		print('hello' + ' ' + self.pram)

class Student2(Student):
	def hello2(self):
		Student.get_grade(self)


# s1 = Student('陈建齐',80,'python')
# s1.get_grade()
# s1.hello()
# s1.hello_1()

s2 = Student2('陈建齐',80,'python')
s2.hello2()