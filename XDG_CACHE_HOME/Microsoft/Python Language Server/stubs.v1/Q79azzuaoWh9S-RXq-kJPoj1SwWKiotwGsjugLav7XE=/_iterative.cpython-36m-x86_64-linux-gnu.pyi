__doc__ = "This module '_iterative' is auto-generated with f2py (version:2).\nFunctions:\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/sparse/linalg/isolve/_iterative.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.linalg.isolve._iterative'
__package__ = 'scipy.sparse.linalg.isolve'
__version__ = b'$Revision: $'
def cbicgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``cbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def cbicgstabrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``cbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def ccgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``ccgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def ccgsrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``ccgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def cgmresrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``cgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('F') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('F') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def cqmrrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``cqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('F') with bounds (n)\nx : input rank-1 array('F') with bounds (n)\nwork : in/output rank-1 array('F') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('F') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def dbicgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def dbicgstabrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def dcgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dcgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def dcgsrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dcgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def dgmresrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``dgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('d') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('d') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def dqmrrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``dqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('d') with bounds (n)\nx : input rank-1 array('d') with bounds (n)\nwork : in/output rank-1 array('d') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def sbicgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``sbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def sbicgstabrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``sbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def scgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``scgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def scgsrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``scgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def sgmresrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``sgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('f') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('f') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def sqmrrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``sqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('f') with bounds (n)\nx : input rank-1 array('f') with bounds (n)\nwork : in/output rank-1 array('f') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('f') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : float\nsclr2 : float\nijob : int\n"
    pass

def zbicgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zbicgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (6 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def zbicgstabrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zbicgstabrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def zcgrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zcgrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (4 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def zcgsrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zcgsrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (7 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def zgmresrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)\n\nWrapper for ``zgmresrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nrestrt : input int\nwork : in/output rank-1 array('D') with bounds (ldw*(6+restrt))\nwork2 : in/output rank-1 array('D') with bounds (ldw2*(2*restrt+2))\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\ntol : input float\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

def zqmrrevcom():
    "x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)\n\nWrapper for ``zqmrrevcom``.\n\nParameters\n----------\nb : input rank-1 array('D') with bounds (n)\nx : input rank-1 array('D') with bounds (n)\nwork : in/output rank-1 array('D') with bounds (11 * ldw)\niter : input int\nresid : input float\ninfo : input int\nndx1 : input int\nndx2 : input int\nijob : input int\n\nReturns\n-------\nx : rank-1 array('D') with bounds (n)\niter : int\nresid : float\ninfo : int\nndx1 : int\nndx2 : int\nsclr1 : complex\nsclr2 : complex\nijob : int\n"
    pass

