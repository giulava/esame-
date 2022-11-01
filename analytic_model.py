import numpy as np
from numba import njit

@njit
def model(x, params):
	
	"""
	This function computes the analytic model that we will try to recover. 
	
	Input: 
	---------
	x: array_like of floats
	indipendent variable.
	
	params: array_like of floats
	parameters of the function.
	
	Output
	---------
	model: ndarray
	analytic function
	
	"""
	a,b,c=params
	return a*x*np.sin(b*x+c) 





def noise(mu, sigma):
	"""
	This function computes the noise to be superimposed to the model. 

	Input: 
	----------
	mu: float
	mean of the distribution
	
	sigma: float 
	standard deviation of the distribution. Must be non-negative.
	
	Output:
	----------
	noise: ndarray
	drawn samples from the parameterized normal distribution.
	"""

	return np.random.normal(mu, sigma) 
	  



def fakedata(start, end, n, params, sigma):
	"""
	This function computes the experimental data points.
	It gives as output an array containing the data points.
	
	Input: 
	----------
	start: float
	beginning of function domain
	
	end: float 
	end of function domain
	
	n: int
	number of points
	
	params: array_like of floats
	parameters of the function.
	
	sigma: float 
	standard deviation of the distribution. Must be non-negative.
	
	Output:
	----------
	data: ndarray
	drawn samples from the parameterized normal distribution.
	
	grid: ndarray
	There are n equally spaced samples in the closed interval [start,end].
	"""
	
	grid=np.linspace(start, end, n)
	data=model(grid, params)
	data=noise(data, sigma)
	
	return data, grid
