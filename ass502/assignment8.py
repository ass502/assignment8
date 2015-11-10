"""Author: Akash Shah (ass502)

This module contains the main function for interacting with the user to simulate investments of various positions.
The user can specify a list of positive integers as positions consisting of the number of shares to invest in. The list must have opening [ and closing ] brackets,
as well as positions separated by commas. The user can also specify the number of trials to run, which must also be a positive integer.

Output of statistics in text form as well as plots are generated upon completion of the simulation."""

from investment import *
from input import *
from generateOutput import *

#set total investment amount, the probability of a share losing its value in a day, and the filename of our results file
investment_amount = 1000
pr_lose = .49
outputFile="results.txt"

def loop():
	positionList = getListPositions()
	num_trials = getNumTrials()	

	clearTextFile(outputFile)
	
	for position in positionList:
		#instantiate investment object for current investment 
		currInvestment = investment(investment_amount,position,pr_lose)

		cumu_ret = np.zeros(num_trials)
		daily_ret = np.zeros(num_trials)
		for trial in range(0, num_trials):
			cumu_ret[trial] = currInvestment.simulate_day()
			daily_ret[trial] = cumu_ret[trial]/investment_amount-1

		printStatistics(outputFile,currInvestment.numShares,daily_ret)
		plotPositionHistogram(currInvestment.numShares,daily_ret)

		

if __name__=="__main__":
	try:
		loop()
	except EOFError:
		pass
