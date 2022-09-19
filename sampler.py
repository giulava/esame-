import numpy as np
from analytic_model import fakedata 


__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '0.0.1'




def main():
	start=0
	end=1
	n=5
	params=(2,1,3)
	sigma=1
	print (fakedata(start,end,n,params,sigma))
























if __name__=="__main__":
	main()

