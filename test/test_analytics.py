import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose




import sys
sys.path.append("../")
from analytic_model import *

def test_model():
	a=1
	b=1
	c=0
	modelv=np.array([0.5,1.5,3.5,6.5])
		#Modelv contains exact values#
	x=np.array([0,1,2,3])
	modelt=model(x,a,b,c)
	assert_array_equal(modelv,modelt) 
