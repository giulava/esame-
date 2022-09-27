import numpy as np
import matplotlib.pyplot as plt
from sampler import MCMC
from analytic_model import fakedata,model

__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'	
__version__='0.1.0'


def main():
	init_MCMC=0.5
	itmax=100000
	n=1000
	params=(0.5,)
	sigma=0.5
	start=0
	end=2
	
	data,grid=fakedata(0,2,50,(0.5),0.5)
	posterior=MCMC(sigma,data,grid,init_MCMC=init_MCMC,itmax=itmax,start=0,end=2)
	
	plt.figure()
	plt.hist(posterior, bins = 100, histtype='step', density = True, label='histogram')
	
	plt.show()
	#print(np.quantile(posterior,0.5))
	
	q_16,q_50,q_84 = np.quantile(posterior, [0.16,0.5, 0.84], axis = 0)
	q_m, q_p=q_50-q_16, q_84-q_50
	print(f'{q_50}  + {q_p} - {q_m}')



	



if __name__=="__main__":
	np.random.seed(1000) #togliere#
	main()

