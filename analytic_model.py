import numpy as np



def model(x,b):
	"""
	This function computes the analytic model that we will try to recover. 
	x is the independent variable, b is the parameter.
	"""

	return b*x 





def noise(mu,sigma):
	"""
	This function computes the noise to be superimposed to the model. 
	Sigma is the standard deviation and mu the mean of the gaussian.
	"""

	return np.random.normal(mu,sigma) 
	  



def fakedata(start,end,n,params,sigma):
	"""
	This function computes the experimental data points.
	Start is the beginning of function domain, end his end, n is the number of points.
	It gives as output an array containing the data points.
	"""
	
	grid=np.linspace(start,end,n)
	data=model(grid,params)
	data=noise(data,sigma)
	
	return data,grid
