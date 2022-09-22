import numpy as np
import matplotlib.pyplot as plt
from sampler import MCMC
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='0.0.4'


def main():
	start=2
	end=5000
	n=5
	params=(2,1,3)
	sigma=1
	data=fakedata(start,end,n,params,sigma)
	r=MCMC(sigma,data,params,start=start,end=end,inf=0,sup=1)
	print(r)
	plt.figure(figsize=(8, 4))
	plt.hist(r, bins = 100, histtype='step', density = True, label='histogram')
	plt.show()



if __name__=="__main__":
	main()
