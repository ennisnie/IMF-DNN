import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

COPY_EXPAND_EXT_LINK_FLAG = 4
COPY_EXPAND_REFERENCE_FLAG = 8
COPY_EXPAND_SOFT_LINK_FLAG = 2
COPY_PRESERVE_NULL_FLAG = 32
COPY_SHALLOW_HIERARCHY_FLAG = 1
COPY_WITHOUT_ATTR_FLAG = 16
class ObjInfo(_ObjInfo):
    '\n        Represents the H5O_info_t structure\n    '
    __class__ = ObjInfo
    def __copy__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        '\n        Represents the H5O_info_t structure\n    '
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
    def hdr(self):
        pass
    

TYPE_DATASET = 1
TYPE_GROUP = 0
TYPE_NAMED_DATATYPE = 2
class _OHdr(_ObjInfoBase):
    __class__ = _OHdr
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
    def mesg(self):
        pass
    
    @property
    def nmesgs(self):
        pass
    
    @property
    def space(self):
        pass
    
    @property
    def version(self):
        pass
    

class _OHdrMesg(_ObjInfoBase):
    __class__ = _OHdrMesg
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
    def present(self):
        pass
    
    @property
    def shared(self):
        pass
    

class _OHdrSpace(_ObjInfoBase):
    __class__ = _OHdrSpace
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
    def free(self):
        pass
    
    @property
    def mesg(self):
        pass
    
    @property
    def meta(self):
        pass
    
    @property
    def total(self):
        pass
    

class _ObjInfo(_ObjInfoBase):
    __class__ = _ObjInfo
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
    def addr(self):
        pass
    
    @property
    def fileno(self):
        pass
    
    @property
    def rc(self):
        pass
    
    @property
    def type(self):
        pass
    

class _ObjInfoBase(_mod_builtins.object):
    __class__ = _ObjInfoBase
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
    

class _ObjectVisitor(_mod_builtins.object):
    __class__ = _ObjectVisitor
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
__doc__ = '\n    Module for HDF5 "H5O" functions.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5o.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5o'
__package__ = 'h5py'
def __pyx_unpickle__ObjectVisitor():
    pass

__test__ = _mod_builtins.dict()
def copy(*args, **kwds):
    '(ObjectID src_loc, STRING src_name, GroupID dst_loc, STRING dst_name,\n    PropID copypl=None, PropID lcpl=None)\n\n    Copy a group, dataset or named datatype from one location to another.  The\n    source and destination need not be in the same file.\n\n    The default behavior is a recursive copy of the object and all objects\n    below it.  This behavior is modified via the "copypl" property list.\n    '
    pass

def exists_by_name(*args, **kwds):
    ' (ObjectID loc, STRING name, PropID lapl=None) => BOOL exists\n\n        Determines whether a link resolves to an actual object.\n        '
    pass

def get_comment(*args, **kwds):
    '(ObjectID loc, STRING comment, **kwds)\n\n    Get the comment for any-file resident object.  Keywords:\n\n    STRING obj_name (".")\n        Set comment on this group member instead\n\n    PropID lapl (None)\n        Link access property list\n    '
    pass

def get_info(*args, **kwds):
    '(ObjectID loc, STRING name=, INT index=, **kwds) => ObjInfo\n\n    Get information describing an object in an HDF5 file.  Provide the object\n    itself, or the containing group and exactly one of "name" or "index".\n\n    STRING obj_name (".")\n        When "index" is specified, look in this subgroup instead.\n        Otherwise ignored.\n\n    PropID lapl (None)\n        Link access property list\n\n    INT index_type (h5.INDEX_NAME)\n\n    INT order (h5.ITER_INC)\n    '
    pass

def link(*args, **kwds):
    '(ObjectID obj, GroupID loc, STRING name, PropID lcpl=None,\n    PropID lapl=None)\n\n    Create a new hard link to an object.  Useful for objects created with\n    h5g.create_anon() or h5d.create_anon().\n    '
    pass

def open(*args, **kwds):
    '(ObjectID loc, STRING name, PropID lapl=None) => ObjectID\n\n    Open a group, dataset, or named datatype attached to an existing group.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def set_comment(*args, **kwds):
    '(ObjectID loc, STRING comment, **kwds)\n\n    Set the comment for any-file resident object.  Keywords:\n\n    STRING obj_name (".")\n        Set comment on this group member instead\n\n    PropID lapl (None)\n        Link access property list\n    '
    pass

def visit(*args, **kwds):
    '(ObjectID loc, CALLABLE func, **kwds) => <Return value from func>\n\n    Iterate a function or callable object over all objects below the\n    specified one.  Your callable should conform to the signature::\n\n        func(STRING name) => Result\n\n    or if the keyword argument "info" is True::\n\n        func(STRING name, ObjInfo info) => Result\n\n    Returning None continues iteration; returning anything else aborts\n    iteration and returns that value.  Keywords:\n\n    BOOL info (False)\n        Callback is func(STRING, Objinfo)\n\n    STRING obj_name (".")\n        Visit a subgroup of "loc" instead\n\n    PropLAID lapl (None)\n        Control how "obj_name" is interpreted\n\n    INT idx_type (h5.INDEX_NAME)\n        What indexing strategy to use\n\n    INT order (h5.ITER_INC)\n        Order in which iteration occurs\n\n    Compatibility note:  No callback is executed for the starting path ("."),\n    as some versions of HDF5 don\'t correctly handle a return value for this\n    case.  This differs from the behavior of the native H5Ovisit, which\n    provides a literal "." as the first value.\n    '
    pass

def with_phil():
    ' Locking decorator '
    pass

