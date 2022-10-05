import pytest
import numpy as np
from numpy.testing import assert_allclose




import sys
sys.path.append("../")
from analytic_model import *

def test_model():
	a=0.5
	b=0.5
	c=0.5
	modelv=np.array([0,0.42073549,0.99749499,1.36394614])
		#Modelv contains exact values#
	params=np.array([a,b,c])
	x=np.array([0,1,2,3])
	modelt=model(x,params)
	assert_array_equal(modelv,modelt) 
