import builtins as _mod_builtins

class OutOfBoundsDatetime(_mod_builtins.ValueError):
    __class__ = OutOfBoundsDatetime
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.tslibs.np_datetime'
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
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/np_datetime.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.np_datetime'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
