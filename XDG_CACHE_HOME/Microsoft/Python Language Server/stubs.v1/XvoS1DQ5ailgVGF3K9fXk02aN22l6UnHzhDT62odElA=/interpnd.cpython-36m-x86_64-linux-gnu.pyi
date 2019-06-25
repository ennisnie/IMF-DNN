import builtins as _mod_builtins

class CloughTocher2DInterpolator(NDInterpolatorBase):
    "\n    CloughTocher2DInterpolator(points, values, tol=1e-6)\n\n    Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    tol : float, optional\n        Absolute/relative tolerance for gradient estimation.\n    maxiter : int, optional\n        Maximum number of iterations in gradient estimation.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and constructing a piecewise cubic\n    interpolating Bezier polynomial on each triangle, using a\n    Clough-Tocher scheme [CT]_.  The interpolant is guaranteed to be\n    continuously differentiable.\n\n    The gradients of the interpolant are chosen so that the curvature\n    of the interpolating surface is approximatively minimized. The\n    gradients necessary for this are estimated using the global\n    algorithm described in [Nielson83,Renka84]_.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    .. [CT] See, for example,\n       P. Alfeld,\n       ''A trivariate Clough-Tocher scheme for tetrahedral data''.\n       Computer Aided Geometric Design, 1, 169 (1984);\n       G. Farin,\n       ''Triangular Bernstein-Bezier patches''.\n       Computer Aided Geometric Design, 3, 83 (1986).\n\n    .. [Nielson83] G. Nielson,\n       ''A method for interpolating scattered data based upon a minimum norm\n       network''.\n       Math. Comp., 40, 253 (1983).\n\n    .. [Renka84] R. J. Renka and A. K. Cline.\n       ''A Triangle-based C1 interpolation method.'',\n       Rocky Mountain J. Math., 14, 223 (1984).\n\n    "
    __class__ = CloughTocher2DInterpolator
    __dict__ = {}
    def __init__(self, points, values, fill_value, tol, maxiter, rescale):
        "\n    CloughTocher2DInterpolator(points, values, tol=1e-6)\n\n    Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    tol : float, optional\n        Absolute/relative tolerance for gradient estimation.\n    maxiter : int, optional\n        Maximum number of iterations in gradient estimation.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and constructing a piecewise cubic\n    interpolating Bezier polynomial on each triangle, using a\n    Clough-Tocher scheme [CT]_.  The interpolant is guaranteed to be\n    continuously differentiable.\n\n    The gradients of the interpolant are chosen so that the curvature\n    of the interpolating surface is approximatively minimized. The\n    gradients necessary for this are estimated using the global\n    algorithm described in [Nielson83,Renka84]_.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    .. [CT] See, for example,\n       P. Alfeld,\n       ''A trivariate Clough-Tocher scheme for tetrahedral data''.\n       Computer Aided Geometric Design, 1, 169 (1984);\n       G. Farin,\n       ''Triangular Bernstein-Bezier patches''.\n       Computer Aided Geometric Design, 3, 83 (1986).\n\n    .. [Nielson83] G. Nielson,\n       ''A method for interpolating scattered data based upon a minimum norm\n       network''.\n       Math. Comp., 40, 253 (1983).\n\n    .. [Renka84] R. J. Renka and A. K. Cline.\n       ''A Triangle-based C1 interpolation method.'',\n       Rocky Mountain J. Math., 14, 223 (1984).\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _do_evaluate(self, xi, dummy):
        pass
    
    def _evaluate_complex(self, xi):
        pass
    
    def _evaluate_double(self, xi):
        pass
    

class GradientEstimationWarning(_mod_builtins.Warning):
    __class__ = GradientEstimationWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'scipy.interpolate.interpnd'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class LinearNDInterpolator(NDInterpolatorBase):
    '\n    LinearNDInterpolator(points, values, fill_value=np.nan, rescale=False)\n\n    Piecewise linear interpolant in N dimensions.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and on each triangle performing linear\n    barycentric interpolation.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    '
    __class__ = LinearNDInterpolator
    __dict__ = {}
    def __init__(self, points, values, fill_value, rescale):
        '\n    LinearNDInterpolator(points, values, fill_value=np.nan, rescale=False)\n\n    Piecewise linear interpolant in N dimensions.\n\n    .. versionadded:: 0.9\n\n    Methods\n    -------\n    __call__\n\n    Parameters\n    ----------\n    points : ndarray of floats, shape (npoints, ndims); or Delaunay\n        Data point coordinates, or a precomputed Delaunay triangulation.\n    values : ndarray of float or complex, shape (npoints, ...)\n        Data values.\n    fill_value : float, optional\n        Value used to fill in for requested points outside of the\n        convex hull of the input points.  If not provided, then\n        the default is ``nan``.\n    rescale : bool, optional\n        Rescale points to unit cube before performing interpolation.\n        This is useful if some of the input dimensions have\n        incommensurable units and differ by many orders of magnitude.\n\n    Notes\n    -----\n    The interpolant is constructed by triangulating the input data\n    with Qhull [1]_, and on each triangle performing linear\n    barycentric interpolation.\n\n    References\n    ----------\n    .. [1] http://www.qhull.org/\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _do_evaluate(self, xi, dummy):
        pass
    
    def _evaluate_complex(self, xi):
        pass
    
    def _evaluate_double(self, xi):
        pass
    

class NDInterpolatorBase(_mod_builtins.object):
    '\n    Common routines for interpolators.\n\n    .. versionadded:: 0.9\n\n    '
    def __call__(self, *args):
        '\n        interpolator(xi)\n\n        Evaluate interpolator at given points.\n\n        Parameters\n        ----------\n        xi : ndarray of float, shape (..., ndim)\n            Points where to interpolate data at.\n\n        '
        pass
    
    __class__ = NDInterpolatorBase
    __dict__ = {}
    def __init__(self, points, values, fill_value, ndim, rescale, need_contiguous, need_values):
        '\n        Check shape of points and values arrays, and reshape values to\n        (npoints, nvalues).  Ensure the `points` and values arrays are\n        C-contiguous, and of correct type.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'scipy.interpolate.interpnd'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _check_call_shape(self, xi):
        pass
    
    def _scale_x(self, xi):
        pass
    

__builtins__ = {}
__doc__ = '\nSimple N-D interpolation\n\n.. versionadded:: 0.9\n\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/interpolate/interpnd.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.interpolate.interpnd'
__package__ = 'scipy.interpolate'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _ndim_coords_from_arrays():
    '\n    Convert a tuple of coordinate arrays to a (..., ndim)-shaped array.\n\n    '
    pass

def estimate_gradients_2d_global():
    pass

