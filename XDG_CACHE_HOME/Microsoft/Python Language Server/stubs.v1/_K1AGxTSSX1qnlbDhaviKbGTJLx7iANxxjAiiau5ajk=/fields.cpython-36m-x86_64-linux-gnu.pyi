import builtins as _mod_builtins

DAYS_FULL = _mod_builtins.list()
DAY_SECONDS = 86400
MONTHS_FULL = _mod_builtins.list()
__builtins__ = {}
__doc__ = '\nFunctions for accessing attributes of Timestamp/datetime64/datetime-like\nobjects and arrays\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/fields.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.fields'
__package__ = 'pandas._libs.tslibs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def build_field_sarray():
    '\n    Datetime as int64 representation to a structured array of fields\n    '
    pass

def get_date_field():
    '\n    Given a int64-based datetime index, extract the year, month, etc.,\n    field and return an array of these values.\n    '
    pass

def get_date_name_field():
    '\n    Given a int64-based datetime index, return array of strings of date\n    name based on requested field (e.g. weekday_name)\n    '
    pass

def get_locale_names():
    'Returns an array of localized day or month names\n\n    Parameters\n    ----------\n    name_type : string, attribute of LocaleTime() in which to return localized\n        names\n    locale : string\n\n    Returns\n    -------\n    list of locale names\n\n    '
    pass

def get_start_end_field():
    '\n    Given an int64-based datetime index return array of indicators\n    of whether timestamps are at the start/end of the month/quarter/year\n    (defined by frequency).\n    '
    pass

def get_time_micros():
    '\n    Return the number of microseconds in the time component of a\n    nanosecond timestamp.\n\n    Parameters\n    ----------\n    dtindex : ndarray[int64_t]\n\n    Returns\n    -------\n    micros : ndarray[int64_t]\n    '
    pass

def get_timedelta_field():
    '\n    Given a int64-based timedelta index, extract the days, hrs, sec.,\n    field and return an array of these values.\n    '
    pass

def isleapyear_arr():
    'vectorized version of isleapyear; NaT evaluates as False'
    pass

