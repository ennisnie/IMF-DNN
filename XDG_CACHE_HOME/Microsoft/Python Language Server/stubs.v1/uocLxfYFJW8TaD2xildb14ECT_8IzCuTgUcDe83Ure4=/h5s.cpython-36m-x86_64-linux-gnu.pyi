import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

ALL = SpaceID()
NO_CLASS = -1
NULL = 2
SCALAR = 0
SELECT_AND = 2
SELECT_APPEND = 6
SELECT_INVALID = 8
SELECT_NOOP = -1
SELECT_NOTA = 5
SELECT_NOTB = 4
SELECT_OR = 1
SELECT_PREPEND = 7
SELECT_SET = 0
SELECT_XOR = 3
SEL_ALL = 3
SEL_ERROR = -1
SEL_HYPERSLABS = 2
SEL_NONE = 0
SEL_POINTS = 1
SIMPLE = 1
class SpaceID(_mod_h5py__objects.ObjectID):
    '\n        Represents a dataspace identifier.\n\n        Properties:\n\n        shape\n            Numpy-style shape tuple with dimensions.\n\n        * Hashable: No\n        * Equality: Unimplemented\n\n        Can be pickled if HDF5 1.8 is available.\n    '
    __class__ = SpaceID
    def __init__(self, *args, **kwargs):
        '\n        Represents a dataspace identifier.\n\n        Properties:\n\n        shape\n            Numpy-style shape tuple with dimensions.\n\n        * Hashable: No\n        * Equality: Unimplemented\n\n        Can be pickled if HDF5 1.8 is available.\n    '
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
    
    def copy(self, *args, **kwds):
        '() => SpaceID\n\n        Create a new copy of this dataspace.\n        '
        pass
    
    def encode(self, *args, **kwds):
        '() => STRING\n\n        Serialize a dataspace, including its selection.  Bear in mind you\n        can also use the native Python pickling machinery to do this.\n        '
        pass
    
    def extent_copy(self, *args, **kwds):
        "(SpaceID source)\n\n        Replace this dataspace's extent with another's, changing its\n        typecode if necessary.\n        "
        pass
    
    def get_regular_hyperslab(self, *args, **kwds):
        '() => (TUPLE start, TUPLE stride, TUPLE count, TUPLE block)\n\n            Retrieve a regular hyperslab selection.\n            '
        pass
    
    def get_select_bounds(self, *args, **kwds):
        '() => (TUPLE start, TUPLE end)\n\n        Determine the bounding box which exactly contains\n        the current selection.\n        '
        pass
    
    def get_select_elem_npoints(self, *args, **kwds):
        '() => LONG npoints\n\n        Determine the number of elements selected in point-selection mode.\n        '
        pass
    
    def get_select_elem_pointlist(self, *args, **kwds):
        '() => NDARRAY\n\n        Get a list of all selected elements.  Return is a Numpy array of\n        unsigned ints, with shape ``(<npoints>, <space rank)``.\n        '
        pass
    
    def get_select_hyper_blocklist(self, *args, **kwds):
        '() => NDARRAY\n\n        Get the current hyperslab selection.  The returned array has shape::\n\n            (<npoints>, 2, <rank>)\n\n        and can be interpreted as a nested sequence::\n\n            [ (corner_coordinate_1, opposite_coordinate_1), ... ]\n\n        with length equal to the total number of blocks.\n        '
        pass
    
    def get_select_hyper_nblocks(self, *args, **kwds):
        '() => LONG nblocks\n\n        Get the number of hyperslab blocks currently selected.\n        '
        pass
    
    def get_select_npoints(self, *args, **kwds):
        '() => LONG npoints\n\n        Determine the total number of points currently selected.\n        Works for all selection techniques.\n        '
        pass
    
    def get_select_type(self, *args, **kwds):
        ' () => INT select_code\n\n            Determine selection type.  Return values are:\n\n            - SEL_NONE\n            - SEL_ALL\n            - SEL_POINTS\n            - SEL_HYPERSLABS\n        '
        pass
    
    def get_simple_extent_dims(self, *args, **kwds):
        '(BOOL maxdims=False) => TUPLE shape\n\n        Determine the shape of a "simple" (slab) dataspace.  If "maxdims"\n        is True, retrieve the maximum dataspace size instead.\n        '
        pass
    
    def get_simple_extent_ndims(self, *args, **kwds):
        '() => INT rank\n\n        Determine the rank of a "simple" (slab) dataspace.\n        '
        pass
    
    def get_simple_extent_npoints(self, *args, **kwds):
        '() => LONG npoints\n\n        Determine the total number of elements in a dataspace.\n        '
        pass
    
    def get_simple_extent_type(self, *args, **kwds):
        '() => INT class_code\n\n        Class code is either SCALAR or SIMPLE.\n        '
        pass
    
    def is_regular_hyperslab(self, *args, **kwds):
        '() => BOOL\n\n            Determine whether a hyperslab selection is regular.\n            '
        pass
    
    def is_simple(self, *args, **kwds):
        '() => BOOL is_simple\n\n        Determine if an existing dataspace is "simple" (including scalar\n        dataspaces). Currently all HDF5 dataspaces are simple.\n        '
        pass
    
    def offset_simple(self, *args, **kwds):
        '(TUPLE offset=None)\n\n        Set the offset of a dataspace.  The length of the given tuple must\n        match the rank of the dataspace. If None is provided (default),\n        the offsets on all axes will be set to 0.\n        '
        pass
    
    def select_all(self, *args, **kwds):
        '()\n\n        Select all points in the dataspace.\n        '
        pass
    
    def select_elements(self, *args, **kwds):
        '(SEQUENCE coords, INT op=SELECT_SET)\n\n        Select elements by specifying coordinates points.  The argument\n        "coords" may be an ndarray or any nested sequence which can be\n        converted to an array of uints with the shape::\n\n            (<npoints>, <space rank>)\n\n        Examples::\n\n            >>> obj.shape\n            (10, 10)\n            >>> obj.select_elements([(1,2), (3,4), (5,9)])\n\n        A zero-length selection (i.e. shape ``(0, <rank>)``) is not allowed\n        by the HDF5 library.\n        '
        pass
    
    def select_hyperslab(self, *args, **kwds):
        '(TUPLE start, TUPLE count, TUPLE stride=None, TUPLE block=None,\n             INT op=SELECT_SET)\n\n        Select a block region from an existing dataspace.  See the HDF5\n        documentation for the meaning of the "block" and "op" keywords.\n        '
        pass
    
    def select_none(self, *args, **kwds):
        '()\n\n        Deselect entire dataspace.\n        '
        pass
    
    def select_valid(self, *args, **kwds):
        '() => BOOL\n\n        Determine if the current selection falls within\n        the dataspace extent.\n        '
        pass
    
    def set_extent_none(self, *args, **kwds):
        '()\n\n        Remove the dataspace extent; typecode changes to NO_CLASS.\n        '
        pass
    
    def set_extent_simple(self, *args, **kwds):
        '(TUPLE dims_tpl, TUPLE max_dims_tpl=None)\n\n        Reset the dataspace extent via a tuple of dimensions.\n        Every element of dims_tpl must be a positive integer.\n\n        You can optionally specify the maximum dataspace size. The\n        special value UNLIMITED, as an element of max_dims, indicates\n        an unlimited dimension.\n        '
        pass
    
    @property
    def shape(self):
        ' Numpy-style shape tuple representing dimensions.  () == scalar.\n        '
        pass
    

UNLIMITED = 18446744073709551615
__builtins__ = {}
__doc__ = '\n    Low-level interface to the "H5S" family of data-space functions.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5s.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5s'
__package__ = 'h5py'
__test__ = _mod_builtins.dict()
def create(*args, **kwds):
    '(INT class_code) => SpaceID\n\n    Create a new HDF5 dataspace object, of the given class.\n    Legal values are SCALAR and SIMPLE.\n    '
    pass

def create_simple(*args, **kwds):
    '(TUPLE dims_tpl, TUPLE max_dims_tpl) => SpaceID\n\n    Create a simple (slab) dataspace from a tuple of dimensions.\n    Every element of dims_tpl must be a positive integer.\n\n    You can optionally specify the maximum dataspace size. The\n    special value UNLIMITED, as an element of max_dims, indicates\n    an unlimited dimension.\n    '
    pass

def decode(*args, **kwds):
    '(STRING buf) => SpaceID\n\n    Unserialize a dataspace.  Bear in mind you can also use the native\n    Python pickling machinery to do this.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

