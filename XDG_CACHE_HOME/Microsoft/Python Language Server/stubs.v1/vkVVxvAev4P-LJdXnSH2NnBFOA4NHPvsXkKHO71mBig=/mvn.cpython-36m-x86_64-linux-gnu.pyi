__doc__ = "This module 'mvn' is auto-generated with f2py (version:2).\nFunctions:\n  value,inform = mvnun(lower,upper,means,covar,maxpts=d*1000,abseps=1e-06,releps=1e-06)\n  value,inform = mvnun_weighted(lower,upper,means,weights,covar,maxpts=d*1000,abseps=1e-06,releps=1e-06)\n  error,value,inform = mvndst(lower,upper,infin,correl,maxpts=2000,abseps=1e-06,releps=1e-06)\nCOMMON blocks:\n  /dkblck/ ivls\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/stats/mvn.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.stats.mvn'
__package__ = 'scipy.stats'
__version__ = b'$Revision: $'
def dkblck():
    "'i'-scalar\n"
    pass

def mvndst():
    "error,value,inform = mvndst(lower,upper,infin,correl,[maxpts,abseps,releps])\n\nWrapper for ``mvndst``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (n)\nupper : input rank-1 array('d') with bounds (n)\ninfin : input rank-1 array('i') with bounds (n)\ncorrel : input rank-1 array('d') with bounds (n*(n-1)/2)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: 2000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nerror : float\nvalue : float\ninform : int\n"
    pass

def mvnun():
    "value,inform = mvnun(lower,upper,means,covar,[maxpts,abseps,releps])\n\nWrapper for ``mvnun``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (d)\nupper : input rank-1 array('d') with bounds (d)\nmeans : input rank-2 array('d') with bounds (d,n)\ncovar : input rank-2 array('d') with bounds (d,d)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: d*1000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nvalue : float\ninform : int\n"
    pass

def mvnun_weighted():
    "value,inform = mvnun_weighted(lower,upper,means,weights,covar,[maxpts,abseps,releps])\n\nWrapper for ``mvnun_weighted``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (d)\nupper : input rank-1 array('d') with bounds (d)\nmeans : input rank-2 array('d') with bounds (d,n)\nweights : input rank-1 array('d') with bounds (n)\ncovar : input rank-2 array('d') with bounds (d,d)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: d*1000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nvalue : float\ninform : int\n"
    pass

