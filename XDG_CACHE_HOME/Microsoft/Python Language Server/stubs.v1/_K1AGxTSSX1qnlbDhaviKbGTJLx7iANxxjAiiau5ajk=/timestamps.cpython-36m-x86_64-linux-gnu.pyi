import builtins as _mod_builtins
import datetime as _mod_datetime
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pandas._libs.tslibs.timedeltas as _mod_pandas__libs_tslibs_timedeltas
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

DAY_SECONDS = 86400
OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
class RoundTo(_mod_builtins.object):
    '\n    enumeration defining the available rounding modes\n\n    Attributes\n    ----------\n    MINUS_INFTY\n        round towards -∞, or floor [2]_\n    PLUS_INFTY\n        round towards +∞, or ceil [3]_\n    NEAREST_HALF_EVEN\n        round to nearest, tie-break half to even [6]_\n    NEAREST_HALF_MINUS_INFTY\n        round to nearest, tie-break half to -∞ [5]_\n    NEAREST_HALF_PLUS_INFTY\n        round to nearest, tie-break half to +∞ [4]_\n\n\n    References\n    ----------\n    .. [1] "Rounding - Wikipedia"\n           https://en.wikipedia.org/wiki/Rounding\n    .. [2] "Rounding down"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\n    .. [3] "Rounding up"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\n    .. [4] "Round half up"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\n    .. [5] "Round half down"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\n    .. [6] "Round half to even"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\n    '
    MINUS_INFTY = _mod_builtins.property()
    NEAREST_HALF_EVEN = _mod_builtins.property()
    NEAREST_HALF_MINUS_INFTY = _mod_builtins.property()
    NEAREST_HALF_PLUS_INFTY = _mod_builtins.property()
    PLUS_INFTY = _mod_builtins.property()
    __class__ = RoundTo
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        '\n    enumeration defining the available rounding modes\n\n    Attributes\n    ----------\n    MINUS_INFTY\n        round towards -∞, or floor [2]_\n    PLUS_INFTY\n        round towards +∞, or ceil [3]_\n    NEAREST_HALF_EVEN\n        round to nearest, tie-break half to even [6]_\n    NEAREST_HALF_MINUS_INFTY\n        round to nearest, tie-break half to -∞ [5]_\n    NEAREST_HALF_PLUS_INFTY\n        round to nearest, tie-break half to +∞ [4]_\n\n\n    References\n    ----------\n    .. [1] "Rounding - Wikipedia"\n           https://en.wikipedia.org/wiki/Rounding\n    .. [2] "Rounding down"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_down\n    .. [3] "Rounding up"\n           https://en.wikipedia.org/wiki/Rounding#Rounding_up\n    .. [4] "Round half up"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_up\n    .. [5] "Round half down"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_down\n    .. [6] "Round half to even"\n           https://en.wikipedia.org/wiki/Rounding#Round_half_to_even\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.timestamps'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

Timedelta = _mod_pandas__libs_tslibs_timedeltas.Timedelta
class Timestamp(_Timestamp):
    "Pandas replacement for datetime.datetime\n\n    Timestamp is the pandas equivalent of python's Datetime\n    and is interchangeable with it in most cases. It's the type used\n    for the entries that make up a DatetimeIndex, and other timeseries\n    oriented data structures in pandas.\n\n    Parameters\n    ----------\n    ts_input : datetime-like, str, int, float\n        Value to be converted to Timestamp\n    freq : str, DateOffset\n        Offset which Timestamp will have\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\n        Time zone for time which Timestamp will have.\n    unit : str\n        Unit used for conversion if ts_input is of type int or float. The\n        valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For\n        example, 's' means seconds and 'ms' means milliseconds.\n    year, month, day : int\n        .. versionadded:: 0.19.0\n    hour, minute, second, microsecond : int, optional, default 0\n        .. versionadded:: 0.19.0\n    nanosecond : int, optional, default 0\n        .. versionadded:: 0.23.0\n    tzinfo : datetime.tzinfo, optional, default None\n        .. versionadded:: 0.19.0\n\n    Notes\n    -----\n    There are essentially three calling conventions for the constructor. The\n    primary form accepts four parameters. They can be passed by position or\n    keyword.\n\n    The other two forms mimic the parameters from ``datetime.datetime``. They\n    can be passed by either position or keyword, but not both mixed together.\n\n    Examples\n    --------\n    Using the primary calling convention:\n\n    This converts a datetime-like string\n    >>> pd.Timestamp('2017-01-01T12')\n    Timestamp('2017-01-01 12:00:00')\n\n    This converts a float representing a Unix epoch in units of seconds\n    >>> pd.Timestamp(1513393355.5, unit='s')\n    Timestamp('2017-12-16 03:02:35.500000')\n\n    This converts an int representing a Unix-epoch in units of seconds\n    and for a particular timezone\n    >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')\n    Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')\n\n    Using the other two forms that mimic the API for ``datetime.datetime``:\n\n    >>> pd.Timestamp(2017, 1, 1, 12)\n    Timestamp('2017-01-01 12:00:00')\n\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\n    Timestamp('2017-01-01 12:00:00')\n    "
    __class__ = Timestamp
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        "Pandas replacement for datetime.datetime\n\n    Timestamp is the pandas equivalent of python's Datetime\n    and is interchangeable with it in most cases. It's the type used\n    for the entries that make up a DatetimeIndex, and other timeseries\n    oriented data structures in pandas.\n\n    Parameters\n    ----------\n    ts_input : datetime-like, str, int, float\n        Value to be converted to Timestamp\n    freq : str, DateOffset\n        Offset which Timestamp will have\n    tz : str, pytz.timezone, dateutil.tz.tzfile or None\n        Time zone for time which Timestamp will have.\n    unit : str\n        Unit used for conversion if ts_input is of type int or float. The\n        valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For\n        example, 's' means seconds and 'ms' means milliseconds.\n    year, month, day : int\n        .. versionadded:: 0.19.0\n    hour, minute, second, microsecond : int, optional, default 0\n        .. versionadded:: 0.19.0\n    nanosecond : int, optional, default 0\n        .. versionadded:: 0.23.0\n    tzinfo : datetime.tzinfo, optional, default None\n        .. versionadded:: 0.19.0\n\n    Notes\n    -----\n    There are essentially three calling conventions for the constructor. The\n    primary form accepts four parameters. They can be passed by position or\n    keyword.\n\n    The other two forms mimic the parameters from ``datetime.datetime``. They\n    can be passed by either position or keyword, but not both mixed together.\n\n    Examples\n    --------\n    Using the primary calling convention:\n\n    This converts a datetime-like string\n    >>> pd.Timestamp('2017-01-01T12')\n    Timestamp('2017-01-01 12:00:00')\n\n    This converts a float representing a Unix epoch in units of seconds\n    >>> pd.Timestamp(1513393355.5, unit='s')\n    Timestamp('2017-12-16 03:02:35.500000')\n\n    This converts an int representing a Unix-epoch in units of seconds\n    and for a particular timezone\n    >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')\n    Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')\n\n    Using the other two forms that mimic the API for ``datetime.datetime``:\n\n    >>> pd.Timestamp(2017, 1, 1, 12)\n    Timestamp('2017-01-01 12:00:00')\n\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\n    Timestamp('2017-01-01 12:00:00')\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __radd__(self, other):
        return Timestamp()
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _has_time_component(self):
        '\n        Returns if the Timestamp has a time component\n        in addition to the date part\n        '
        pass
    
    def _round(self, freq, mode, ambiguous, nonexistent):
        pass
    
    def astimezone(self, tz):
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        pass
    
    def ceil(self, freq, ambiguous, nonexistent):
        "\n        return a new Timestamp ceiled to this resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the ceiling resolution\n        ambiguous : bool, 'NaT', default 'raise'\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n            .. versionadded:: 0.24.0\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    def combine(self, cls, date, time):
        '\n        Timsetamp.combine(date, time)\n\n        date, time -> datetime with same date and time fields\n        '
        pass
    
    def day_name(self, locale):
        '\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : string, default None (English locale)\n            locale determining the language in which to return the day name\n\n        Returns\n        -------\n        day_name : string\n\n        .. versionadded:: 0.23.0\n        '
        pass
    
    dayofweek = _mod_builtins.property()
    dayofyear = _mod_builtins.property()
    days_in_month = _mod_builtins.property()
    daysinmonth = _mod_builtins.property()
    def floor(self, freq, ambiguous, nonexistent):
        "\n        return a new Timestamp floored to this resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the flooring resolution\n        ambiguous : bool, 'NaT', default 'raise'\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n            .. versionadded:: 0.24.0\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    freqstr = _mod_builtins.property()
    def fromordinal(self, cls, ordinal, freq, tz):
        '\n        Timestamp.fromordinal(ordinal, freq=None, tz=None)\n\n        passed an ordinal, translate and convert to a ts\n        note: by definition there cannot be any tz info on the ordinal itself\n\n        Parameters\n        ----------\n        ordinal : int\n            date corresponding to a proleptic Gregorian ordinal\n        freq : str, DateOffset\n            Offset which Timestamp will have\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will have.\n        '
        pass
    
    def fromtimestamp(self, cls, ts):
        "\n        Timestamp.fromtimestamp(ts)\n\n        timestamp[, tz] -> tz's local time from POSIX timestamp.\n        "
        pass
    
    is_leap_year = _mod_builtins.property()
    is_month_end = _mod_builtins.property()
    is_month_start = _mod_builtins.property()
    is_quarter_end = _mod_builtins.property()
    is_quarter_start = _mod_builtins.property()
    is_year_end = _mod_builtins.property()
    is_year_start = _mod_builtins.property()
    def isoformat(self, sep):
        pass
    
    max = Timestamp()
    min = Timestamp()
    def month_name(self, locale):
        '\n        Return the month name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : string, default None (English locale)\n            locale determining the language in which to return the month name\n\n        Returns\n        -------\n        month_name : string\n\n        .. versionadded:: 0.23.0\n        '
        pass
    
    def normalize(self):
        '\n        Normalize Timestamp to midnight, preserving\n        tz information.\n        '
        pass
    
    def now(self, cls, tz):
        '\n        Timestamp.now(tz=None)\n\n        Returns new Timestamp object representing current time local to\n        tz.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to\n        '
        pass
    
    quarter = _mod_builtins.property()
    def replace(self, year, month, day, hour, minute, second, microsecond, nanosecond, tzinfo, fold):
        '\n        implements datetime.replace, handles nanoseconds\n\n        Parameters\n        ----------\n        year : int, optional\n        month : int, optional\n        day : int, optional\n        hour : int, optional\n        minute : int, optional\n        second : int, optional\n        microsecond : int, optional\n        nanosecond : int, optional\n        tzinfo : tz-convertible, optional\n        fold : int, optional, default is 0\n            added in 3.6, NotImplemented\n\n        Returns\n        -------\n        Timestamp with fields replaced\n        '
        pass
    
    def round(self, freq, ambiguous, nonexistent):
        "\n        Round the Timestamp to the specified resolution\n\n        Parameters\n        ----------\n        freq : a freq string indicating the rounding resolution\n        ambiguous : bool, 'NaT', default 'raise'\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n            .. versionadded:: 0.24.0\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n        "
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    def to_julian_date(self):
        '\n        Convert TimeStamp to a Julian Date.\n        0 Julian date is noon January 1, 4713 BC.\n        '
        pass
    
    def to_period(self, freq):
        '\n        Return an period of which this timestamp is an observation.\n        '
        pass
    
    def today(self, cls, tz):
        '\n        Timestamp.today(cls, tz=None)\n\n        Return the current time in the local timezone.  This differs\n        from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to\n        '
        pass
    
    tz = _mod_builtins.property()
    def tz_convert(self, tz):
        '\n        Convert tz-aware Timestamp to another time zone.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n        '
        pass
    
    def tz_localize(self, tz, ambiguous, nonexistent, errors):
        "\n        Convert naive Timestamp to local time zone, or remove\n        timezone from tz-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            - bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates)\n            - 'NaT' will return NaT for an ambiguous time\n            - 'raise' will raise an AmbiguousTimeError for an ambiguous time\n\n        nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta,\n                      default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            - 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time\n            - 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time\n            - 'NaT' will return NaT where there are nonexistent times\n            - timedelta objects will shift nonexistent times by the timedelta\n            - 'raise' will raise an NonExistentTimeError if there are\n              nonexistent times\n\n            .. versionadded:: 0.24.0\n\n        errors : 'raise', 'coerce', default None\n            - 'raise' will raise a NonExistentTimeError if a timestamp is not\n               valid in the specified timezone (e.g. due to a transition from\n               or to DST time). Use ``nonexistent='raise'`` instead.\n            - 'coerce' will return NaT if the timestamp can not be converted\n              into the specified timezone. Use ``nonexistent='NaT'`` instead.\n\n              .. deprecated:: 0.24.0\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n        "
        pass
    
    def utcfromtimestamp(self, cls, ts):
        '\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a naive UTC datetime from a POSIX timestamp.\n        '
        pass
    
    def utcnow(self, cls):
        '\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n        '
        pass
    
    week = _mod_builtins.property()
    weekday_name = _mod_builtins.property()
    weekofyear = _mod_builtins.property()

UTC = _mod_pytz.UTC()
class _Timestamp(_mod_datetime.datetime):
    def __add__(self, value):
        'Return self+value.'
        return _Timestamp()
    
    __class__ = _Timestamp
    def __eq__(self, value):
        'Return self==value.'
        return False
    
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
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __radd__(self, value):
        'Return value+self.'
        return _Timestamp()
    
    def __reduce_ex__(self, protocol):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rsub__(self, value):
        'Return value-self.'
        return _Timestamp()
    
    def __sub__(self, value):
        'Return self-value.'
        return _Timestamp()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _date_attributes(self):
        pass
    
    @property
    def _date_repr(self):
        pass
    
    def _get_date_name_field(self):
        pass
    
    def _get_start_end_field(self):
        pass
    
    @property
    def _repr_base(self):
        pass
    
    @property
    def _short_repr(self):
        pass
    
    @property
    def _time_repr(self):
        pass
    
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
    def nanosecond(self):
        pass
    
    @classmethod
    def now(cls, type, tz):
        'Returns new datetime object representing current time local to tz.\n\n  tz\n    Timezone object.\n\nIf no tz is specified, uses local timezone.'
        pass
    
    @property
    def resolution(self):
        '\n        Return resolution describing the smallest difference between two\n        times that can be represented by Timestamp object_state\n        '
        pass
    
    @classmethod
    def strptime(cls):
        'string, format -> new datetime parsed from a string (like time.strptime()).'
        pass
    
    def timestamp(self):
        'Return POSIX timestamp as float.'
        pass
    
    def to_datetime64(self):
        " Returns a numpy.datetime64 object with 'ns' precision "
        pass
    
    def to_pydatetime(self):
        '\n        Convert a Timestamp object to a native Python datetime object.\n\n        If warn=True, issue a warning if nanoseconds is nonzero.\n        '
        pass
    
    @classmethod
    def today(cls):
        'Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).'
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
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/timestamps.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.timestamps'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
_no_input = _mod_builtins.object()
_zero_time = _mod_datetime.time()
datetime_time = _mod_datetime.time
def get_date_name_field():
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. weekday_name)\n    '
    pass

def get_start_end_field():
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    pass

def maybe_integer_op_deprecated():
    pass

def normalize_i8_timestamps():
    '\n    Normalize each of the (nanosecond) timezone aware timestamps in the given\n    array by rounding down to the beginning of the day (i.e. midnight).\n    This is midnight for timezone, `tz`.\n\n    Parameters\n    ----------\n    stamps : int64 ndarray\n    tz : tzinfo or None\n\n    Returns\n    -------\n    result : int64 ndarray of converted of normalized nanosecond timestamps\n    '
    pass

def npdivmod():
    "divmod(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nReturn element-wise quotient and remainder simultaneously.\n\n.. versionadded:: 1.13.0\n\n``np.divmod(x, y)`` is equivalent to ``(x // y, x % y)``, but faster\nbecause it avoids redundant work. It is used to implement the Python\nbuilt-in function ``divmod`` on NumPy arrays.\n\nParameters\n----------\nx1 : array_like\n    Dividend array.\nx2 : array_like\n    Divisor array.\nout : ndarray, None, or tuple of ndarray and None, optional\n    A location into which the result is stored. If provided, it must have\n    a shape that the inputs broadcast to. If not provided or `None`,\n    a freshly-allocated array is returned. A tuple (possible only as a\n    keyword argument) must have length equal to the number of outputs.\nwhere : array_like, optional\n    Values of True indicate to calculate the ufunc at that position, values\n    of False indicate to leave the value in the output alone.\n**kwargs\n    For other keyword-only arguments, see the\n    :ref:`ufunc docs <ufuncs.kwargs>`.\n\nReturns\n-------\nout1 : ndarray\n    Element-wise quotient resulting from floor division.\n    This is a scalar if both `x1` and `x2` are scalars.\nout2 : ndarray\n    Element-wise remainder from floor division.\n    This is a scalar if both `x1` and `x2` are scalars.\n\nSee Also\n--------\nfloor_divide : Equivalent to Python's ``//`` operator.\nremainder : Equivalent to Python's ``%`` operator.\nmodf : Equivalent to ``divmod(x, 1)`` for positive ``x`` with the return\n       values switched.\n\nExamples\n--------\n>>> np.divmod(np.arange(5), 3)\n(array([0, 0, 0, 1, 1]), array([0, 1, 2, 0, 1]))"
    pass

def round_nsint64():
    '\n    Applies rounding mode at given frequency\n\n    Parameters\n    ----------\n    values : :obj:`ndarray`\n    mode : instance of `RoundTo` enumeration\n    freq : str, obj\n\n    Returns\n    -------\n    :obj:`ndarray`\n    '
    pass

timedelta = _mod_datetime.timedelta
def tz_localize_to_utc():
    '\n    Localize tzinfo-naive i8 to given time zone (using pytz). If\n    there are ambiguities in the values, raise AmbiguousTimeError.\n\n    Parameters\n    ----------\n    vals : ndarray[int64_t]\n    tz : tzinfo or None\n    ambiguous : str, bool, or arraylike\n        When clocks moved backward due to DST, ambiguous times may arise.\n        For example in Central European Time (UTC+01), when going from 03:00\n        DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC\n        and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter\n        dictates how ambiguous times should be handled.\n\n        - \'infer\' will attempt to infer fall dst-transition hours based on\n          order\n        - bool-ndarray where True signifies a DST time, False signifies a\n          non-DST time (note that this flag is only applicable for ambiguous\n          times, but the array must have the same length as vals)\n        - bool if True, treat all vals as DST. If False, treat them as non-DST\n        - \'NaT\' will return NaT where there are ambiguous times\n\n    nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise",\n                   timedelta-like}\n        How to handle non-existent times when converting wall times to UTC\n\n        .. versionadded:: 0.24.0\n\n    Returns\n    -------\n    localized : ndarray[int64_t]\n    '
    pass

