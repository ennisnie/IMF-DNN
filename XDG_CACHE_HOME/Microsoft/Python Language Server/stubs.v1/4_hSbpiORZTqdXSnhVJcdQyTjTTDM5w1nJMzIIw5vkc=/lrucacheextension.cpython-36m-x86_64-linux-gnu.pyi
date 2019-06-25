import builtins as _mod_builtins

class BaseCache(_mod_builtins.object):
    'Base class that implements automatic probing/disabling of the cache.'
    __class__ = BaseCache
    def __init__(self, *args, **kwargs):
        'Base class that implements automatic probing/disabling of the cache.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def couldenablecache(self):
        pass
    

DISABLE_EVERY_CYCLES = 10
ENABLE_EVERY_CYCLES = 50
LOWEST_HIT_RATIO = 0.6
class NodeCache(_mod_builtins.object):
    'Least-Recently-Used (LRU) cache for PyTables nodes.'
    __class__ = NodeCache
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __init__(self, LRU):
        "Maximum nslots of the cache.\n\n    If more than 'nslots' elements are added to the cache,\n    the least-recently-used ones will be discarded.\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return NodeCache()
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __marker = _mod_builtins.object()
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def nslots(self):
        pass
    
    def pop(self):
        pass
    

class NumCache(BaseCache):
    'Least-Recently-Used (LRU) cache specific for Numerical data.'
    __class__ = NumCache
    def __init__(self, LRU):
        "Maximum size of the cache.\n\n    If more than 'nslots' elements are added to the cache,\n    the least-recently-used ones will be discarded.\n\n    Parameters:\n    shape - The rectangular shape of the cache (nslots, nelemsperslot)\n    itemsize - The size of the element base in cache\n    name - A descriptive name for this cache\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def getitem(self):
        pass
    
    def getslot(self):
        pass
    
    def setitem(self):
        pass
    

class ObjectCache(BaseCache):
    'Least-Recently-Used (LRU) cache specific for python objects.'
    __class__ = ObjectCache
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, LRU):
        "Maximum size of the cache.\n\n    If more than 'nslots' elements are added to the cache,\n    the least-recently-used ones will be discarded.\n\n    Parameters:\n    nslots - The number of slots in cache\n    name - A descriptive name for this cache\n\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def getitem(self):
        pass
    
    def getslot(self):
        pass
    
    def setitem(self):
        pass
    

class ObjectNode(_mod_builtins.object):
    'Record of a cached value. Not for public consumption.'
    __class__ = ObjectNode
    def __init__(self, *args, **kwargs):
        'Record of a cached value. Not for public consumption.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__builtins__ = {}
__doc__ = 'Cython interface for several LRU cache systems.\n\nClasses (type extensions):\n\n    NodeCache\n    ObjectCache\n    NumCache\n\nFunctions:\n\nMisc variables:\n\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/tables/lrucacheextension.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'tables.lrucacheextension'
__package__ = 'tables'
def __pyx_unpickle_NodeCache():
    pass

def __pyx_unpickle_ObjectNode():
    pass

__test__ = _mod_builtins.dict()
