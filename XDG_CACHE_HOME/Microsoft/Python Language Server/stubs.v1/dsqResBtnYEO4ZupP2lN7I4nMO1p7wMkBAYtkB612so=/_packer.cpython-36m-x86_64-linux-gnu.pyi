import builtins as _mod_builtins
import pandas.io.msgpack as _mod_pandas_io_msgpack
import pandas.io.msgpack.exceptions as _mod_pandas_io_msgpack_exceptions

ExtType = _mod_pandas_io_msgpack.ExtType
PackValueError = _mod_pandas_io_msgpack_exceptions.PackValueError
class Packer(_mod_builtins.object):
    "Packer(default=None, encoding='utf-8', unicode_errors='strict', use_single_float=False, bool autoreset=1, bool use_bin_type=0)\n\n    MessagePack Packer\n\n    usage::\n\n        packer = Packer()\n        astream.write(packer.pack(a))\n        astream.write(packer.pack(b))\n\n    Packer's constructor has some keyword arguments:\n\n    :param callable default:\n        Convert user type to builtin type that Packer supports.\n        See also simplejson's document.\n    :param str encoding:\n        Convert unicode to bytes with this encoding. (default: 'utf-8')\n    :param str unicode_errors:\n        Error handler for encoding unicode. (default: 'strict')\n    :param bool use_single_float:\n        Use single precision float type for float. (default: False)\n    :param bool autoreset:\n        Reset buffer after each pack and return it's\n        content as `bytes`. (default: True).\n        If set this to false, use `bytes()` to get\n        content and `.reset()` to clear buffer.\n    :param bool use_bin_type:\n        Use bin type introduced in msgpack spec 2.0 for bytes.\n        It also enable str8 type for unicode.\n    "
    __class__ = Packer
    def __init__(self, default=None, encoding='utf-8', unicode_errors='strict', use_single_float=False, boolautoreset=1, booluse_bin_type=0):
        '\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        'Packer.__reduce_cython__(self)'
        return ''; return ()
    
    def __setstate__(self, state):
        'Packer.__setstate_cython__(self, __pyx_state)'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bytes(self):
        'Packer.bytes(self)\nReturn buffer content.'
        pass
    
    def pack(self):
        'Packer.pack(self, obj)'
        pass
    
    def pack_array_header(self):
        'Packer.pack_array_header(self, size_t size)'
        pass
    
    def pack_ext_type(self):
        'Packer.pack_ext_type(self, typecode, data)'
        pass
    
    def pack_map_header(self):
        'Packer.pack_map_header(self, size_t size)'
        pass
    
    def pack_map_pairs(self):
        'Packer.pack_map_pairs(self, pairs)\n\n        Pack *pairs* as msgpack map type.\n\n        *pairs* should sequence of pair.\n        (`len(pairs)` and `for k, v in pairs:` should be supported.)\n        '
        pass
    
    def reset(self):
        'Packer.reset(self)\nClear internal buffer.'
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/io/msgpack/_packer.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas.io.msgpack._packer'
__package__ = 'pandas.io.msgpack'
__test__ = _mod_builtins.dict()
