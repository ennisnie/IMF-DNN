__doc__ = "This module '_cobyla' is auto-generated with f2py (version:2).\nFunctions:\n  x,dinfo = minimize(calcfc,m,x,rhobeg,rhoend,dinfo,iprint=1,maxfun=100,calcfc_extra_args=())\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/optimize/_cobyla.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize._cobyla'
__package__ = 'scipy.optimize'
__version__ = b'$Revision: $'
def minimize():
    "x,dinfo = minimize(calcfc,m,x,rhobeg,rhoend,dinfo,[iprint,maxfun,calcfc_extra_args])\n\nWrapper for ``minimize``.\n\nParameters\n----------\ncalcfc : call-back function\nm : input int\nx : input rank-1 array('d') with bounds (n)\nrhobeg : input float\nrhoend : input float\ndinfo : input rank-1 array('d') with bounds (4)\n\nOther Parameters\n----------------\ncalcfc_extra_args : input tuple, optional\n    Default: ()\niprint : input int, optional\n    Default: 1\nmaxfun : input int, optional\n    Default: 100\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\ndinfo : rank-1 array('d') with bounds (4)\n\nNotes\n-----\nCall-back functions::\n\n  def calcfc(x,con): return f\n  Required arguments:\n    x : input rank-1 array('d') with bounds (n)\n    con : input rank-1 array('d') with bounds (m)\n  Return objects:\n    f : float\n"
    pass

