import builtins as _mod_builtins

class Infinity(_mod_builtins.object):
    ' provide a positive Infinity comparison method for ranking '
    __class__ = Infinity
    __dict__ = {}
    def __eq__(self):
        return False
    
    def __ge__(self):
        return False
    
    def __gt__(self):
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        ' provide a positive Infinity comparison method for ranking '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self):
        return False
    
    def __lt__(self):
        return False
    
    __module__ = 'pandas._libs.algos'
    def __ne__(self):
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class NegInfinity(_mod_builtins.object):
    ' provide a negative Infinity comparison method for ranking '
    __class__ = NegInfinity
    __dict__ = {}
    def __eq__(self):
        return False
    
    def __ge__(self):
        return False
    
    def __gt__(self):
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        ' provide a negative Infinity comparison method for ranking '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self):
        return False
    
    def __lt__(self):
        return False
    
    __module__ = 'pandas._libs.algos'
    def __ne__(self):
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/algos.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.algos'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _take_2d_float64(values, idx):
    "wrap(values: 'ndarray', idx)"
    pass

def _take_2d_int64(values, idx):
    "wrap(values: 'ndarray', idx)"
    pass

def _take_2d_object(values, idx):
    "wrap(values: 'ndarray', idx)"
    pass

def _take_2d_uint64(values, idx):
    "wrap(values: 'ndarray', idx)"
    pass

def arrmap(index, func):
    pass

def arrmap_bool(index, func):
    pass

def arrmap_float32(index, func):
    pass

def arrmap_float64(index, func):
    pass

def arrmap_int32(index, func):
    pass

def arrmap_int64(index, func):
    pass

def arrmap_object(index, func):
    pass

def arrmap_uint64(index, func):
    pass

def backfill():
    pass

def backfill_2d_inplace():
    pass

def backfill_inplace():
    pass

def diff_2d_float32():
    pass

def diff_2d_float64():
    pass

def diff_2d_int16():
    pass

def diff_2d_int32():
    pass

def diff_2d_int64():
    pass

def diff_2d_int8():
    pass

def ensure_float32():
    pass

def ensure_float64():
    pass

def ensure_int16():
    pass

def ensure_int32():
    pass

def ensure_int64():
    pass

def ensure_int8():
    pass

def ensure_object():
    pass

def ensure_platform_int():
    pass

def ensure_uint16():
    pass

def ensure_uint32():
    pass

def ensure_uint64():
    pass

def ensure_uint8():
    pass

def groupsort_indexer():
    '\n    compute a 1-d indexer that is an ordering of the passed index,\n    ordered by the groups. This is a reverse of the label\n    factorization process.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        mappings from group -> position\n    ngroups: int64\n        number of groups\n\n    return a tuple of (1-d indexer ordered by groups, group counts)\n    '
    pass

def is_lexsorted():
    pass

def is_monotonic(arr, timelike):
    '\n    Returns\n    -------\n    is_monotonic_inc, is_monotonic_dec, is_unique\n    '
    pass

def kth_smallest(a, k):
    pass

def nancorr():
    pass

def nancorr_spearman():
    pass

def pad():
    pass

def pad_2d_inplace():
    pass

def pad_inplace():
    pass

def rank_1d_float64():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_1d_int64():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_1d_object():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_1d_uint64():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_2d_float64():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_2d_int64():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_2d_object():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def rank_2d_uint64():
    '\n    Fast NaN-friendly version of scipy.stats.rankdata\n    '
    pass

def take_1d_bool_bool():
    pass

def take_1d_bool_object():
    pass

def take_1d_float32_float32():
    pass

def take_1d_float32_float64():
    pass

def take_1d_float64_float64():
    pass

def take_1d_int16_float64():
    pass

def take_1d_int16_int16():
    pass

def take_1d_int16_int32():
    pass

def take_1d_int16_int64():
    pass

def take_1d_int32_float64():
    pass

def take_1d_int32_int32():
    pass

def take_1d_int32_int64():
    pass

def take_1d_int64_float64():
    pass

def take_1d_int64_int64():
    pass

def take_1d_int8_float64():
    pass

def take_1d_int8_int32():
    pass

def take_1d_int8_int64():
    pass

def take_1d_int8_int8():
    pass

def take_1d_object_object():
    pass

def take_2d_axis0_bool_bool():
    pass

def take_2d_axis0_bool_object():
    pass

def take_2d_axis0_float32_float32():
    pass

def take_2d_axis0_float32_float64():
    pass

def take_2d_axis0_float64_float64():
    pass

def take_2d_axis0_int16_float64():
    pass

def take_2d_axis0_int16_int16():
    pass

def take_2d_axis0_int16_int32():
    pass

def take_2d_axis0_int16_int64():
    pass

def take_2d_axis0_int32_float64():
    pass

def take_2d_axis0_int32_int32():
    pass

def take_2d_axis0_int32_int64():
    pass

def take_2d_axis0_int64_float64():
    pass

def take_2d_axis0_int64_int64():
    pass

def take_2d_axis0_int8_float64():
    pass

def take_2d_axis0_int8_int32():
    pass

def take_2d_axis0_int8_int64():
    pass

def take_2d_axis0_int8_int8():
    pass

def take_2d_axis0_object_object():
    pass

def take_2d_axis1_bool_bool():
    pass

def take_2d_axis1_bool_object():
    pass

def take_2d_axis1_float32_float32():
    pass

def take_2d_axis1_float32_float64():
    pass

def take_2d_axis1_float64_float64():
    pass

def take_2d_axis1_int16_float64():
    pass

def take_2d_axis1_int16_int16():
    pass

def take_2d_axis1_int16_int32():
    pass

def take_2d_axis1_int16_int64():
    pass

def take_2d_axis1_int32_float64():
    pass

def take_2d_axis1_int32_int32():
    pass

def take_2d_axis1_int32_int64():
    pass

def take_2d_axis1_int64_float64():
    pass

def take_2d_axis1_int64_int64():
    pass

def take_2d_axis1_int8_float64():
    pass

def take_2d_axis1_int8_int32():
    pass

def take_2d_axis1_int8_int64():
    pass

def take_2d_axis1_int8_int8():
    pass

def take_2d_axis1_object_object():
    pass

def take_2d_multi_bool_bool():
    pass

def take_2d_multi_bool_object():
    pass

def take_2d_multi_float32_float32():
    pass

def take_2d_multi_float32_float64():
    pass

def take_2d_multi_float64_float64():
    pass

def take_2d_multi_int16_float64():
    pass

def take_2d_multi_int16_int16():
    pass

def take_2d_multi_int16_int32():
    pass

def take_2d_multi_int16_int64():
    pass

def take_2d_multi_int32_float64():
    pass

def take_2d_multi_int32_int32():
    pass

def take_2d_multi_int32_int64():
    pass

def take_2d_multi_int64_float64():
    pass

def take_2d_multi_int64_int64():
    pass

def take_2d_multi_int8_float64():
    pass

def take_2d_multi_int8_int32():
    pass

def take_2d_multi_int8_int64():
    pass

def take_2d_multi_int8_int8():
    pass

def take_2d_multi_object_object():
    pass

tiebreakers = _mod_builtins.dict()
def unique_deltas():
    '\n    Efficiently find the unique first-differences of the given array.\n\n    Parameters\n    ----------\n    arr : ndarray[in64_t]\n\n    Returns\n    -------\n    result : ndarray[int64_t]\n        result is sorted\n    '
    pass

