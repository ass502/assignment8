"""unittest for functions and user-defined exceptions in the input module"""

from input import *
from unittest import TestCase

class InputTest(TestCase):

	def test_valid_list(self):
		list1="[1,1000,10,100]"
		self.assertEqual(getList(list1),[1,1000,10,100])
		
	def test_invalid_list(self):
		list1="[1,abc]"
		self.assertRaises(NonPositiveIntegerException,getList,list1)

		list2="[1,3.14]"
		self.assertRaises(NonPositiveIntegerException,getList,list2)
		
		list3="[1,100,1000"
		self.assertRaises(ImproperListFormatException,getList,list3)

		list4="1,100,1000"
		self.assertRaises(ImproperListFormatException,getList,list4)
		
		list5="[1,5,100]"
		self.assertRaises(InvalidIntegerException,getList,list5)

		list6="[1,-10]"
		self.assertRaises(NonPositiveIntegerException,getList,list6)
		
	def test_valid_num_trials(self):
		num1="1000"
		self.assertEqual(getInt(num1),1000)
		
	def test_invalid_num_trials(self):
		num1= "-5"
		self.assertRaises(NonPositiveIntegerException,getInt,num1)
		
		num2= "0"
		self.assertRaises(ZeroException,getInt,num2)
		
		num3= "1.54"
		self.assertRaises(NonPositiveIntegerException,getInt,num3)
		
		num4= "a1b2"
		self.assertRaises(NonPositiveIntegerException,getInt,num4)
		
