import numpy as np
from sampler import MCMC
from analytic_model import fakedata,model
from plots import makeplot 


__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='1.0.0'


def main():
	"""Input
	"""
	init_MCMC=np.array([0.5,0.5,0.5], dtype = np.float64)
	itmax=1000000
	n=50
	params=np.array([0.5,0.5,0.5], dtype = np.float64)
	sigma=0.25
	start=np.array([0,0,0], dtype = np.float64)
	end=np.array([2,2,2], dtype = np.float64)
	xstart=0
	xend=10

	data,grid=fakedata(xstart,xend,n,params,sigma)
	posterior=MCMC(sigma,data,grid,init_MCMC=init_MCMC,itmax=itmax,start=start,end=end)
	posteriorA=posterior[:,0]
	posteriorB=posterior[:,1]	
	posteriorC=posterior[:,2]
	
	makeplot(posteriorA,posteriorB,posteriorC,xstart,xend,grid,data)
	
if __name__=="__main__":
	 
	main()

