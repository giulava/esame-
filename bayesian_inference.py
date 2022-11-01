import numpy as np
from config import *
from sampler import MCMC
from analytic_model import fakedata,model
from plots import makeplot 



__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='1.0.0'


def main():
	
	data,grid=fakedata(xstart,xend,n,params,sigma)
	posterior=MCMC(sigma,data,grid,init_MCMC=init_MCMC,itmax=itmax,start=start,end=end)
	posteriorA=posterior[:,0]
	posteriorB=posterior[:,1]	
	posteriorC=posterior[:,2]
	
	makeplot(posteriorA,posteriorB,posteriorC,xstart,xend,grid,data)
	
if __name__=="__main__":
	 
	main()

