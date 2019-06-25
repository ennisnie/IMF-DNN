import builtins as _mod_builtins

class _NDFrameIndexerBase(_mod_builtins.object):
    '\n    A base class for _NDFrameIndexer for fast instantiation and attribute\n    access.\n    '
    __class__ = _NDFrameIndexerBase
    def __init__(self, *args, **kwargs):
        '\n    A base class for _NDFrameIndexer for fast instantiation and attribute\n    access.\n    '
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
    
    @property
    def _ndim(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def ndim(self):
        pass
    
    @property
    def obj(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/indexing.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.indexing'
__package__ = 'pandas._libs'
def __pyx_unpickle__NDFrameIndexerBase():
    pass

__test__ = _mod_builtins.dict()
