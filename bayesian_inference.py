import numpy as np
import matplotlib.pyplot as plt
from sampler import MCMC
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='0.1.0'


def main():
	init_MCMC=0
	itmax=10000
	n=100
	params=(1,)
	sigma=1
	xstart=0
	xend=1
	data,grid=fakedata(xstart,xend,n,params,sigma)
	r,zeta,posterior=MCMC(sigma,data,grid,init_MCMC=init_MCMC,itmax=itmax,inf=0,sup=2)
	
	plt.figure(figsize=(8, 4))
	plt.hist(posterior, bins = 100, histtype='step', density = True, label='histogram')
	plt.show()
	#print(np.quantile(posterior,0.5))
	
	q_16,q_50,q_84 = np.quantile(posterior, [0.16,0.5, 0.84], axis = 0)
	q_m, q_p=q_50-q_16, q_84-q_50
	print(f'{q_50}  + {q_p} - {q_m}')



	



if __name__=="__main__":
	main()
