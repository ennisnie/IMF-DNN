import builtins as _mod_builtins
import tables.exceptions as _mod_tables_exceptions
import tables.hdf5extension as _mod_tables_hdf5extension

class CacheArray(_mod_tables_hdf5extension.Array):
    'Container for keeping index caches of 1st and 2nd level.'
    __class__ = CacheArray
    def __init__(self, *args, **kwargs):
        'Container for keeping index caches of 1st and 2nd level.'
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
    
    def _g_close(self):
        pass
    

HDF5ExtError = _mod_tables_exceptions.HDF5ExtError
class Index(_mod_builtins.object):
    __class__ = Index
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class IndexArray(_mod_tables_hdf5extension.Array):
    'Container for keeping sorted and indices values.'
    __class__ = IndexArray
    def __init__(self, *args, **kwargs):
        'Container for keeping sorted and indices values.'
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
    
    def _g_close(self):
        pass
    
    def _init_sorted_slice(self):
        'Initialize the structures for doing a binary search.'
        pass
    
    def _read_index_slice(self):
        pass
    
    def _read_sorted_slice(self):
        'Read the sorted part of an index.'
        pass
    
    def _search_bin_na_b(self):
        pass
    
    def _search_bin_na_d(self):
        pass
    
    def _search_bin_na_e(self):
        pass
    
    def _search_bin_na_f(self):
        pass
    
    def _search_bin_na_g(self):
        pass
    
    def _search_bin_na_i(self):
        pass
    
    def _search_bin_na_ll(self):
        pass
    
    def _search_bin_na_s(self):
        pass
    
    def _search_bin_na_ub(self):
        pass
    
    def _search_bin_na_ui(self):
        pass
    
    def _search_bin_na_ull(self):
        pass
    
    def _search_bin_na_us(self):
        pass
    

class LastRowArray(_mod_tables_hdf5extension.Array):
    '\n  Container for keeping sorted and indices values of last rows of an index.\n  '
    __class__ = LastRowArray
    def __init__(self, *args, **kwargs):
        '\n  Container for keeping sorted and indices values of last rows of an index.\n  '
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
    
    def _read_index_slice(self):
        'Read the reverse index part of an LR index.'
        pass
    
    def _read_sorted_slice(self):
        'Read the sorted part of an LR index.'
        pass
    

__builtins__ = {}
__doc__ = 'cython interface for keeping indexes classes.\n\nClasses (type extensions):\n\n    IndexArray\n    CacheArray\n    LastRowArray\n\nFunctions:\n\n    keysort\n\nMisc variables:\n\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/tables/indexesextension.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'tables.indexesextension'
__package__ = 'tables'
def __pyx_unpickle_Index():
    pass

__test__ = _mod_builtins.dict()
def _bisect_left():
    'Return the index where to insert item x in list a, assuming a is sorted.\n\n  The return value i is such that all e in a[:i] have e < x, and all e in\n  a[i:] have e >= x.  So if x already appears in the list, i points just\n  before the leftmost x already there.\n\n  '
    pass

def _bisect_right():
    'Return the index where to insert item x in list a, assuming a is sorted.\n\n  The return value i is such that all e in a[:i] have e <= x, and all e in\n  a[i:] have e > x.  So if x already appears in the list, i points just\n  beyond the rightmost x already there.\n\n  '
    pass

def keysort():
    'Sort array1 in-place. array2 is also sorted following the array1 order.\n\n    array1 can be of any type, except complex or string.  array2 may be made of\n    elements on any size.\n\n    '
    pass

