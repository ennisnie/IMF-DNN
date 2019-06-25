import builtins as _mod_builtins

class BaseRowProxy(_mod_builtins.object):
    'BaseRowProxy is a abstract base class for RowProxy'
    __class__ = BaseRowProxy
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'BaseRowProxy is a abstract base class for RowProxy'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return BaseRowProxy()
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __reduce__(self):
        'Pickle support method.'
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _keymap(self):
        'Key to (processor, index) dict'
        pass
    
    @property
    def _parent(self):
        'ResultMetaData'
        pass
    
    @property
    def _processors(self):
        'list of type processors'
        pass
    
    @property
    def _row(self):
        'Original row tuple'
        pass
    
    def values(self):
        'Return the values represented by this BaseRowProxy as a list.'
        pass
    

__doc__ = 'Module containing C versions of core ResultProxy classes.'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/sqlalchemy/cresultproxy.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'sqlalchemy.cresultproxy'
__package__ = 'sqlalchemy'
def safe_rowproxy_reconstructor():
    'reconstruct a RowProxy instance from its pickled form.'
    pass

