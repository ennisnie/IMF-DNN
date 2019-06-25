import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

CRT_ORDER_TRACKED = 1
DATASET = 1
GROUP = 0
class GroupID(_mod_h5py__objects.ObjectID):
    '\n        Represents an HDF5 group identifier\n\n        Python extensions:\n\n        __contains__\n            Test for group member ("if name in grpid")\n\n        __iter__\n            Get an iterator over member names\n\n        __len__\n            Number of members in this group; len(grpid) = N\n\n        If HDF5 1.8.X is used, the attribute "links" contains a proxy object\n        providing access to the H5L family of routines.  See the docs\n        for h5py.h5l.LinkProxy for more information.\n\n        * Hashable: Yes, unless anonymous\n        * Equality: True HDF5 identity unless anonymous\n    '
    __class__ = GroupID
    def __contains__(self, value):
        '(STRING name)\n\n        Determine if a group member of the given name is present\n        '
        return False
    
    def __init__(self, *args, **kwargs):
        '\n        Represents an HDF5 group identifier\n\n        Python extensions:\n\n        __contains__\n            Test for group member ("if name in grpid")\n\n        __iter__\n            Get an iterator over member names\n\n        __len__\n            Number of members in this group; len(grpid) = N\n\n        If HDF5 1.8.X is used, the attribute "links" contains a proxy object\n        providing access to the H5L family of routines.  See the docs\n        for h5py.h5l.LinkProxy for more information.\n\n        * Hashable: Yes, unless anonymous\n        * Equality: True HDF5 identity unless anonymous\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        ' Return an iterator over the names of group members. '
        return GroupID()
    
    def __len__(self):
        ' Number of group members '
        return 0
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_comment(self, *args, **kwds):
        '(STRING name) => STRING comment\n\n        Retrieve the comment for a group member.\n        '
        pass
    
    def get_create_plist(self, *args, **kwds):
        '() => PropGCID\n\n        Retrieve a copy of the group creation property list used to\n        create this group.\n        '
        pass
    
    def get_linkval(self, *args, **kwds):
        '(STRING name) => STRING link_value\n\n        Retrieve the value (target name) of a symbolic link.\n        Limited to 2048 characters on Windows.\n        '
        pass
    
    def get_num_objs(self, *args, **kwds):
        '() => INT number_of_objects\n\n        Get the number of objects directly attached to a given group.\n        '
        pass
    
    def get_objname_by_idx(self, *args, **kwds):
        '(INT idx) => STRING\n\n        Get the name of a group member given its zero-based index.\n        '
        pass
    
    def get_objtype_by_idx(self, *args, **kwds):
        '(INT idx) => INT object_type_code\n\n        Get the type of an object attached to a group, given its zero-based\n        index.  Possible return values are:\n\n        - LINK\n        - GROUP\n        - DATASET\n        - TYPE\n        '
        pass
    
    def link(self, *args, **kwds):
        '(STRING current_name, STRING new_name, INT link_type=LINK_HARD,\n        GroupID remote=None)\n\n        Create a new hard or soft link.  current_name identifies\n        the link target (object the link will point to).  The new link is\n        identified by new_name and (optionally) another group "remote".\n\n        Link types are:\n\n        LINK_HARD\n            Hard link to existing object (default)\n\n        LINK_SOFT\n            Symbolic link; link target need not exist.\n        '
        pass
    
    @property
    def links(self):
        pass
    
    def move(self, *args, **kwds):
        '(STRING current_name, STRING new_name, GroupID remote=None)\n\n        Relink an object.  current_name identifies the object.\n        new_name and (optionally) another group "remote" determine\n        where it should be moved.\n        '
        pass
    
    def set_comment(self, *args, **kwds):
        '(STRING name, STRING comment)\n\n        Set the comment on a group member.\n        '
        pass
    
    def unlink(self, *args, **kwds):
        '(STRING name)\n\n        Remove a link to an object from this group.\n        '
        pass
    

class GroupIter(_mod_builtins.object):
    '\n        Iterator over the names of group members.  After this iterator is\n        exhausted, it releases its reference to the group ID.\n    '
    __class__ = GroupIter
    def __init__(self, *args, **kwargs):
        '\n        Iterator over the names of group members.  After this iterator is\n        exhausted, it releases its reference to the group ID.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return GroupIter()
    
    def __next__(self):
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class GroupStat(_mod_builtins.object):
    'Represents the H5G_stat_t structure containing group member info.\n\n    Fields (read-only):\n\n    * fileno:   2-tuple uniquely identifying the current file\n    * objno:    2-tuple uniquely identifying this object\n    * nlink:    Number of hard links to this object\n    * mtime:    Modification time of this object\n    * linklen:  Length of the symbolic link name, or 0 if not a link.\n\n    "Uniquely identifying" means unique among currently open files,\n    not universally unique.\n\n    * Hashable: Yes\n    * Equality: Yes\n    '
    __class__ = GroupStat
    def __init__(self, *args, **kwargs):
        'Represents the H5G_stat_t structure containing group member info.\n\n    Fields (read-only):\n\n    * fileno:   2-tuple uniquely identifying the current file\n    * objno:    2-tuple uniquely identifying this object\n    * nlink:    Number of hard links to this object\n    * mtime:    Modification time of this object\n    * linklen:  Length of the symbolic link name, or 0 if not a link.\n\n    "Uniquely identifying" means unique among currently open files,\n    not universally unique.\n\n    * Hashable: Yes\n    * Equality: Yes\n    '
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
    def fileno(self):
        pass
    
    @property
    def linklen(self):
        pass
    
    @property
    def mtime(self):
        pass
    
    @property
    def nlink(self):
        pass
    
    @property
    def objno(self):
        pass
    
    @property
    def type(self):
        pass
    

LINK = 3
LINK_ERROR = -1
LINK_HARD = 0
LINK_SOFT = 1
TYPE = 2
UNKNOWN = -1
class _GroupVisitor(_mod_builtins.object):
    __class__ = _GroupVisitor
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
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5g.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5g'
__package__ = 'h5py'
def __pyx_unpickle_GroupID():
    pass

def __pyx_unpickle_GroupIter():
    pass

def __pyx_unpickle__GroupVisitor():
    pass

__test__ = _mod_builtins.dict()
def _path_valid(*args, **kwds):
    " Determine if *path* points to an object in the file.\n\n        If *path* represents an external or soft link, the link's validity is not\n        checked.\n        "
    pass

def create(*args, **kwds):
    '(ObjectID loc, STRING name or None, PropLCID lcpl=None,\n        PropGCID gcpl=None)\n    => GroupID\n\n    Create a new group, under a given parent group.  If name is None,\n    an anonymous group will be created in the file.\n    '
    pass

def get_objinfo(*args, **kwds):
    '(ObjectID obj, STRING name=\'.\', BOOL follow_link=True) => GroupStat object\n\n    Obtain information about a named object.  If "name" is provided,\n    "obj" is taken to be a GroupID object containing the target.\n    The return value is a GroupStat object; see that class\'s docstring\n    for a description of its attributes.\n\n    If follow_link is True (default) and the object is a symbolic link,\n    the information returned describes its target.  Otherwise the\n    information describes the link itself.\n    '
    pass

def iterate(*args, **kwds):
    ' (GroupID loc, CALLABLE func, UINT startidx=0, **kwds)\n    => Return value from func\n\n    Iterate a callable (function, method or callable object) over the\n    members of a group.  Your callable should have the signature::\n\n        func(STRING name) => Result\n\n    Returning None continues iteration; returning anything else aborts\n    iteration and returns that value. Keywords:\n\n    STRING obj_name (".")\n        Iterate over this subgroup instead\n    '
    pass

def open(*args, **kwds):
    '(ObjectID loc, STRING name) => GroupID\n\n    Open an existing HDF5 group, attached to some other group.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

