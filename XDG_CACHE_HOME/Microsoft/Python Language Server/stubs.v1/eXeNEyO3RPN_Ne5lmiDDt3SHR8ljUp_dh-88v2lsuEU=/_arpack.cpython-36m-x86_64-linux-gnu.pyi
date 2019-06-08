__doc__ = "This module '_arpack' is auto-generated with f2py (version:2).\nFunctions:\n  ido,tol,resid,v,iparam,ipntr,info = ssaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))\n  ido,tol,resid,v,iparam,ipntr,info = dsaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))\n  d,z,info = sseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))\n  d,z,info = dseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))\n  ido,tol,resid,v,iparam,ipntr,info = snaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))\n  ido,tol,resid,v,iparam,ipntr,info = dnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))\n  dr,di,z,info = sneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))\n  dr,di,z,info = dneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))\n  ido,tol,resid,v,iparam,ipntr,info = cnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))\n  ido,tol,resid,v,iparam,ipntr,info = znaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))\n  d,z,info = cneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))\n  d,z,info = zneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))\nCOMMON blocks:\n  /debug/ logfil,ndigit,mgetv0,msaupd,msaup2,msaitr,mseigt,msapps,msgets,mseupd,mnaupd,mnaup2,mnaitr,mneigh,mnapps,mngets,mneupd,mcaupd,mcaup2,mcaitr,mceigh,mcapps,mcgets,mceupd\n  /timing/ nopx,nbx,nrorth,nitref,nrstrt,tsaupd,tsaup2,tsaitr,tseigt,tsgets,tsapps,tsconv,tnaupd,tnaup2,tnaitr,tneigh,tngets,tnapps,tnconv,tcaupd,tcaup2,tcaitr,tceigh,tcgets,tcapps,tcconv,tmvopx,tmvbx,tgetv0,titref,trvec\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/sparse/linalg/eigen/arpack/_arpack.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.linalg.eigen.arpack._arpack'
__package__ = 'scipy.sparse.linalg.eigen.arpack'
__version__ = b'$Revision: $'
def cnaupd():
    "ido,tol,resid,v,iparam,ipntr,info = cnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``cnaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('F') with bounds (n)\nv : input rank-2 array('F') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('F') with bounds (3 * n)\nworkl : in/output rank-1 array('F') with bounds (lworkl)\nrwork : in/output rank-1 array('f') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('F') with bounds (n)\nv : rank-2 array('F') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    pass

def cneupd():
    "d,z,info = cneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``cneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input complex\nworkev : input rank-1 array('F') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('F') with bounds (n)\nv : input rank-2 array('F') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('F') with bounds (3 * n)\nworkl : input rank-1 array('F') with bounds (lworkl)\nrwork : input rank-1 array('f') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('F') with bounds (nev)\nz : rank-2 array('F') with bounds (n,nev)\ninfo : int\n"
    pass

def debug():
    "'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n"
    pass

def dnaupd():
    "ido,tol,resid,v,iparam,ipntr,info = dnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``dnaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('d') with bounds (3 * n)\nworkl : in/output rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    pass

def dneupd():
    "dr,di,z,info = dneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``dneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigmar : input float\nsigmai : input float\nworkev : input rank-1 array('d') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (n,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('d') with bounds (3 * n)\nworkl : input rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\ndr : rank-1 array('d') with bounds (nev + 1)\ndi : rank-1 array('d') with bounds (nev + 1)\nz : rank-2 array('d') with bounds (n,nev + 1)\ninfo : int\n"
    pass

def dsaupd():
    "ido,tol,resid,v,iparam,ipntr,info = dsaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``dsaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : in/output rank-1 array('d') with bounds (3 * n)\nworkl : in/output rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('d') with bounds (n)\nv : rank-2 array('d') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (11)\ninfo : int\n"
    pass

def dseupd():
    "d,z,info = dseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``dseupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input float\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('d') with bounds (n)\nv : input rank-2 array('d') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (7)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : input rank-1 array('d') with bounds (2 * n)\nworkl : input rank-1 array('d') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('d') with bounds (nev)\nz : rank-2 array('d') with bounds (n,nev)\ninfo : int\n"
    pass

def snaupd():
    "ido,tol,resid,v,iparam,ipntr,info = snaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``snaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('f') with bounds (3 * n)\nworkl : in/output rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    pass

def sneupd():
    "dr,di,z,info = sneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``sneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigmar : input float\nsigmai : input float\nworkev : input rank-1 array('f') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (n,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('f') with bounds (3 * n)\nworkl : input rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\ndr : rank-1 array('f') with bounds (nev + 1)\ndi : rank-1 array('f') with bounds (nev + 1)\nz : rank-2 array('f') with bounds (n,nev + 1)\ninfo : int\n"
    pass

def ssaupd():
    "ido,tol,resid,v,iparam,ipntr,info = ssaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``ssaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : in/output rank-1 array('f') with bounds (3 * n)\nworkl : in/output rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('f') with bounds (n)\nv : rank-2 array('f') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (11)\ninfo : int\n"
    pass

def sseupd():
    "d,z,info = sseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``sseupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input float\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('f') with bounds (n)\nv : input rank-2 array('f') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (7)\nipntr : input rank-1 array('i') with bounds (11)\nworkd : input rank-1 array('f') with bounds (2 * n)\nworkl : input rank-1 array('f') with bounds (lworkl)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('f') with bounds (nev)\nz : rank-2 array('f') with bounds (n,nev)\ninfo : int\n"
    pass

def timing():
    "'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'i'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n'f'-scalar\n"
    pass

def znaupd():
    "ido,tol,resid,v,iparam,ipntr,info = znaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[n,ncv,ldv,lworkl])\n\nWrapper for ``znaupd``.\n\nParameters\n----------\nido : input int\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('D') with bounds (n)\nv : input rank-2 array('D') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : in/output rank-1 array('D') with bounds (3 * n)\nworkl : in/output rank-1 array('D') with bounds (lworkl)\nrwork : in/output rank-1 array('d') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: shape(v,1)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nido : int\ntol : float\nresid : rank-1 array('D') with bounds (n)\nv : rank-2 array('D') with bounds (ldv,ncv)\niparam : rank-1 array('i') with bounds (11)\nipntr : rank-1 array('i') with bounds (14)\ninfo : int\n"
    pass

def zneupd():
    "d,z,info = zneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[ldz,n,ncv,ldv,lworkl])\n\nWrapper for ``zneupd``.\n\nParameters\n----------\nrvec : input int\nhowmny : input string(len=1)\nselect : input rank-1 array('i') with bounds (ncv)\nsigma : input complex\nworkev : input rank-1 array('D') with bounds (3 * ncv)\nbmat : input string(len=1)\nwhich : input string(len=2)\nnev : input int\ntol : input float\nresid : input rank-1 array('D') with bounds (n)\nv : input rank-2 array('D') with bounds (ldv,ncv)\niparam : input rank-1 array('i') with bounds (11)\nipntr : input rank-1 array('i') with bounds (14)\nworkd : input rank-1 array('D') with bounds (3 * n)\nworkl : input rank-1 array('D') with bounds (lworkl)\nrwork : input rank-1 array('d') with bounds (ncv)\ninfo : input int\n\nOther Parameters\n----------------\nldz : input int, optional\n    Default: shape(z,0)\nn : input int, optional\n    Default: len(resid)\nncv : input int, optional\n    Default: len(select)\nldv : input int, optional\n    Default: shape(v,0)\nlworkl : input int, optional\n    Default: len(workl)\n\nReturns\n-------\nd : rank-1 array('D') with bounds (nev)\nz : rank-2 array('D') with bounds (n,nev)\ninfo : int\n"
    pass
