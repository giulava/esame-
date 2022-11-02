import matplotlib.pyplot as plt
import numpy as np
from analytic_model import model

"""
This function gives us the plots. 

-------
Input

posteriorA: ndarray
Estimated parameter a

posteriorB: ndarray
Estimated parameter b

posteriorC: ndarray
Estimated parameter c

xstart: int
initial value of the domain

xend: int
final value of the domain


grid: ndarray
There are n equally spaced samples in the closed interval [start,end].


data: ndarray

experimental points

--------
Output
plots

"""

def makeplot(posteriorA,posteriorB,posteriorC,xstart,xend,grid,data):



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
  
  
  
