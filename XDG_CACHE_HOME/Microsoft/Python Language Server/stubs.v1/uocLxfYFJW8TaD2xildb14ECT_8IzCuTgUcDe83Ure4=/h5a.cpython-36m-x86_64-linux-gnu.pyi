import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

class AttrID(_mod_h5py__objects.ObjectID):
    '\n        Logical representation of an HDF5 attribute identifier.\n\n        Objects of this class can be used in any HDF5 function call\n        which expects an attribute identifier.  Additionally, all ``H5A*``\n        functions which always take an attribute instance as the first\n        argument are presented as methods of this class.\n\n        * Hashable: No\n        * Equality: Identifier comparison\n    '
    __class__ = AttrID
    def __init__(self, *args, **kwargs):
        '\n        Logical representation of an HDF5 attribute identifier.\n\n        Objects of this class can be used in any HDF5 function call\n        which expects an attribute identifier.  Additionally, all ``H5A*``\n        functions which always take an attribute instance as the first\n        argument are presented as methods of this class.\n\n        * Hashable: No\n        * Equality: Identifier comparison\n    '
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
    def dtype(self):
        "A Numpy-stype dtype object representing the attribute's datatype"
        pass
    
    def get_name(self, *args, **kwds):
        '() => STRING name\n\n        Determine the name of this attribute.\n        '
        pass
    
    def get_space(self, *args, **kwds):
        "() => SpaceID\n\n        Create and return a copy of the attribute's dataspace.\n        "
        pass
    
    def get_storage_size(self, *args, **kwds):
        '() => INT\n\n        Get the amount of storage required for this attribute.\n        '
        pass
    
    def get_type(self, *args, **kwds):
        "() => TypeID\n\n        Create and return a copy of the attribute's datatype.\n        "
        pass
    
    @property
    def name(self):
        "The attribute's name"
        pass
    
    def read(self, *args, **kwds):
        "(NDARRAY arr, TypeID mtype=None)\n\n        Read the attribute data into the given Numpy array.  Note that the\n        Numpy array must have the same shape as the HDF5 attribute, and a\n        conversion-compatible datatype.\n\n        The Numpy array must be writable and C-contiguous.  If this is not\n        the case, the read will fail with an exception.\n\n        If provided, the HDF5 TypeID mtype will override the array's dtype.\n        "
        pass
    
    @property
    def shape(self):
        "A Numpy-style shape tuple representing the attribute's dataspace"
        pass
    
    def write(self, *args, **kwds):
        '(NDARRAY arr)\n\n        Write the contents of a Numpy array too the attribute.  Note that\n        the Numpy array must have the same shape as the HDF5 attribute, and\n        a conversion-compatible datatype.\n\n        The Numpy array must be C-contiguous.  If this is not the case,\n        the write will fail with an exception.\n        '
        pass
    

class AttrInfo(_mod_builtins.object):
    __class__ = AttrInfo
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
    
    def _hash(self):
        pass
    
    @property
    def corder(self):
        'Creation order'
        pass
    
    @property
    def corder_valid(self):
        'Indicates if the creation order is valid'
        pass
    
    @property
    def cset(self):
        'Character set of attribute name (integer typecode from h5t)'
        pass
    
    @property
    def data_size(self):
        'Size of raw data'
        pass
    

class _AttrVisitor(_mod_builtins.object):
    __class__ = _AttrVisitor
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
__doc__ = '\n    Provides access to the low-level HDF5 "H5A" attribute interface.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5a.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5a'
__package__ = 'h5py'
def __pyx_unpickle_AttrID():
    pass

def __pyx_unpickle__AttrVisitor():
    pass

__test__ = _mod_builtins.dict()
def create(*args, **kwds):
    '(ObjectID loc, STRING name, TypeID tid, SpaceID space, **kwds) => AttrID\n\n    Create a new attribute, attached to an existing object.\n\n    STRING obj_name (".")\n        Attach attribute to this group member instead\n\n    PropID lapl\n        Link access property list for obj_name\n    '
    pass

def delete(*args, **kwds):
    '(ObjectID loc, STRING name=, INT index=, **kwds)\n\n    Remove an attribute from an object.  Specify exactly one of "name"\n    or "index". Keyword-only arguments:\n\n    STRING obj_name (".")\n        Attribute is attached to this group member\n\n    PropID lapl (None)\n        Link access property list for obj_name\n\n    INT index_type (h5.INDEX_NAME)\n\n    INT order (h5.ITER_INC)\n    '
    pass

def exists(*args, **kwds):
    '(ObjectID loc, STRING name, **kwds) => BOOL\n\n    Determine if an attribute is attached to this object.  Keywords:\n\n    STRING obj_name (".")\n        Look for attributes attached to this group member\n\n    PropID lapl (None):\n        Link access property list for obj_name\n    '
    pass

def get_info(*args, **kwds):
    '(ObjectID loc, STRING name=, INT index=, **kwds) => AttrInfo\n\n    Get information about an attribute, in one of two ways:\n\n    1. If you have the attribute identifier, just pass it in\n    2. If you have the parent object, supply it and exactly one of\n       either name or index.\n\n    STRING obj_name (".")\n        Use this group member instead\n\n    PropID lapl (None)\n        Link access property list for obj_name\n\n    INT index_type (h5.INDEX_NAME)\n        Which index to use\n\n    INT order (h5.ITER_INC)\n        What order the index is in\n    '
    pass

def get_num_attrs(*args, **kwds):
    '(ObjectID loc) => INT\n\n    Determine the number of attributes attached to an HDF5 object.\n    '
    pass

def iterate(*args, **kwds):
    '(ObjectID loc, CALLABLE func, INT index=0, **kwds) => <Return value from func>\n\n    Iterate a callable (function, method or callable object) over the\n    attributes attached to this object.  You callable should have the\n    signature::\n\n        func(STRING name) => Result\n\n    or if the keyword argument "info" is True::\n\n        func(STRING name, AttrInfo info) => Result\n\n    Returning None continues iteration; returning anything else aborts\n    iteration and returns that value.  Keywords:\n\n    BOOL info (False)\n        Callback is func(STRING name, AttrInfo info), not func(STRING name)\n\n    INT index_type (h5.INDEX_NAME)\n        Which index to use\n\n    INT order (h5.ITER_INC)\n        Index order to use\n    '
    pass

def open(*args, **kwds):
    '(ObjectID loc, STRING name=, INT index=, **kwds) => AttrID\n\n    Open an attribute attached to an existing object.  You must specify\n    exactly one of either name or idx.  Keywords are:\n\n    STRING obj_name (".")\n        Attribute is attached to this group member\n\n    PropID lapl (None)\n        Link access property list for obj_name\n\n    INT index_type (h5.INDEX_NAME)\n\n    INT order (h5.ITER_INC)\n\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def rename(*args, **kwds):
    '(ObjectID loc, STRING name, STRING new_name, **kwds)\n\n    Rename an attribute.  Keywords:\n\n    STRING obj_name (".")\n        Attribute is attached to this group member\n\n    PropID lapl (None)\n        Link access property list for obj_name\n    '
    pass

def with_phil():
    ' Locking decorator '
    pass

