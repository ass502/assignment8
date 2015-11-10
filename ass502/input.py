"""contains functions and user-defined exceptions related to obtaining and validating user input"""

import sys

def getListPositions():
	"""prompts the user for a list of positions until a valid one is obtained, and returns the list of positions"""

       	try:
              	listInput=raw_input("List of positions? ")
               	listInput=listInput.replace(" ","") #remove whitespace
       	except (KeyboardInterrupt,EOFError): #catch ctrl-c and ctrl-d, quit on these inputs
                sys.exit()

	if listInput=="quit" or listInput=="Quit": #normal way to exit program
		sys.exit()

	try:
		return getList(listInput)
	except (NonPositiveIntegerException,ImproperListFormatException):
		print("Invalid input")
		return getListPositions()
	except InvalidIntegerException:
		print("Each integer in the list must be 1, 10, 100, or 1000")
		return getListPositions()

def getNumTrials():
	"""prompts the user for the number of trials until a valid one is obtained, and returns the number"""

	try:
		numTrialsInput=raw_input("Number of trials? ")
		numTrialsInput=numTrialsInput.replace(" ","") #remove whitespace
	except (KeyboardInterrupt,EOFError): #catch ctrl-c and ctrl-d, quit on these inputs
        	sys.exit()
	
	if numTrialsInput=="quit" or numTrialsInput=="Quit": #normal way to exit program
		sys.exit()

	try:
		return getInt(numTrialsInput)
	except ZeroException:
		print("The input cannot be 0")
		return getNumTrials()
	except NonPositiveIntegerException:
		print("The input must be a positive integer")
		return getNumTrials()

def getListInt(input):
	"""validates an integer in our input list of positions"""

	if input.isdigit():
		n = int(input)
		if n==1 or n==10 or n==100 or n==1000:
			return n
		else:
			raise InvalidIntegerException()
	else:
		raise NonPositiveIntegerException()

def getInt(input):
	"""validates a positive integer input"""

	if input.isdigit(): #check if the input is a digit
		n=int(input)
		if n!=0: #check if integer is non-zero
			return n
		else:
			raise ZeroException()
	else:
		raise NonPositiveIntegerException()

def getList(input):
	"""parses and validates an input list of positive integers separated by commas"""

	list=[]
	if input[0]=='[' and input[len(input)-1]==']': #check for open and close brackets in list
		c=1
		currInt=""
		while c!=len(input)-1: #go through each character in the input string, until you reach the 2nd to last one
			if input[c]==',': #once we reach a comma, we try to get the integer right before it
				list.append(getListInt(currInt))
				currInt=""
			else: #until we reach a comma, every character is part of the integer
				currInt+=input[c]
			c+=1
		list.append(getListInt(currInt))
		return list
	else:
		raise ImproperListFormatException()

class NonPositiveIntegerException(Exception):
	"""exception if an input is not a positive integer"""
	def __str__(self):
		return 'The input is not a positive integer'

class ZeroException(Exception):
	"""exception if an integer input is zero"""
	def __str__(self):
		return 'The integer is zero'

class InvalidIntegerException(Exception):
	"""exception if an integer in the list input is not one of 1, 10, 100, or 1000"""
	def __str__(self):
		return 'The integers in the list must be 1, 10, 100, or 1000'

class ImproperListFormatException(Exception):
        """exception if a list input is not properly formatted"""
        def __str__(self):
                return 'The list is not properly formatted'

