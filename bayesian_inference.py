import numpy as np
from config import *
from sampler import MCMC
from analytic_model import fakedata,model
from plots import makeplot 



__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='1.0.0'

"""
Main code that implements the MCMC algorithm and estimates the parameters from simulated data.
-----
input

xstart: int
initial value of the domain

xend: int
final value of the domain

n: int
number of iterations

params: ndarray
parameters of the analytic function

sigma: float 
standard deviation of the distribution. Must be non-negative
	
data:ndarray
drawn samples from the parameterized normal distribution

grid: ndarray
There are n equally spaced samples in the closed interval [start,end].
	
init_MCMC: ndarray
initial guessed of the parameters
	
itmax: int
final step of cycle
	
start: float
beginning of function domain

end: float
end of function domain

-----
output

posteriorA: ndarray
estimated parameter a

posteriorB: ndarray
estimated parameter b

posteriorC: ndarray
estimated parameter c


"""
def main():
	
	data,grid=fakedata(xstart,xend,n,params,sigma)
	posterior=MCMC(sigma,data,grid,init_MCMC=init_MCMC,itmax=itmax,start=start,end=end)
	posteriorA=posterior[:,0]
	posteriorB=posterior[:,1]	
	posteriorC=posterior[:,2]
	
	makeplot(posteriorA,posteriorB,posteriorC,xstart,xend,grid,data)
	
if __name__=="__main__":
	 
	main()

