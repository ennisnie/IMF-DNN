import _thread as _mod__thread
import builtins as _mod_builtins
import datetime as _mod_datetime

class LocaleTime(_mod_builtins.object):
    'Stores and handles locale-specific information related to time.\n\n    ATTRIBUTES:\n        f_weekday -- full weekday names (7-item list)\n        a_weekday -- abbreviated weekday names (7-item list)\n        f_month -- full month names (13-item list; dummy value in [0], which\n                    is added by code)\n        a_month -- abbreviated month names (13-item list, dummy value in\n                    [0], which is added by code)\n        am_pm -- AM/PM representation (2-item list)\n        LC_date_time -- format string for date/time representation (string)\n        LC_date -- format string for date representation (string)\n        LC_time -- format string for time representation (string)\n        timezone -- daylight- and non-daylight-savings timezone representation\n                    (2-item list of sets)\n        lang -- Language used by instance (2-item tuple)\n    '
    def _LocaleTime__calc_am_pm(self):
        pass
    
    def _LocaleTime__calc_date_time(self):
        pass
    
    def _LocaleTime__calc_month(self):
        pass
    
    def _LocaleTime__calc_timezone(self):
        pass
    
    def _LocaleTime__calc_weekday(self):
        pass
    
    def _LocaleTime__pad(self, seq, front):
        pass
    
    __class__ = LocaleTime
    __dict__ = {}
    def __init__(self):
        'Set all attributes.\n\n        Order of methods called matters for dependency reasons.\n\n        The locale language is set at the offset and then checked again before\n        exiting.  This is to make sure that the attributes were not set with a\n        mix of information from more than one locale.  This would most likely\n        happen when using threads where one thread calls a locale-dependent\n        function while another thread changes the locale while the function in\n        the other thread is still running.  Proper coding would call for\n        locks to prevent changing the locale while locale-dependent code is\n        running.  The check here is done in case someone does not think about\n        doing this.\n\n        Only other possible issue is if someone changed the timezone and did\n        not call tz.tzset .  That is an issue for the programmer, though,\n        since changing the timezone is worthless without that call.\n\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.strptime'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class TimeRE(_mod_builtins.dict):
    '\n    Handle conversion from format directives to regexes.\n\n    Creates regexes for pattern matching a string of text containing\n    time information\n    '
    def _TimeRE__seqToRE(self, to_convert, directive):
        "Convert a list to a regex string for matching a directive.\n\n        Want possible matching values to be from longest to shortest.  This\n        prevents the possibility of a match occurring for a value that also\n        a substring of a larger value that should have matched (e.g., 'abc'\n        matching when 'abcdef' should have been the match).\n\n        "
        pass
    
    __class__ = TimeRE
    __dict__ = {}
    def __init__(self, locale_time):
        'Create keys/values.\n\n        Order of execution is important for dependency reasons.\n\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.strptime'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def compile(self, format):
        'Return a compiled re object for the format string.'
        pass
    
    @classmethod
    def fromkeys(cls, type, iterable, value):
        'Returns a new dict with keys from iterable and values equal to value.'
        pass
    
    def pattern(self, format):
        'Return regex pattern for the format string.\n\n        Need to make sure that any characters that might be interpreted as\n        regex syntax are escaped.\n\n        '
        pass
    

_CACHE_MAX_SIZE = 5
_TimeRE_cache = TimeRE()
__builtins__ = {}
__doc__ = 'Strptime-related classes and functions.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/strptime.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.strptime'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
_cache_lock = _mod__thread.lock()
def _getlang():
    'Figure out what language is being used for the locale'
    pass

_regex_cache = _mod_builtins.dict()
def _thread_allocate_lock():
    'allocate_lock() -> lock object\n(allocate() is an obsolete synonym)\n\nCreate a new lock object. See help(type(threading.Lock())) for\ninformation about locks.'
    pass

def array_strptime():
    "\n    Calculates the datetime structs represented by the passed array of strings\n\n    Parameters\n    ----------\n    values : ndarray of string-like objects\n    fmt : string-like regex\n    exact : matches must be exact if True, search if False\n    errors : string specifying error handling, {'raise', 'ignore', 'coerce'}\n    "
    pass

datetime_date = _mod_datetime.date
nat_strings = _mod_builtins.set()
