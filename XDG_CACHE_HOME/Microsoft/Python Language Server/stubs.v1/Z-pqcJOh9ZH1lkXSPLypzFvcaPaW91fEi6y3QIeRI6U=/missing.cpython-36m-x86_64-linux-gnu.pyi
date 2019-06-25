import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/missing.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.missing'
__package__ = 'pandas._libs'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def checknull():
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def checknull_old():
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def isnaobj():
    '\n    Return boolean mask denoting which elements of a 1-D array are na-like,\n    according to the criteria defined in `checknull`:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n    '
    pass

def isnaobj2d():
    '\n    Return boolean mask denoting which elements of a 2-D array are na-like,\n    according to the criteria defined in `checknull`:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n\n    Notes\n    -----\n    The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def isnaobj2d_old():
    '\n    Return boolean mask denoting which elements of a 2-D array are na-like,\n    according to the criteria defined in `checknull_old`:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n\n    Notes\n    -----\n    The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def isnaobj_old():
    '\n    Return boolean mask denoting which elements of a 1-D array are na-like,\n    defined as being any of:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n    '
    pass

def isneginf_scalar():
    pass

def isposinf_scalar():
    pass

