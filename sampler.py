import numpy as np
from analytic_model import fakedata 


__author__ = 'Giulia Avato'
__email__ = 'giulia.avato@studio.unibo.it'
__version__ = '0.0.2'




def main():
	start=0
	end=1
	n=5
	params=(2,1,3)
	sigma=1
	data=fakedata(start,end,n,params,sigma)




MCMC(start=0,end=1000,inf=0,sup=1)
sigma=1
xn = start

for i in range (end):
	xn1= np.random.normal(xn,sigma)
	controll =  prob(xn1,inf,sup)/prob(xn,inf,sup)

	if controll>=1 :
		xn1_acc=xn1
	else :
		U = np.random.rand(1,1)
		
		if U<=controll
			xn1_acc=xn1
		else :
			xn=xn1














if __name__=="__main__":
	main()

