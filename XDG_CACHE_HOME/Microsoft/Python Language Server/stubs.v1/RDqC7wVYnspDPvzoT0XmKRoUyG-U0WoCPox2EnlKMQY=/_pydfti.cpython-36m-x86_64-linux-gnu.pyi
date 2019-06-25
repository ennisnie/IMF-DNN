import _thread as _mod__thread
import builtins as _mod_builtins

def Lock():
    'allocate_lock() -> lock object\n(allocate() is an obsolete synonym)\n\nCreate a new lock object. See help(type(threading.Lock())) for\ninformation about locks.'
    pass

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/mkl_fft/_pydfti.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'mkl_fft._pydfti'
__package__ = 'mkl_fft'
__test__ = _mod_builtins.dict()
def _check_shapes_for_direct():
    pass

def _cook_nd_args():
    pass

def _direct_fftnd():
    'Perform n-dimensional FFT over all axes'
    pass

def _fft1d_impl():
    '\n    Uses MKL to perform 1D FFT on the input array x along the given axis.\n    '
    pass

def _fftnd_impl():
    pass

def _fix_dimensions():
    'Pads array arr with zeros to attain shape s associated with axes'
    pass

def _init_nd_shape_and_axes():
    'Handle shape and axes arguments for n-dimensional transforms.\n    Returns the shape and axes in a standard form, taking into account negative\n    values and checking for various potential errors.\n    Parameters\n    ----------\n    x : array_like\n        The input array.\n    shape : int or array_like of ints or None\n        The shape of the result.  If both `shape` and `axes` (see below) are\n        None, `shape` is ``x.shape``; if `shape` is None but `axes` is\n        not None, then `shape` is ``scipy.take(x.shape, axes, axis=0)``.\n        If `shape` is -1, the size of the corresponding dimension of `x` is\n        used.\n    axes : int or array_like of ints or None\n        Axes along which the calculation is computed.\n        The default is over all axes.\n        Negative indices are automatically converted to their positive\n        counterpart.\n    Returns\n    -------\n    shape : array\n        The shape of the result. It is a 1D integer array.\n    axes : array\n        The shape of the result. It is a 1D integer array.\n    '
    pass

def _iter_fftnd():
    pass

_lock = _mod__thread.lock()
def _rc_fft1d_impl():
    '\n    Uses MKL to perform 1D FFT on the real input array x along the given axis,\n    producing complex output, but giving only half of the harmonics.\n\n    cf. numpy.fft.rfft\n    '
    pass

def _rc_ifft1d_impl():
    '\n    Uses MKL to perform 1D FFT on the real input array x along the given axis,\n    producing complex output, but giving only half of the harmonics.\n\n    cf. numpy.fft.rfft\n    '
    pass

def _remove_axis():
    pass

def _rrfft1d_impl():
    '\n    Uses MKL to perform real packed 1D FFT on the input array x along the given axis.\n    '
    pass

def fft():
    pass

def fft2():
    pass

def fftn():
    pass

def ifft():
    pass

def ifft2():
    pass

def ifftn():
    pass

def internal_overlap():
    pass

def irfft():
    'Inverse FFT of a real sequence, takes packed real-valued harmonics of FFT'
    pass

def irfft2_numpy():
    pass

def irfft_numpy():
    pass

def irfftn_numpy():
    pass

def rfft():
    'Packed real-valued harmonics of FFT of a real sequence x'
    pass

def rfft2_numpy():
    pass

def rfft_numpy():
    pass

def rfftn_numpy():
    pass

