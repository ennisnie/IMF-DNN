import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects
import h5py.h5g as _mod_h5py_h5g

ACC_EXCL = 4
ACC_RDONLY = 0
ACC_RDWR = 1
ACC_SWMR_READ = 64
ACC_SWMR_WRITE = 32
ACC_TRUNC = 2
CLOSE_DEFAULT = 0
CLOSE_SEMI = 2
CLOSE_STRONG = 3
CLOSE_WEAK = 1
FILE_IMAGE_OPEN_RW = 1
class FileID(_mod_h5py_h5g.GroupID):
    '\n        Represents an HDF5 file identifier.\n\n        These objects wrap a small portion of the H5F interface; all the\n        H5F functions which can take arbitrary objects in addition to\n        file identifiers are provided as functions in the h5f module.\n\n        Properties:\n\n        * name:   File name on disk\n\n        Behavior:\n\n        * Hashable: Yes, unique to the file (but not the access mode)\n        * Equality: Hash comparison\n    '
    __class__ = FileID
    def __init__(self, *args, **kwargs):
        '\n        Represents an HDF5 file identifier.\n\n        These objects wrap a small portion of the H5F interface; all the\n        H5F functions which can take arbitrary objects in addition to\n        file identifiers are provided as functions in the h5f module.\n\n        Properties:\n\n        * name:   File name on disk\n\n        Behavior:\n\n        * Hashable: Yes, unique to the file (but not the access mode)\n        * Equality: Hash comparison\n    '
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
    
    def close(self, *args, **kwds):
        '()\n\n        Terminate access through this identifier.  Note that depending on\n        what property list settings were used to open the file, the\n        physical file might not be closed until all remaining open\n        identifiers are freed.\n        '
        pass
    
    def get_access_plist(self, *args, **kwds):
        '() => PropFAID\n\n        Retrieve a copy of the file access property list which manages access\n        to this file.\n        '
        pass
    
    def get_create_plist(self, *args, **kwds):
        '() => PropFCID\n\n        Retrieve a copy of the file creation property list used to\n        create this file.\n        '
        pass
    
    def get_file_image(self, *args, **kwds):
        ' () => BYTES\n\n            Retrieves a copy of the image of an existing, open file.\n\n            Feature requires: 1.8.9\n            '
        pass
    
    def get_filesize(self, *args, **kwds):
        '() => LONG size\n\n        Determine the total size (in bytes) of the HDF5 file,\n        including any user block.\n        '
        pass
    
    def get_freespace(self, *args, **kwds):
        '() => LONG freespace\n\n        Determine the amount of free space in this file.  Note that this\n        only tracks free space until the file is closed.\n        '
        pass
    
    def get_intent(self, *args, **kwds):
        " () => INT\n\n        Determine the file's write intent, either of:\n        - H5F_ACC_RDONLY\n        - H5F_ACC_RDWR\n        "
        pass
    
    def get_mdc_config(self, *args, **kwds):
        '() => CacheConfig\n        Returns an object that stores all the information about the meta-data cache\n        configuration\n        '
        pass
    
    def get_mdc_hit_rate(self, *args, **kwds):
        '() => DOUBLE\n\n        Retrieve the cache hit rate\n\n        '
        pass
    
    def get_mdc_size(self, *args, **kwds):
        '() => (max_size, min_clean_size, cur_size, cur_num_entries) [SIZE_T, SIZE_T, SIZE_T, INT]\n\n        Obtain current metadata cache size data for specified file.\n\n        '
        pass
    
    def get_vfd_handle(self, *args, **kwds):
        ' () => INT\n\n        Retrieve the file handle used by the virtual file driver.\n\n        This method is only functional when the the SEC2 driver is used.\n        '
        pass
    
    @property
    def name(self):
        ' File name on disk (according to h5f.get_name()) '
        pass
    
    def reopen(self, *args, **kwds):
        '() => FileID\n\n        Retrieve another identifier for a file (which must still be open).\n        The new identifier is guaranteed to neither be mounted nor contain\n        a mounted file.\n        '
        pass
    
    def reset_mdc_hit_rate_stats(self, *args, **kwds):
        'no return\n\n        rests the hit-rate statistics\n\n        '
        pass
    
    def set_mdc_config(self, *args, **kwds):
        '(CacheConfig) => None\n        Returns an object that stores all the information about the meta-data cache\n        configuration\n        '
        pass
    
    def start_swmr_write(self, *args, **kwds):
        ' no return\n\n            Enables SWMR writing mode for a file.\n\n            This function will activate SWMR writing mode for a file associated\n            with file_id. This routine will prepare and ensure the file is safe\n            for SWMR writing as follows:\n\n                * Check that the file is opened with write access (H5F_ACC_RDWR).\n                * Check that the file is opened with the latest library format\n                  to ensure data structures with check-summed metadata are used.\n                * Check that the file is not already marked in SWMR writing mode.\n                * Enable reading retries for check-summed metadata to remedy\n                  possible checksum failures from reading inconsistent metadata\n                  on a system that is not atomic.\n                * Turn off usage of the library’s accumulator to avoid possible\n                  ordering problem on a system that is not atomic.\n                * Perform a flush of the file’s data buffers and metadata to set\n                  a consistent state for starting SWMR write operations.\n\n            Library objects are groups, datasets, and committed datatypes. For\n            the current implementation, groups and datasets can remain open when\n            activating SWMR writing mode, but not committed datatypes. Attributes\n            attached to objects cannot remain open.\n\n            Feature requires: 1.9.178 HDF5\n            '
        pass
    

LIBVER_EARLIEST = 0
LIBVER_LATEST = 2
OBJ_ALL = 31
OBJ_ATTR = 16
OBJ_DATASET = 2
OBJ_DATATYPE = 8
OBJ_FILE = 1
OBJ_GROUP = 4
OBJ_LOCAL = 32
SCOPE_GLOBAL = 1
SCOPE_LOCAL = 0
UNLIMITED = 18446744073709551615
__builtins__ = {}
__doc__ = '\n    Low-level operations on HDF5 file objects.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5f.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5f'
__package__ = 'h5py'
def __pyx_unpickle_FileID():
    pass

__test__ = _mod_builtins.dict()
def create(*args, **kwds):
    '(STRING name, INT flags=ACC_TRUNC, PropFCID fcpl=None,\n    PropFAID fapl=None) => FileID\n\n    Create a new HDF5 file.  Keyword "flags" may be:\n\n    ACC_TRUNC\n        Truncate an existing file, discarding its data\n\n    ACC_EXCL\n        Fail if a conflicting file exists\n\n    To keep the behavior in line with that of Python\'s built-in functions,\n    the default is ACC_TRUNC.  Be careful!\n    '
    pass

def flush(*args, **kwds):
    '(ObjectID obj, INT scope=SCOPE_LOCAL)\n\n    Tell the HDF5 library to flush file buffers to disk.  "obj" may\n    be the file identifier, or the identifier of any object residing in\n    the file.  Keyword "scope" may be:\n\n    SCOPE_LOCAL\n        Flush only the given file\n\n    SCOPE_GLOBAL\n        Flush the entire virtual file\n    '
    pass

def get_name(*args, **kwds):
    '(ObjectID obj) => STRING\n\n    Determine the name of the file in which the specified object resides.\n    '
    pass

def get_obj_count(*args, **kwds):
    '(OBJECT where=OBJ_ALL, types=OBJ_ALL) => INT\n\n    Get the number of open objects.\n\n    where\n        Either a FileID instance representing an HDF5 file, or the\n        special constant OBJ_ALL, to count objects in all files.\n\n    type\n        Specify what kinds of object to include.  May be one of OBJ*,\n        or any bitwise combination (e.g. OBJ_FILE | OBJ_ATTR).\n\n        The special value OBJ_ALL matches all object types, and\n        OBJ_LOCAL will only match objects opened through a specific\n        identifier.\n    '
    pass

def get_obj_ids(*args, **kwds):
    '(OBJECT where=OBJ_ALL, types=OBJ_ALL) => LIST\n\n    Get a list of identifier instances for open objects.\n\n    where\n        Either a FileID instance representing an HDF5 file, or the\n        special constant OBJ_ALL, to list objects in all files.\n\n    type\n        Specify what kinds of object to include.  May be one of OBJ*,\n        or any bitwise combination (e.g. OBJ_FILE | OBJ_ATTR).\n\n        The special value OBJ_ALL matches all object types, and\n        OBJ_LOCAL will only match objects opened through a specific\n        identifier.\n    '
    pass

def is_hdf5(*args, **kwds):
    "(STRING name) => BOOL\n\n    Determine if a given file is an HDF5 file.  Note this raises an\n    exception if the file doesn't exist.\n    "
    pass

def mount(*args, **kwds):
    '(ObjectID loc, STRING name, FileID fid)\n\n    Mount an open file on the group "name" under group loc_id.  Note that\n    "name" must already exist.\n    '
    pass

def open(*args, **kwds):
    '(STRING name, UINT flags=ACC_RDWR, PropFAID fapl=None) => FileID\n\n    Open an existing HDF5 file.  Keyword "flags" may be:\n\n    ACC_RDWR\n        Open in read-write mode\n\n    ACC_RDONLY\n        Open in readonly mode\n\n    Keyword fapl may be a file access property list.\n    '
    pass

def open_file_image(*args, **kwds):
    '(STRING image, INT flags=0) => FileID\n\n        Load a new HDF5 file into memory.  Keyword "flags" may be:\n\n        FILE_IMAGE_OPEN_RW\n            Specifies opening the file image in read/write mode.\n        '
    pass

phil = _mod_h5py__objects.FastRLock()
def unmount(*args, **kwds):
    '(ObjectID loc, STRING name)\n\n    Unmount a file, mounted at "name" under group loc_id.\n    '
    pass

def with_phil():
    ' Locking decorator '
    pass

