__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/signal/spline.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.signal.spline'
__package__ = 'scipy.signal'
__version__ = '0.2'
def cspline2d(input, lambda_, precision):
    'cspline2d(input {, lambda, precision}) -> ck\n\n  Description:\n\n    Return the third-order B-spline coefficients over a regularly spacedi\n    input grid for the two-dimensional input image.  The lambda argument\n    specifies the amount of smoothing.  The precision argument allows specifying\n    the precision used when computing the infinite sum needed to apply mirror-\n    symmetric boundary conditions.\n'
    pass

def qspline2d(input, lambda_, precision):
    'qspline2d(input {, lambda, precision}) -> qk\n\n  Description:\n\n    Return the second-order B-spline coefficients over a regularly spaced\n    input grid for the two-dimensional input image.  The lambda argument\n    specifies the amount of smoothing.  The precision argument allows specifying\n    the precision used when computing the infinite sum needed to apply mirror-\n    symmetric boundary conditions.\n'
    pass

def sepfir2d(input, hrow, hcol):
    ' sepfir2d(input, hrow, hcol) -> output\n\n  Description:\n\n    Convolve the rank-2 input array with the separable filter defined by the\n    rank-1 arrays hrow, and hcol. Mirror symmetric boundary conditions are\n    assumed.  This function can be used to find an image given its B-spline\n    representation.'
    pass

def symiirorder1(input, c0, z1, precision):
    ' symiirorder1(input, c0, z1 {, precision}) -> output\n\n    Implement a smoothing IIR filter with mirror-symmetric boundary conditions\n    using a cascade of first-order sections.  The second section uses a\n    reversed sequence.  This implements a system with the following\n    transfer function and mirror-symmetric boundary conditions::\n\n                           c0              \n           H(z) = ---------------------    \n                   (1-z1/z) (1 - z1 z)     \n\n    The resulting signal will have mirror symmetric boundary conditions as well.\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal.\n    c0, z1 : scalar\n        Parameters in the transfer function.\n    precision :\n        Specifies the precision for calculating initial conditions\n        of the recursive filter based on mirror-symmetric input.\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.'
    pass

def symiirorder2(input, r, omega, precision):
    ' symiirorder2(input, r, omega {, precision}) -> output\n\n    Implement a smoothing IIR filter with mirror-symmetric boundary conditions\n    using a cascade of second-order sections.  The second section uses a\n    reversed sequence.  This implements the following transfer function::\n\n                                  cs^2\n         H(z) = ---------------------------------------\n                (1 - a2/z - a3/z^2) (1 - a2 z - a3 z^2 )\n\n    where::\n\n          a2 = (2 r cos omega)\n          a3 = - r^2\n          cs = 1 - 2 r cos omega + r^2\n\n    Parameters\n    ----------\n    input : ndarray\n        The input signal.\n    r, omega : scalar\n        Parameters in the transfer function.\n    precision :\n        Specifies the precision for calculating initial conditions\n        of the recursive filter based on mirror-symmetric input.\n\n    Returns\n    -------\n    output : ndarray\n        The filtered signal.'
    pass

