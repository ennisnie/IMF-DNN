__doc__ = "This module '_fblas' is auto-generated with f2py (version:2).\nFunctions:\n  c,s = srotg(a,b)\n  c,s = drotg(a,b)\n  c,s = crotg(a,b)\n  c,s = zrotg(a,b)\n  param = srotmg(d1,d2,x1,y1)\n  param = drotmg(d1,d2,x1,y1)\n  x,y = srot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = drot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = csrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = zdrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = srotm(x,y,param,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = drotm(x,y,param,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)\n  x,y = sswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  x,y = dswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  x,y = cswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  x,y = zswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  x = sscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  x = dscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  x = cscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  x = zscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  x = csscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1,overwrite_x=0)\n  x = zdscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1,overwrite_x=0)\n  y = scopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  y = dcopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  y = ccopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  y = zcopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  z = saxpy(x,y,n=(len(x)-offx)/abs(incx),a=1.0,offx=0,incx=1,offy=0,incy=1)\n  z = daxpy(x,y,n=(len(x)-offx)/abs(incx),a=1.0,offx=0,incx=1,offy=0,incy=1)\n  z = caxpy(x,y,n=(len(x)-offx)/abs(incx),a=(1.0, 0.0),offx=0,incx=1,offy=0,incy=1)\n  z = zaxpy(x,y,n=(len(x)-offx)/abs(incx),a=(1.0, 0.0),offx=0,incx=1,offy=0,incy=1)\n  xy = sdot(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  xy = ddot(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  xy = cdotu(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  xy = zdotu(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  xy = cdotc(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  xy = zdotc(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)\n  n2 = snrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  n2 = scnrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  n2 = dnrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  n2 = dznrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  s = sasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  s = scasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  s = dasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  s = dzasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  k = isamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  k = idamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  k = icamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  k = izamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)\n  y = sgemv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)\n  y = dgemv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)\n  y = cgemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)\n  y = zgemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)\n  yout = sgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,trans=0,overwrite_y=0)\n  yout = dgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,trans=0,overwrite_y=0)\n  yout = cgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,trans=0,overwrite_y=0)\n  yout = zgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,trans=0,overwrite_y=0)\n  yout = ssbmv(k,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = dsbmv(k,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = chbmv(k,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = zhbmv(k,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = sspmv(n,alpha,ap,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = dspmv(n,alpha,ap,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = cspmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = zspmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = chpmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  yout = zhpmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)\n  y = ssymv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)\n  y = dsymv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)\n  y = chemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)\n  y = zhemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)\n  a = sger(alpha,x,y,incx=1,incy=1,a=0.0,overwrite_x=1,overwrite_y=1,overwrite_a=0)\n  a = dger(alpha,x,y,incx=1,incy=1,a=0.0,overwrite_x=1,overwrite_y=1,overwrite_a=0)\n  a = cgeru(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)\n  a = zgeru(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)\n  a = cgerc(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)\n  a = zgerc(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)\n  a = ssyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)\n  a = dsyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)\n  a = csyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)\n  a = zsyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)\n  a = cher(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)\n  a = zher(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)\n  a = ssyr2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)\n  a = dsyr2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)\n  a = cher2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)\n  a = zher2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)\n  apu = sspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)\n  apu = dspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)\n  apu = cspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)\n  apu = zspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)\n  apu = chpr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)\n  apu = zhpr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)\n  apu = sspr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)\n  apu = dspr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)\n  apu = chpr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)\n  apu = zhpr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)\n  xout = stbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = dtbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ctbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ztbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = stpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = dtpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ctpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ztpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  x = strmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)\n  x = dtrmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)\n  x = ctrmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)\n  x = ztrmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = strsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = dtrsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ctrsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ztrsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = stbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = dtbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ctbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ztbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = stpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = dtpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ctpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  xout = ztpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)\n  c = sgemm(alpha,a,b,beta=0.0,c=,trans_a=0,trans_b=0,overwrite_c=0)\n  c = dgemm(alpha,a,b,beta=0.0,c=,trans_a=0,trans_b=0,overwrite_c=0)\n  c = cgemm(alpha,a,b,beta=(0.0, 0.0),c=,trans_a=0,trans_b=0,overwrite_c=0)\n  c = zgemm(alpha,a,b,beta=(0.0, 0.0),c=,trans_a=0,trans_b=0,overwrite_c=0)\n  c = ssymm(alpha,a,b,beta=0.0,c=,side=0,lower=0,overwrite_c=0)\n  c = dsymm(alpha,a,b,beta=0.0,c=,side=0,lower=0,overwrite_c=0)\n  c = csymm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)\n  c = zsymm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)\n  c = chemm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)\n  c = zhemm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)\n  c = ssyrk(alpha,a,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)\n  c = dsyrk(alpha,a,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)\n  c = csyrk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = zsyrk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = cherk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = zherk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = ssyr2k(alpha,a,b,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)\n  c = dsyr2k(alpha,a,b,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)\n  c = csyr2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = zsyr2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = cher2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  c = zher2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)\n  b = strmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  b = dtrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  b = ctrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  b = ztrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  x = strsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  x = dtrsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  x = ctrsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n  x = ztrsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/linalg/_fblas.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.linalg._fblas'
__package__ = 'scipy.linalg'
__version__ = b'$Revision: $'
def caxpy():
    "z = caxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``caxpy``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input complex, optional\n    Default: (1.0, 0.0)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('F') with bounds (*) and y storage\n"
    pass

def ccopy():
    "y = ccopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``ccopy``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('F') with bounds (*)\n"
    pass

def cdotc():
    "xy = cdotc(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``cdotc``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    pass

def cdotu():
    "xy = cdotu(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``cdotu``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    pass

def cgbmv():
    "yout = cgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``cgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    pass

def cgemm():
    "c = cgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``cgemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    pass

def cgemv():
    "y = cgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``cgemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (m,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('F') with bounds (ly)\n"
    pass

def cgerc():
    "a = cgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``cgerc``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (m)\ny : input rank-1 array('F') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('F') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (m,n)\n"
    pass

def cgeru():
    "a = cgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``cgeru``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (m)\ny : input rank-1 array('F') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('F') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (m,n)\n"
    pass

def chbmv():
    "yout = chbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``chbmv``.\n\nParameters\n----------\nk : input int\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    pass

def chemm():
    "c = chemm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``chemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    pass

def chemv():
    "y = chemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``chemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (n,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('F') with bounds (ly)\n"
    pass

def cher():
    "a = cher(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``cher``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('F') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\n"
    pass

def cher2():
    "a = cher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``cher2``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('F') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\n"
    pass

def cher2k():
    "c = cher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``cher2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    pass

def cherk():
    "c = cherk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``cherk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    pass

def chpmv():
    "yout = chpmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``chpmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    pass

def chpr():
    "apu = chpr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``chpr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('F') with bounds (*)\nap : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('F') with bounds (*) and ap storage\n"
    pass

def chpr2():
    "apu = chpr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``chpr2``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\nap : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('F') with bounds (*) and ap storage\n"
    pass

def crotg():
    'c,s = crotg(a,b)\n\nWrapper for ``crotg``.\n\nParameters\n----------\na : input complex\nb : input complex\n\nReturns\n-------\nc : complex\ns : complex\n'
    pass

def cscal():
    "x = cscal(a,x,[n,offx,incx])\n\nWrapper for ``cscal``.\n\nParameters\n----------\na : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\n"
    pass

def cspmv():
    "yout = cspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``cspmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('F') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('F') with bounds (ly) and y storage\n"
    pass

def cspr():
    "apu = cspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``cspr``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\nap : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('F') with bounds (*) and ap storage\n"
    pass

def csrot():
    "x,y = csrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``csrot``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\ny : rank-1 array('F') with bounds (*)\n"
    pass

def csscal():
    "x = csscal(a,x,[n,offx,incx,overwrite_x])\n\nWrapper for ``csscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\n"
    pass

def cswap():
    "x,y = cswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``cswap``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\ny : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\ny : rank-1 array('F') with bounds (*)\n"
    pass

def csymm():
    "c = csymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``csymm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (m,n)\n"
    pass

def csyr():
    "a = csyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``csyr``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('F') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('F') with bounds (n,n)\n"
    pass

def csyr2k():
    "c = csyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``csyr2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\nb : input rank-2 array('F') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    pass

def csyrk():
    "c = csyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``csyrk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('F') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('F') with bounds (n,n)\n"
    pass

def ctbmv():
    "xout = ctbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def ctbsv():
    "xout = ctbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('F') with bounds (lda,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def ctpmv():
    "xout = ctpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def ctpsv():
    "xout = ctpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('F') with bounds (*)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def ctrmm():
    "b = ctrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ctrmm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,k)\nb : input rank-2 array('F') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('F') with bounds (ldb,n)\n"
    pass

def ctrmv():
    "x = ctrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctrmv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('F') with bounds (*)\n"
    pass

def ctrsm():
    "x = ctrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ctrsm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('F') with bounds (lda,*)\nb : input rank-2 array('F') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('F') with bounds (ldb,n) and b storage\n"
    pass

def ctrsv():
    "xout = ctrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ctrsv``.\n\nParameters\n----------\na : input rank-2 array('F') with bounds (n,n)\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def dasum():
    "s = dasum(x,[n,offx,incx])\n\nWrapper for ``dasum``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    pass

def daxpy():
    "z = daxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``daxpy``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input float, optional\n    Default: 1.0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('d') with bounds (*) and y storage\n"
    pass

def dcopy():
    "y = dcopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``dcopy``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*)\n"
    pass

def ddot():
    "xy = ddot(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``ddot``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : float\n"
    pass

def dgbmv():
    "yout = dgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``dgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input float\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('d') with bounds (ly) and y storage\n"
    pass

def dgemm():
    "c = dgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``dgemm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nb : input rank-2 array('d') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\n"
    pass

def dgemv():
    "y = dgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``dgemv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (m,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (ly)\n"
    pass

def dger():
    "a = dger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``dger``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('d') with bounds (m)\ny : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('d') with bounds (m,n), optional\n    Default: 0.0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (m,n)\n"
    pass

def dnrm2():
    "n2 = dnrm2(x,[n,offx,incx])\n\nWrapper for ``dnrm2``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    pass

def drot():
    "x,y = drot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``drot``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\ny : rank-1 array('d') with bounds (*)\n"
    pass

def drotg():
    'c,s = drotg(a,b)\n\nWrapper for ``drotg``.\n\nParameters\n----------\na : input float\nb : input float\n\nReturns\n-------\nc : float\ns : float\n'
    pass

def drotm():
    "x,y = drotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``drotm``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\nparam : input rank-1 array('d') with bounds (5)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\ny : rank-1 array('d') with bounds (*)\n"
    pass

def drotmg():
    "param = drotmg(d1,d2,x1,y1)\n\nWrapper for ``drotmg``.\n\nParameters\n----------\nd1 : input float\nd2 : input float\nx1 : input float\ny1 : input float\n\nReturns\n-------\nparam : rank-1 array('d') with bounds (5)\n"
    pass

def dsbmv():
    "yout = dsbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``dsbmv``.\n\nParameters\n----------\nk : input int\nalpha : input float\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('d') with bounds (ly) and y storage\n"
    pass

def dscal():
    "x = dscal(a,x,[n,offx,incx])\n\nWrapper for ``dscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\n"
    pass

def dspmv():
    "yout = dspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``dspmv``.\n\nParameters\n----------\nn : input int\nalpha : input float\nap : input rank-1 array('d') with bounds (*)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('d') with bounds (ly) and y storage\n"
    pass

def dspr():
    "apu = dspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``dspr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\nap : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('d') with bounds (*) and ap storage\n"
    pass

def dspr2():
    "apu = dspr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``dspr2``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\nap : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('d') with bounds (*) and ap storage\n"
    pass

def dswap():
    "x,y = dswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``dswap``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\ny : rank-1 array('d') with bounds (*)\n"
    pass

def dsymm():
    "c = dsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``dsymm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nb : input rank-2 array('d') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (m,n)\n"
    pass

def dsymv():
    "y = dsymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``dsymv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (n,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('d') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (ly)\n"
    pass

def dsyr():
    "a = dsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``dsyr``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('d') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\n"
    pass

def dsyr2():
    "a = dsyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``dsyr2``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('d') with bounds (*)\ny : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('d') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('d') with bounds (n,n)\n"
    pass

def dsyr2k():
    "c = dsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``dsyr2k``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\nb : input rank-2 array('d') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n)\n"
    pass

def dsyrk():
    "c = dsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``dsyrk``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('d') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('d') with bounds (n,n)\n"
    pass

def dtbmv():
    "xout = dtbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def dtbsv():
    "xout = dtbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('d') with bounds (lda,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def dtpmv():
    "xout = dtpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (*)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def dtpsv():
    "xout = dtpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('d') with bounds (*)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def dtrmm():
    "b = dtrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``dtrmm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,k)\nb : input rank-2 array('d') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('d') with bounds (ldb,n)\n"
    pass

def dtrmv():
    "x = dtrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtrmv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('d') with bounds (*)\n"
    pass

def dtrsm():
    "x = dtrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``dtrsm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('d') with bounds (lda,*)\nb : input rank-2 array('d') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('d') with bounds (ldb,n) and b storage\n"
    pass

def dtrsv():
    "xout = dtrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``dtrsv``.\n\nParameters\n----------\na : input rank-2 array('d') with bounds (n,n)\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def dzasum():
    "s = dzasum(x,[n,offx,incx])\n\nWrapper for ``dzasum``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    pass

def dznrm2():
    "n2 = dznrm2(x,[n,offx,incx])\n\nWrapper for ``dznrm2``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    pass

def icamax():
    "k = icamax(x,[n,offx,incx])\n\nWrapper for ``icamax``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    pass

def idamax():
    "k = idamax(x,[n,offx,incx])\n\nWrapper for ``idamax``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    pass

def isamax():
    "k = isamax(x,[n,offx,incx])\n\nWrapper for ``isamax``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    pass

def izamax():
    "k = izamax(x,[n,offx,incx])\n\nWrapper for ``izamax``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nk : int\n"
    pass

def sasum():
    "s = sasum(x,[n,offx,incx])\n\nWrapper for ``sasum``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    pass

def saxpy():
    "z = saxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``saxpy``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input float, optional\n    Default: 1.0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('f') with bounds (*) and y storage\n"
    pass

def scasum():
    "s = scasum(x,[n,offx,incx])\n\nWrapper for ``scasum``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\ns : float\n"
    pass

def scnrm2():
    "n2 = scnrm2(x,[n,offx,incx])\n\nWrapper for ``scnrm2``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    pass

def scopy():
    "y = scopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``scopy``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*)\n"
    pass

def sdot():
    "xy = sdot(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``sdot``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : float\n"
    pass

def sgbmv():
    "yout = sgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``sgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input float\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('f') with bounds (ly) and y storage\n"
    pass

def sgemm():
    "c = sgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``sgemm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nb : input rank-2 array('f') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\n"
    pass

def sgemv():
    "y = sgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``sgemv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (m,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (ly)\n"
    pass

def sger():
    "a = sger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``sger``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('f') with bounds (m)\ny : input rank-1 array('f') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('f') with bounds (m,n), optional\n    Default: 0.0\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (m,n)\n"
    pass

def snrm2():
    "n2 = snrm2(x,[n,offx,incx])\n\nWrapper for ``snrm2``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nn2 : float\n"
    pass

def srot():
    "x,y = srot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``srot``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\ny : rank-1 array('f') with bounds (*)\n"
    pass

def srotg():
    'c,s = srotg(a,b)\n\nWrapper for ``srotg``.\n\nParameters\n----------\na : input float\nb : input float\n\nReturns\n-------\nc : float\ns : float\n'
    pass

def srotm():
    "x,y = srotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``srotm``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\nparam : input rank-1 array('f') with bounds (5)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\ny : rank-1 array('f') with bounds (*)\n"
    pass

def srotmg():
    "param = srotmg(d1,d2,x1,y1)\n\nWrapper for ``srotmg``.\n\nParameters\n----------\nd1 : input float\nd2 : input float\nx1 : input float\ny1 : input float\n\nReturns\n-------\nparam : rank-1 array('f') with bounds (5)\n"
    pass

def ssbmv():
    "yout = ssbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``ssbmv``.\n\nParameters\n----------\nk : input int\nalpha : input float\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('f') with bounds (ly) and y storage\n"
    pass

def sscal():
    "x = sscal(a,x,[n,offx,incx])\n\nWrapper for ``sscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\n"
    pass

def sspmv():
    "yout = sspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``sspmv``.\n\nParameters\n----------\nn : input int\nalpha : input float\nap : input rank-1 array('f') with bounds (*)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('f') with bounds (ly) and y storage\n"
    pass

def sspr():
    "apu = sspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``sspr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\nap : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('f') with bounds (*) and ap storage\n"
    pass

def sspr2():
    "apu = sspr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``sspr2``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\nap : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('f') with bounds (*) and ap storage\n"
    pass

def sswap():
    "x,y = sswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``sswap``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\ny : rank-1 array('f') with bounds (*)\n"
    pass

def ssymm():
    "c = ssymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``ssymm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nb : input rank-2 array('f') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (m,n)\n"
    pass

def ssymv():
    "y = ssymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``ssymv``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (n,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\ny : input rank-1 array('f') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (ly)\n"
    pass

def ssyr():
    "a = ssyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``ssyr``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('f') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\n"
    pass

def ssyr2():
    "a = ssyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``ssyr2``.\n\nParameters\n----------\nalpha : input float\nx : input rank-1 array('f') with bounds (*)\ny : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('f') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('f') with bounds (n,n)\n"
    pass

def ssyr2k():
    "c = ssyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``ssyr2k``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\nb : input rank-2 array('f') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n)\n"
    pass

def ssyrk():
    "c = ssyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``ssyrk``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input float, optional\n    Default: 0.0\nc : input rank-2 array('f') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('f') with bounds (n,n)\n"
    pass

def stbmv():
    "xout = stbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def stbsv():
    "xout = stbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('f') with bounds (lda,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def stpmv():
    "xout = stpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (*)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def stpsv():
    "xout = stpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``stpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('f') with bounds (*)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def strmm():
    "b = strmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``strmm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,k)\nb : input rank-2 array('f') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('f') with bounds (ldb,n)\n"
    pass

def strmv():
    "x = strmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``strmv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('f') with bounds (*)\n"
    pass

def strsm():
    "x = strsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``strsm``.\n\nParameters\n----------\nalpha : input float\na : input rank-2 array('f') with bounds (lda,*)\nb : input rank-2 array('f') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('f') with bounds (ldb,n) and b storage\n"
    pass

def strsv():
    "xout = strsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``strsv``.\n\nParameters\n----------\na : input rank-2 array('f') with bounds (n,n)\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def zaxpy():
    "z = zaxpy(x,y,[n,a,offx,incx,offy,incy])\n\nWrapper for ``zaxpy``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\na : input complex, optional\n    Default: (1.0, 0.0)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nz : rank-1 array('D') with bounds (*) and y storage\n"
    pass

def zcopy():
    "y = zcopy(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zcopy``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\ny : rank-1 array('D') with bounds (*)\n"
    pass

def zdotc():
    "xy = zdotc(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zdotc``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    pass

def zdotu():
    "xy = zdotu(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zdotu``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nxy : complex\n"
    pass

def zdrot():
    "x,y = zdrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])\n\nWrapper for ``zdrot``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\nc : input float\ns : input float\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 0\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\ny : rank-1 array('D') with bounds (*)\n"
    pass

def zdscal():
    "x = zdscal(a,x,[n,offx,incx,overwrite_x])\n\nWrapper for ``zdscal``.\n\nParameters\n----------\na : input float\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\n"
    pass

def zgbmv():
    "yout = zgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])\n\nWrapper for ``zgbmv``.\n\nParameters\n----------\nm : input int\nn : input int\nkl : input int\nku : input int\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    pass

def zgemm():
    "c = zgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])\n\nWrapper for ``zgemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ntrans_b : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    pass

def zgemv():
    "y = zgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])\n\nWrapper for ``zgemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (m,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\ntrans : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('D') with bounds (ly)\n"
    pass

def zgerc():
    "a = zgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``zgerc``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (m)\ny : input rank-1 array('D') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('D') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (m,n)\n"
    pass

def zgeru():
    "a = zgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])\n\nWrapper for ``zgeru``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (m)\ny : input rank-1 array('D') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nincx : input int, optional\n    Default: 1\noverwrite_y : input int, optional\n    Default: 1\nincy : input int, optional\n    Default: 1\na : input rank-2 array('D') with bounds (m,n), optional\n    Default: (0.0,0.0)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (m,n)\n"
    pass

def zhbmv():
    "yout = zhbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``zhbmv``.\n\nParameters\n----------\nk : input int\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    pass

def zhemm():
    "c = zhemm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``zhemm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    pass

def zhemv():
    "y = zhemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])\n\nWrapper for ``zhemv``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (n,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('D') with bounds (ly)\n"
    pass

def zher():
    "a = zher(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``zher``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('D') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\n"
    pass

def zher2():
    "a = zher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])\n\nWrapper for ``zher2``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nn : input int, optional\n    Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)\na : input rank-2 array('D') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\n"
    pass

def zher2k():
    "c = zher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zher2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    pass

def zherk():
    "c = zherk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zherk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    pass

def zhpmv():
    "yout = zhpmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``zhpmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    pass

def zhpr():
    "apu = zhpr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``zhpr``.\n\nParameters\n----------\nn : input int\nalpha : input float\nx : input rank-1 array('D') with bounds (*)\nap : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('D') with bounds (*) and ap storage\n"
    pass

def zhpr2():
    "apu = zhpr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])\n\nWrapper for ``zhpr2``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\nap : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('D') with bounds (*) and ap storage\n"
    pass

def zrotg():
    'c,s = zrotg(a,b)\n\nWrapper for ``zrotg``.\n\nParameters\n----------\na : input complex\nb : input complex\n\nReturns\n-------\nc : complex\ns : complex\n'
    pass

def zscal():
    "x = zscal(a,x,[n,offx,incx])\n\nWrapper for ``zscal``.\n\nParameters\n----------\na : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\n"
    pass

def zspmv():
    "yout = zspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])\n\nWrapper for ``zspmv``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nbeta : input complex, optional\n    Default: (0.0, 0.0)\ny : input rank-1 array('D') with bounds (ly)\noverwrite_y : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nyout : rank-1 array('D') with bounds (ly) and y storage\n"
    pass

def zspr():
    "apu = zspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])\n\nWrapper for ``zspr``.\n\nParameters\n----------\nn : input int\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\nap : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\noverwrite_ap : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\napu : rank-1 array('D') with bounds (*) and ap storage\n"
    pass

def zswap():
    "x,y = zswap(x,y,[n,offx,incx,offy,incy])\n\nWrapper for ``zswap``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\ny : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nn : input int, optional\n    Default: (len(x)-offx)/abs(incx)\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffy : input int, optional\n    Default: 0\nincy : input int, optional\n    Default: 1\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\ny : rank-1 array('D') with bounds (*)\n"
    pass

def zsymm():
    "c = zsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])\n\nWrapper for ``zsymm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (m,n)\noverwrite_c : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (m,n)\n"
    pass

def zsyr():
    "a = zsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])\n\nWrapper for ``zsyr``.\n\nParameters\n----------\nalpha : input complex\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\nlower : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nn : input int, optional\n    Default: (len(x)-1-offx)/abs(incx)+1\na : input rank-2 array('D') with bounds (n,n)\noverwrite_a : input int, optional\n    Default: 0\n\nReturns\n-------\na : rank-2 array('D') with bounds (n,n)\n"
    pass

def zsyr2k():
    "c = zsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zsyr2k``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\nb : input rank-2 array('D') with bounds (ldb,kb)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    pass

def zsyrk():
    "c = zsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])\n\nWrapper for ``zsyrk``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,ka)\n\nOther Parameters\n----------------\nbeta : input complex, optional\n    Default: (0.0, 0.0)\nc : input rank-2 array('D') with bounds (n,n)\noverwrite_c : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\n\nReturns\n-------\nc : rank-2 array('D') with bounds (n,n)\n"
    pass

def ztbmv():
    "xout = ztbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztbmv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    pass

def ztbsv():
    "xout = ztbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztbsv``.\n\nParameters\n----------\nk : input int\na : input rank-2 array('D') with bounds (lda,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    pass

def ztpmv():
    "xout = ztpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztpmv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    pass

def ztpsv():
    "xout = ztpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztpsv``.\n\nParameters\n----------\nn : input int\nap : input rank-1 array('D') with bounds (*)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    pass

def ztrmm():
    "b = ztrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ztrmm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,k)\nb : input rank-2 array('D') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nb : rank-2 array('D') with bounds (ldb,n)\n"
    pass

def ztrmv():
    "x = ztrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztrmv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\noffx : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-1 array('D') with bounds (*)\n"
    pass

def ztrsm():
    "x = ztrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])\n\nWrapper for ``ztrsm``.\n\nParameters\n----------\nalpha : input complex\na : input rank-2 array('D') with bounds (lda,*)\nb : input rank-2 array('D') with bounds (ldb,n)\n\nOther Parameters\n----------------\noverwrite_b : input int, optional\n    Default: 0\nside : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans_a : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nx : rank-2 array('D') with bounds (ldb,n) and b storage\n"
    pass

def ztrsv():
    "xout = ztrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])\n\nWrapper for ``ztrsv``.\n\nParameters\n----------\na : input rank-2 array('D') with bounds (n,n)\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nincx : input int, optional\n    Default: 1\noffx : input int, optional\n    Default: 0\nlower : input int, optional\n    Default: 0\ntrans : input int, optional\n    Default: 0\ndiag : input int, optional\n    Default: 0\n\nReturns\n-------\nxout : rank-1 array('D') with bounds (*) and x storage\n"
    pass

