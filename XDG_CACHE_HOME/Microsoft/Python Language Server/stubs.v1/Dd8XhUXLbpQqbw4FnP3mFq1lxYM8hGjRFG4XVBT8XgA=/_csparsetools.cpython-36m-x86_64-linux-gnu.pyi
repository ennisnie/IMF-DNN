import builtins as _mod_builtins

__builtins__ = {}
__doc__ = '\nFast snippets for LIL matrices.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/sparse/_csparsetools.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse._csparsetools'
__package__ = 'scipy.sparse'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _lil_fancy_get_int32():
    pass

def _lil_fancy_get_int64():
    pass

def _lil_fancy_set_int32_bool_():
    pass

def _lil_fancy_set_int32_clongdouble():
    pass

def _lil_fancy_set_int32_complex128():
    pass

def _lil_fancy_set_int32_complex64():
    pass

def _lil_fancy_set_int32_float32():
    pass

def _lil_fancy_set_int32_float64():
    pass

def _lil_fancy_set_int32_int16():
    pass

def _lil_fancy_set_int32_int32():
    pass

def _lil_fancy_set_int32_int64():
    pass

def _lil_fancy_set_int32_int8():
    pass

def _lil_fancy_set_int32_longdouble():
    pass

def _lil_fancy_set_int32_uint16():
    pass

def _lil_fancy_set_int32_uint32():
    pass

def _lil_fancy_set_int32_uint64():
    pass

def _lil_fancy_set_int32_uint8():
    pass

def _lil_fancy_set_int64_bool_():
    pass

def _lil_fancy_set_int64_clongdouble():
    pass

def _lil_fancy_set_int64_complex128():
    pass

def _lil_fancy_set_int64_complex64():
    pass

def _lil_fancy_set_int64_float32():
    pass

def _lil_fancy_set_int64_float64():
    pass

def _lil_fancy_set_int64_int16():
    pass

def _lil_fancy_set_int64_int32():
    pass

def _lil_fancy_set_int64_int64():
    pass

def _lil_fancy_set_int64_int8():
    pass

def _lil_fancy_set_int64_longdouble():
    pass

def _lil_fancy_set_int64_uint16():
    pass

def _lil_fancy_set_int64_uint32():
    pass

def _lil_fancy_set_int64_uint64():
    pass

def _lil_fancy_set_int64_uint8():
    pass

def lil_fancy_get():
    '\n    Get multiple items at given indices in LIL matrix and store to\n    another LIL.\n\n    Parameters\n    ----------\n    M, N, rows, data\n        LIL matrix data, initially empty\n    new_rows, new_idx\n        Data for LIL matrix to insert to.\n        Must be preallocated to shape `i_idx.shape`!\n    i_idx, j_idx\n        Indices of elements to insert to the new LIL matrix.\n\n    '
    pass

def lil_fancy_set():
    '\n    Set multiple items to a LIL matrix.\n\n    Checks for zero elements and deletes them.\n\n    Parameters\n    ----------\n    M, N, rows, data\n        LIL matrix data\n    i_idx, j_idx\n        Indices of elements to insert to the new LIL matrix.\n    values\n        Values of items to set.\n\n    '
    pass

def lil_get1():
    "\n    Get a single item from LIL matrix.\n\n    Doesn't do output type conversion. Checks for bounds errors.\n\n    Parameters\n    ----------\n    M, N, rows, datas\n        Shape and data arrays for a LIL matrix\n    i, j : int\n        Indices at which to get\n\n    Returns\n    -------\n    x\n        Value at indices.\n\n    "
    pass

def lil_get_row_ranges():
    '\n    Column-slicing fast path for LIL matrices.\n    Extracts values from rows/datas and inserts in to\n    new_rows/new_datas.\n    Parameters\n    ----------\n    M, N\n         Shape of input array\n    rows, datas\n         LIL data for input array, shape (M, N)\n    new_rows, new_datas\n         LIL data for output array, shape (len(irows), nj)\n    irows : iterator\n         Iterator yielding row indices\n    j_start, j_stop, j_stride\n         Column range(j_start, j_stop, j_stride) to get\n    nj : int\n         Number of columns corresponding to j_* variables.\n    '
    pass

def lil_insert():
    '\n    Insert a single item to LIL matrix.\n\n    Checks for bounds errors and deletes item if x is zero.\n\n    Parameters\n    ----------\n    M, N, rows, datas\n        Shape and data arrays for a LIL matrix\n    i, j : int\n        Indices at which to get\n    x\n        Value to insert.\n\n    '
    pass

