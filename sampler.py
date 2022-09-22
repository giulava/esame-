import numpy as np
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '0.0.3'




def main():
	start=0
	end=1
	n=5
	params=(2,1,3)
	sigma=1
	data=fakedata(start,end,n,params,sigma)


def likelihood(data,sigma=1,xn,params):

	L = np.exp(-0.5*(np.log(2*np.pi*sigma**2) + 0.5*(data - model(x, params))**2 / sigma**2 )  )
	#verosimiglianza #
	return L  


def prior(xn,inf,sup): 
	#sarà uniforme e normalizzata#
	
	if inf <= xn <= sup:
		h=1/(sup-inf)
	else:
		h=0
		
	return h
	 


def prob(data,sigma,xn,params,inf,sup):
	
	p=likelihood(data,sigma,xn,params)*prior(xn,inf,sup)
	
	return p





def MCMC(sigma,data, start=0,end=1000,inf=0,sup=1) : 
	"""This function samples a random number, which steps resemble
	a random walk."""

	"""
	xn : starting position
	controll : Metropolis ratio 
	xn1_acc : accepted value 
	U : uniform random number 
	"""
 
	sigma=1	
	xn = start

	for i in range (end):
	
		xn1= np.random.normal(xn,sigma)
		controll =  prob(data,sigma,xn1,params,inf,sup)/prob(data,sigma,xn,params,inf,sup)

		if controll>=1 :
			xn=xn1
		else :
			U = np.random.rand(1,1)
		
			if U<=controll
				xn=xn1
				#else xn=xn#
	return xn		














if __name__=="__main__":
	main()

