import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

class _DimensionScaleVisitor(_mod_builtins.object):
    __class__ = _DimensionScaleVisitor
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
    

__builtins__ = {}
__doc__ = '\n    Low-level HDF5 "H5G" group interface.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5ds.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5ds'
__package__ = 'h5py'
def __pyx_unpickle__DimensionScaleVisitor():
    pass

__test__ = _mod_builtins.dict()
def attach_scale(*args, **kwds):
    pass

def detach_scale(*args, **kwds):
    pass

def get_label(*args, **kwds):
    pass

def get_num_scales(*args, **kwds):
    pass

def get_scale_name(*args, **kwds):
    pass

def is_attached(*args, **kwds):
    pass

def is_scale(*args, **kwds):
    '(DatasetID dset)\n\n    Determines whether dset is a dimension scale.\n    '
    pass

def iterate(*args, **kwds):
    ' (DatasetID loc, UINT dim, CALLABLE func, UINT startidx=0)\n    => Return value from func\n\n    Iterate a callable (function, method or callable object) over the\n    members of a group.  Your callable should have the signature::\n\n        func(STRING name) => Result\n\n    Returning None continues iteration; returning anything else aborts\n    iteration and returns that value. Keywords:\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def set_label(*args, **kwds):
    pass

def set_scale(*args, **kwds):
    '(DatasetID dset, STRING dimname)\n\n    Convert dataset dset to a dimension scale, with optional name dimname.\n    '
    pass

def with_phil():
    ' Locking decorator '
    pass

