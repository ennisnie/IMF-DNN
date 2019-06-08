import builtins as _mod_builtins
import datetime as _mod_datetime

NaT = NaTType()
class NaTType(_NaT):
    '(N)ot-(A)-(T)ime, the time equivalent of NaN'
    __class__ = NaTType
    __dict__ = {}
    def __init__(self):
        '(N)ot-(A)-(T)ime, the time equivalent of NaN'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __rdiv__(self, other):
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __reduce_ex__(self, protocol):
        return ''; return ()
    
    def __rfloordiv__(self, other):
        return NaTType()
    
    def __rmul__(self, other):
        return NaTType()
    
    def __rtruediv__(self, other):
        return NaTType()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def astimezone(self, *args, **kwargs):
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        pass
    
    def ceil(self, *args, **kwargs):
        "\n        return a new Timestamp ceiled to this resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the ceiling resolution\n        ambiguous : bool, 'NaT', default 'raise'\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n            .. versionadded:: 0.24.0\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    def combine(self, *args, **kwargs):
        '\n        Timsetamp.combine(date, time)\n\n        date, time -> datetime with same date and time fields\n        '
        pass
    
    def ctime(self, *args, **kwargs):
        'Return ctime() style string.'
        pass
    
    def date(self, *args, **kwargs):
        'Return date object with same year, month and day.'
        pass
    
    day = _mod_builtins.property()
    def day_name(self, *args, **kwargs):
        '\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : string, default None (English locale)\n            locale determining the language in which to return the day name\n\n        Returns\n        -------\n        day_name : string\n\n        .. versionadded:: 0.23.0\n        '
        pass
    
    dayofweek = _mod_builtins.property()
    dayofyear = _mod_builtins.property()
    days = _mod_builtins.property()
    days_in_month = _mod_builtins.property()
    daysinmonth = _mod_builtins.property()
    def dst(self, *args, **kwargs):
        'Return self.tzinfo.dst(self).'
        pass
    
    def floor(self, *args, **kwargs):
        "\n        return a new Timestamp floored to this resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the flooring resolution\n        ambiguous : bool, 'NaT', default 'raise'\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n            .. versionadded:: 0.24.0\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    def fromordinal(self, *args, **kwargs):
        '\n        Timestamp.fromordinal(ordinal, freq=None, tz=None)\n\n        passed an ordinal, translate and convert to a ts\n        note: by definition there cannot be any tz info on the ordinal itself\n\n        Parameters\n        ----------\n        ordinal : int\n            date corresponding to a proleptic Gregorian ordinal\n        freq : str, DateOffset\n            Offset which Timestamp will have\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will have.\n        '
        pass
    
    def fromtimestamp(self, *args, **kwargs):
        "\n        Timestamp.fromtimestamp(ts)\n\n        timestamp[, tz] -> tz's local time from POSIX timestamp.\n        "
        pass
    
    hour = _mod_builtins.property()
    def isocalendar(self, *args, **kwargs):
        'Return a 3-tuple containing ISO year, week number, and weekday.'
        pass
    
    def isoweekday(self, *args, **kwargs):
        'Return the day of the week represented by the date.\nMonday == 1 ... Sunday == 7'
        pass
    
    microsecond = _mod_builtins.property()
    microseconds = _mod_builtins.property()
    millisecond = _mod_builtins.property()
    minute = _mod_builtins.property()
    month = _mod_builtins.property()
    def month_name(self, *args, **kwargs):
        '\n        Return the month name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : string, default None (English locale)\n            locale determining the language in which to return the month name\n\n        Returns\n        -------\n        month_name : string\n\n        .. versionadded:: 0.23.0\n        '
        pass
    
    nanosecond = _mod_builtins.property()
    nanoseconds = _mod_builtins.property()
    def now(self, *args, **kwargs):
        '\n        Timestamp.now(tz=None)\n\n        Returns new Timestamp object representing current time local to\n        tz.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to\n        '
        pass
    
    quarter = _mod_builtins.property()
    qyear = _mod_builtins.property()
    def replace(self, *args, **kwargs):
        '\n        implements datetime.replace, handles nanoseconds\n\n        Parameters\n        ----------\n        year : int, optional\n        month : int, optional\n        day : int, optional\n        hour : int, optional\n        minute : int, optional\n        second : int, optional\n        microsecond : int, optional\n        nanosecond : int, optional\n        tzinfo : tz-convertible, optional\n        fold : int, optional, default is 0\n            added in 3.6, NotImplemented\n\n        Returns\n        -------\n        Timestamp with fields replaced\n        '
        pass
    
    def round(self, *args, **kwargs):
        "\n        Round the Timestamp to the specified resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the rounding resolution\n        ambiguous : bool, 'NaT', default 'raise'\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n            .. versionadded:: 0.24.0\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    second = _mod_builtins.property()
    seconds = _mod_builtins.property()
    def strftime(self, *args, **kwargs):
        'format -> strftime() style string.'
        return ''
    
    def strptime(self, *args, **kwargs):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    def time(self, *args, **kwargs):
        'Return time object with same time but with tzinfo=None.'
        pass
    
    def timestamp(self, *args, **kwargs):
        'Return POSIX timestamp as float.'
        pass
    
    def timetuple(self, *args, **kwargs):
        'Return time tuple, compatible with time.localtime().'
        pass
    
    def timetz(self, *args, **kwargs):
        'Return time object with same time and tzinfo.'
        pass
    
    def to_pydatetime(self, *args, **kwargs):
        '\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n        '
        pass
    
    def today(self, *args, **kwargs):
        '\n        Timestamp.today(cls, tz=None)\n\n        Return the current time in the local timezone.  This differs\n        from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to\n        '
        pass
    
    def toordinal(self, *args, **kwargs):
        'Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.'
        pass
    
    def tz_convert(self, *args, **kwargs):
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        pass
    
    def tz_localize(self, *args, **kwargs):
        "\n        Convert naive Timestamp to local time zone, or remove\n        timezone from tz-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        errors : 'raise', 'coerce', default None\n            - 'raise' will raise a NonExistentTimeError if a timestamp is not\n               valid in the specified timezone (e.g. due to a transition from\n               or to DST time). Use ``nonexistent='raise'`` instead.\n            - 'coerce' will return NaT if the timestamp can not be converted\n              into the specified timezone. Use ``nonexistent='NaT'`` instead.\n\n              .. deprecated:: 0.24.0\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n        "
        pass
    
    def tzname(self, *args, **kwargs):
        'Return self.tzinfo.tzname(self).'
        pass
    
    def utcfromtimestamp(self, *args, **kwargs):
        '\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a naive UTC datetime from a POSIX timestamp.\n        '
        pass
    
    def utcnow(self, *args, **kwargs):
        '\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n        '
        pass
    
    def utcoffset(self, *args, **kwargs):
        'Return self.tzinfo.utcoffset(self).'
        pass
    
    def utctimetuple(self, *args, **kwargs):
        'Return UTC time tuple, compatible with time.localtime().'
        pass
    
    week = _mod_builtins.property()
    def weekday(self, *args, **kwargs):
        'Return the day of the week represented by the date.\nMonday == 0 ... Sunday == 6'
        pass
    
    weekday_name = _mod_builtins.property()
    weekofyear = _mod_builtins.property()
    year = _mod_builtins.property()

class _NaT(_mod_datetime.datetime):
    def __add__(self, value):
        'Return self+value.'
        return _NaT()
    
    __class__ = _NaT
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __floordiv__(self, value):
        'Return self//value.'
        return 0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return _NaT()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return _NaT()
    
    def __pos__(self):
        '+self'
        return _NaT()
    
    def __radd__(self, value):
        'Return value+self.'
        return _NaT()
    
    def __reduce_cython__(self):
        pass
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rfloordiv__(self, value):
        'Return value//self.'
        return _NaT()
    
    def __rmul__(self, value):
        'Return value*self.'
        return _NaT()
    
    def __rsub__(self, value):
        'Return value-self.'
        return _NaT()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return _NaT()
    
    def __setstate_cython__(self):
        pass
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    def __sub__(self, value):
        'Return self-value.'
        return _NaT()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def asm8(self):
        pass
    
    @classmethod
    def combine(cls):
        'date, time -> datetime with same date and time fields'
        pass
    
    @property
    def freq(self):
        pass
    
    @classmethod
    def fromordinal(cls):
        'int -> date corresponding to a proleptic Gregorian ordinal.'
        pass
    
    @classmethod
    def fromtimestamp(cls):
        "timestamp[, tz] -> tz's local time from POSIX timestamp."
        pass
    
    @property
    def is_leap_year(self):
        pass
    
    @property
    def is_month_end(self):
        pass
    
    @property
    def is_month_start(self):
        pass
    
    @property
    def is_quarter_end(self):
        pass
    
    @property
    def is_quarter_start(self):
        pass
    
    @property
    def is_year_end(self):
        pass
    
    @property
    def is_year_start(self):
        pass
    
    def isoformat(self):
        pass
    
    @classmethod
    def now(cls, type, tz):
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    def to_datetime64(self):
        " Returns a numpy.datetime64 object with 'ns' precision "
        pass
    
    @classmethod
    def today(cls):
        'Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).'
        pass
    
    def total_seconds(self):
        '\n        Total duration of timedelta in seconds (to ns precision)\n        '
        pass
    
    @classmethod
    def utcfromtimestamp(cls):
        'Construct a naive UTC datetime from a POSIX timestamp.'
        pass
    
    @classmethod
    def utcnow(cls):
        'Return a new datetime representing UTC day and time.'
        pass
    
    @property
    def value(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/nattype.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.nattype'
def __nat_unpickle():
    pass

__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle__NaT():
    pass

__test__ = _mod_builtins.dict()
def _make_error_func():
    pass

def _make_nan_func():
    pass

def _make_nat_func():
    pass

iNaT = -9223372036854775808
def is_null_datetimelike():
    '\n    Determine if we have a null for a timedelta/datetime (or integer versions)\n\n    Parameters\n    ----------\n    val : object\n    inat_is_null : bool, default True\n        Whether to treat integer iNaT value as null\n\n    Returns\n    -------\n    null_datetimelike : bool\n    '
    pass

nat_strings = _mod_builtins.set()
