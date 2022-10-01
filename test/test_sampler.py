import pytest
import numpy as np
from numpy.testing import assert_allclose




import sys
sys.path.append("../")
from sampler import *


def test_check():
        start=1
        end=2

        checkc=np.array([0,0,1,1,0,0])
                #checkv contains exact values#
        x=np.array([0,0.5,1.5,1.8,3,4])
        checkt=np.zeros_like(x)
        for i,e in enumerate(x)
                check[i]=check(e,start,end)
        assert_allclose(checkv,checkt)
