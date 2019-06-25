import builtins as _mod_builtins
import importlib._bootstrap as _mod_importlib__bootstrap
import numpy as _mod_numpy
import tables.atom as _mod_tables_atom
import tables.exceptions as _mod_tables_exceptions

class Array(Leaf):
    __class__ = Array
    def __init__(self, *args, **kwargs):
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
    
    def _append(self):
        pass
    
    def _create_array(self):
        pass
    
    def _create_carray(self):
        pass
    
    def _g_read_coords(self):
        'Read coordinates in an already created NumPy array.'
        pass
    
    def _g_read_selection(self):
        'Read a selection in an already created NumPy array.'
        pass
    
    def _g_read_slice(self):
        pass
    
    def _g_write_coords(self):
        'Write a selection in an already created NumPy array.'
        pass
    
    def _g_write_selection(self):
        'Write a selection in an already created NumPy array.'
        pass
    
    def _g_write_slice(self):
        'Write a slice in an already created NumPy array.'
        pass
    
    def _open_array(self):
        pass
    
    def _read_array(self):
        pass
    
    def perform_selection(self):
        'Performs a selection using start/count/step in the given axis.\n\n    All other axes have their full range selected.  The selection is\n    added to the current `space_id` selection using the given mode.\n\n    Note: This is a backport from the h5py project.\n\n    '
        pass
    

Atom = _mod_tables_atom.Atom
class AttributeSet(_mod_builtins.object):
    __class__ = AttributeSet
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
    
    def _g_getattr(self):
        'Get HDF5 attributes and retrieve them as NumPy objects.\n\n    H5T_SCALAR types will be retrieved as scalar NumPy.\n    H5T_ARRAY types will be retrieved as ndarray NumPy objects.\n\n    '
        pass
    
    def _g_list_attr(self):
        'Return a tuple with the attribute list'
        pass
    
    def _g_new(self):
        pass
    
    def _g_remove(self):
        pass
    
    def _g_setattr(self):
        'Save Python or NumPy objects as HDF5 attributes.\n\n    Scalar Python objects, scalar NumPy & 0-dim NumPy objects will all be\n    saved as H5T_SCALAR type.  N-dim NumPy objects will be saved as H5T_ARRAY\n    type.\n\n    '
        pass
    

DataTypeWarning = _mod_tables_exceptions.DataTypeWarning
class File(_mod_builtins.object):
    __class__ = File
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
    
    def _close_file(self):
        pass
    
    def _flush_file(self):
        pass
    
    def _g_new(self):
        pass
    
    def _get_file_id(self):
        pass
    
    def fileno(self):
        'Return the underlying OS integer file descriptor.\n\n    This is needed for lower-level file interfaces, such as the ``fcntl``\n    module.\n\n    '
        pass
    
    def get_file_image(self):
        'Retrieves an in-memory image of an existing, open HDF5 file.\n\n    .. note:: this method requires HDF5 >= 1.8.9.\n\n    .. versionadded:: 3.0\n\n    '
        pass
    
    def get_filesize(self):
        'Returns the size of an HDF5 file.\n\n    The returned size is that of the entire file, as opposed to only\n    the HDF5 portion of the file. I.e., size includes the user block,\n    if any, the HDF5 portion of the file, and any data that may have\n    been appended beyond the data written through the HDF5 Library.\n\n    .. versionadded:: 3.0\n\n    '
        pass
    
    def get_userblock_size(self):
        'Retrieves the size of a user block.\n\n    .. versionadded:: 3.0\n\n    '
        pass
    

class Group(Node):
    __class__ = Group
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
    
    def _g_close_group(self):
        pass
    
    def _g_create(self):
        pass
    
    def _g_flush_group(self):
        pass
    
    def _g_get_gchild_attr(self):
        'Return an attribute of a child `Group`.\n\n    If the attribute does not exist, ``None`` is returned.\n\n    '
        pass
    
    def _g_get_lchild_attr(self):
        'Return an attribute of a child `Leaf`.\n\n    If the attribute does not exist, ``None`` is returned.\n\n    '
        pass
    
    def _g_get_objinfo(self):
        "Check whether 'name' is a children of 'self' and return its type."
        pass
    
    def _g_list_group(self):
        'Return a tuple with the groups and the leaves hanging from self.'
        pass
    
    def _g_move_node(self):
        pass
    
    def _g_open(self):
        pass
    

HAVE_DIRECT_DRIVER = False
HAVE_WINDOWS_DRIVER = False
HDF5ExtError = _mod_tables_exceptions.HDF5ExtError
class Leaf(Node):
    __class__ = Leaf
    def __init__(self, *args, **kwargs):
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
    
    def _g_close(self):
        pass
    
    def _g_flush(self):
        pass
    
    def _g_new(self):
        pass
    
    def _g_truncate(self):
        'Truncate a Leaf to `size` nrows.'
        pass
    
    def _get_obj_track_times(self):
        'Get track_times boolean for dataset\n\n    Uses H5Pget_obj_track_times to determine if the dataset was\n    created with the track_times property.  If the leaf is not a\n    dataset, this will fail with HDF5ExtError.\n\n    The track times dataset creation property does not seem to survive\n    closing and reopening as of HDF5 1.8.17.  Currently, it may be\n    more accurate to test whether the ctime for the dataset is 0:\n    track_times = (leaf._get_obj_timestamps().ctime == 0)\n    '
        pass
    
    def _get_storage_size(self):
        pass
    

class Node(_mod_builtins.object):
    __class__ = Node
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
    
    def _g_delete(self):
        pass
    
    def _g_new(self):
        pass
    
    def _get_obj_info(self):
        pass
    
    def _get_obj_timestamps(self):
        pass
    

ObjInfo = _mod_importlib__bootstrap.ObjInfo
ObjTimestamps = _mod_importlib__bootstrap.ObjTimestamps
SizeType = _mod_numpy.int64
class UnImplemented(Leaf):
    __class__ = UnImplemented
    def __init__(self, *args, **kwargs):
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
    
    def _g_close(self):
        pass
    
    def _open_unimplemented(self):
        pass
    

class VLArray(Leaf):
    __class__ = VLArray
    def __init__(self, *args, **kwargs):
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
    
    def _append(self):
        pass
    
    def _create_array(self):
        pass
    
    def _get_memory_size(self):
        pass
    
    def _modify(self):
        pass
    
    def _open_array(self):
        pass
    
    def _read_array(self):
        pass
    
    def get_row_size(self):
        'Return the total size in bytes of all the elements contained in a given row.'
        pass
    

__builtins__ = {}
__doc__ = 'Cython interface between several PyTables classes and HDF5 library.\n\nClasses (type extensions):\n\n    File\n    AttributeSet\n    Node\n    Leaf\n    Group\n    Array\n    VLArray\n    UnImplemented\n\nFunctions:\n\nMisc variables:\n\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/tables/hdf5extension.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'tables.hdf5extension'
__package__ = 'tables'
def __pyx_unpickle_AttributeSet():
    pass

def __pyx_unpickle_File():
    pass

def __pyx_unpickle_Group():
    pass

def __pyx_unpickle_Node():
    pass

__test__ = _mod_builtins.dict()
_supported_drivers = _mod_builtins.tuple()
def atom_from_hdf5_type():
    'Get an atom from a type_id.\n\n  See `hdf5_to_np_ext_type` for an explanation of the `pure_numpy_types`\n  parameter.\n\n  '
    pass

def atom_to_hdf5_type():
    pass

byteorders = _mod_builtins.dict()
def check_file_access(filename, mode):
    'Check for file access in the specified `mode`.\n\n    `mode` is one of the modes supported by `File` objects.  If the file\n    indicated by `filename` can be accessed using that `mode`, the\n    function ends successfully.  Else, an ``IOError`` is raised\n    explaining the reason of the failure.\n\n    All this paraphernalia is used to avoid the lengthy and scaring HDF5\n    messages produced when there are problems opening a file.  No\n    changes are ever made to the file system.\n\n    '
    pass

def correct_byteorder(ptype, byteorder):
    'Fix the byteorder depending on the PyTables types.'
    pass

def create_nested_type():
    'Create a nested type based on a description and return an HDF5 type.'
    pass

def descr_from_dtype(dtype_, ptparams):
    'Get a description instance and byteorder from a (nested) NumPy dtype.'
    pass

def encode_filename():
    'Return the encoded filename in the filesystem encoding.'
    pass

hdf5_class_to_string = _mod_builtins.dict()
def hdf5_to_np_ext_type():
    'Map the atomic HDF5 type to a string repr of NumPy extended codes.\n\n  If `pure_numpy_types` is true, detected HDF5 types that does not match pure\n  NumPy types will raise a ``TypeError`` exception.  If not, HDF5 types like\n  TIME, VLEN or ENUM are passed through.\n\n  If `atom` is true, the resulting repr is meant for atoms.  If not, the\n  result is meant for attributes.\n\n  Returns the string repr of type and its shape.  The exception is for\n  compounds types, that returns a NumPy dtype and shape instead.\n\n  '
    pass

def namedtuple(typename, field_names):
    "Returns a new subclass of tuple with named fields.\n\n    >>> Point = namedtuple('Point', ['x', 'y'])\n    >>> Point.__doc__                   # docstring for the new class\n    'Point(x, y)'\n    >>> p = Point(11, y=22)             # instantiate with positional args or keywords\n    >>> p[0] + p[1]                     # indexable like a plain tuple\n    33\n    >>> x, y = p                        # unpack like a regular tuple\n    >>> x, y\n    (11, 22)\n    >>> p.x + p.y                       # fields also accessible by name\n    33\n    >>> d = p._asdict()                 # convert to a dictionary\n    >>> d['x']\n    11\n    >>> Point(**d)                      # convert from a dictionary\n    Point(x=11, y=22)\n    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields\n    Point(x=100, y=22)\n\n    "
    pass

npext_prefixes_to_ptkinds = _mod_builtins.dict()
platform_byteorder = 0
pt_special_kinds = _mod_builtins.list()
pttype_to_hdf5 = _mod_builtins.dict()
def set_blosc_max_threads(nthreads):
    'set_blosc_max_threads(nthreads)\n\n  Set the maximum number of threads that Blosc can use.\n\n  This actually overrides the :data:`tables.parameters.MAX_BLOSC_THREADS`\n  setting in :mod:`tables.parameters`, so the new value will be effective until\n  this function is called again or a new file with a different\n  :data:`tables.parameters.MAX_BLOSC_THREADS` value is specified.\n\n  Returns the previous setting for maximum threads.\n\n  '
    pass

