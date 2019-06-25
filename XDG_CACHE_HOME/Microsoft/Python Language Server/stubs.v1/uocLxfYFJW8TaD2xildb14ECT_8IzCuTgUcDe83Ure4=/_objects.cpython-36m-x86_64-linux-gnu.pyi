import builtins as _mod_builtins

class BogoLock(_mod_builtins.object):
    __class__ = BogoLock
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
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
    

class FastRLock(_mod_builtins.object):
    "Fast, re-entrant locking.\n\n    Under uncongested conditions, the lock is never acquired but only\n    counted.  Only when a second thread comes in and notices that the\n    lock is needed, it acquires the lock and notifies the first thread\n    to release it when it's done.  This is all made possible by the\n    wonderful GIL.\n    "
    __class__ = FastRLock
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        "Fast, re-entrant locking.\n\n    Under uncongested conditions, the lock is never acquired but only\n    counted.  Only when a second thread comes in and notices that the\n    lock is needed, it acquires the lock and notifies the first thread\n    to release it when it's done.  This is all made possible by the\n    wonderful GIL.\n    "
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
    
    def _is_owned(self):
        pass
    
    def acquire(self):
        pass
    
    def release(self):
        pass
    

class ObjectID(_mod_builtins.object):
    '\n        Represents an HDF5 identifier.\n\n    '
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = ObjectID
    def __copy__(self):
        pass
    
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
        " Default hashing mechanism for HDF5 objects\n\n        Default hashing strategy:\n        1. Try to hash based on the object's fileno and objno records\n        2. If (1) succeeds, cache the resulting value\n        3. If (1) fails, raise TypeError\n        "
        return 0
    
    def __init__(self, *args, **kwargs):
        '\n        Represents an HDF5 identifier.\n\n    '
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
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _close(self):
        ' Manually close this object. '
        pass
    
    def close(self):
        ' Close this identifier. '
        pass
    
    @property
    def fileno(self):
        pass
    
    @property
    def id(self):
        pass
    
    @property
    def locked(self):
        pass
    
    @property
    def valid(self):
        pass
    

__builtins__ = {}
__doc__ = '\n    Implements ObjectID base class.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/_objects.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py._objects'
__package__ = 'h5py'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_BogoLock():
    pass

__test__ = _mod_builtins.dict()
def nonlocal_close(*args, **kwds):
    ' Find dead ObjectIDs and set their integer identifiers to 0.\n    '
    pass

phil = FastRLock()
def print_reg(*args, **kwds):
    pass

def with_phil():
    ' Locking decorator '
    pass

