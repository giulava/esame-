import numpy as np
from numba import njit
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '1.0.0'



@njit
def likelihood(data, grid, xn, sigma):
	""" This function gives us the likelihood once having experimental data$
        """
	L =np.exp(-0.5*(np.sum((data - model(grid,xn))**2)) / sigma**2)/np.sqrt(2*np.pi*sigma**2)
	return L  

@njit
def inrange(x, start, end):
	""" This function gives us a continuos uniform distribution between 
	sup and inf.
	""" 

	if start<=x<=end:
		h=1/(end-start)
	else:
		h=0
	return h

@njit
def prior(params, start, end):

	"""This function computes the normalized value of the uniform prior in a point of parameter space.
	"""
	
	Vol= np.prod(end-start)
	out= np.zeros(len(params))
	i= 0
	
	for par in params:

		out[i] = check(params[i], start[i], end[i])

		i= i + 1

    
	if np.any(out)==False  : #se uno qualunque dei parametri è fuori dall'intervallo
		
		return 0
	else:
		return 1/Vol

@njit
def check(value, start, end):

	"""This function checks if a value is between two limits.
	It implements uniform prior in a range.
	"""

	if start <= value <= end:

		return True
	else:

		return False



			
@njit	 
def posterior_dist(data, grid, sigma, xn, start, end):
	""" This function is the posterior distribution that depends on likelihood.
	"""
	
	p=likelihood(data,grid,xn,sigma)*prior(xn,start,end)
	return p



@njit
def MCMC(sigma, data, grid, init_MCMC=0, itmax=10000, start=0, end=1) : 
	"""This function samples a random number, which steps resemble
	a random walk.

	
	xn : starting position
        posterior_dist : posterior distribution
        controll : Metropolis ratio
	 
	
	Output
	
	out : list, list of accepted steps from the posterior distribution

	"""
	
	
	burnin=1000
	skip=2	
	out=np.ones((int((itmax-burnin)/skip),len(init_MCMC)), dtype = np.float64) 

	#We remove the first 1000 drawn from the list of numbers and take one yes and one no.
	
	
	xn = init_MCMC
	saved=False
	j=0

	for i in range (itmax):
	
		xn1=np.array([np.random.normal(xn[i],sigma) for i in range(len(xn))], dtype = np.float64)
		
		controll = min(1,
				posterior_dist(data, grid, sigma, xn1, start, end)/posterior_dist(data, grid, sigma, xn, start, end)
				)


		
		if np.random.rand()<=controll:
			xn=xn1
				
			
		if i>burnin and saved==False : 
			out[j,:]=xn
			saved=True
			j+=1
		
		elif saved==True:
			saved=False

	
	return out		
















