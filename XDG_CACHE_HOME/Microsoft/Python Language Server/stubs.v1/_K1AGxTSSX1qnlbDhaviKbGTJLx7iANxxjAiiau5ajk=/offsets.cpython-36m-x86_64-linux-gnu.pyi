import builtins as _mod_builtins
import dateutil.relativedelta as _mod_dateutil_relativedelta
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

class ApplyTypeError(_mod_builtins.TypeError):
    __class__ = ApplyTypeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.offsets'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class BaseOffset(_BaseOffset):
    __class__ = BaseOffset
    __dict__ = {}
    def __init__(self, n, normalize):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __radd__(self, other):
        return BaseOffset()
    
    def __rmul__(self, other):
        return BaseOffset()
    
    def __rsub__(self, other):
        return BaseOffset()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

DAYS = _mod_builtins.list()
MONTHS = _mod_builtins.list()
PY2 = False
UTC = _mod_pytz.UTC()
class _BaseOffset(_mod_builtins.object):
    '\n    Base class for DateOffset methods that are not overridden by subclasses\n    and will (after pickle errors are resolved) go into a cdef class.\n    '
    def __add__(self, other):
        return _BaseOffset()
    
    def __call__(self, other):
        pass
    
    __class__ = _BaseOffset
    __dict__ = {}
    def __eq__(self, other):
        return False
    
    def __getstate__(self):
        'Return a pickleable state'
        pass
    
    def __hash__(self):
        return 0
    
    def __init__(self, n, normalize):
        '\n    Base class for DateOffset methods that are not overridden by subclasses\n    and will (after pickle errors are resolved) go into a cdef class.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.offsets'
    def __mul__(self, other):
        return _BaseOffset()
    
    def __ne__(self, other):
        return False
    
    def __neg__(self):
        return _BaseOffset()
    
    def __repr__(self):
        return ''
    
    def __setattr__(self, name, value):
        return None
    
    def __setstate__(self, state):
        'Reconstruct an instance from a pickled state'
        return None
    
    def __sub__(self, other):
        return _BaseOffset()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    _attributes = _mod_builtins.frozenset()
    _day_opt = None
    def _get_offset_day(self, other):
        pass
    
    _params = _mod_builtins.property()
    _typ = 'dateoffset'
    def _validate_n(self, n):
        '\n        Require that `n` be a nonzero integer.\n\n        Parameters\n        ----------\n        n : int\n\n        Returns\n        -------\n        nint : int\n\n        Raises\n        ------\n        TypeError if `int(n)` raises\n        ValueError if n != int(n)\n        '
        pass
    
    base = _mod_builtins.property()
    def copy(self):
        pass
    
    kwds = _mod_builtins.property()

class _Tick(_mod_builtins.object):
    '\n    dummy class to mix into tseries.offsets.Tick so that in tslibs.period we\n    can do isinstance checks on _Tick and avoid importing tseries.offsets\n    '
    __class__ = _Tick
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        '\n    dummy class to mix into tseries.offsets.Tick so that in tslibs.period we\n    can do isinstance checks on _Tick and avoid importing tseries.offsets\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.offsets'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, other):
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/offsets.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.offsets'
__package__ = 'pandas._libs.tslibs'
__prefix = 'Q'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
_alias = 'Q-DEC'
_d = 'SUN'
def _determine_offset():
    pass

def _get_calendar():
    'Generate busdaycalendar'
    pass

def _is_normalized():
    pass

_m = 'DEC'
_offset_to_period_map = _mod_builtins.dict()
def _to_dt64():
    pass

def _validate_business_time():
    pass

def apply_index_wraps():
    pass

def as_datetime():
    pass

def get_day_of_month():
    "\n    Find the day in `other`'s month that satisfies a DateOffset's onOffset\n    policy, as described by the `day_opt` argument.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    day_opt : 'start', 'end', 'business_start', 'business_end', or int\n        'start': returns 1\n        'end': returns last day of the month\n        'business_start': returns the first business day of the month\n        'business_end': returns the last business day of the month\n        int: returns the day in the month indicated by `other`, or the last of\n            day the month if the value exceeds in that month's number of days.\n\n    Returns\n    -------\n    day_of_month : int\n\n    Examples\n    -------\n    >>> other = datetime(2017, 11, 14)\n    >>> get_day_of_month(other, 'start')\n    1\n    >>> get_day_of_month(other, 'end')\n    30\n\n    "
    pass

def get_firstbday():
    '\n    Find the first day of the month that is a business day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    first_bday : int\n    '
    pass

def get_lastbday():
    '\n    Find the last day of the month that is a business day.\n\n    Parameters\n    ----------\n    year : int\n    month : int\n\n    Returns\n    -------\n    last_bday : int\n    '
    pass

key = 'BAS-DEC'
need_suffix = _mod_builtins.list()
relativedelta = _mod_dateutil_relativedelta.relativedelta
relativedelta_kwds = _mod_builtins.set()
def roll_convention():
    '\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : int, generally the day component of a datetime\n    n : number of periods to increment, before adjusting for rolling\n    compare : int, generally the day component of a datetime, in the same\n              month as the datetime form which `other` was taken.\n\n    Returns\n    -------\n    n : int number of periods to increment\n    '
    pass

def roll_qtrday():
    "\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    n : number of periods to increment, before adjusting for rolling\n    month : int reference month giving the first month of the year\n    day_opt : 'start', 'end', 'business_start', 'business_end', or int\n        The convention to use in finding the day in a given month against\n        which to compare for rollforward/rollbackward decisions.\n    modby : int 3 for quarters, 12 for years\n\n    Returns\n    -------\n    n : int number of periods to increment\n\n    See Also\n    --------\n    get_day_of_month : Find the day in a month provided an offset.\n    "
    pass

def roll_yearday():
    "\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    n : number of periods to increment, before adjusting for rolling\n    month : reference month giving the first month of the year\n    day_opt : 'start', 'end', 'business_start', 'business_end', or int\n        The day of the month to compare against that of `other` when\n        incrementing or decrementing the number of periods:\n\n        'start': 1\n        'end': last day of the month\n        'business_start': first business day of the month\n        'business_end': last business day of the month\n        int: day in the month indicated by `other`, or the last of day\n            the month if the value exceeds in that month's number of days.\n\n    Returns\n    -------\n    n : int number of periods to increment\n\n    Notes\n    -----\n    * Mirrors `roll_check` in shift_months\n\n    Examples\n    -------\n    >>> month = 3\n    >>> day_opt = 'start'              # `other` will be compared to March 1\n    >>> other = datetime(2017, 2, 10)  # before March 1\n    >>> roll_yearday(other, 2, month, day_opt)\n    1\n    >>> roll_yearday(other, -7, month, day_opt)\n    -7\n    >>>\n    >>> other = Timestamp('2014-03-15', tz='US/Eastern')  # after March 1\n    >>> roll_yearday(other, 2, month, day_opt)\n    2\n    >>> roll_yearday(other, -7, month, day_opt)\n    -6\n\n    >>> month = 6\n    >>> day_opt = 'end'                # `other` will be compared to June 30\n    >>> other = datetime(1999, 6, 29)  # before June 30\n    >>> roll_yearday(other, 5, month, day_opt)\n    4\n    >>> roll_yearday(other, -7, month, day_opt)\n    -7\n    >>>\n    >>> other = Timestamp(2072, 8, 24, 6, 17, 18)  # after June 30\n    >>> roll_yearday(other, 5, month, day_opt)\n    5\n    >>> roll_yearday(other, -7, month, day_opt)\n    -6\n\n    "
    pass

def shift_day():
    "\n    Increment the datetime `other` by the given number of days, retaining\n    the time-portion of the datetime.  For tz-naive datetimes this is\n    equivalent to adding a timedelta.  For tz-aware datetimes it is similar to\n    dateutil's relativedelta.__add__, but handles pytz tzinfo objects.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    days : int\n\n    Returns\n    -------\n    shifted: datetime or Timestamp\n    "
    pass

def shift_month():
    "\n    Given a datetime (or Timestamp) `stamp`, an integer `months` and an\n    option `day_opt`, return a new datetimelike that many months later,\n    with day determined by `day_opt` using relativedelta semantics.\n\n    Scalar analogue of shift_months\n\n    Parameters\n    ----------\n    stamp : datetime or Timestamp\n    months : int\n    day_opt : None, 'start', 'end', 'business_start', 'business_end', or int\n        None: returned datetimelike has the same day as the input, or the\n              last day of the month if the new month is too short\n        'start': returned datetimelike has day=1\n        'end': returned datetimelike has day on the last day of the month\n        'business_start': returned datetimelike has day on the first\n            business day of the month\n        'business_end': returned datetimelike has day on the last\n            business day of the month\n        int: returned datetimelike has day equal to day_opt\n\n    Returns\n    -------\n    shifted : datetime or Timestamp (same as input `stamp`)\n    "
    pass

def shift_months():
    "\n    Given an int64-based datetime index, shift all elements\n    specified number of months using DateOffset semantics\n\n    day: {None, 'start', 'end'}\n       * None: day of month\n       * 'start' 1st day of month\n       * 'end' last day of month\n    "
    pass

def shift_quarters():
    "\n    Given an int64 array representing nanosecond timestamps, shift all elements\n    by the specified number of quarters using DateOffset semantics.\n\n    Parameters\n    ----------\n    dtindex : int64_t[:] timestamps for input dates\n    quarters : int number of quarters to shift\n    q1start_month : int month in which Q1 begins by convention\n    day : {'start', 'end', 'business_start', 'business_end'}\n    modby : int (3 for quarters, 12 for years)\n\n    Returns\n    -------\n    out : ndarray[int64_t]\n    "
    pass

