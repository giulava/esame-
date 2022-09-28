import numpy as np
import matplotlib.pyplot as plt
from sampler import MCMC
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='1.0.0'


def main():
	"""Input
	"""
	init_MCMC=np.array([0.5,0.5,0.5], dtype = np.float64)
	itmax=1000000
	n=50
	params=np.array([0.5,0.5,0.5], dtype = np.float64)
	sigma=0.25
	start=np.array([0,0,0], dtype = np.float64)
	end=np.array([2,2,2], dtype = np.float64)
	xstart=0
	xend=5

	data,grid=fakedata(xstart,xend,n,params,sigma)
	posterior=MCMC(sigma,data,grid,init_MCMC=init_MCMC,itmax=itmax,start=start,end=end)
	posteriorA=posterior[:,0]
	posteriorB=posterior[:,1]	
	posteriorC=posterior[:,2]
	
	#plots
	
	plt.figure()
	plt.hist(posteriorA, bins = 100, histtype='step', density = True, label='histogram') 
	plt.show()

	plt.figure()
	plt.hist(posteriorB, bins = 100, histtype='step', density = True, label='histogram')
	plt.show()

	plt.figure()
	plt.hist(posteriorC, bins = 100, histtype='step', density = True, label='histogram')
	plt.show()
	
	q_16A,q_50A,q_84A = np.quantile(posteriorA, [0.16,0.5, 0.84], axis = 0)
	q_mA, q_pA=q_50A-q_16A, q_84A-q_50A
	print(f'{q_50A}  + {q_pA} - {q_mA}')


	q_16B,q_50B,q_84B = np.quantile(posteriorB, [0.16,0.5, 0.84], axis = 0)
	q_mB, q_pB=q_50B-q_16B, q_84B-q_50B
	print(f'{q_50B}  + {q_pB} - {q_mB}')

	q_16C,q_50C,q_84C = np.quantile(posteriorC, [0.16,0.5, 0.84], axis = 0)
	q_mC, q_pC=q_50C-q_16C, q_84C-q_50C
	print(f'{q_50C}  + {q_pC} - {q_mC}')

	
	eparams=np.array([q_50A,q_50B,q_50C])
	xx=np.linspace(xstart,xend,1000)
	fig=plt.figure()
	plt.plot(grid,data,"o")
	plt.plot(xx,model(xx,eparams))
	plt.show()


	



if __name__=="__main__":
	 #togliere#
	main()

