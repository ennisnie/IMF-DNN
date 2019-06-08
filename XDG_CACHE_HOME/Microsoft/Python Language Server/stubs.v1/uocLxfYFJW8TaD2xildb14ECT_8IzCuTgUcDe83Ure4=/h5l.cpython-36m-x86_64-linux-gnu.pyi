import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

class LinkInfo(_mod_builtins.object):
    __class__ = LinkInfo
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
    
    @property
    def corder(self):
        ' Creation order '
        pass
    
    @property
    def corder_valid(self):
        ' Indicates if the creation order is valid '
        pass
    
    @property
    def cset(self):
        ' Integer type code for character set (h5t.CSET_*) '
        pass
    
    @property
    def type(self):
        ' Integer type code for link (h5l.TYPE_*) '
        pass
    
    @property
    def u(self):
        ' Either the address of a hard link or the size of a soft/UD link '
        pass
    

class LinkProxy(_mod_builtins.object):
    '\n        Proxy class which provides access to the HDF5 "H5L" API.\n\n        These come attached to GroupID objects as "obj.links".  Since every\n        H5L function operates on at least one group, the methods provided\n        operate on their parent group identifier.  For example::\n\n            >>> g = h5g.open(fid, \'/\')\n            >>> g.links.exists("MyGroup")\n            True\n            >>> g.links.exists("FooBar")\n            False\n\n        * Hashable: No\n        * Equality: Undefined\n\n        You will note that this class does *not* inherit from ObjectID.\n    '
    __class__ = LinkProxy
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        '\n        Proxy class which provides access to the HDF5 "H5L" API.\n\n        These come attached to GroupID objects as "obj.links".  Since every\n        H5L function operates on at least one group, the methods provided\n        operate on their parent group identifier.  For example::\n\n            >>> g = h5g.open(fid, \'/\')\n            >>> g.links.exists("MyGroup")\n            True\n            >>> g.links.exists("FooBar")\n            False\n\n        * Hashable: No\n        * Equality: Undefined\n\n        You will note that this class does *not* inherit from ObjectID.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def create_external(self, *args, **kwds):
        '(STRING link_name, STRING file_name, STRING obj_name,\n        PropLCID lcpl=None, PropLAID lapl=None)\n\n        Create a new external link, pointing to an object in another file.\n        '
        pass
    
    def create_hard(self, *args, **kwds):
        ' (STRING new_name, GroupID cur_loc, STRING cur_name,\n        PropID lcpl=None, PropID lapl=None)\n\n        Create a new hard link in this group pointing to an existing link\n        in another group.\n        '
        pass
    
    def create_soft(self, *args, **kwds):
        '(STRING new_name, STRING target, PropID lcpl=None, PropID lapl=None)\n\n        Create a new soft link in this group, with the given string value.\n        The link target does not need to exist.\n        '
        pass
    
    def exists(self, *args, **kwds):
        ' (STRING name, PropID lapl=None) => BOOL\n\n            Check if a link of the specified name exists in this group.\n        '
        pass
    
    def get_info(self, *args, **kwds):
        '(STRING name=, INT index=, **kwds) => LinkInfo instance\n\n        Get information about a link, either by name or its index.\n\n        Keywords:\n        '
        pass
    
    def get_val(self, *args, **kwds):
        '(STRING name, PropLAID lapl=None) => STRING or TUPLE(file, obj)\n\n        Get the string value of a soft link, or a 2-tuple representing\n        the contents of an external link.\n        '
        pass
    
    def iterate(self, *args, **kwds):
        '(CALLABLE func, **kwds) => <Return value from func>, <index to restart at>\n\n        Iterate a function or callable object over all groups in this\n        one.  Your callable should conform to the signature::\n\n            func(STRING name) => Result\n\n        or if the keyword argument "info" is True::\n\n            func(STRING name, LinkInfo info) => Result\n\n        Returning None or a logical False continues iteration; returning\n        anything else aborts iteration and returns that value.\n\n        BOOL info (False)\n            Provide a LinkInfo instance to callback\n\n        STRING obj_name (".")\n            Visit this subgroup instead\n\n        PropLAID lapl (None)\n            Link access property list for "obj_name"\n\n        INT idx_type (h5.INDEX_NAME)\n\n        INT order (h5.ITER_INC)\n\n        hsize_t idx (0)\n            The index to start iterating at\n        '
        pass
    
    def move(self, *args, **kwds):
        ' (STRING src_name, GroupID dst_loc, STRING dst_name)\n\n        Move a link to a new location in the file.\n        '
        pass
    
    def visit(self, *args, **kwds):
        '(CALLABLE func, **kwds) => <Return value from func>\n\n        Iterate a function or callable object over all groups below this\n        one.  Your callable should conform to the signature::\n\n            func(STRING name) => Result\n\n        or if the keyword argument "info" is True::\n\n            func(STRING name, LinkInfo info) => Result\n\n        Returning None or a logical False continues iteration; returning\n        anything else aborts iteration and returns that value.\n\n        BOOL info (False)\n            Provide a LinkInfo instance to callback\n\n        STRING obj_name (".")\n            Visit this subgroup instead\n\n        PropLAID lapl (None)\n            Link access property list for "obj_name"\n\n        INT idx_type (h5.INDEX_NAME)\n\n        INT order (h5.ITER_INC)\n        '
        pass
    

TYPE_EXTERNAL = 64
TYPE_HARD = 0
TYPE_SOFT = 1
class _LinkVisitor(_mod_builtins.object):
    ' Helper class for iteration callback '
    __class__ = _LinkVisitor
    def __init__(self, *args, **kwargs):
        ' Helper class for iteration callback '
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
__doc__ = '\n    API for the "H5L" family of link-related operations.  Defines the class\n    LinkProxy, which comes attached to GroupID objects as <obj>.links.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5l.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5l'
__package__ = 'h5py'
def __pyx_unpickle_LinkProxy():
    pass

def __pyx_unpickle__LinkVisitor():
    pass

__test__ = _mod_builtins.dict()
phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

