__doc__ = "This module 'minpack2' is auto-generated with f2py (version:2).\nFunctions:\n  stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)\n  stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/optimize/minpack2.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize.minpack2'
__package__ = 'scipy.optimize'
__version__ = b'$Revision: $'
def dcsrch():
    "stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)\n\nWrapper for ``dcsrch``.\n\nParameters\n----------\nstp : input float\nf : input float\ng : input float\nftol : input float\ngtol : input float\nxtol : input float\ntask : input string(len=60)\nstpmin : input float\nstpmax : input float\nisave : in/output rank-1 array('i') with bounds (2)\ndsave : in/output rank-1 array('d') with bounds (13)\n\nReturns\n-------\nstp : float\nf : float\ng : float\ntask : string(len=60)\n"
    pass

def dcstep():
    'stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)\n\nWrapper for ``dcstep``.\n\nParameters\n----------\nstx : input float\nfx : input float\ndx : input float\nsty : input float\nfy : input float\ndy : input float\nstp : input float\nfp : input float\ndp : input float\nbrackt : input int\nstpmin : input float\nstpmax : input float\n\nReturns\n-------\nstx : float\nfx : float\ndx : float\nsty : float\nfy : float\ndy : float\nstp : float\nbrackt : int\n'
    pass

