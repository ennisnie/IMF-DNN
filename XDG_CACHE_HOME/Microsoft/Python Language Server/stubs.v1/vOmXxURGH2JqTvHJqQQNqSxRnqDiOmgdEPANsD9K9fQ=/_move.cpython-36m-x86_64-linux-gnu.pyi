import builtins as _mod_builtins

class BadMove(_mod_builtins.Exception):
    'Exception used to indicate that a move was attempted on a value with\nmore than a single reference.\n\nParameters\n----------\ndata : any\n    The data which was passed to ``move_into_mutable_buffer``.\n\nSee Also\n--------\npandas.util._move.move_into_mutable_buffer\n'
    __class__ = BadMove
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Exception used to indicate that a move was attempted on a value with\nmore than a single reference.\n\nParameters\n----------\ndata : any\n    The data which was passed to ``move_into_mutable_buffer``.\n\nSee Also\n--------\npandas.util._move.move_into_mutable_buffer\n'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas.util._move'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/util/_move.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas.util._move'
__package__ = 'pandas.util'
def move_into_mutable_buffer():
    'Moves a bytes object that is about to be destroyed into a mutable buffer\nwithout copying the data.\n\nParameters\n----------\nbytes_rvalue : bytes with 1 refcount.\n    The bytes object that you want to move into a mutable buffer. This\n    cannot be a named object. It must only have a single reference.\n\nReturns\n-------\nbuf : stolenbuf\n    An object that supports the buffer protocol which can give a mutable\n    view of the data that was previously owned by ``bytes_rvalue``.\n\nRaises\n------\nBadMove\n    Raised when a move is attempted on an object with more than one\n    reference.\n\nNotes\n-----\nIf you want to use this function you are probably wrong.\n\nWarning: Do not call this function through *unpacking. This can\npotentially trick the reference checks which may allow you to get a\nmutable reference to a shared string!\n\n'
    pass

class stolenbuf(_mod_builtins.object):
    "A buffer that is wrapping a stolen bytes object's buffer."
    __class__ = stolenbuf
    def __init__(self, *args, **kwargs):
        "A buffer that is wrapping a stolen bytes object's buffer."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

