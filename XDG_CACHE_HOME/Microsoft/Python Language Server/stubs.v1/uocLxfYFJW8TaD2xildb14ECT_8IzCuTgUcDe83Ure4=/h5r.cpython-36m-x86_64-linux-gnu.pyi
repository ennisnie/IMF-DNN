import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

DATASET_REGION = 1
OBJECT = 0
class Reference(_mod_builtins.object):
    '\n        Opaque representation of an HDF5 reference.\n\n        Objects of this class are created exclusively by the library and\n        cannot be modified.  The read-only attribute "typecode" determines\n        whether the reference is to an object in an HDF5 file (OBJECT)\n        or a dataset region (DATASET_REGION).\n\n        The object\'s truth value indicates whether it contains a nonzero\n        reference.  This does not guarantee that is valid, but is useful\n        for rejecting "background" elements in a dataset.\n    '
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = Reference
    def __init__(self, *args, **kwargs):
        '\n        Opaque representation of an HDF5 reference.\n\n        Objects of this class are created exclusively by the library and\n        cannot be modified.  The read-only attribute "typecode" determines\n        whether the reference is to an object in an HDF5 file (OBJECT)\n        or a dataset region (DATASET_REGION).\n\n        The object\'s truth value indicates whether it contains a nonzero\n        reference.  This does not guarantee that is valid, but is useful\n        for rejecting "background" elements in a dataset.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def typecode(self):
        pass
    
    @property
    def typesize(self):
        pass
    

class RegionReference(Reference):
    '\n        Opaque representation of an HDF5 region reference.\n\n        This is a subclass of Reference which exists mainly for programming\n        convenience.\n    '
    __class__ = RegionReference
    def __init__(self, *args, **kwargs):
        '\n        Opaque representation of an HDF5 region reference.\n\n        This is a subclass of Reference which exists mainly for programming\n        convenience.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__builtins__ = {}
__doc__ = '\n    H5R API for object and region references.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5r.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5r'
__package__ = 'h5py'
__test__ = _mod_builtins.dict()
def create(*args, **kwds):
    '(ObjectID loc, STRING name, INT ref_type, SpaceID space=None)\n    => ReferenceObject ref\n\n    Create a new reference. The value of ref_type determines the kind\n    of reference created:\n\n    OBJECT\n        Reference to an object in an HDF5 file.  Parameters "loc"\n        and "name" identify the object; "space" is unused.\n\n    DATASET_REGION\n        Reference to a dataset region.  Parameters "loc" and\n        "name" identify the dataset; the selection on "space"\n        identifies the region.\n    '
    pass

def dereference(*args, **kwds):
    '(Reference ref, ObjectID id) => ObjectID or None\n\n    Open the object pointed to by the reference and return its\n    identifier.  The file identifier (or the identifier for any object\n    in the file) must also be provided.  Returns None if the reference\n    is zero-filled.\n\n    The reference may be either Reference or RegionReference.\n    '
    pass

def get_name(*args, **kwds):
    '(Reference ref, ObjectID loc) => STRING name\n\n    Determine the name of the object pointed to by this reference.\n    Requires the HDF5 1.8 API.\n    '
    pass

def get_obj_type(*args, **kwds):
    '(Reference ref, ObjectID id) => INT obj_code or None\n\n    Determine what type of object the reference points to.  The\n    reference may be a Reference or RegionReference.  The file\n    identifier or the identifier of any object in the file must also\n    be provided.\n\n    The return value is one of:\n\n    - h5g.LINK\n    - h5g.GROUP\n    - h5g.DATASET\n    - h5g.TYPE\n\n    If the reference is zero-filled, returns None.\n    '
    pass

def get_region(*args, **kwds):
    "(Reference ref, ObjectID id) => SpaceID or None\n\n    Retrieve the dataspace selection pointed to by the reference.\n    Returns a copy of the dataset's dataspace, with the appropriate\n    elements selected.  The file identifier or the identifier of any\n    object in the file (including the dataset itself) must also be\n    provided.\n\n    The reference object must be a RegionReference.  If it is zero-filled,\n    returns None.\n    "
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

