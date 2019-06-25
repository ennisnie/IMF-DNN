import builtins as _mod_builtins
import numpy as _mod_numpy
import pandas.core.arrays.categorical as _mod_pandas_core_arrays_categorical
import pandas.errors as _mod_pandas_errors

CParserError = _mod_pandas_errors.ParserError
Categorical = _mod_pandas_core_arrays_categorical.Categorical
DEFAULT_CHUNKSIZE = 262144
DtypeWarning = _mod_pandas_errors.DtypeWarning
ENOENT = 2
EmptyDataError = _mod_pandas_errors.EmptyDataError
ParserError = _mod_pandas_errors.ParserError
ParserWarning = _mod_pandas_errors.ParserWarning
QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2
class TextReader(_mod_builtins.object):
    '\n\n    # source: StringIO or file object\n\n    '
    __class__ = TextReader
    def __init__(self, *args, **kwargs):
        '\n\n    # source: StringIO or file object\n\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _convert_column_data(self):
        pass
    
    def _get_converter(self):
        pass
    
    def _set_quoting(self):
        pass
    
    @property
    def allow_leading_cols(self):
        pass
    
    @property
    def buffer_lines(self):
        pass
    
    def close(self):
        pass
    
    @property
    def compression(self):
        pass
    
    @property
    def converters(self):
        pass
    
    @property
    def delim_whitespace(self):
        pass
    
    @property
    def delimiter(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    @property
    def dtype_cast_order(self):
        pass
    
    @property
    def encoding(self):
        pass
    
    @property
    def header(self):
        pass
    
    @property
    def header_end(self):
        pass
    
    @property
    def header_start(self):
        pass
    
    @property
    def index_col(self):
        pass
    
    @property
    def leading_cols(self):
        pass
    
    @property
    def low_memory(self):
        pass
    
    @property
    def mangle_dupe_cols(self):
        pass
    
    @property
    def memory_map(self):
        pass
    
    @property
    def na_values(self):
        pass
    
    @property
    def names(self):
        pass
    
    @property
    def noconvert(self):
        pass
    
    @property
    def orig_header(self):
        pass
    
    def read(self):
        '\n        rows=None --> read all rows\n        '
        pass
    
    def remove_noconvert(self):
        pass
    
    def set_error_bad_lines(self):
        pass
    
    def set_noconvert(self):
        pass
    
    @property
    def skipfooter(self):
        pass
    
    @property
    def skiprows(self):
        pass
    
    @property
    def table_width(self):
        pass
    
    @property
    def tupleize_cols(self):
        pass
    
    @property
    def unnamed_cols(self):
        pass
    
    @property
    def usecols(self):
        pass
    

_NA_VALUES = _mod_builtins.list()
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/parsers.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.parsers'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _compute_na_values():
    pass

def _concatenate_chunks():
    pass

def _ensure_encoded():
    pass

def _maybe_encode():
    pass

def _maybe_upcast():
    '\n\n    '
    pass

basestring = _mod_builtins.str
def is_bool_dtype(arr_or_dtype):
    "\n    Check whether the provided array or dtype is of a boolean dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array or dtype to check.\n\n    Returns\n    -------\n    boolean : Whether or not the array or dtype is of a boolean dtype.\n\n    Notes\n    -----\n    An ExtensionArray is considered boolean when the ``_is_boolean``\n    attribute is set to True.\n\n    Examples\n    --------\n    >>> is_bool_dtype(str)\n    False\n    >>> is_bool_dtype(int)\n    False\n    >>> is_bool_dtype(bool)\n    True\n    >>> is_bool_dtype(np.bool)\n    True\n    >>> is_bool_dtype(np.array(['a', 'b']))\n    False\n    >>> is_bool_dtype(pd.Series([1, 2]))\n    False\n    >>> is_bool_dtype(np.array([True, False]))\n    True\n    >>> is_bool_dtype(pd.Categorical([True, False]))\n    True\n    >>> is_bool_dtype(pd.SparseArray([True, False]))\n    True\n    "
    pass

def is_categorical_dtype(arr_or_dtype):
    '\n    Check whether an array-like or dtype is of the Categorical dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array-like or dtype to check.\n\n    Returns\n    -------\n    boolean : Whether or not the array-like or dtype is\n              of the Categorical dtype.\n\n    Examples\n    --------\n    >>> is_categorical_dtype(object)\n    False\n    >>> is_categorical_dtype(CategoricalDtype())\n    True\n    >>> is_categorical_dtype([1, 2, 3])\n    False\n    >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))\n    True\n    >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))\n    True\n    '
    pass

def is_datetime64_dtype(arr_or_dtype):
    '\n    Check whether an array-like or dtype is of the datetime64 dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array-like or dtype to check.\n\n    Returns\n    -------\n    boolean : Whether or not the array-like or dtype is of\n              the datetime64 dtype.\n\n    Examples\n    --------\n    >>> is_datetime64_dtype(object)\n    False\n    >>> is_datetime64_dtype(np.datetime64)\n    True\n    >>> is_datetime64_dtype(np.array([], dtype=int))\n    False\n    >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))\n    True\n    >>> is_datetime64_dtype([1, 2, 3])\n    False\n    '
    pass

def is_extension_array_dtype(arr_or_dtype):
    "\n    Check if an object is a pandas extension array type.\n\n    See the :ref:`Use Guide <extending.extension-types>` for more.\n\n    Parameters\n    ----------\n    arr_or_dtype : object\n        For array-like input, the ``.dtype`` attribute will\n        be extracted.\n\n    Returns\n    -------\n    bool\n        Whether the `arr_or_dtype` is an extension array type.\n\n    Notes\n    -----\n    This checks whether an object implements the pandas extension\n    array interface. In pandas, this includes:\n\n    * Categorical\n    * Sparse\n    * Interval\n    * Period\n    * DatetimeArray\n    * TimedeltaArray\n\n    Third-party libraries may implement arrays or types satisfying\n    this interface as well.\n\n    Examples\n    --------\n    >>> from pandas.api.types import is_extension_array_dtype\n    >>> arr = pd.Categorical(['a', 'b'])\n    >>> is_extension_array_dtype(arr)\n    True\n    >>> is_extension_array_dtype(arr.dtype)\n    True\n\n    >>> arr = np.array(['a', 'b'])\n    >>> is_extension_array_dtype(arr.dtype)\n    False\n    "
    pass

def is_float_dtype(arr_or_dtype):
    "\n    Check whether the provided array or dtype is of a float dtype.\n\n    This function is internal and should not be exposed in the public API.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array or dtype to check.\n\n    Returns\n    -------\n    boolean : Whether or not the array or dtype is of a float dtype.\n\n    Examples\n    --------\n    >>> is_float_dtype(str)\n    False\n    >>> is_float_dtype(int)\n    False\n    >>> is_float_dtype(float)\n    True\n    >>> is_float_dtype(np.array(['a', 'b']))\n    False\n    >>> is_float_dtype(pd.Series([1, 2]))\n    False\n    >>> is_float_dtype(pd.Index([1, 2.]))\n    True\n    "
    pass

def is_integer_dtype(arr_or_dtype):
    "\n    Check whether the provided array or dtype is of an integer dtype.\n\n    Unlike in `in_any_int_dtype`, timedelta64 instances will return False.\n\n    .. versionchanged:: 0.24.0\n\n       The nullable Integer dtypes (e.g. pandas.Int64Dtype) are also considered\n       as integer by this function.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array or dtype to check.\n\n    Returns\n    -------\n    boolean : Whether or not the array or dtype is of an integer dtype\n              and not an instance of timedelta64.\n\n    Examples\n    --------\n    >>> is_integer_dtype(str)\n    False\n    >>> is_integer_dtype(int)\n    True\n    >>> is_integer_dtype(float)\n    False\n    >>> is_integer_dtype(np.uint64)\n    True\n    >>> is_integer_dtype('int8')\n    True\n    >>> is_integer_dtype('Int8')\n    True\n    >>> is_integer_dtype(pd.Int8Dtype)\n    True\n    >>> is_integer_dtype(np.datetime64)\n    False\n    >>> is_integer_dtype(np.timedelta64)\n    False\n    >>> is_integer_dtype(np.array(['a', 'b']))\n    False\n    >>> is_integer_dtype(pd.Series([1, 2]))\n    True\n    >>> is_integer_dtype(np.array([], dtype=np.timedelta64))\n    False\n    >>> is_integer_dtype(pd.Index([1, 2.]))  # float\n    False\n    "
    pass

def is_object_dtype(arr_or_dtype):
    '\n    Check whether an array-like or dtype is of the object dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array-like or dtype to check.\n\n    Returns\n    -------\n    boolean : Whether or not the array-like or dtype is of the object dtype.\n\n    Examples\n    --------\n    >>> is_object_dtype(object)\n    True\n    >>> is_object_dtype(int)\n    False\n    >>> is_object_dtype(np.array([], dtype=object))\n    True\n    >>> is_object_dtype(np.array([], dtype=int))\n    False\n    >>> is_object_dtype([1, 2, 3])\n    False\n    '
    pass

k = _mod_numpy.object_
na_values = _mod_builtins.dict()
def pandas_dtype(dtype):
    '\n    Converts input into a pandas only dtype object or a numpy dtype object.\n\n    Parameters\n    ----------\n    dtype : object to be converted\n\n    Returns\n    -------\n    np.dtype or a pandas dtype\n\n    Raises\n    ------\n    TypeError if not a dtype\n    '
    pass

def sanitize_objects():
    '\n    Convert specified values, including the given set na_values and empty\n    strings if convert_empty is True, to np.nan.\n\n    Parameters\n    ----------\n    values : ndarray[object]\n    na_values : set\n    convert_empty : bool (default True)\n    '
    pass

def union_categoricals(to_union, sort_categories, ignore_order):
    '\n    Combine list-like of Categorical-like, unioning categories. All\n    categories must have the same dtype.\n\n    .. versionadded:: 0.19.0\n\n    Parameters\n    ----------\n    to_union : list-like of Categorical, CategoricalIndex,\n               or Series with dtype=\'category\'\n    sort_categories : boolean, default False\n        If true, resulting categories will be lexsorted, otherwise\n        they will be ordered as they appear in the data.\n    ignore_order : boolean, default False\n        If true, the ordered attribute of the Categoricals will be ignored.\n        Results in an unordered categorical.\n\n        .. versionadded:: 0.20.0\n\n    Returns\n    -------\n    result : Categorical\n\n    Raises\n    ------\n    TypeError\n        - all inputs do not have the same dtype\n        - all inputs do not have the same ordered property\n        - all inputs are ordered and their categories are not identical\n        - sort_categories=True and Categoricals are ordered\n    ValueError\n        Empty list of categoricals passed\n\n    Notes\n    -----\n\n    To learn more about categories, see `link\n    <http://pandas.pydata.org/pandas-docs/stable/categorical.html#unioning>`__\n\n    Examples\n    --------\n\n    >>> from pandas.api.types import union_categoricals\n\n    If you want to combine categoricals that do not necessarily have\n    the same categories, `union_categoricals` will combine a list-like\n    of categoricals. The new categories will be the union of the\n    categories being combined.\n\n    >>> a = pd.Categorical(["b", "c"])\n    >>> b = pd.Categorical(["a", "b"])\n    >>> union_categoricals([a, b])\n    [b, c, a, b]\n    Categories (3, object): [b, c, a]\n\n    By default, the resulting categories will be ordered as they appear\n    in the `categories` of the data. If you want the categories to be\n    lexsorted, use `sort_categories=True` argument.\n\n    >>> union_categoricals([a, b], sort_categories=True)\n    [b, c, a, b]\n    Categories (3, object): [a, b, c]\n\n    `union_categoricals` also works with the case of combining two\n    categoricals of the same categories and order information (e.g. what\n    you could also `append` for).\n\n    >>> a = pd.Categorical(["a", "b"], ordered=True)\n    >>> b = pd.Categorical(["a", "b", "a"], ordered=True)\n    >>> union_categoricals([a, b])\n    [a, b, a, b, a]\n    Categories (2, object): [a < b]\n\n    Raises `TypeError` because the categories are ordered and not identical.\n\n    >>> a = pd.Categorical(["a", "b"], ordered=True)\n    >>> b = pd.Categorical(["a", "b", "c"], ordered=True)\n    >>> union_categoricals([a, b])\n    TypeError: to union ordered Categoricals, all categories must be the same\n\n    New in version 0.20.0\n\n    Ordered categoricals with different categories or orderings can be\n    combined by using the `ignore_ordered=True` argument.\n\n    >>> a = pd.Categorical(["a", "b", "c"], ordered=True)\n    >>> b = pd.Categorical(["c", "b", "a"], ordered=True)\n    >>> union_categoricals([a, b], ignore_order=True)\n    [a, b, c, c, b, a]\n    Categories (3, object): [a, b, c]\n\n    `union_categoricals` also works with a `CategoricalIndex`, or `Series`\n    containing categorical data, but note that the resulting array will\n    always be a plain `Categorical`\n\n    >>> a = pd.Series(["b", "c"], dtype=\'category\')\n    >>> b = pd.Series(["a", "b"], dtype=\'category\')\n    >>> union_categoricals([a, b])\n    [b, c, a, b]\n    Categories (3, object): [b, c, a]\n    '
    pass

