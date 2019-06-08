__doc__ = "This module '_lbfgsb' is auto-generated with f2py (version:2).\nFunctions:\n  setulb(m,x,l,u,nbd,f,g,factr,pgtol,wa,iwa,task,iprint,csave,lsave,isave,dsave,maxls,n=len(x))\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/optimize/_lbfgsb.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize._lbfgsb'
__package__ = 'scipy.optimize'
__version__ = b'$Revision: $'
def setulb(m, x, l, u, nbd, f, g, factr, pgtol, wa, iwa, task, iprint, csave, lsave, isave, dsave, maxls, n=None):
    "setulb(m,x,l,u,nbd,f,g,factr,pgtol,wa,iwa,task,iprint,csave,lsave,isave,dsave,maxls,[n])\n\nWrapper for ``setulb``.\n\nParameters\n----------\nm : input int\nx : in/output rank-1 array('d') with bounds (n)\nl : input rank-1 array('d') with bounds (n)\nu : input rank-1 array('d') with bounds (n)\nnbd : input rank-1 array('i') with bounds (n)\nf : in/output rank-0 array(float,'d')\ng : in/output rank-1 array('d') with bounds (n)\nfactr : input float\npgtol : input float\nwa : in/output rank-1 array('d') with bounds (2*m*n+5*n+11*m*m+8*m)\niwa : in/output rank-1 array('i') with bounds (3 * n)\ntask : in/output rank-0 array(string(len=60),'c')\niprint : input int\ncsave : in/output rank-0 array(string(len=60),'c')\nlsave : in/output rank-1 array('i') with bounds (4)\nisave : in/output rank-1 array('i') with bounds (44)\ndsave : in/output rank-1 array('d') with bounds (29)\nmaxls : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(x)\n"
    pass

