import builtins as _mod_builtins
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pandas._libs.tslibs.timestamps as _mod_pandas__libs_tslibs_timestamps
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
Timestamp = _mod_pandas__libs_tslibs_timestamps.Timestamp
UTC = _mod_pytz.UTC()
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslib.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslib'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _test_parse_iso8601():
    '\n    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used\n    only for testing, actual construction uses `convert_str_to_tsobject`\n    '
    pass

def array_to_datetime():
    "\n    Converts a 1D array of date-like values to a numpy array of either:\n        1) datetime64[ns] data\n        2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError\n           is encountered\n\n    Also returns a pytz.FixedOffset if an array of strings with the same\n    timezone offset is passed and utc=True is not passed. Otherwise, None\n    is returned\n\n    Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,\n    strings\n\n    Parameters\n    ----------\n    values : ndarray of object\n         date-like objects to convert\n    errors : str, default 'raise'\n         error behavior when parsing\n    dayfirst : bool, default False\n         dayfirst parsing behavior when encountering datetime strings\n    yearfirst : bool, default False\n         yearfirst parsing behavior when encountering datetime strings\n    utc : bool, default None\n         indicator whether the dates should be UTC\n    require_iso8601 : bool, default False\n         indicator whether the datetime string should be iso8601\n\n    Returns\n    -------\n    tuple (ndarray, tzoffset)\n    "
    pass

def array_with_unit_to_datetime():
    '\n    convert the ndarray according to the unit\n    if errors:\n      - raise: return converted values or raise OutOfBoundsDatetime\n          if out of range on the conversion or\n          ValueError for other conversions (e.g. a string)\n      - ignore: return non-convertible values as the same unit\n      - coerce: NaT for non-convertibles\n\n    '
    pass

def format_array_from_datetime():
    '\n    return a np object array of the string formatted values\n\n    Parameters\n    ----------\n    values : a 1-d i8 array\n    tz : the timezone (or None)\n    format : optional, default is None\n          a strftime capable string\n    na_rep : optional, default is None\n          a nat format\n\n    '
    pass

iNaT = -9223372036854775808
def ints_to_pydatetime():
    "\n    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp\n\n    Parameters\n    ----------\n    arr  : array of i8\n    tz   : str, default None\n         convert to this timezone\n    freq : str/Offset, default None\n         freq to convert\n    box  : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'\n         If datetime, convert to datetime.datetime\n         If date, convert to datetime.date\n         If time, convert to datetime.time\n         If Timestamp, convert to pandas.Timestamp\n\n    Returns\n    -------\n    result : array of dtype specified by box\n    "
    pass

nat_strings = _mod_builtins.set()
def parse_datetime_string():
    'parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    pass

