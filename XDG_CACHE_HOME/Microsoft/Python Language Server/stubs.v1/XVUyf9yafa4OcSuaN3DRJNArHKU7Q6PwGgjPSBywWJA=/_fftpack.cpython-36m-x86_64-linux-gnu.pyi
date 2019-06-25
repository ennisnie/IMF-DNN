__doc__ = "This module '_fftpack' is auto-generated with f2py (version:2).\nFunctions:\n  y = zfft(x,n=size(x),direction=1,normalize=(direction<0),overwrite_x=0)\n  y = drfft(x,n=size(x),direction=1,normalize=(direction<0),overwrite_x=0)\n  y = zrfft(x,n=size(x),direction=1,normalize=(direction<0),overwrite_x=1)\n  y = zfftnd(x,s=old_shape(x,j++),direction=1,normalize=(direction<0),overwrite_x=0)\n  destroy_zfft_cache()\n  destroy_zfftnd_cache()\n  destroy_drfft_cache()\n  y = cfft(x,n=size(x),direction=1,normalize=(direction<0),overwrite_x=0)\n  y = rfft(x,n=size(x),direction=1,normalize=(direction<0),overwrite_x=0)\n  y = crfft(x,n=size(x),direction=1,normalize=(direction<0),overwrite_x=1)\n  y = cfftnd(x,s=old_shape(x,j++),direction=1,normalize=(direction<0),overwrite_x=0)\n  destroy_cfft_cache()\n  destroy_cfftnd_cache()\n  destroy_rfft_cache()\n  y = ddct1(x,n=size(x),normalize=0,overwrite_x=0)\n  y = ddct2(x,n=size(x),normalize=0,overwrite_x=0)\n  y = ddct3(x,n=size(x),normalize=0,overwrite_x=0)\n  y = ddct4(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dct1(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dct2(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dct3(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dct4(x,n=size(x),normalize=0,overwrite_x=0)\n  destroy_ddct2_cache()\n  destroy_ddct1_cache()\n  destroy_ddct4_cache()\n  destroy_dct2_cache()\n  destroy_dct1_cache()\n  destroy_dct4_cache()\n  y = ddst1(x,n=size(x),normalize=0,overwrite_x=0)\n  y = ddst2(x,n=size(x),normalize=0,overwrite_x=0)\n  y = ddst3(x,n=size(x),normalize=0,overwrite_x=0)\n  y = ddst4(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dst1(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dst2(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dst3(x,n=size(x),normalize=0,overwrite_x=0)\n  y = dst4(x,n=size(x),normalize=0,overwrite_x=0)\n  destroy_ddst2_cache()\n  destroy_ddst1_cache()\n  destroy_dst2_cache()\n  destroy_dst1_cache()\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/fftpack/_fftpack.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.fftpack._fftpack'
__package__ = 'scipy.fftpack'
__version__ = b'$Revision: $'
def cfft():
    "y = cfft(x,[n,direction,normalize,overwrite_x])\n\nWrapper for ``cfft``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def cfftnd():
    "y = cfftnd(x,[s,direction,normalize,overwrite_x])\n\nWrapper for ``cfftnd``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\ns : input rank-1 array('i') with bounds (r), optional\n    Default: old_shape(x,j++)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def crfft():
    "y = crfft(x,[n,direction,normalize,overwrite_x])\n\nWrapper for ``crfft``.\n\nParameters\n----------\nx : input rank-1 array('F') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nn : input int, optional\n    Default: size(x)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('F') with bounds (*) and x storage\n"
    pass

def dct1():
    "y = dct1(x,[n,normalize,overwrite_x])\n\nWrapper for ``dct1``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def dct2():
    "y = dct2(x,[n,normalize,overwrite_x])\n\nWrapper for ``dct2``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def dct3():
    "y = dct3(x,[n,normalize,overwrite_x])\n\nWrapper for ``dct3``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def dct4():
    "y = dct4(x,[n,normalize,overwrite_x])\n\nWrapper for ``dct4``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def ddct1():
    "y = ddct1(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddct1``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddct2():
    "y = ddct2(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddct2``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddct3():
    "y = ddct3(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddct3``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddct4():
    "y = ddct4(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddct4``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddst1():
    "y = ddst1(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddst1``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddst2():
    "y = ddst2(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddst2``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddst3():
    "y = ddst3(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddst3``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def ddst4():
    "y = ddst4(x,[n,normalize,overwrite_x])\n\nWrapper for ``ddst4``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def destroy_cfft_cache():
    'destroy_cfft_cache()\n\nWrapper for ``destroy_cfft_cache``.\n\n'
    pass

def destroy_cfftnd_cache():
    'destroy_cfftnd_cache()\n\nWrapper for ``destroy_cfftnd_cache``.\n\n'
    pass

def destroy_dct1_cache():
    'destroy_dct1_cache()\n\nWrapper for ``destroy_dct1_cache``.\n\n'
    pass

def destroy_dct2_cache():
    'destroy_dct2_cache()\n\nWrapper for ``destroy_dct2_cache``.\n\n'
    pass

def destroy_dct4_cache():
    'destroy_dct4_cache()\n\nWrapper for ``destroy_dct4_cache``.\n\n'
    pass

def destroy_ddct1_cache():
    'destroy_ddct1_cache()\n\nWrapper for ``destroy_ddct1_cache``.\n\n'
    pass

def destroy_ddct2_cache():
    'destroy_ddct2_cache()\n\nWrapper for ``destroy_ddct2_cache``.\n\n'
    pass

def destroy_ddct4_cache():
    'destroy_ddct4_cache()\n\nWrapper for ``destroy_ddct4_cache``.\n\n'
    pass

def destroy_ddst1_cache():
    'destroy_ddst1_cache()\n\nWrapper for ``destroy_ddst1_cache``.\n\n'
    pass

def destroy_ddst2_cache():
    'destroy_ddst2_cache()\n\nWrapper for ``destroy_ddst2_cache``.\n\n'
    pass

def destroy_drfft_cache():
    'destroy_drfft_cache()\n\nWrapper for ``destroy_drfft_cache``.\n\n'
    pass

def destroy_dst1_cache():
    'destroy_dst1_cache()\n\nWrapper for ``destroy_dst1_cache``.\n\n'
    pass

def destroy_dst2_cache():
    'destroy_dst2_cache()\n\nWrapper for ``destroy_dst2_cache``.\n\n'
    pass

def destroy_rfft_cache():
    'destroy_rfft_cache()\n\nWrapper for ``destroy_rfft_cache``.\n\n'
    pass

def destroy_zfft_cache():
    'destroy_zfft_cache()\n\nWrapper for ``destroy_zfft_cache``.\n\n'
    pass

def destroy_zfftnd_cache():
    'destroy_zfftnd_cache()\n\nWrapper for ``destroy_zfftnd_cache``.\n\n'
    pass

def drfft():
    "y = drfft(x,[n,direction,normalize,overwrite_x])\n\nWrapper for ``drfft``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('d') with bounds (*) and x storage\n"
    pass

def dst1():
    "y = dst1(x,[n,normalize,overwrite_x])\n\nWrapper for ``dst1``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def dst2():
    "y = dst2(x,[n,normalize,overwrite_x])\n\nWrapper for ``dst2``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def dst3():
    "y = dst3(x,[n,normalize,overwrite_x])\n\nWrapper for ``dst3``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def dst4():
    "y = dst4(x,[n,normalize,overwrite_x])\n\nWrapper for ``dst4``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\nnormalize : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def rfft():
    "y = rfft(x,[n,direction,normalize,overwrite_x])\n\nWrapper for ``rfft``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('f') with bounds (*) and x storage\n"
    pass

def zfft():
    "y = zfft(x,[n,direction,normalize,overwrite_x])\n\nWrapper for ``zfft``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nn : input int, optional\n    Default: size(x)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('D') with bounds (*) and x storage\n"
    pass

def zfftnd():
    "y = zfftnd(x,[s,direction,normalize,overwrite_x])\n\nWrapper for ``zfftnd``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\ns : input rank-1 array('i') with bounds (r), optional\n    Default: old_shape(x,j++)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('D') with bounds (*) and x storage\n"
    pass

def zrfft():
    "y = zrfft(x,[n,direction,normalize,overwrite_x])\n\nWrapper for ``zrfft``.\n\nParameters\n----------\nx : input rank-1 array('D') with bounds (*)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 1\nn : input int, optional\n    Default: size(x)\ndirection : input int, optional\n    Default: 1\nnormalize : input int, optional\n    Default: (direction<0)\n\nReturns\n-------\ny : rank-1 array('D') with bounds (*) and x storage\n"
    pass

