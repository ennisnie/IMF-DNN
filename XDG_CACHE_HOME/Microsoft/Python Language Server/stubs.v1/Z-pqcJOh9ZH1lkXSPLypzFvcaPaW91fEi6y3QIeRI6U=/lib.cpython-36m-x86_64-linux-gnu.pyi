import builtins as _mod_builtins
import decimal as _mod_decimal
import fractions as _mod_fractions
import numbers as _mod_numbers
import pandas._libs.tslibs.nattype as _mod_pandas__libs_tslibs_nattype

class AnyTimedeltaValidator(TimedeltaValidator):
    __class__ = AnyTimedeltaValidator
    def __init__(self, *args, **kwargs):
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
    

class BoolValidator(Validator):
    __class__ = BoolValidator
    def __init__(self, *args, **kwargs):
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
    

class BytesValidator(Validator):
    __class__ = BytesValidator
    def __init__(self, *args, **kwargs):
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
    

class DateValidator(Validator):
    __class__ = DateValidator
    def __init__(self, *args, **kwargs):
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
    

class Datetime64Validator(DatetimeValidator):
    __class__ = Datetime64Validator
    def __init__(self, *args, **kwargs):
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
    

class DatetimeValidator(TemporalValidator):
    __class__ = DatetimeValidator
    def __init__(self, *args, **kwargs):
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
    

Decimal = _mod_decimal.Decimal
class FloatValidator(Validator):
    __class__ = FloatValidator
    def __init__(self, *args, **kwargs):
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
    

Fraction = _mod_fractions.Fraction
class IntegerFloatValidator(Validator):
    __class__ = IntegerFloatValidator
    def __init__(self, *args, **kwargs):
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
    

class IntegerValidator(Validator):
    __class__ = IntegerValidator
    def __init__(self, *args, **kwargs):
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
    

class IntervalValidator(Validator):
    __class__ = IntervalValidator
    def __init__(self, *args, **kwargs):
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
    

NaT = _mod_pandas__libs_tslibs_nattype.NaTType()
Number = _mod_numbers.Number
class PeriodValidator(TemporalValidator):
    __class__ = PeriodValidator
    def __init__(self, *args, **kwargs):
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
    

class Seen(_mod_builtins.object):
    '\n    Class for keeping track of the types of elements\n    encountered when trying to perform type conversions.\n    '
    __class__ = Seen
    def __init__(self, *args, **kwargs):
        '\n    Class for keeping track of the types of elements\n    encountered when trying to perform type conversions.\n    '
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
    
    @property
    def is_bool(self):
        pass
    
    @property
    def is_float_or_complex(self):
        pass
    
    @property
    def numeric_(self):
        pass
    

class StringValidator(Validator):
    __class__ = StringValidator
    def __init__(self, *args, **kwargs):
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
    

class TemporalValidator(Validator):
    __class__ = TemporalValidator
    def __init__(self, *args, **kwargs):
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
    

class TimeValidator(Validator):
    __class__ = TimeValidator
    def __init__(self, *args, **kwargs):
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
    

class TimedeltaValidator(TemporalValidator):
    __class__ = TimedeltaValidator
    def __init__(self, *args, **kwargs):
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
    

class UnicodeValidator(Validator):
    __class__ = UnicodeValidator
    def __init__(self, *args, **kwargs):
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
    

class Validator(_mod_builtins.object):
    __class__ = Validator
    def __init__(self, *args, **kwargs):
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
    

_TYPE_MAP = _mod_builtins.dict()
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/lib.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.lib'
__package__ = 'pandas._libs'
__test__ = _mod_builtins.dict()
def array_equivalent_object():
    ' perform an element by element comparion on 1-d object arrays\n        taking into account nan positions '
    pass

def array_to_datetime():
    "\n    Converts a 1D array of date-like values to a numpy array of either:\n        1) datetime64[ns] data\n        2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError\n           is encountered\n\n    Also returns a pytz.FixedOffset if an array of strings with the same\n    timezone offset is passed and utc=True is not passed. Otherwise, None\n    is returned\n\n    Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,\n    strings\n\n    Parameters\n    ----------\n    values : ndarray of object\n         date-like objects to convert\n    errors : str, default 'raise'\n         error behavior when parsing\n    dayfirst : bool, default False\n         dayfirst parsing behavior when encountering datetime strings\n    yearfirst : bool, default False\n         yearfirst parsing behavior when encountering datetime strings\n    utc : bool, default None\n         indicator whether the dates should be UTC\n    require_iso8601 : bool, default False\n         indicator whether the datetime string should be iso8601\n\n    Returns\n    -------\n    tuple (ndarray, tzoffset)\n    "
    pass

def astype_intsafe():
    pass

def astype_str():
    "\n    Convert all elements in an array to string.\n\n    Parameters\n    ----------\n    arr : ndarray\n        The array whose elements we are casting.\n    skipna : bool, default False\n        Whether or not to coerce nulls to their stringified form\n        (e.g. NaN becomes 'nan').\n\n    Returns\n    -------\n    casted_arr : ndarray\n        A new array with the input array's elements casted.\n    "
    pass

def astype_unicode():
    "\n    Convert all elements in an array to unicode.\n\n    Parameters\n    ----------\n    arr : ndarray\n        The array whose elements we are casting.\n    skipna : bool, default False\n        Whether or not to coerce nulls to their stringified form\n        (e.g. NaN becomes 'nan').\n\n    Returns\n    -------\n    casted_arr : ndarray\n        A new array with the input array's elements casted.\n    "
    pass

def clean_index_list():
    '\n    Utility used in pandas.core.index.ensure_index\n    '
    pass

def count_level_2d():
    pass

def dicts_to_array():
    pass

def fast_multiget():
    pass

def fast_unique_multiple():
    '\n    Generate a list of unique values from a list of arrays.\n\n    Parameters\n    ----------\n    list : array-like\n        A list of array-like objects\n    sort : boolean\n        Whether or not to sort the resulting unique list\n\n    Returns\n    -------\n    unique_list : list of unique values\n    '
    pass

def fast_unique_multiple_list():
    pass

def fast_unique_multiple_list_gen():
    '\n    Generate a list of unique values from a generator of lists.\n\n    Parameters\n    ----------\n    gen : generator object\n        A generator of lists from which the unique list is created\n    sort : boolean\n        Whether or not to sort the resulting unique list\n\n    Returns\n    -------\n    unique_list : list of unique values\n    '
    pass

def fast_zip():
    '\n    For zipping multiple ndarrays into an ndarray of tuples\n    '
    pass

def generate_bins_dt64():
    '\n    Int64 (datetime64) version of generic python version in groupby.py\n    '
    pass

def generate_slices():
    pass

def get_level_sorter():
    "\n    argsort for a single level of a multi-index, keeping the order of higher\n    levels unchanged. `starts` points to starts of same-key indices w.r.t\n    to leading levels; equivalent to:\n        np.hstack([label[starts[i]:starts[i+1]].argsort(kind='mergesort')\n            + starts[i] for i in range(len(starts) - 1)])\n    "
    pass

def get_reverse_indexer():
    '\n    Reverse indexing operation.\n\n    Given `indexer`, make `indexer_inv` of it, such that::\n\n        indexer_inv[indexer[x]] = x\n\n    .. note:: If indexer is not unique, only first occurrence is accounted.\n\n    '
    pass

def has_infs_f4():
    pass

def has_infs_f8():
    pass

def indices_fast():
    pass

def infer_datetimelike_array():
    '\n    infer if we have a datetime or timedelta array\n    - date: we have *only* date and maybe strings, nulls\n    - datetime: we have *only* datetimes and maybe strings, nulls\n    - timedelta: we have *only* timedeltas and maybe strings, nulls\n    - nat: we do not have *any* date, datetimes or timedeltas, but do have\n      at least a NaT\n    - mixed: other objects (strings, a mix of tz-aware and tz-naive, or\n                            actual objects)\n\n    Parameters\n    ----------\n    arr : object array\n\n    Returns\n    -------\n    string: {datetime, timedelta, date, nat, mixed}\n    '
    pass

def infer_dtype():
    "\n    Efficiently infer the type of a passed val, or list-like\n    array of values. Return a string describing the type.\n\n    Parameters\n    ----------\n    value : scalar, list, ndarray, or pandas type\n    skipna : bool, default False\n        Ignore NaN values when inferring the type.\n\n        .. versionadded:: 0.21.0\n\n    Returns\n    -------\n    string describing the common type of the input data.\n    Results can include:\n\n    - string\n    - unicode\n    - bytes\n    - floating\n    - integer\n    - mixed-integer\n    - mixed-integer-float\n    - decimal\n    - complex\n    - categorical\n    - boolean\n    - datetime64\n    - datetime\n    - date\n    - timedelta64\n    - timedelta\n    - time\n    - period\n    - mixed\n\n    Raises\n    ------\n    TypeError if ndarray-like but cannot infer the dtype\n\n    Notes\n    -----\n    - 'mixed' is the catchall for anything that is not otherwise\n      specialized\n    - 'mixed-integer-float' are floats and integers\n    - 'mixed-integer' are integers mixed with non-integers\n\n    Examples\n    --------\n    >>> infer_dtype(['foo', 'bar'])\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=True)\n    'string'\n\n    >>> infer_dtype(['a', np.nan, 'b'], skipna=False)\n    'mixed'\n\n    >>> infer_dtype([b'foo', b'bar'])\n    'bytes'\n\n    >>> infer_dtype([1, 2, 3])\n    'integer'\n\n    >>> infer_dtype([1, 2, 3.5])\n    'mixed-integer-float'\n\n    >>> infer_dtype([1.0, 2.0, 3.5])\n    'floating'\n\n    >>> infer_dtype(['a', 1])\n    'mixed-integer'\n\n    >>> infer_dtype([Decimal(1), Decimal(2.0)])\n    'decimal'\n\n    >>> infer_dtype([True, False])\n    'boolean'\n\n    >>> infer_dtype([True, False, np.nan])\n    'mixed'\n\n    >>> infer_dtype([pd.Timestamp('20130101')])\n    'datetime'\n\n    >>> infer_dtype([datetime.date(2013, 1, 1)])\n    'date'\n\n    >>> infer_dtype([np.datetime64('2013-01-01')])\n    'datetime64'\n\n    >>> infer_dtype([datetime.timedelta(0, 1, 1)])\n    'timedelta'\n\n    >>> infer_dtype(pd.Series(list('aabc')).astype('category'))\n    'categorical'\n    "
    pass

def is_bool():
    pass

def is_bool_array():
    pass

def is_complex():
    pass

def is_date_array():
    pass

def is_datetime64_array():
    pass

def is_datetime_array():
    pass

def is_datetime_with_singletz_array():
    "\n    Check values have the same tzinfo attribute.\n    Doesn't check values are datetime-like types.\n    "
    pass

def is_decimal():
    pass

def is_float():
    pass

def is_float_array():
    pass

def is_integer():
    pass

def is_integer_array():
    pass

def is_interval():
    pass

def is_interval_array():
    pass

def is_period():
    ' Return a boolean if this is a Period object '
    pass

def is_period_array():
    pass

def is_scalar():
    '\n    Return True if given value is scalar.\n\n    Parameters\n    ----------\n    val : object\n        This includes:\n\n        - numpy array scalar (e.g. np.int64)\n        - Python builtin numerics\n        - Python builtin byte arrays and strings\n        - None\n        - datetime.datetime\n        - datetime.timedelta\n        - Period\n        - decimal.Decimal\n        - Interval\n        - DateOffset\n        - Fraction\n        - Number\n\n    Returns\n    -------\n    bool\n        Return True if given object is scalar, False otherwise\n\n    Examples\n    --------\n    >>> dt = pd.datetime.datetime(2018, 10, 3)\n    >>> pd.is_scalar(dt)\n    True\n\n    >>> pd.api.types.is_scalar([2, 3])\n    False\n\n    >>> pd.api.types.is_scalar({0: 1, 2: 3})\n    False\n\n    >>> pd.api.types.is_scalar((0, 2))\n    False\n\n    pandas supports PEP 3141 numbers:\n\n    >>> from fractions import Fraction\n    >>> pd.api.types.is_scalar(Fraction(3, 5))\n    True\n    '
    pass

def is_string_array():
    pass

def is_time_array():
    pass

def is_timedelta_or_timedelta64_array():
    ' infer with timedeltas and/or nat/none '
    pass

def item_from_zerodim():
    "\n    If the value is a zerodim array, return the item it contains.\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : object\n\n    Examples\n    --------\n    >>> item_from_zerodim(1)\n    1\n    >>> item_from_zerodim('foobar')\n    'foobar'\n    >>> item_from_zerodim(np.array(1))\n    1\n    >>> item_from_zerodim(np.array([1]))\n    array([1])\n\n    "
    pass

def map_infer():
    '\n    Substitute for np.vectorize with pandas-friendly dtype inference\n\n    Parameters\n    ----------\n    arr : ndarray\n    f : function\n\n    Returns\n    -------\n    mapped : ndarray\n    '
    pass

def map_infer_mask():
    '\n    Substitute for np.vectorize with pandas-friendly dtype inference\n\n    Parameters\n    ----------\n    arr : ndarray\n    f : function\n\n    Returns\n    -------\n    mapped : ndarray\n    '
    pass

def maybe_booleans_to_slice():
    pass

def maybe_convert_numeric():
    "\n    Convert object array to a numeric array if possible.\n\n    Parameters\n    ----------\n    values : ndarray\n        Array of object elements to convert.\n    na_values : set\n        Set of values that should be interpreted as NaN.\n    convert_empty : bool, default True\n        If an empty array-like object is encountered, whether to interpret\n        that element as NaN or not. If set to False, a ValueError will be\n        raised if such an element is encountered and 'coerce_numeric' is False.\n    coerce_numeric : bool, default False\n        If initial attempts to convert to numeric have failed, whether to\n        force conversion to numeric via alternative methods or by setting the\n        element to NaN. Otherwise, an Exception will be raised when such an\n        element is encountered.\n\n        This boolean also has an impact on how conversion behaves when a\n        numeric array has no suitable numerical dtype to return (i.e. uint64,\n        int32, uint8). If set to False, the original object array will be\n        returned. Otherwise, a ValueError will be raised.\n\n    Returns\n    -------\n    numeric_array : array of converted object values to numerical ones\n    "
    pass

def maybe_convert_objects():
    '\n    Type inference function-- convert object array to proper dtype\n    '
    pass

def maybe_indices_to_slice():
    pass

def memory_usage_of_objects():
    ' return the memory usage of an object array in bytes,\n    does not include the actual bytes of the pointers '
    pass

def row_bool_subset():
    pass

def row_bool_subset_object():
    pass

def to_object_array():
    '\n    Convert a list of lists into an object array.\n\n    Parameters\n    ----------\n    rows : 2-d array (N, K)\n        A list of lists to be converted into an array\n    min_width : int\n        The minimum width of the object array. If a list\n        in `rows` contains fewer than `width` elements,\n        the remaining elements in the corresponding row\n        will all be `NaN`.\n\n    Returns\n    -------\n    obj_array : numpy array of the object dtype\n    '
    pass

def to_object_array_tuples():
    pass

def tuples_to_object_array():
    pass

def values_from_object():
    ' return my values or the object if we are say an ndarray '
    pass

