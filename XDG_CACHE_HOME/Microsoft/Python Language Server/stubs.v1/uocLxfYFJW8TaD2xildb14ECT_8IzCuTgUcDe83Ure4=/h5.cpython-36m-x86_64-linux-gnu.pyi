import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

class ByteStringContext(_mod_builtins.object):
    def __bool__(self):
        return False
    
    __class__ = ByteStringContext
    __dict__ = {}
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass
    
    def __init__(self):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'h5py.h5'
    def __nonzero__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class H5PYConfig(_mod_builtins.object):
    "\n        Provides runtime access to global library settings.  You retrieve the\n        master copy of this object by calling h5py.get_config().\n\n        complex_names (tuple, r/w)\n            Settable 2-tuple controlling how complex numbers are saved.\n            Defaults to ('r','i').\n\n        bool_names (tuple, r/w)\n            Settable 2-tuple controlling the HDF5 enum names used for boolean\n            values.  Defaults to ('FALSE', 'TRUE') for values 0 and 1.\n    "
    @property
    def API_16(self):
        pass
    
    @property
    def API_18(self):
        pass
    
    __class__ = H5PYConfig
    def __init__(self, *args, **kwargs):
        "\n        Provides runtime access to global library settings.  You retrieve the\n        master copy of this object by calling h5py.get_config().\n\n        complex_names (tuple, r/w)\n            Settable 2-tuple controlling how complex numbers are saved.\n            Defaults to ('r','i').\n\n        bool_names (tuple, r/w)\n            Settable 2-tuple controlling the HDF5 enum names used for boolean\n            values.  Defaults to ('FALSE', 'TRUE') for values 0 and 1.\n    "
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
    def _bytestrings(self):
        pass
    
    @property
    def _f_name(self):
        pass
    
    @property
    def _i_name(self):
        pass
    
    @property
    def _r_name(self):
        pass
    
    @property
    def _t_name(self):
        pass
    
    @property
    def _track_order(self):
        pass
    
    @property
    def bool_names(self):
        " Settable 2-tuple controlling HDF5 ENUM names for boolean types.\n\n        Format is (false_name, real_name), defaulting to ('FALSE', 'TRUE').\n        "
        pass
    
    @property
    def complex_names(self):
        " Settable 2-tuple controlling how complex numbers are saved.\n\n        Format is (real_name, imag_name), defaulting to ('r','i').\n        "
        pass
    
    @property
    def mpi(self):
        ' Boolean indicating if Parallel HDF5 is available '
        pass
    
    @property
    def read_byte_strings(self):
        ' Returns a context manager which forces all strings to be returned\n        as byte strings. '
        pass
    
    @property
    def swmr_min_hdf5_version(self):
        ' Tuple indicating the minimum HDF5 version required for SWMR features'
        pass
    
    @property
    def track_order(self):
        ' Default value for track_order argument of\n        File.open()/Group.create_group()/Group.create_dataset() '
        pass
    
    @property
    def vds_min_hdf5_version(self):
        'Tuple indicating the minimum HDF5 version required for virtual dataset (VDS) features'
        pass
    

HDF5_VERSION_COMPILED_AGAINST = _mod_builtins.tuple()
INDEX_CRT_ORDER = 1
INDEX_NAME = 0
ITER_DEC = 1
ITER_INC = 0
ITER_NATIVE = 2
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5'
__package__ = 'h5py'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_H5PYConfig():
    pass

__test__ = _mod_builtins.dict()
def get_config():
    '() => H5PYConfig\n\n    Get a reference to the global library configuration object.\n    '
    pass

def get_libversion(*args, **kwds):
    ' () => TUPLE (major, minor, release)\n\n        Retrieve the HDF5 library version as a 3-tuple.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

