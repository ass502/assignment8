"""consists of helper functions related to printing statistical results and generating pdf files of matplotlib plots"""

import numpy as np
import matplotlib.pyplot as plt

def clearTextFile(filename):
	"""clears the results output text file"""

	open(filename,'w').close()
	

def printStatistics(filename,position,daily_ret):
	"""writes the mean and standard deviation of each position to the results output text file"""

	with open(filename,'a') as output:
		output.write('For the position of '+str(position)+' share(s), the mean daily return was '+str(np.mean(daily_ret))+'\n')
		output.write('For the position of '+str(position)+' share(s), the standard deviation of the daily return was '+str(np.std(daily_ret))+'\n\n')

def plotPositionHistogram(position,daily_ret):
	"""plots histogram chart of the daily returns of a position and saves it as a pdf file"""

	plt.hist(daily_ret,100,range=[-1,1])
	plt.xlim(-1, 1)
	plt.savefig('histogram_'+str(position).zfill(4)+'_pos.pdf')
	plt.clf()

