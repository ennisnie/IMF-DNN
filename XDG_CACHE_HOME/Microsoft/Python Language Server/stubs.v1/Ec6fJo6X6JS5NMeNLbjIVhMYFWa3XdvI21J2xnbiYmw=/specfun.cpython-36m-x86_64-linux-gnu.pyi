__doc__ = "This module 'specfun' is auto-generated with f2py (version:2).\nFunctions:\n  cqm,cqd = clqmn(m,n,z)\n  qm,qd = lqmn(m,n,x)\n  cpm,cpd = clpmn(m,n,x,y,ntype)\n  n,m,pcode,zo = jdzo(nt)\n  bn = bernob(n)\n  bn = bernoa(n)\n  pm,pd = lpmns(m,n,x)\n  en = eulera(n)\n  cqn,cqd = clqn(n,z)\n  xa,xb,xc,xd = airyzo(nt,kf=1)\n  en = eulerb(n)\n  cv = cva1(kd,m,q)\n  qn,qd = lqnb(n,x)\n  vm,vl,dl = lamv(v,x)\n  x,w = lagzo(n)\n  x,w = legzo(n)\n  dv,dp,pdf,pdd = pbdv(v,x)\n  zo = cerzo(nt)\n  nm,bl,dl = lamn(n,x)\n  cpn,cpd = clpn(n,z)\n  qm,qd = lqmns(m,n,x)\n  hg = chgm(a,b,x)\n  pm,pd = lpmn(m,n,x)\n  zo = fcszo(kf,nt)\n  s1f,s1d = aswfb(m,n,c,x,kd,cv)\n  qn,qd = lqna(n,x)\n  cpb,cpd = cpbdn(n,z)\n  pn,pd = lpn(n,x)\n  fc = fcoef(kd,m,q,a)\n  nm,ry,dy = rcty(n,x)\n  pn,pd,pl = lpni(n,x)\n  zo,zv = cyzo(nt,kf,kc)\n  pl,dpl = othpl(kf,n,x)\n  zo = klvnzo(nt,kd)\n  rj0,rj1,ry0,ry1 = jyzo(n,nt)\n  nm,rj,dj = rctj(n,x)\n  x,w = herzo(n)\n  vv,vp,pvf,pvd = pbvv(v,x)\n  cv,eg = segv(m,n,c,kd)\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/special/specfun.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.special.specfun'
__package__ = 'scipy.special'
__version__ = b'$Revision: $'
def airyzo():
    "xa,xb,xc,xd = airyzo(nt,[kf])\n\nWrapper for ``airyzo``.\n\nParameters\n----------\nnt : input int\n\nOther Parameters\n----------------\nkf : input int, optional\n    Default: 1\n\nReturns\n-------\nxa : rank-1 array('d') with bounds (nt)\nxb : rank-1 array('d') with bounds (nt)\nxc : rank-1 array('d') with bounds (nt)\nxd : rank-1 array('d') with bounds (nt)\n"
    pass

def aswfb():
    's1f,s1d = aswfb(m,n,c,x,kd,cv)\n\nWrapper for ``aswfb``.\n\nParameters\n----------\nm : input int\nn : input int\nc : input float\nx : input float\nkd : input int\ncv : input float\n\nReturns\n-------\ns1f : float\ns1d : float\n'
    pass

def bernoa():
    "bn = bernoa(n)\n\nWrapper for ``bernoa``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nbn : rank-1 array('d') with bounds (n + 1)\n"
    pass

def bernob():
    "bn = bernob(n)\n\nWrapper for ``bernob``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nbn : rank-1 array('d') with bounds (n + 1)\n"
    pass

def cerzo():
    "zo = cerzo(nt)\n\nWrapper for ``cerzo``.\n\nParameters\n----------\nnt : input int\n\nReturns\n-------\nzo : rank-1 array('D') with bounds (nt)\n"
    pass

def chgm():
    'hg = chgm(a,b,x)\n\nWrapper for ``chgm``.\n\nParameters\n----------\na : input float\nb : input float\nx : input float\n\nReturns\n-------\nhg : float\n'
    pass

def clpmn():
    "cpm,cpd = clpmn(m,n,x,y,ntype)\n\nWrapper for ``clpmn``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\ny : input float\nntype : input int\n\nReturns\n-------\ncpm : rank-2 array('D') with bounds (m + 1,n + 1)\ncpd : rank-2 array('D') with bounds (m + 1,n + 1)\n"
    pass

def clpn():
    "cpn,cpd = clpn(n,z)\n\nWrapper for ``clpn``.\n\nParameters\n----------\nn : input int\nz : input complex\n\nReturns\n-------\ncpn : rank-1 array('D') with bounds (n + 1)\ncpd : rank-1 array('D') with bounds (n + 1)\n"
    pass

def clqmn():
    "cqm,cqd = clqmn(m,n,z)\n\nWrapper for ``clqmn``.\n\nParameters\n----------\nm : input int\nn : input int\nz : input complex\n\nReturns\n-------\ncqm : rank-2 array('D') with bounds (mm + 1,n + 1)\ncqd : rank-2 array('D') with bounds (mm + 1,n + 1)\n"
    pass

def clqn():
    "cqn,cqd = clqn(n,z)\n\nWrapper for ``clqn``.\n\nParameters\n----------\nn : input int\nz : input complex\n\nReturns\n-------\ncqn : rank-1 array('D') with bounds (n + 1)\ncqd : rank-1 array('D') with bounds (n + 1)\n"
    pass

def cpbdn():
    "cpb,cpd = cpbdn(n,z)\n\nWrapper for ``cpbdn``.\n\nParameters\n----------\nn : input int\nz : input complex\n\nReturns\n-------\ncpb : rank-1 array('D') with bounds (abs(n)+2)\ncpd : rank-1 array('D') with bounds (abs(n)+2)\n"
    pass

def cva1():
    "cv = cva1(kd,m,q)\n\nWrapper for ``cva1``.\n\nParameters\n----------\nkd : input int\nm : input int\nq : input float\n\nReturns\n-------\ncv : rank-1 array('d') with bounds (m)\n"
    pass

def cyzo():
    "zo,zv = cyzo(nt,kf,kc)\n\nWrapper for ``cyzo``.\n\nParameters\n----------\nnt : input int\nkf : input int\nkc : input int\n\nReturns\n-------\nzo : rank-1 array('D') with bounds (nt)\nzv : rank-1 array('D') with bounds (nt)\n"
    pass

def eulera():
    "en = eulera(n)\n\nWrapper for ``eulera``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nen : rank-1 array('d') with bounds (n + 1)\n"
    pass

def eulerb():
    "en = eulerb(n)\n\nWrapper for ``eulerb``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nen : rank-1 array('d') with bounds (n + 1)\n"
    pass

def fcoef():
    "fc = fcoef(kd,m,q,a)\n\nWrapper for ``fcoef``.\n\nParameters\n----------\nkd : input int\nm : input int\nq : input float\na : input float\n\nReturns\n-------\nfc : rank-1 array('d') with bounds (251)\n"
    pass

def fcszo():
    "zo = fcszo(kf,nt)\n\nWrapper for ``fcszo``.\n\nParameters\n----------\nkf : input int\nnt : input int\n\nReturns\n-------\nzo : rank-1 array('D') with bounds (nt)\n"
    pass

def herzo():
    "x,w = herzo(n)\n\nWrapper for ``herzo``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\nw : rank-1 array('d') with bounds (n)\n"
    pass

def jdzo():
    "n,m,pcode,zo = jdzo(nt)\n\nWrapper for ``jdzo``.\n\nParameters\n----------\nnt : input int\n\nReturns\n-------\nn : rank-1 array('i') with bounds (1400)\nm : rank-1 array('i') with bounds (1400)\npcode : rank-1 array('i') with bounds (1400)\nzo : rank-1 array('d') with bounds (1401)\n"
    pass

def jyzo():
    "rj0,rj1,ry0,ry1 = jyzo(n,nt)\n\nWrapper for ``jyzo``.\n\nParameters\n----------\nn : input int\nnt : input int\n\nReturns\n-------\nrj0 : rank-1 array('d') with bounds (nt)\nrj1 : rank-1 array('d') with bounds (nt)\nry0 : rank-1 array('d') with bounds (nt)\nry1 : rank-1 array('d') with bounds (nt)\n"
    pass

def klvnzo():
    "zo = klvnzo(nt,kd)\n\nWrapper for ``klvnzo``.\n\nParameters\n----------\nnt : input int\nkd : input int\n\nReturns\n-------\nzo : rank-1 array('d') with bounds (nt)\n"
    pass

def lagzo():
    "x,w = lagzo(n)\n\nWrapper for ``lagzo``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\nw : rank-1 array('d') with bounds (n)\n"
    pass

def lamn():
    "nm,bl,dl = lamn(n,x)\n\nWrapper for ``lamn``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nnm : int\nbl : rank-1 array('d') with bounds (n + 1)\ndl : rank-1 array('d') with bounds (n + 1)\n"
    pass

def lamv():
    "vm,vl,dl = lamv(v,x)\n\nWrapper for ``lamv``.\n\nParameters\n----------\nv : input float\nx : input float\n\nReturns\n-------\nvm : float\nvl : rank-1 array('d') with bounds ((int)v+1)\ndl : rank-1 array('d') with bounds ((int)v+1)\n"
    pass

def legzo():
    "x,w = legzo(n)\n\nWrapper for ``legzo``.\n\nParameters\n----------\nn : input int\n\nReturns\n-------\nx : rank-1 array('d') with bounds (n)\nw : rank-1 array('d') with bounds (n)\n"
    pass

def lpmn():
    "pm,pd = lpmn(m,n,x)\n\nWrapper for ``lpmn``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\n\nReturns\n-------\npm : rank-2 array('d') with bounds (m + 1,n + 1)\npd : rank-2 array('d') with bounds (m + 1,n + 1)\n"
    pass

def lpmns():
    "pm,pd = lpmns(m,n,x)\n\nWrapper for ``lpmns``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\n\nReturns\n-------\npm : rank-1 array('d') with bounds (n + 1)\npd : rank-1 array('d') with bounds (n + 1)\n"
    pass

def lpn():
    "pn,pd = lpn(n,x)\n\nWrapper for ``lpn``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\npn : rank-1 array('d') with bounds (n + 1)\npd : rank-1 array('d') with bounds (n + 1)\n"
    pass

def lpni():
    "pn,pd,pl = lpni(n,x)\n\nWrapper for ``lpni``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\npn : rank-1 array('d') with bounds (n + 1)\npd : rank-1 array('d') with bounds (n + 1)\npl : rank-1 array('d') with bounds (n + 1)\n"
    pass

def lqmn():
    "qm,qd = lqmn(m,n,x)\n\nWrapper for ``lqmn``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\n\nReturns\n-------\nqm : rank-2 array('d') with bounds (mm + 1,n + 1)\nqd : rank-2 array('d') with bounds (mm + 1,n + 1)\n"
    pass

def lqmns():
    "qm,qd = lqmns(m,n,x)\n\nWrapper for ``lqmns``.\n\nParameters\n----------\nm : input int\nn : input int\nx : input float\n\nReturns\n-------\nqm : rank-1 array('d') with bounds (n + 1)\nqd : rank-1 array('d') with bounds (n + 1)\n"
    pass

def lqna():
    "qn,qd = lqna(n,x)\n\nWrapper for ``lqna``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nqn : rank-1 array('d') with bounds (n + 1)\nqd : rank-1 array('d') with bounds (n + 1)\n"
    pass

def lqnb():
    "qn,qd = lqnb(n,x)\n\nWrapper for ``lqnb``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nqn : rank-1 array('d') with bounds (n + 1)\nqd : rank-1 array('d') with bounds (n + 1)\n"
    pass

def othpl():
    "pl,dpl = othpl(kf,n,x)\n\nWrapper for ``othpl``.\n\nParameters\n----------\nkf : input int\nn : input int\nx : input float\n\nReturns\n-------\npl : rank-1 array('d') with bounds (n + 1)\ndpl : rank-1 array('d') with bounds (n + 1)\n"
    pass

def pbdv():
    "dv,dp,pdf,pdd = pbdv(v,x)\n\nWrapper for ``pbdv``.\n\nParameters\n----------\nv : input float\nx : input float\n\nReturns\n-------\ndv : rank-1 array('d') with bounds (abs((int)v)+2)\ndp : rank-1 array('d') with bounds (abs((int)v)+2)\npdf : float\npdd : float\n"
    pass

def pbvv():
    "vv,vp,pvf,pvd = pbvv(v,x)\n\nWrapper for ``pbvv``.\n\nParameters\n----------\nv : input float\nx : input float\n\nReturns\n-------\nvv : rank-1 array('d') with bounds (abs((int)v)+2)\nvp : rank-1 array('d') with bounds (abs((int)v)+2)\npvf : float\npvd : float\n"
    pass

def rctj():
    "nm,rj,dj = rctj(n,x)\n\nWrapper for ``rctj``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nnm : int\nrj : rank-1 array('d') with bounds (n + 1)\ndj : rank-1 array('d') with bounds (n + 1)\n"
    pass

def rcty():
    "nm,ry,dy = rcty(n,x)\n\nWrapper for ``rcty``.\n\nParameters\n----------\nn : input int\nx : input float\n\nReturns\n-------\nnm : int\nry : rank-1 array('d') with bounds (n + 1)\ndy : rank-1 array('d') with bounds (n + 1)\n"
    pass

def segv():
    "cv,eg = segv(m,n,c,kd)\n\nWrapper for ``segv``.\n\nParameters\n----------\nm : input int\nn : input int\nc : input float\nkd : input int\n\nReturns\n-------\ncv : float\neg : rank-1 array('d') with bounds (n-m+2)\n"
    pass

