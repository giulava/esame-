import numpy as np
from numba import njit
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '1.0.0'



@njit
def likelihood(data, grid, xn, sigma):
	""" This function gives us the likelihood once having experimental data
	
        Input: 
	---------
	data: ndarray
	drawn samples from the parameterized normal distribution.
	
	grid: ndarray
	There are n equally spaced samples in the closed interval [start,end].
	
	xn: array_like of floats
	guessed parameters
	
	sigma: float 
	standard deviation of the distribution. Must be non-negative.
	
	Output
	---------
	L: ndarray
	likelihood values
        """
	L =np.exp(-0.5*(np.sum((data - model(grid,xn))**2)) / sigma**2)/np.sqrt(2*np.pi*sigma**2)
	return L  


@njit
def prior(xn, start, end):

	"""This function computes the normalized value of the uniform prior in a point of parameter space.
	
	Input: 
	---------
	xn: array_like of floats
	guessed parameters
	
	
	start: float
	beginning of function domain
	
	
	end: float
	end of function domain
	
	Output
	---------
	prior: float
	prior distribution
	"""
	
	Vol= np.prod(end-start)
	out= np.zeros(len(xn))
	i= 0
	
	for par in xn:

		out[i] = check(xn[i], start[i], end[i])

		i= i + 1

    
	if np.any(out)==False  : #if any of the parameters are out of range
		
		return 0
	else:
		return 1/Vol

@njit
def check(value, start, end):

	"""This function checks if a value is between two limits.
	It implements uniform prior in a range.
	
	Input: 
	---------
	value: float
	guessed parameter
	
	
	start: float
	beginning of function domain
	
	
	end: float
	end of function domain
	
	Output
	---------
	_ : bool
	returns true if value is in [start,end] else return false
	"""
	

	if start <= value <= end:

		return True
	else:

		return False



			
@njit	 
def posterior_dist(data, grid, sigma, xn, start, end):
	""" This function is the posterior distribution that depends on likelihood and prior.
	
	Input: 
	---------
	data: ndarray
	experimental points 
	
	grid: ndarray
	There are n equally spaced samples in the closed interval [start,end].
	
	sigma: float 
	standard deviation of the distribution. Must be non-negative.
	
	xn: float
	guessed parameters
	
	start: float
	beginning of function domain
	
	end: float
	end of function domain
	
	Output
	---------
	p: float
	posterior distribution
	"""
	
	p=likelihood(data,grid,xn,sigma)*prior(xn,start,end)
	return p



@njit
def MCMC(sigma, data, grid, init_MCMC=0, itmax=10000, start=0, end=1) : 
	"""This function samples a random number, which steps resemble
	a random walk.
	
	Input: 
	---------
	sigma: float 
	standard deviation of the distribution. Must be non-negative.
	
	data: ndarray
	experimental points 
	
	grid: ndarray
	There are n equally spaced samples in the closed interval [start,end].
	
	init_MCMC: int
	initial guessed of the parameters
	
	itmax: int
	final step of cycle
		
	start: float
	beginning of function domain
	
	
	end: float
	end of function domain
	
	Output
	---------
	
	out : ndarray
	list of accepted sample points from the posterior distribution

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
















