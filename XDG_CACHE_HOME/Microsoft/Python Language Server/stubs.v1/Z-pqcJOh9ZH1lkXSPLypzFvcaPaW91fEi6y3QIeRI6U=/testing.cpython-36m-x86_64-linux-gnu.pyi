import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/testing.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.testing'
__package__ = 'pandas._libs'
__test__ = _mod_builtins.dict()
def array_equivalent(left, right, strict_nan):
    '\n    True if two arrays, left and right, have equal non-NaN elements, and NaNs\n    in corresponding locations.  False otherwise. It is assumed that left and\n    right are NumPy arrays of the same dtype. The behavior of this function\n    (particularly with respect to NaNs) is not defined if the dtypes are\n    different.\n\n    Parameters\n    ----------\n    left, right : ndarrays\n    strict_nan : bool, default False\n        If True, consider NaN and None to be different.\n\n    Returns\n    -------\n    b : bool\n        Returns True if the arrays are equivalent.\n\n    Examples\n    --------\n    >>> array_equivalent(\n    ...     np.array([1, 2, np.nan]),\n    ...     np.array([1, 2, np.nan]))\n    True\n    >>> array_equivalent(\n    ...     np.array([1, np.nan, 2]),\n    ...     np.array([1, 2, np.nan]))\n    False\n    '
    pass

def assert_almost_equal():
    'Check that left and right objects are almost equal.\n\n    Parameters\n    ----------\n    a : object\n    b : object\n    check_less_precise : bool or int, default False\n        Specify comparison precision.\n        5 digits (False) or 3 digits (True) after decimal points are\n        compared. If an integer, then this will be the number of decimal\n        points to compare\n    check_dtype: bool, default True\n        check dtype if both a and b are np.ndarray\n    obj : str, default None\n        Specify object name being compared, internally used to show\n        appropriate assertion message\n    lobj : str, default None\n        Specify left object name being compared, internally used to show\n        appropriate assertion message\n    robj : str, default None\n        Specify right object name being compared, internally used to show\n        appropriate assertion message\n    '
    pass

def assert_dict_equal():
    pass

def is_dtype_equal(source, target):
    '\n    Check if two dtypes are equal.\n\n    Parameters\n    ----------\n    source : The first dtype to compare\n    target : The second dtype to compare\n\n    Returns\n    ----------\n    boolean : Whether or not the two dtypes are equal.\n\n    Examples\n    --------\n    >>> is_dtype_equal(int, float)\n    False\n    >>> is_dtype_equal("int", int)\n    True\n    >>> is_dtype_equal(object, "category")\n    False\n    >>> is_dtype_equal(CategoricalDtype(), "category")\n    True\n    >>> is_dtype_equal(DatetimeTZDtype(), "datetime64")\n    False\n    '
    pass

def isna(obj):
    '\n    Detect missing values for an array-like object.\n\n    This function takes a scalar or array-like object and indicates\n    whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``\n    in object arrays, ``NaT`` in datetimelike).\n\n    Parameters\n    ----------\n    obj : scalar or array-like\n        Object to check for null or missing values.\n\n    Returns\n    -------\n    bool or array-like of bool\n        For scalar input, returns a scalar boolean.\n        For array input, returns an array of boolean indicating whether each\n        corresponding element is missing.\n\n    See Also\n    --------\n    notna : Boolean inverse of pandas.isna.\n    Series.isna : Detect missing values in a Series.\n    DataFrame.isna : Detect missing values in a DataFrame.\n    Index.isna : Detect missing values in an Index.\n\n    Examples\n    --------\n    Scalar arguments (including strings) result in a scalar boolean.\n\n    >>> pd.isna(\'dog\')\n    False\n\n    >>> pd.isna(np.nan)\n    True\n\n    ndarrays result in an ndarray of booleans.\n\n    >>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])\n    >>> array\n    array([[ 1., nan,  3.],\n           [ 4.,  5., nan]])\n    >>> pd.isna(array)\n    array([[False,  True, False],\n           [False, False,  True]])\n\n    For indexes, an ndarray of booleans is returned.\n\n    >>> index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,\n    ...                           "2017-07-08"])\n    >>> index\n    DatetimeIndex([\'2017-07-05\', \'2017-07-06\', \'NaT\', \'2017-07-08\'],\n                  dtype=\'datetime64[ns]\', freq=None)\n    >>> pd.isna(index)\n    array([False, False,  True, False])\n\n    For Series and DataFrame, the same type is returned, containing booleans.\n\n    >>> df = pd.DataFrame([[\'ant\', \'bee\', \'cat\'], [\'dog\', None, \'fly\']])\n    >>> df\n         0     1    2\n    0  ant   bee  cat\n    1  dog  None  fly\n    >>> pd.isna(df)\n           0      1      2\n    0  False  False  False\n    1  False   True  False\n\n    >>> pd.isna(df[1])\n    0    False\n    1     True\n    Name: 1, dtype: bool\n    '
    pass

