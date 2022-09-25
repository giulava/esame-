import numpy as np
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '0.0.4'




def likelihood(data,grid,xn,sigma):
	
	L = np.exp(-0.5*sum(np.log(2*np.pi*sigma**2) + (data - model(grid,xn))**2 / sigma**2 ))
	#verosimiglianza #
	return L  


def inrange(x,inf,sup):
	if inf<=x<=sup:
		h=1/(sup-inf)
	else:
		h=0

	return h


def prior(xn,inf,sup): 
	#sarà uniforme e normalizzata#
	if isinstance(xn, float) or isinstance (xn,int):
		return inrange(xn,inf,sup)	
	else:
		out=np.zeros_like(xn) #creo un array di zero lungo come xn#
		for i,x in enumerate(xn): #prendo gli elementi dentro l'array#
			out[i]=inrange(x,inf,sup)
		return out
			
			
	 


def prob(data,grid,sigma,xn,inf,sup):
	
	if isinstance(xn, float) or isinstance (xn,int):
		p=likelihood(data,grid,xn,sigma)*prior(xn,inf,sup)
		return p

	else:
		out=np.zeros_like(xn) #creo un array di zero lungo come xn#
		for i,x in enumerate(xn): #prendo gli elementi dentro l'array#
			out[i]=likelihood(data,grid,x,sigma)*prior(x,inf,sup)
		return out
	


def evidence(data,grid,sigma,out,inf,sup):

	z=((sup-inf)*np.sum(prob(data,grid,sigma,out,inf,sup)))/len(out)
	return z

	#len è la lunghezza di out#




def MCMC(sigma,data,grid,init_MCMC=0,itmax=5000,inf=0,sup=1) : 
	"""This function samples a random number, which steps resemble
	a random walk."""

	"""
	xn : starting position
	controll : Metropolis ratio 
	xn1_acc : accepted value 
	U : uniform random number 
	"""
 
	burnin=	1000
	skip=2

	sigma=1	
	out=np.ones(int((itmax-burnin)/skip)) 
	#tolgo dalla lista dei numeri i primi 1000 estratti e ne prendo uno sì e uno no#
	xn = init_MCMC
	saved=False
	j=0

	for i in range (itmax):
	
		xn1= np.random.normal(xn,sigma)
		controll =  prob(data,grid,sigma,xn1,inf,sup)/prob(data,grid,sigma,xn,inf,sup)
		
		if controll>=1 :
			xn=xn1
		else :
			U = np.random.rand(1,1)
		
			if U<=controll:
				xn=xn1
				#else xn=xn#
		if i>burnin and saved==False : 
			out[j]=xn
			saved=True
			j+=1
		elif saved==True:
			saved=False
	zeta=evidence(data,grid,sigma,out,inf,sup)
	posterior=prob(data,grid,sigma,out,inf,sup)/zeta
	return out,zeta,posterior		
















