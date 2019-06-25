import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

ATTR = 6
BADID = -1
DATASET = 5
DATASPACE = 4
DATATYPE = 3
FILE = 1
GENPROP_CLS = 9
GENPROP_LST = 10
GROUP = 2
REFERENCE = 7
__builtins__ = {}
__doc__ = '\n    Identifier interface for object inspection.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5i.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5i'
__package__ = 'h5py'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def dec_ref(*args, **kwds):
    ' (ObjectID obj)\n\n        Decrement the reference count for the given object.\n\n        This function is provided for debugging only.  Reference counting\n        is automatically synchronized with Python, and you can easily break\n        ObjectID instances by abusing this function.\n    '
    pass

def get_file_id(*args, **kwds):
    ' (ObjectID obj) => FileID\n\n        Obtain an identifier for the file in which this object resides.\n    '
    pass

def get_name(*args, **kwds):
    ' (ObjectID obj) => STRING name, or None\n\n        Determine (a) name of an HDF5 object.  Because an object has as many\n        names as there are hard links to it, this may not be unique.\n\n        If the identifier is invalid or is not associated with a name\n        (in the case of transient datatypes, dataspaces, etc), returns None.\n\n        For some reason, this does not work on dereferenced objects.\n    '
    pass

def get_ref(*args, **kwds):
    ' (ObjectID obj) => INT\n\n        Retrieve the reference count for the given object.\n    '
    pass

def get_type(*args, **kwds):
    ' (ObjectID obj) => INT type_code\n\n        Determine the HDF5 typecode of an arbitrary HDF5 object.  The return\n        value is always one of the type constants defined in this module; if\n        the ID is invalid, BADID is returned.\n    '
    pass

def inc_ref(*args, **kwds):
    ' (ObjectID obj)\n\n        Increment the reference count for the given object.\n\n        This function is provided for debugging only.  Reference counting\n        is automatically synchronized with Python, and you can easily break\n        ObjectID instances by abusing this function.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

def wrap_identifier():
    pass

