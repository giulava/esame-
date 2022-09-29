import pytest
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose




import sys
sys.path.append("../")
from analytic_model import fakedata, model
from sampler import *


def test_inrange():
        start=0
        end=2

        inrangev=np.array([0,0,1,1,0,0])
                #inrangev contains exact values#
        x=np.array([-1,-0.5,0.5,0.8,2,3])
        inranget=inrange(x,start,end)
        assert_array_equal(inrangev,inranget)
