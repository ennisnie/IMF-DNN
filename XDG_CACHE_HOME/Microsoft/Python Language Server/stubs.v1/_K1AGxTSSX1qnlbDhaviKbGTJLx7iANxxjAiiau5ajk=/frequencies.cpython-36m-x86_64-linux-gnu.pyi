import _sre as _mod__sre
import builtins as _mod_builtins

class FreqGroup(_mod_builtins.object):
    FR_ANN = 1000
    FR_BUS = 5000
    FR_DAY = 6000
    FR_HR = 7000
    FR_MIN = 8000
    FR_MS = 10000
    FR_MTH = 3000
    FR_NS = 12000
    FR_QTR = 2000
    FR_SEC = 9000
    FR_US = 11000
    FR_WK = 4000
    __class__ = FreqGroup
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.frequencies'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'
MONTH_NUMBERS = _mod_builtins.dict()
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/frequencies.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.frequencies'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def _base_and_stride():
    "\n    Return base freq and stride info from string representation\n\n    Returns\n    -------\n    base : str\n    stride : int\n\n    Examples\n    --------\n    _freq_and_stride('5Min') -> 'Min', 5\n    "
    pass

_dont_uppercase = _mod_builtins.set()
_lite_rule_alias = _mod_builtins.dict()
_period_code_map = _mod_builtins.dict()
def _period_str_to_code():
    pass

_reverse_period_code_map = _mod_builtins.dict()
def get_base_alias():
    "\n    Returns the base frequency alias, e.g., '5D' -> 'D'\n\n    Parameters\n    ----------\n    freqstr : str\n\n    Returns\n    -------\n    base_alias : str\n    "
    pass

def get_freq():
    "\n    Return frequency code of given frequency str.\n    If input is not string, return input as it is.\n\n    Examples\n    --------\n    >>> get_freq('A')\n    1000\n\n    >>> get_freq('3A')\n    1000\n    "
    pass

def get_freq_code():
    "\n    Return freq str or tuple to freq code and stride (mult)\n\n    Parameters\n    ----------\n    freqstr : str or tuple\n\n    Returns\n    -------\n    return : tuple of base frequency code and stride (mult)\n\n    Examples\n    --------\n    >>> get_freq_code('3D')\n    (6000, 3)\n\n    >>> get_freq_code('D')\n    (6000, 1)\n\n    >>> get_freq_code(('D', 3))\n    (6000, 3)\n    "
    pass

def get_freq_str():
    '\n    Return the summary string associated with this offset code, possibly\n    adjusted by a multiplier.\n\n    Parameters\n    ----------\n    base : int (member of FreqGroup)\n\n    Returns\n    -------\n    freq_str : str\n\n    Examples\n    --------\n    >>> get_freq_str(1000)\n    \'A-DEC\'\n\n    >>> get_freq_str(2000, 2)\n    \'2Q-DEC\'\n\n    >>> get_freq_str("foo")\n    '
    pass

def get_rule_month():
    '\n    Return starting month of given freq, default is December.\n\n    Parameters\n    ----------\n    source : object\n    default : object (default "DEC")\n\n    Returns\n    -------\n    rule_month: object (usually string)\n\n    Examples\n    --------\n    >>> get_rule_month(\'D\')\n    \'DEC\'\n\n    >>> get_rule_month(\'A-JAN\')\n    \'JAN\'\n    '
    pass

def get_to_timestamp_base():
    "\n    Return frequency code group used for base of to_timestamp against\n    frequency code.\n\n    Parameters\n    ----------\n    base : int (member of FreqGroup)\n\n    Returns\n    -------\n    base : int\n\n    Examples\n    --------\n    # Return day freq code against longer freq than day\n    >>> get_to_timestamp_base(get_freq_code('D')[0])\n    6000\n    >>> get_to_timestamp_base(get_freq_code('W')[0])\n    6000\n    >>> get_to_timestamp_base(get_freq_code('M')[0])\n    6000\n\n    # Return second freq code against hour between second\n    >>> get_to_timestamp_base(get_freq_code('H')[0])\n    9000\n    >>> get_to_timestamp_base(get_freq_code('S')[0])\n    9000\n    "
    pass

def is_subperiod():
    '\n    Returns True if downsampling is possible between source and target\n    frequencies\n\n    Parameters\n    ----------\n    source : string or DateOffset\n        Frequency converting from\n    target : string or DateOffset\n        Frequency converting to\n\n    Returns\n    -------\n    is_subperiod : boolean\n    '
    pass

def is_superperiod():
    '\n    Returns True if upsampling is possible between source and target\n    frequencies\n\n    Parameters\n    ----------\n    source : string\n        Frequency converting from\n    target : string\n        Frequency converting to\n\n    Returns\n    -------\n    is_superperiod : boolean\n    '
    pass

opattern = _mod__sre.SRE_Pattern()
