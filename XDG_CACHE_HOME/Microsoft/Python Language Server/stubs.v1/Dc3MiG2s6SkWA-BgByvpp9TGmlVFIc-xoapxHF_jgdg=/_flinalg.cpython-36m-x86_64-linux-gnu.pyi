__doc__ = "This module '_flinalg' is auto-generated with f2py (version:2).\nFunctions:\n  det,info = ddet_c(a,overwrite_a=0)\n  det,info = ddet_r(a,overwrite_a=0)\n  det,info = sdet_c(a,overwrite_a=0)\n  det,info = sdet_r(a,overwrite_a=0)\n  det,info = zdet_c(a,overwrite_a=0)\n  det,info = zdet_r(a,overwrite_a=0)\n  det,info = cdet_c(a,overwrite_a=0)\n  det,info = cdet_r(a,overwrite_a=0)\n  p,l,u,info = dlu_c(a,permute_l=0,overwrite_a=0)\n  p,l,u,info = zlu_c(a,permute_l=0,overwrite_a=0)\n  p,l,u,info = slu_c(a,permute_l=0,overwrite_a=0)\n  p,l,u,info = clu_c(a,permute_l=0,overwrite_a=0)\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/linalg/_flinalg.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.linalg._flinalg'
__package__ = 'scipy.linalg'
__version__ = b'$Revision: $'
def cdet_c():
    "det,info = cdet_c(a,[overwrite_a])\n\nWrapper for ``cdet_c``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    pass

def cdet_r():
    "det,info = cdet_r(a,[overwrite_a])\n\nWrapper for ``cdet_r``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    pass

def clu_c():
    "p,l,u,info = clu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``clu_c``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('f') with bounds (m1,m1)\nl : rank-2 array('F') with bounds (m,k)\nu : rank-2 array('F') with bounds (k,n)\ninfo : int\n"
    pass

def ddet_c():
    "det,info = ddet_c(a,[overwrite_a])\n\nWrapper for ``ddet_c``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    pass

def ddet_r():
    "det,info = ddet_r(a,[overwrite_a])\n\nWrapper for ``ddet_r``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    pass

def dlu_c():
    "p,l,u,info = dlu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``dlu_c``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('d') with bounds (m1,m1)\nl : rank-2 array('d') with bounds (m,k)\nu : rank-2 array('d') with bounds (k,n)\ninfo : int\n"
    pass

def sdet_c():
    "det,info = sdet_c(a,[overwrite_a])\n\nWrapper for ``sdet_c``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    pass

def sdet_r():
    "det,info = sdet_r(a,[overwrite_a])\n\nWrapper for ``sdet_r``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : float\ninfo : int\n"
    pass

def slu_c():
    "p,l,u,info = slu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``slu_c``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('f') with bounds (m1,m1)\nl : rank-2 array('f') with bounds (m,k)\nu : rank-2 array('f') with bounds (k,n)\ninfo : int\n"
    pass

def zdet_c():
    "det,info = zdet_c(a,[overwrite_a])\n\nWrapper for ``zdet_c``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    pass

def zdet_r():
    "det,info = zdet_r(a,[overwrite_a])\n\nWrapper for ``zdet_r``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\ndet : complex\ninfo : int\n"
    pass

def zlu_c():
    "p,l,u,info = zlu_c(a,[permute_l,overwrite_a])\n\nWrapper for ``zlu_c``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (m,n)\n\nOther Parameters\n----------------\noverwrite_a : input int, optional\n    Default: 0\npermute_l : input int, optional\n    Default: 0\n\nReturns\n-------\np : rank-2 array('d') with bounds (m1,m1)\nl : rank-2 array('D') with bounds (m,k)\nu : rank-2 array('D') with bounds (k,n)\ninfo : int\n"
    pass

