import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/join.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.join'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _get_result_indexer():
    pass

def asof_join_backward():
    pass

def asof_join_backward_on_X_by_Y():
    pass

def asof_join_forward():
    pass

def asof_join_forward_on_X_by_Y():
    pass

def asof_join_nearest():
    pass

def asof_join_nearest_on_X_by_Y():
    pass

def ensure_platform_int():
    pass

def ffill_indexer():
    pass

def full_outer_join():
    pass

def groupsort_indexer():
    '\n    compute a 1-d indexer that is an ordering of the passed index,\n    ordered by the groups. This is a reverse of the label\n    factorization process.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        mappings from group -> position\n    ngroups: int64\n        number of groups\n\n    return a tuple of (1-d indexer ordered by groups, group counts)\n    '
    pass

def inner_join():
    pass

def inner_join_indexer(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def inner_join_indexer_float32(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def inner_join_indexer_float64(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def inner_join_indexer_int32(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def inner_join_indexer_int64(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def inner_join_indexer_object(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def inner_join_indexer_uint64(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_float32(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_float64(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_int32(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_int64(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_object(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_uint64(left, right):
    '\n    Two-pass algorithm for monotonic indexes. Handles many-to-one merges\n    '
    pass

def left_join_indexer_unique(left, right):
    pass

def left_join_indexer_unique_float32(left, right):
    pass

def left_join_indexer_unique_float64(left, right):
    pass

def left_join_indexer_unique_int32(left, right):
    pass

def left_join_indexer_unique_int64(left, right):
    pass

def left_join_indexer_unique_object(left, right):
    pass

def left_join_indexer_unique_uint64(left, right):
    pass

def left_outer_join():
    pass

def outer_join_indexer(left, right):
    pass

def outer_join_indexer_float32(left, right):
    pass

def outer_join_indexer_float64(left, right):
    pass

def outer_join_indexer_int32(left, right):
    pass

def outer_join_indexer_int64(left, right):
    pass

def outer_join_indexer_object(left, right):
    pass

def outer_join_indexer_uint64(left, right):
    pass

def take_nd(arr, indexer, axis, out, fill_value, mask_info, allow_fill):
    '\n    Specialized Cython take which sets NaN values in one pass\n\n    This dispatches to ``take`` defined on ExtensionArrays. It does not\n    currently dispatch to ``SparseArray.take`` for sparse ``arr``.\n\n    Parameters\n    ----------\n    arr : array-like\n        Input array.\n    indexer : ndarray\n        1-D array of indices to take, subarrays corresponding to -1 value\n        indices are filed with fill_value\n    axis : int, default 0\n        Axis to take from\n    out : ndarray or None, default None\n        Optional output array, must be appropriate type to hold input and\n        fill_value together, if indexer has any -1 value entries; call\n        _maybe_promote to determine this type for any fill_value\n    fill_value : any, default np.nan\n        Fill value to replace -1 values with\n    mask_info : tuple of (ndarray, boolean)\n        If provided, value should correspond to:\n            (indexer != -1, (indexer != -1).any())\n        If not provided, it will be computed internally if necessary\n    allow_fill : boolean, default True\n        If False, indexer is assumed to contain no -1 values so no filling\n        will be done.  This short-circuits computation of a mask.  Result is\n        undefined if allow_fill == False and -1 is present in indexer.\n\n    Returns\n    -------\n    subarray : array-like\n        May be the same type as the input, or cast to an ndarray.\n    '
    pass

