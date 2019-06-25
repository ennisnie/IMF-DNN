import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

DISABLE_EDC = 0
ENABLE_EDC = 1
ERROR_EDC = -1
FILTER_ALL = 0
FILTER_CONFIG_DECODE_ENABLED = 2
FILTER_CONFIG_ENCODE_ENABLED = 1
FILTER_DEFLATE = 1
FILTER_ERROR = -1
FILTER_FLETCHER32 = 3
FILTER_LZF = 32000
FILTER_MAX = 65535
FILTER_NBIT = 5
FILTER_NONE = 0
FILTER_RESERVED = 256
FILTER_SCALEOFFSET = 6
FILTER_SHUFFLE = 2
FILTER_SZIP = 4
FLAG_DEFMASK = 255
FLAG_INVMASK = 65280
FLAG_MANDATORY = 0
FLAG_OPTIONAL = 1
FLAG_REVERSE = 256
FLAG_SKIP_EDC = 512
NO_EDC = 2
SO_FLOAT_DSCALE = 0
SO_FLOAT_ESCALE = 1
SO_INT = 2
SO_INT_MINBITS_DEFAULT = 0
SZIP_ALLOW_K13_OPTION_MASK = 1
SZIP_CHIP_OPTION_MASK = 2
SZIP_EC_OPTION_MASK = 4
SZIP_MAX_PIXELS_PER_BLOCK = 32
SZIP_NN_OPTION_MASK = 32
__builtins__ = {}
__doc__ = '\n    Filter API and constants.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5z.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5z'
__package__ = 'h5py'
__test__ = _mod_builtins.dict()
def _register_lzf():
    pass

def filter_avail(*args, **kwds):
    '(INT filter_code) => BOOL\n\n    Determine if the given filter is available to the library. The\n    filter code should be one of:\n\n    - FILTER_DEFLATE\n    - FILTER_SHUFFLE\n    - FILTER_FLETCHER32\n    - FILTER_SZIP\n    '
    pass

def get_filter_info(*args, **kwds):
    '(INT filter_code) => INT filter_flags\n\n    Retrieve a bitfield with information about the given filter. The\n    filter code should be one of:\n\n    - FILTER_DEFLATE\n    - FILTER_SHUFFLE\n    - FILTER_FLETCHER32\n    - FILTER_SZIP\n\n    Valid bitmasks for use with the returned bitfield are:\n\n    - FILTER_CONFIG_ENCODE_ENABLED\n    - FILTER_CONFIG_DECODE_ENABLED\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

