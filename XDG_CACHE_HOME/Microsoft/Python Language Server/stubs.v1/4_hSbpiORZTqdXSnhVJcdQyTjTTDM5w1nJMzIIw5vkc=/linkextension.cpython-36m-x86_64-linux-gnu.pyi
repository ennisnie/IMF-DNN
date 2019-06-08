import builtins as _mod_builtins
import tables.exceptions as _mod_tables_exceptions
import tables.hdf5extension as _mod_tables_hdf5extension

class ExternalLink(Link):
    'Extension class representing an external link.'
    __class__ = ExternalLink
    def __init__(self, *args, **kwargs):
        'Extension class representing an external link.'
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
    
    def _g_create(self):
        'Create the link in file.'
        pass
    
    def _g_open(self):
        'Open the link in file.'
        pass
    

HDF5ExtError = _mod_tables_exceptions.HDF5ExtError
class Link(_mod_tables_hdf5extension.Node):
    'Extension class from which all link extensions inherits.'
    __class__ = Link
    def __init__(self, *args, **kwargs):
        'Extension class from which all link extensions inherits.'
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
    
    def _g_copy(self):
        'Private part for the _f_copy() method.'
        pass
    

class SoftLink(Link):
    'Extension class representing a soft link.'
    __class__ = SoftLink
    def __init__(self, *args, **kwargs):
        'Extension class representing a soft link.'
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
    
    def _g_create(self):
        'Create the link in file.'
        pass
    
    def _g_open(self):
        'Open the link in file.'
        pass
    

__builtins__ = {}
__doc__ = 'Cython functions and classes for supporting links in HDF5.'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/tables/linkextension.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'tables.linkextension'
__package__ = 'tables'
def __pyx_unpickle_ExternalLink():
    pass

def __pyx_unpickle_Link():
    pass

def __pyx_unpickle_SoftLink():
    pass

__test__ = _mod_builtins.dict()
def _g_create_hard_link():
    'Create a hard link in the file.'
    pass

def _get_link_class():
    'Guess the link class.'
    pass

