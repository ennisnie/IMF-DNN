import builtins as _mod_builtins
import scipy.interpolate.polyint as _mod_scipy_interpolate_polyint

_Interpolator1D = _mod_scipy_interpolate_polyint._Interpolator1D
__builtins__ = {}
__doc__ = '\nRoutines for evaluating and manipulating piecewise polynomials in\nlocal power basis.\n\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/interpolate/_ppoly.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.interpolate._ppoly'
__package__ = 'scipy.interpolate'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _croots_poly1():
    '\n    Find roots of polynomials.\n\n    This function is for testing croots_poly1\n\n    Parameters\n    ----------\n    c : ndarray, (k, m, n)\n        Coefficients of several order-k polynomials\n    w : ndarray, (k, m, n)\n        Output argument --- roots of the polynomials.\n\n    '
    pass

def evaluate(c, x, xp, dx, extrapolate, out):
    '\n    Evaluate a piecewise polynomial.\n\n    Parameters\n    ----------\n    c : ndarray, shape (k, m, n)\n        Coefficients local polynomials of order `k-1` in `m` intervals.\n        There are `n` polynomials in each interval.\n        Coefficient of highest order-term comes first.\n    x : ndarray, shape (m+1,)\n        Breakpoints of polynomials.\n    xp : ndarray, shape (r,)\n        Points to evaluate the piecewise polynomial at.\n    dx : int\n        Order of derivative to evaluate.  The derivative is evaluated\n        piecewise and may have discontinuities.\n    extrapolate : bint\n        Whether to extrapolate to out-of-bounds points based on first\n        and last intervals, or to return NaNs.\n    out : ndarray, shape (r, n)\n        Value of each polynomial at each of the input points.\n        This argument is modified in-place.\n\n    '
    pass

def evaluate_bernstein(c, x, xp, nu, extrapolate, out):
    '\n    Evaluate a piecewise polynomial in the Bernstein basis.\n\n    Parameters\n    ----------\n    c : ndarray, shape (k, m, n)\n        Coefficients local polynomials of order `k-1` in `m` intervals.\n        There are `n` polynomials in each interval.\n        Coefficient of highest order-term comes first.\n    x : ndarray, shape (m+1,)\n        Breakpoints of polynomials\n    xp : ndarray, shape (r,)\n        Points to evaluate the piecewise polynomial at.\n    nu : int\n        Order of derivative to evaluate.  The derivative is evaluated\n        piecewise and may have discontinuities.\n    extrapolate : bint, optional\n        Whether to extrapolate to out-of-bounds points based on first\n        and last intervals, or to return NaNs.\n    out : ndarray, shape (r, n)\n        Value of each polynomial at each of the input points.\n        This argument is modified in-place.\n\n    '
    pass

def evaluate_nd(c, xs, ks, xp, dx, extrapolate, out):
    '\n    Evaluate a piecewise tensor-product polynomial.\n\n    Parameters\n    ----------\n    c : ndarray, shape (k_1*...*k_d, m_1*...*m_d, n)\n        Coefficients local polynomials of order `k-1` in\n        `m_1`, ..., `m_d` intervals. There are `n` polynomials\n        in each interval.\n    ks : ndarray of int, shape (d,)\n        Orders of polynomials in each dimension\n    xs : d-tuple of ndarray of shape (m_d+1,) each\n        Breakpoints of polynomials\n    xp : ndarray, shape (r, d)\n        Points to evaluate the piecewise polynomial at.\n    dx : ndarray of int, shape (d,)\n        Orders of derivative to evaluate.  The derivative is evaluated\n        piecewise and may have discontinuities.\n    extrapolate : int, optional\n        Whether to extrapolate to out-of-bounds points based on first\n        and last intervals, or to return NaNs.\n    out : ndarray, shape (r, n)\n        Value of each polynomial at each of the input points.\n        For points outside the span ``x[0] ... x[-1]``,\n        ``nan`` is returned.\n        This argument is modified in-place.\n\n    '
    pass

def fix_continuity(c, x, order):
    '\n    Make a piecewise polynomial continuously differentiable to given order.\n\n    Parameters\n    ----------\n    c : ndarray, shape (k, m, n)\n        Coefficients local polynomials of order `k-1` in `m` intervals.\n        There are `n` polynomials in each interval.\n        Coefficient of highest order-term comes first.\n\n        Coefficients c[-order-1:] are modified in-place.\n    x : ndarray, shape (m+1,)\n        Breakpoints of polynomials\n    order : int\n        Order up to which enforce piecewise differentiability.\n\n    '
    pass

def integrate(c, x, a, b, extrapolate, out):
    '\n    Compute integral over a piecewise polynomial.\n\n    Parameters\n    ----------\n    c : ndarray, shape (k, m, n)\n        Coefficients local polynomials of order `k-1` in `m` intervals.\n    x : ndarray, shape (m+1,)\n        Breakpoints of polynomials\n    a : double\n        Start point of integration.\n    b : double\n        End point of integration.\n    extrapolate : bint, optional\n        Whether to extrapolate to out-of-bounds points based on first\n        and last intervals, or to return NaNs.\n    out : ndarray, shape (n,)\n        Integral of the piecewise polynomial, assuming the polynomial\n        is zero outside the range (x[0], x[-1]).\n        This argument is modified in-place.\n\n    '
    pass

def real_roots():
    '\n    Compute real roots of a real-valued piecewise polynomial function.\n\n    If a section of the piecewise polynomial is identically zero, the\n    values (x[begin], nan) are appended to the root list.\n\n    If the piecewise polynomial is not continuous, and the sign\n    changes across a breakpoint, the breakpoint is added to the root\n    set if `report_discont` is True.\n\n    Parameters\n    ----------\n    c, x\n        Polynomial coefficients, as above\n    y : float\n        Find roots of ``pp(x) == y``.\n    report_discont : bint, optional\n        Whether to report discontinuities across zero at breakpoints\n        as roots\n    extrapolate : bint, optional\n        Whether to consider roots obtained by extrapolating based\n        on first and last intervals.\n\n    '
    pass

