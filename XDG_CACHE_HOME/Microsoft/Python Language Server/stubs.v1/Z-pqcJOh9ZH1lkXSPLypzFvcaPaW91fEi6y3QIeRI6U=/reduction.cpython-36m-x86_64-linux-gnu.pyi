import builtins as _mod_builtins
import distutils.version as _mod_distutils_version

class BlockSlider(_mod_builtins.object):
    '\n    Only capable of sliding on axis=0\n    '
    __class__ = BlockSlider
    def __init__(self, *args, **kwargs):
        '\n    Only capable of sliding on axis=0\n    '
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
    
    @property
    def blocks(self):
        pass
    
    @property
    def dummy(self):
        pass
    
    @property
    def frame(self):
        pass
    
    @property
    def idx_slider(self):
        pass
    
    @property
    def index(self):
        pass
    
    def move(self):
        pass
    
    @property
    def nblocks(self):
        pass
    

class InvalidApply(_mod_builtins.Exception):
    __class__ = InvalidApply
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.reduction'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

LooseVersion = _mod_distutils_version.LooseVersion
class Reducer(_mod_builtins.object):
    '\n    Performs generic reduction operation on a C or Fortran-contiguous ndarray\n    while avoiding ndarray construction overhead\n    '
    __class__ = Reducer
    def __init__(self, *args, **kwargs):
        '\n    Performs generic reduction operation on a C or Fortran-contiguous ndarray\n    while avoiding ndarray construction overhead\n    '
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
    
    def _check_dummy(self):
        pass
    
    def get_result(self):
        pass
    

class SeriesBinGrouper(_mod_builtins.object):
    '\n    Performs grouping operation according to bin edges, rather than labels\n    '
    __class__ = SeriesBinGrouper
    def __init__(self, *args, **kwargs):
        '\n    Performs grouping operation according to bin edges, rather than labels\n    '
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
    
    def _check_dummy(self):
        pass
    
    @property
    def arr(self):
        pass
    
    @property
    def bins(self):
        pass
    
    @property
    def dummy_arr(self):
        pass
    
    @property
    def dummy_index(self):
        pass
    
    @property
    def f(self):
        pass
    
    def get_result(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def ityp(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def typ(self):
        pass
    
    @property
    def values(self):
        pass
    

class SeriesGrouper(_mod_builtins.object):
    '\n    Performs generic grouping operation while avoiding ndarray construction\n    overhead\n    '
    __class__ = SeriesGrouper
    def __init__(self, *args, **kwargs):
        '\n    Performs generic grouping operation while avoiding ndarray construction\n    overhead\n    '
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
    
    def _check_dummy(self):
        pass
    
    @property
    def arr(self):
        pass
    
    @property
    def dummy_arr(self):
        pass
    
    @property
    def dummy_index(self):
        pass
    
    @property
    def f(self):
        pass
    
    def get_result(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def ityp(self):
        pass
    
    @property
    def labels(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def typ(self):
        pass
    
    @property
    def values(self):
        pass
    

class Slider(_mod_builtins.object):
    '\n    Only handles contiguous data for now\n    '
    __class__ = Slider
    def __init__(self, *args, **kwargs):
        '\n    Only handles contiguous data for now\n    '
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
    
    def advance(self):
        pass
    
    def reset(self):
        pass
    
    def set_length(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/reduction.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.reduction'
__package__ = 'pandas._libs'
def __pyx_unpickle_Reducer():
    pass

def __pyx_unpickle_SeriesBinGrouper():
    pass

def __pyx_unpickle_SeriesGrouper():
    pass

def __pyx_unpickle_Slider():
    pass

__test__ = _mod_builtins.dict()
def apply_frame_axis0():
    pass

def maybe_convert_objects():
    '\n    Type inference function-- convert object array to proper dtype\n    '
    pass

def reduce():
    '\n\n    Parameters\n    -----------\n    arr : NDFrame object\n    f : function\n    axis : integer axis\n    dummy : type of reduced output (series)\n    labels : Index or None\n    '
    pass

