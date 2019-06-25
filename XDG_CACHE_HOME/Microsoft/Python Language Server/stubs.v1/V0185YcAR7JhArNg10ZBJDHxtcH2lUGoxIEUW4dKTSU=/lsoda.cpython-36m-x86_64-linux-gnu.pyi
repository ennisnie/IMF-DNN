__doc__ = "This module 'lsoda' is auto-generated with f2py (version:2).\nFunctions:\n  y,t,istate = lsoda(f,y,t,tout,rtol,atol,itask,istate,rwork,iwork,jac,jt,f_extra_args=(),overwrite_y=0,jac_extra_args=())\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/integrate/lsoda.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.integrate.lsoda'
__package__ = 'scipy.integrate'
__version__ = b'$Revision: $'
def lsoda():
    "y,t,istate = lsoda(f,y,t,tout,rtol,atol,itask,istate,rwork,iwork,jac,jt,[f_extra_args,overwrite_y,jac_extra_args])\n\nWrapper for ``lsoda``.\n\nParameters\n----------\nf : call-back function\ny : input rank-1 array('d') with bounds (neq)\nt : input float\ntout : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nitask : input int\nistate : input int\nrwork : input rank-1 array('d') with bounds (lrw)\niwork : input rank-1 array('i') with bounds (liw)\njac : call-back function\njt : input int\n\nOther Parameters\n----------------\nf_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\njac_extra_args : input tuple, optional\n    Default: ()\n\nReturns\n-------\ny : rank-1 array('d') with bounds (neq)\nt : float\nistate : int\n\nNotes\n-----\nCall-back functions::\n\n  def f(t,y): return ydot\n  Required arguments:\n    t : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    ydot : rank-1 array('d') with bounds (n)\n  def jac(t,y): return jac\n  Required arguments:\n    t : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    jac : rank-2 array('d') with bounds (nrowpd,n)\n"
    pass

