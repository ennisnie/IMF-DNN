import _io as _mod__io
import builtins as _mod_builtins
import datetime as _mod_datetime
import dateutil.parser._parser as _mod_dateutil_parser__parser
import dateutil.relativedelta as _mod_dateutil_relativedelta
import dateutil.tz.tz as _mod_dateutil_tz_tz
import pandas._libs.tslibs.nattype as _mod_pandas__libs_tslibs_nattype

DEFAULTPARSER = _mod_dateutil_parser__parser.parser()
class DateParseError(_mod_builtins.ValueError):
    __class__ = DateParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.parsing'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

MONTH_NUMBERS = _mod_builtins.dict()
NaT = _mod_pandas__libs_tslibs_nattype.NaTType()
StringIO = _mod__io.StringIO
def _DATEUTIL_LEXER_SPLIT(cls, s):
    pass

_DEFAULT_DATETIME = _mod_datetime.datetime()
__builtins__ = {}
__doc__ = '\nParsing functions for datetime and datetime-like strings.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/parsing.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.parsing'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
_dateutil_tzlocal = _mod_dateutil_tz_tz.tzlocal
_dateutil_tzstr = _mod_dateutil_tz_tz.tzstr
_dateutil_tzutc = _mod_dateutil_tz_tz.tzutc
def _does_string_look_like_datetime():
    pass

def _format_is_iso():
    '\n    Does format match the iso8601 set that can be handled by the C parser?\n    Generally of form YYYY-MM-DDTHH:MM:SS - date separator can be different\n    but must be consistent.  Leading 0s in dates and times are optional.\n    '
    pass

_get_option = None
def _guess_datetime_format():
    "\n    Guess the datetime format of a given datetime string.\n\n    Parameters\n    ----------\n    dt_str : string, datetime string to guess the format of\n    dayfirst : boolean, default False\n        If True parses dates with the day first, eg 20/01/2005\n        Warning: dayfirst=True is not strict, but will prefer to parse\n        with day first (this is a known bug).\n    dt_str_parse : function, defaults to `compat.parse_date` (dateutil)\n        This function should take in a datetime string and return\n        a `datetime.datetime` guess that the datetime string represents\n    dt_str_split : function, defaults to `_DATEUTIL_LEXER_SPLIT` (dateutil)\n        This function should take in a datetime string and return\n        a list of strings, the guess of the various specific parts\n        e.g. '2011/12/30' -> ['2011', '/', '12', '/', '30']\n\n    Returns\n    -------\n    ret : datetime format string (for `strftime` or `strptime`)\n    "
    pass

class _timelex(_mod_builtins.object):
    __class__ = _timelex
    __dict__ = {}
    def __init__(self, instream):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.parsing'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def get_tokens(self):
        '\n        This function breaks the time string into lexical units (tokens), which\n        can be parsed by the parser. Lexical units are demarcated by changes in\n        the character set, so any continuous string of letters is considered\n        one unit, any continuous string of numbers is considered one unit.\n        The main complication arises from the fact that dots (\'.\') can be used\n        both as separators (e.g. "Sep.20.2009") or decimal points (e.g.\n        "4:30:21.447"). As such, it is necessary to read the full context of\n        any dot-separated strings before breaking it into tokens; as such, this\n        function maintains a "token stack", for when the ambiguous context\n        demands that multiple tokens be parsed at once.\n        '
        pass
    
    def split(self, cls, s):
        pass
    

binary_type = _mod_builtins.bytes
def du_parse(timestr, parserinfo, **kwargs):
    '\n\n    Parse a string in one of the supported formats, using the\n    ``parserinfo`` parameters.\n\n    :param timestr:\n        A string containing a date/time stamp.\n\n    :param parserinfo:\n        A :class:`parserinfo` object containing parameters for the parser.\n        If ``None``, the default arguments to the :class:`parserinfo`\n        constructor are used.\n\n    The ``**kwargs`` parameter takes the following keyword arguments:\n\n    :param default:\n        The default datetime object, if this is a datetime object and not\n        ``None``, elements specified in ``timestr`` replace elements in the\n        default object.\n\n    :param ignoretz:\n        If set ``True``, time zones in parsed strings are ignored and a naive\n        :class:`datetime` object is returned.\n\n    :param tzinfos:\n        Additional time zone names / aliases which may be present in the\n        string. This argument maps time zone names (and optionally offsets\n        from those time zones) to time zones. This parameter can be a\n        dictionary with timezone aliases mapping time zone names to time\n        zones or a function taking two parameters (``tzname`` and\n        ``tzoffset``) and returning a time zone.\n\n        The timezones to which the names are mapped can be an integer\n        offset from UTC in seconds or a :class:`tzinfo` object.\n\n        .. doctest::\n           :options: +NORMALIZE_WHITESPACE\n\n            >>> from dateutil.parser import parse\n            >>> from dateutil.tz import gettz\n            >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}\n            >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)\n            datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u\'BRST\', -7200))\n            >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)\n            datetime.datetime(2012, 1, 19, 17, 21,\n                              tzinfo=tzfile(\'/usr/share/zoneinfo/America/Chicago\'))\n\n        This parameter is ignored if ``ignoretz`` is set.\n\n    :param dayfirst:\n        Whether to interpret the first value in an ambiguous 3-integer date\n        (e.g. 01/05/09) as the day (``True``) or month (``False``). If\n        ``yearfirst`` is set to ``True``, this distinguishes between YDM and\n        YMD. If set to ``None``, this value is retrieved from the current\n        :class:`parserinfo` object (which itself defaults to ``False``).\n\n    :param yearfirst:\n        Whether to interpret the first value in an ambiguous 3-integer date\n        (e.g. 01/05/09) as the year. If ``True``, the first number is taken to\n        be the year, otherwise the last number is taken to be the year. If\n        this is set to ``None``, the value is retrieved from the current\n        :class:`parserinfo` object (which itself defaults to ``False``).\n\n    :param fuzzy:\n        Whether to allow fuzzy parsing, allowing for string like "Today is\n        January 1, 2047 at 8:21:00AM".\n\n    :param fuzzy_with_tokens:\n        If ``True``, ``fuzzy`` is automatically set to True, and the parser\n        will return a tuple where the first element is the parsed\n        :class:`datetime.datetime` datetimestamp and the second element is\n        a tuple containing the portions of the string which were ignored:\n\n        .. doctest::\n\n            >>> from dateutil.parser import parse\n            >>> parse("Today is January 1, 2047 at 8:21:00AM", fuzzy_with_tokens=True)\n            (datetime.datetime(2047, 1, 1, 8, 21), (u\'Today is \', u\' \', u\'at \'))\n\n    :return:\n        Returns a :class:`datetime.datetime` object or, if the\n        ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the\n        first element being a :class:`datetime.datetime` object, the second\n        a tuple containing the fuzzy tokens.\n\n    :raises ValueError:\n        Raised for invalid or unknown string format, if the provided\n        :class:`tzinfo` is not in a valid format, or if an invalid date\n        would be created.\n\n    :raises OverflowError:\n        Raised if the parsed date exceeds the largest valid C integer on\n        your system.\n    '
    pass

def get_option():
    ' Defer import of get_option to break an import cycle that caused\n    significant performance degradation in Period construction. See\n    GH#24118 for details\n    '
    pass

nat_strings = _mod_builtins.set()
def parse_datetime_string():
    'parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    pass

def parse_time_string():
    '\n    Try hard to parse datetime string, leveraging dateutil plus some extra\n    goodies like quarter recognition.\n\n    Parameters\n    ----------\n    arg : compat.string_types\n    freq : str or DateOffset, default None\n        Helps with interpreting time string if supplied\n    dayfirst : bool, default None\n        If None uses default from print_config\n    yearfirst : bool, default None\n        If None uses default from print_config\n\n    Returns\n    -------\n    datetime, datetime/dateutil.parser._result, str\n    '
    pass

relativedelta = _mod_dateutil_relativedelta.relativedelta
text_type = _mod_builtins.str
def try_parse_date_and_time():
    pass

def try_parse_dates():
    pass

def try_parse_datetime_components():
    pass

def try_parse_year_month_day():
    pass

tzoffset = _mod_dateutil_tz_tz.tzoffset
