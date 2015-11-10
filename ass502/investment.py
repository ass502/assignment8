"""defines an investment class, an instance of which consists of the number of positions to take within the given investment amount, along with a probability of the amount being lost in a single day of trading.
Also contains a member method which simulates a single day of trading on our investment and returns the outcome"""

import numpy as np

class investment:
	
	def __init__(self,investment_amount,position,pr_lose):
		
		self.numShares = position
		self.position_value = investment_amount/position
		self.pr_lose = pr_lose

	def simulate_day(self):
		"""simulate a single day of trading on an instance of an investment"""
		
		outcome=0

		rands = np.random.random_sample(self.numShares)

		#determine outcome of each share in our position and take the sum of all outcomes
		for share in range(0,self.numShares):	
			if rands[share] >= self.pr_lose:
				outcome += 2*self.position_value
		return outcome
