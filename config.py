import numpy as np

"""
  
	---------
	init_MCMC: ndarray
	initial guessed of the parameters
	
	itmax: int
	final step of cycle
	
	n: int
	number of iterations
	
	params: ndarray
	parameters of the analytic function.
	
	sigma: float 
	standard deviation of the distribution. Must be non-negative.
	
        start: float
	beginning of function domain
  
  
	end: float
	end of function domain
	
        xstart: int
  
        initial value of the domain
  
        xend: int
        final value of the domain
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
