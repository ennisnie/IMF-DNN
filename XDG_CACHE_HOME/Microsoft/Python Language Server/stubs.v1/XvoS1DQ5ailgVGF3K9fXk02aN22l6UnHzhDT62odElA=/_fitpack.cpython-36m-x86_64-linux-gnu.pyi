__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/interpolate/_fitpack.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.interpolate._fitpack'
__package__ = 'scipy.interpolate'
__version__ = ' 1.7 '
def _bispev():
    ' [z,ier] = _bispev(tx,ty,c,kx,ky,x,y,nux,nuy)'
    pass

def _bspldismat():
    'B = _bspldismat(order,xk)\nConstruct the kth derivative discontinuity jump constraint matrix \nfor spline fitting of order k given sample positions in xk.\n\nIf xk is an integer (N+1), then the result is equivalent to\nxk=arange(N+1)+x0 for any value of x0.   This produces the\ninteger-spaced matrix a bit faster.  If xk is a 2-tuple (N+1,dx)\nthen it produces the result as if the sample distance were dx'
    pass

def _bspleval():
    'y = _bspleval(xx,xk,coef,k,{deriv (0)})\n\nThe spline is defined by the approximation interval xk[0] to xk[-1],\nthe length of xk (N+1), the order of the spline, k, and \nthe number of coeficients N+k.  The coefficients range from xk_{-K}\nto xk_{N-1} inclusive and are all the coefficients needed to define\nan arbitrary spline of order k, on the given approximation interval\n\nExtra knot points are internally added using knot-point symmetry \naround xk[0] and xk[-1]'
    pass

def _bsplmat():
    'B = _bsplmat(order,xk)\nConstruct the constraint matrix for spline fitting of order k\ngiven sample positions in xk.\n\nIf xk is an integer (N+1), then the result is equivalent to\nxk=arange(N+1)+x0 for any value of x0.   This produces the\ninteger-spaced, or cardinal spline matrix a bit faster.'
    pass

def _curfit():
    ' [t,c,o] = _curfit(x,y,w,xb,xe,k,iopt,s,t,nest,wrk,iwrk,per)'
    pass

def _insert():
    ' [tt,cc,ier] = _insert(iopt,t,c,k,x,m)'
    pass

def _parcur():
    ' [t,c,o] = _parcur(x,w,u,ub,ue,k,iopt,ipar,s,t,nest,wrk,iwrk,per)'
    pass

def _spalde():
    ' [d,ier] = _spalde(t,c,k,x)'
    pass

def _spl_():
    ' [y,ier] = _spl_(x,nu,t,c,k,e)'
    pass

def _splint():
    ' [aint,wrk] = _splint(t,c,k,a,b)'
    pass

def _sproot():
    ' [z,ier] = _sproot(t,c,k,mest)'
    pass

def _surfit():
    ' [tx,ty,c,o] = _surfit(x, y, z, w, xb, xe, yb, ye, kx,ky,iopt,s,eps,tx,ty,nxest,nyest,wrk,lwrk1,lwrk2)'
    pass

