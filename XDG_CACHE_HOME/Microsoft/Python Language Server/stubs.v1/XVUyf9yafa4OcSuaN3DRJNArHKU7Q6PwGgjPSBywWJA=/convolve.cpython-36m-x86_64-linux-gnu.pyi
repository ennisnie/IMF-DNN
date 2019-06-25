__doc__ = "This module 'convolve' is auto-generated with f2py (version:2).\nFunctions:\n  omega = init_convolution_kernel(n,kernel_func,d=0,zero_nyquist=d%2,kernel_func_extra_args=())\n  destroy_convolve_cache()\n  y = convolve(x,omega,swap_real_imag=0,overwrite_x=0)\n  y = convolve_z(x,omega_real,omega_imag,overwrite_x=0)\n."
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/fftpack/convolve.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.fftpack.convolve'
__package__ = 'scipy.fftpack'
__version__ = b'$Revision: $'
def convolve():
    "y = convolve(x,omega,[swap_real_imag,overwrite_x])\n\nWrapper for ``convolve``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (n)\nomega : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\nswap_real_imag : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (n) and x storage\n"
    pass

def convolve_z():
    "y = convolve_z(x,omega_real,omega_imag,[overwrite_x])\n\nWrapper for ``convolve_z``.\n\nParameters\n----------\nx : input rank-1 array('d') with bounds (n)\nomega_real : input rank-1 array('d') with bounds (n)\nomega_imag : input rank-1 array('d') with bounds (n)\n\nOther Parameters\n----------------\noverwrite_x : input int, optional\n    Default: 0\n\nReturns\n-------\ny : rank-1 array('d') with bounds (n) and x storage\n"
    pass

def destroy_convolve_cache():
    'destroy_convolve_cache()\n\nWrapper for ``destroy_convolve_cache``.\n\n'
    pass

def init_convolution_kernel():
    "omega = init_convolution_kernel(n,kernel_func,[d,zero_nyquist,kernel_func_extra_args])\n\nWrapper for ``init_convolution_kernel``.\n\nParameters\n----------\nn : input int\nkernel_func : call-back function\n\nOther Parameters\n----------------\nd : input int, optional\n    Default: 0\nkernel_func_extra_args : input tuple, optional\n    Default: ()\nzero_nyquist : input int, optional\n    Default: d%2\n\nReturns\n-------\nomega : rank-1 array('d') with bounds (n)\n\nNotes\n-----\nCall-back functions::\n\n  def kernel_func(k): return kernel_func\n  Required arguments:\n    k : input int\n  Return objects:\n    kernel_func : float\n"
    pass

