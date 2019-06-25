import builtins as _mod_builtins

class FixedWindowIndexer(WindowIndexer):
    '\n    create a fixed length window indexer object\n    that has start & end, that point to offsets in\n    the index object; these are defined based on the win\n    arguments\n\n    Parameters\n    ----------\n    values: ndarray\n        values data array\n    win: int64_t\n        window size\n    minp: int64_t\n        min number of obs in a window to consider non-NaN\n    index: object\n        index of the values\n    floor: optional\n        unit for flooring the unit\n    left_closed: bint\n        left endpoint closedness\n    right_closed: bint\n        right endpoint closedness\n\n    '
    __class__ = FixedWindowIndexer
    def __init__(self, *args, **kwargs):
        '\n    create a fixed length window indexer object\n    that has start & end, that point to offsets in\n    the index object; these are defined based on the win\n    arguments\n\n    Parameters\n    ----------\n    values: ndarray\n        values data array\n    win: int64_t\n        window size\n    minp: int64_t\n        min number of obs in a window to consider non-NaN\n    index: object\n        index of the values\n    floor: optional\n        unit for flooring the unit\n    left_closed: bint\n        left endpoint closedness\n    right_closed: bint\n        right endpoint closedness\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class MockFixedWindowIndexer(WindowIndexer):
    '\n\n    We are just checking parameters of the indexer,\n    and returning a consistent API with fixed/variable\n    indexers.\n\n    Parameters\n    ----------\n    values: ndarray\n        values data array\n    win: int64_t\n        window size\n    minp: int64_t\n        min number of obs in a window to consider non-NaN\n    index: object\n        index of the values\n    floor: optional\n        unit for flooring\n    left_closed: bint\n        left endpoint closedness\n    right_closed: bint\n        right endpoint closedness\n\n    '
    __class__ = MockFixedWindowIndexer
    def __init__(self, *args, **kwargs):
        '\n\n    We are just checking parameters of the indexer,\n    and returning a consistent API with fixed/variable\n    indexers.\n\n    Parameters\n    ----------\n    values: ndarray\n        values data array\n    win: int64_t\n        window size\n    minp: int64_t\n        min number of obs in a window to consider non-NaN\n    index: object\n        index of the values\n    floor: optional\n        unit for flooring\n    left_closed: bint\n        left endpoint closedness\n    right_closed: bint\n        right endpoint closedness\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class VariableWindowIndexer(WindowIndexer):
    '\n    create a variable length window indexer object\n    that has start & end, that point to offsets in\n    the index object; these are defined based on the win\n    arguments\n\n    Parameters\n    ----------\n    values: ndarray\n        values data array\n    win: int64_t\n        window size\n    minp: int64_t\n        min number of obs in a window to consider non-NaN\n    index: ndarray\n        index of the values\n    left_closed: bint\n        left endpoint closedness\n        True if the left endpoint is closed, False if open\n    right_closed: bint\n        right endpoint closedness\n        True if the right endpoint is closed, False if open\n    floor: optional\n        unit for flooring the unit\n    '
    __class__ = VariableWindowIndexer
    def __init__(self, *args, **kwargs):
        '\n    create a variable length window indexer object\n    that has start & end, that point to offsets in\n    the index object; these are defined based on the win\n    arguments\n\n    Parameters\n    ----------\n    values: ndarray\n        values data array\n    win: int64_t\n        window size\n    minp: int64_t\n        min number of obs in a window to consider non-NaN\n    index: ndarray\n        index of the values\n    left_closed: bint\n        left endpoint closedness\n        True if the left endpoint is closed, False if open\n    right_closed: bint\n        right endpoint closedness\n        True if the right endpoint is closed, False if open\n    floor: optional\n        unit for flooring the unit\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def build(self):
        pass
    

class WindowIndexer(_mod_builtins.object):
    __class__ = WindowIndexer
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_data(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/window.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.window'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_FixedWindowIndexer():
    pass

def __pyx_unpickle_MockFixedWindowIndexer():
    pass

def __pyx_unpickle_VariableWindowIndexer():
    pass

def __pyx_unpickle_WindowIndexer():
    pass

__test__ = _mod_builtins.dict()
def _check_minp():
    '\n    Parameters\n    ----------\n    win: int\n    minp: int or None\n    N: len of window\n    floor: int, optional\n        default 1\n\n    Returns\n    -------\n    minimum period\n    '
    pass

def ewma():
    '\n    Compute exponentially-weighted moving average using center-of-mass.\n\n    Parameters\n    ----------\n    vals : ndarray (float64 type)\n    com : float64\n    adjust: int\n    ignore_na: int\n    minp: int\n\n    Returns\n    -------\n    y : ndarray\n    '
    pass

def ewmcov():
    '\n    Compute exponentially-weighted moving variance using center-of-mass.\n\n    Parameters\n    ----------\n    input_x : ndarray (float64 type)\n    input_y : ndarray (float64 type)\n    com : float64\n    adjust: int\n    ignore_na: int\n    minp: int\n    bias: int\n\n    Returns\n    -------\n    y : ndarray\n    '
    pass

def get_window_indexer():
    "\n    return the correct window indexer for the computation\n\n    Parameters\n    ----------\n    values: 1d ndarray\n    win: integer, window size\n    minp: integer, minimum periods\n    index: 1d ndarray, optional\n        index to the values array\n    closed: string, default None\n        {'right', 'left', 'both', 'neither'}\n        window endpoint closedness. Defaults to 'right' in\n        VariableWindowIndexer and to 'both' in FixedWindowIndexer\n    floor: optional\n        unit for flooring the unit\n    use_mock: boolean, default True\n        if we are a fixed indexer, return a mock indexer\n        instead of the FixedWindow Indexer. This is a type\n        compat Indexer that allows us to use a standard\n        code path with all of the indexers.\n\n\n    Returns\n    -------\n    tuple of 1d int64 ndarrays of the offsets & data about the window\n\n    "
    pass

interpolation_types = _mod_builtins.dict()
def roll_count():
    pass

def roll_generic():
    pass

def roll_kurt():
    pass

def roll_max(values, win, minp, index, closed):
    "\n    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values: numpy array\n    window: int, size of rolling window\n    minp: if number of observations in window\n          is below this, output a NaN\n    index: ndarray, optional\n       index for window computation\n    closed: 'right', 'left', 'both', 'neither'\n            make the interval closed on the right, left,\n            both or neither endpoints\n    "
    pass

def roll_mean():
    pass

def roll_median_c():
    pass

def roll_min(values, win, minp, index, closed):
    '\n    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values: numpy array\n    window: int, size of rolling window\n    minp: if number of observations in window\n          is below this, output a NaN\n    index: ndarray, optional\n       index for window computation\n    '
    pass

def roll_quantile():
    '\n    O(N log(window)) implementation using skip list\n    '
    pass

def roll_skew():
    pass

def roll_sum():
    pass

def roll_var():
    "\n    Numerically stable implementation using Welford's method.\n    "
    pass

def roll_window():
    '\n    Assume len(weights) << len(values)\n    '
    pass

