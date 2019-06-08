import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

ALLOC_TIME_DEFAULT = 0
ALLOC_TIME_EARLY = 1
ALLOC_TIME_INCR = 3
ALLOC_TIME_LATE = 2
CHUNKED = 2
COMPACT = 0
CONTIGUOUS = 1
class DatasetID(_mod_h5py__objects.ObjectID):
    '\n        Represents an HDF5 dataset identifier.\n\n        Objects of this class may be used in any HDF5 function which expects\n        a dataset identifier.  Also, all H5D* functions which take a dataset\n        instance as their first argument are presented as methods of this\n        class.\n\n        Properties:\n        dtype:  Numpy dtype representing the dataset type\n        shape:  Numpy-style shape tuple representing the dataspace\n        rank:   Integer giving dataset rank\n\n        * Hashable: Yes, unless anonymous\n        * Equality: True HDF5 identity if unless anonymous\n    '
    __class__ = DatasetID
    def __init__(self, *args, **kwargs):
        '\n        Represents an HDF5 dataset identifier.\n\n        Objects of this class may be used in any HDF5 function which expects\n        a dataset identifier.  Also, all H5D* functions which take a dataset\n        instance as their first argument are presented as methods of this\n        class.\n\n        Properties:\n        dtype:  Numpy dtype representing the dataset type\n        shape:  Numpy-style shape tuple representing the dataspace\n        rank:   Integer giving dataset rank\n\n        * Hashable: Yes, unless anonymous\n        * Equality: True HDF5 identity if unless anonymous\n    '
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
        ' Numpy dtype object representing the dataset type '
        pass
    
    def extend(self, *args, **kwds):
        ' (TUPLE shape)\n\n            Extend the given dataset so it\'s at least as big as "shape".  Note\n            that a dataset may only be extended up to the maximum dimensions of\n            its dataspace, which are fixed when the dataset is created.\n        '
        pass
    
    def flush(self, *args, **kwds):
        ' no return\n\n            Flushes all buffers associated with a dataset to disk.\n\n            This function causes all buffers associated with a dataset to be\n            immediately flushed to disk without removing the data from the cache.\n\n            Use this in SWMR write mode to allow readers to be updated with the\n            dataset changes.\n\n            Feature requires: 1.9.178 HDF5\n            '
        pass
    
    def get_access_plist(self, *args, **kwds):
        ' () => PropDAID\n\n            Create an return a new copy of the dataset access property list.\n        '
        pass
    
    def get_create_plist(self, *args, **kwds):
        ' () => PropDCID\n\n            Create an return a new copy of the dataset creation property list\n            used when this dataset was created.\n        '
        pass
    
    def get_offset(self, *args, **kwds):
        " () => LONG offset or None\n\n            Get the offset of this dataset in the file, in bytes, or None if\n            it doesn't have one.  This is always the case for datasets which\n            use chunked storage, compact datasets, and datasets for which space\n            has not yet been allocated in the file.\n        "
        pass
    
    def get_space(self, *args, **kwds):
        ' () => SpaceID\n\n            Create and return a new copy of the dataspace for this dataset.\n        '
        pass
    
    def get_space_status(self, *args, **kwds):
        ' () => INT space_status_code\n\n            Determine if space has been allocated for a dataset.\n            Return value is one of:\n\n            * SPACE_STATUS_NOT_ALLOCATED\n            * SPACE_STATUS_PART_ALLOCATED\n            * SPACE_STATUS_ALLOCATED\n        '
        pass
    
    def get_storage_size(self, *args, **kwds):
        ' () => LONG storage_size\n\n            Determine the amount of file space required for a dataset.  Note\n            this only counts the space which has actually been allocated; it\n            may even be zero.\n        '
        pass
    
    def get_type(self, *args, **kwds):
        ' () => TypeID\n\n            Create and return a new copy of the datatype for this dataset.\n        '
        pass
    
    @property
    def rank(self):
        ' Integer giving the dataset rank (0 = scalar) '
        pass
    
    def read(self, *args, **kwds):
        " (SpaceID mspace, SpaceID fspace, NDARRAY arr_obj,\n             TypeID mtype=None, PropDXID dxpl=None)\n\n            Read data from an HDF5 dataset into a Numpy array.\n\n            It is your responsibility to ensure that the memory dataspace\n            provided is compatible with the shape of the Numpy array.  Since a\n            wide variety of dataspace configurations are possible, this is not\n            checked.  You can easily crash Python by reading in data from too\n            large a dataspace.\n\n            If a memory datatype is not specified, one will be auto-created\n            based on the array's dtype.\n\n            The provided Numpy array must be writable and C-contiguous.  If\n            this is not the case, ValueError will be raised and the read will\n            fail.  Keyword dxpl may be a dataset transfer property list.\n        "
        pass
    
    def refresh(self, *args, **kwds):
        ' no return\n\n            Refreshes all buffers associated with a dataset.\n\n            This function causes all buffers associated with a dataset to be\n            cleared and immediately re-loaded with updated contents from disk.\n\n            This function essentially closes the dataset, evicts all metadata\n            associated with it from the cache, and then re-opens the dataset.\n            The reopened dataset is automatically re-registered with the same ID.\n\n            Use this in SWMR read mode to poll for dataset changes.\n\n            Feature requires: 1.9.178 HDF5\n            '
        pass
    
    def set_extent(self, *args, **kwds):
        ' (TUPLE shape)\n\n            Set the size of the dataspace to match the given shape.  If the new\n            size is larger in any dimension, it must be compatible with the\n            maximum dataspace size.\n        '
        pass
    
    @property
    def shape(self):
        ' Numpy-style shape tuple representing the dataspace '
        pass
    
    def write(self, *args, **kwds):
        " (SpaceID mspace, SpaceID fspace, NDARRAY arr_obj,\n             TypeID mtype=None, PropDXID dxpl=None)\n\n            Write data from a Numpy array to an HDF5 dataset. Keyword dxpl may\n            be a dataset transfer property list.\n\n            It is your responsibility to ensure that the memory dataspace\n            provided is compatible with the shape of the Numpy array.  Since a\n            wide variety of dataspace configurations are possible, this is not\n            checked.  You can easily crash Python by writing data from too\n            large a dataspace.\n\n            If a memory datatype is not specified, one will be auto-created\n            based on the array's dtype.\n\n            The provided Numpy array must be C-contiguous.  If this is not the\n            case, ValueError will be raised and the read will fail.\n        "
        pass
    
    def write_direct_chunk(self):
        ' (offsets, bytes data, H5Z_filter_t filter_mask=H5Z_FILTER_NONE, PropID dxpl=None)\n\n            Writes data from a bytes array (as provided e.g. by struct.pack) directly\n            to a chunk at position specified by the offsets argument.\n\n            Feature requires: 1.8.11 HDF5\n            '
        pass
    

FILL_TIME_ALLOC = 0
FILL_TIME_IFSET = 2
FILL_TIME_NEVER = 1
FILL_VALUE_DEFAULT = 1
FILL_VALUE_UNDEFINED = 0
FILL_VALUE_USER_DEFINED = 2
SPACE_STATUS_ALLOCATED = 2
SPACE_STATUS_NOT_ALLOCATED = 0
SPACE_STATUS_PART_ALLOCATED = 1
VDS_FIRST_MISSING = 0
VDS_LAST_AVAILABLE = 1
VIRTUAL = 3
__builtins__ = {}
__doc__ = '\n    Provides access to the low-level HDF5 "H5D" dataset interface.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5d.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5d'
__package__ = 'h5py'
def __pyx_unpickle_DatasetID():
    pass

__test__ = _mod_builtins.dict()
def create(*args, **kwds):
    ' (objectID loc, STRING name or None, TypeID tid, SpaceID space,\n             PropDCID dcpl=None, PropID lcpl=None) => DatasetID\n\n        Create a new dataset.  If "name" is None, the dataset will be\n        anonymous.\n        '
    pass

def open(*args, **kwds):
    ' (ObjectID loc, STRING name, PropID dapl=None) => DatasetID\n\n    Open an existing dataset attached to a group or file object, by name.\n\n    If specified, dapl may be a dataset access property list.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

