import numpy as np
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '0.1.0'




def likelihood(data,grid,xn,sigma):
	L = np.sqrt(2*np.pi*sigma**2)*np.exp(-0.5*(sum(data - model(grid,xn))**2 / sigma**2))
	#verosimiglianza #
	return L  


def inrange(x,start,end):
	""" This function gives us a continuos uniform distribution between 
	sup and inf.
	""" 

	if start<=x<=end:
		h=1/(end-start)
	else:
		h=0
	return h


def prior(xn,start,end): 
	""" This function is a uniform and normalized function.
	We have to consider 2 cases: xn is a number (real or integer) or xn is an array.
	"""


	if isinstance(xn, float) or isinstance (xn,int):
		return inrange(xn,start,end)	
	else:
		out=np.zeros_like(xn) 
		"""We create an array of only zeros of length xn"""
		
		for i,x in enumerate(xn): #prendo gli elementi dentro l'array#
			out[i]=inrange(x,start,end)
		return out
			
			
	 
def posterior_dist(data,grid,sigma,xn,start,end):
	"""As in prior we consider two cases.
	"""
	
	if isinstance(xn, float) or isinstance (xn,int):
		p=likelihood(data,grid,xn,sigma)*prior(xn,start,end)
		return p

	else:
		out=np.zeros_like(xn) #creo un array di zero lungo come xn#
		for i,x in enumerate(xn): #prendo gli elementi dentro l'array#
			out[i]=likelihood(data,grid,x,sigma)*prior(x,start,end)
		return out
	


def evidence(data,grid,sigma,out,start,end):

	z=((end-start)*np.sum(posterior_dist(data,grid,sigma,out,start,end)))/len(out)
	return z

	#len è la lunghezza di out#




def MCMC(sigma,data,grid,init_MCMC=0,itmax=10000,start=0,end=1) : 
	"""This function samples a random number, which steps resemble
	a random walk."""

	"""
	Input
	xn : starting position
	controll : Metropolis ratio 
	xn1_acc : accepted value 
	U : uniform random number 
	
	Output
	samples : list, list of samples from the posterior fistribution
	numb_accept : float, number of accepted unique samples
	"""
	
	sigma=1
	burnin=1000
	skip=2	
	out=np.ones(int((itmax-burnin)/skip)) 

	"""We remove the first 1000 drawn from the list of numbers and take one yes and one no.
	"""
	
	xn = init_MCMC
	saved=False
	j=0

	for i in range (itmax):
	
		xn1= np.random.normal(xn,sigma)
		controll =  min(1,
				posterior_dist(data,grid,sigma,xn1,start,end)/
posterior_dist(data,grid,sigma,xn,start,end)
				)


		
		if np.random.rand()<=controll:
			xn=xn1
				#else xn=xn#
		if i>burnin and saved==False : 
			out[j]=xn
			saved=True
			j+=1
		elif saved==True:
			saved=False

	
	return out		
















