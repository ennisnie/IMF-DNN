import builtins as _mod_builtins

FFI = _mod_builtins.CompiledFFI
FFI_CDECL = 2
FFI_DEFAULT_ABI = 2
Lib = _mod_builtins.CompiledLib
RTLD_DEEPBIND = 8
RTLD_GLOBAL = 256
RTLD_LAZY = 1
RTLD_LOCAL = 0
RTLD_NODELETE = 4096
RTLD_NOLOAD = 4
RTLD_NOW = 2
_C_API = _mod_builtins.PyCapsule()
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/_cffi_backend.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_cffi_backend'
__package__ = ''
__version__ = '1.12.2'
def _get_common_types():
    pass

def _get_types():
    pass

def _init_cffi_1_0_external_module():
    pass

def _testbuff():
    pass

def _testfunc():
    pass

def alignof():
    pass

class buffer(_mod_builtins.object):
    "ffi.buffer(cdata[, byte_size]):\nReturn a read-write buffer object that references the raw C data\npointed to by the given 'cdata'.  The 'cdata' must be a pointer or an\narray.  Can be passed to functions expecting a buffer, or directly\nmanipulated with:\n\n    buf[:]          get a copy of it in a regular string, or\n    buf[idx]        as a single character\n    buf[:] = ...\n    buf[idx] = ...  change the content"
    __class__ = buffer
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, cdata, byte_size=None):
        "ffi.buffer(cdata[, byte_size]):\nReturn a read-write buffer object that references the raw C data\npointed to by the given 'cdata'.  The 'cdata' must be a pointer or an\narray.  Can be passed to functions expecting a buffer, or directly\nmanipulated with:\n\n    buf[:]          get a copy of it in a regular string, or\n    buf[idx]        as a single character\n    buf[:] = ...\n    buf[idx] = ...  change the content"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def callback():
    pass

def cast():
    pass

def complete_struct_or_union():
    pass

def from_buffer():
    pass

def from_handle():
    pass

def gcp():
    pass

def get_errno():
    pass

def getcname():
    pass

def load_library():
    pass

def memmove():
    pass

def new_array_type():
    pass

def new_enum_type():
    pass

def new_function_type():
    pass

def new_pointer_type():
    pass

def new_primitive_type():
    pass

def new_struct_type():
    pass

def new_union_type():
    pass

def new_void_type():
    pass

def newp():
    pass

def newp_handle():
    pass

def rawaddressof():
    pass

def release():
    pass

def set_errno():
    pass

def sizeof():
    pass

def string():
    pass

def typeof():
    pass

def typeoffsetof():
    pass

def unpack():
    pass

