import builtins as _mod_builtins
import h5py._objects as _mod_h5py__objects

CRT_ORDER_INDEXED = 2
CRT_ORDER_TRACKED = 1
DATASET_ACCESS = PropClassID()
DATASET_CREATE = PropClassID()
DATASET_XFER = PropClassID()
DEFAULT = None
FILE_ACCESS = PropClassID()
FILE_CREATE = PropClassID()
GROUP_CREATE = PropClassID()
LINK_ACCESS = PropClassID()
LINK_CREATE = PropClassID()
NO_CLASS = PropClassID()
OBJECT_COPY = PropClassID()
OBJECT_CREATE = PropClassID()
class PropClassID(PropID):
    '\n        An HDF5 property list class.\n\n        * Hashable: Yes, by identifier\n        * Equality: Logical H5P comparison\n    '
    __class__ = PropClassID
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
        ' Since classes are library-created and immutable, they are uniquely\n            identified by their HDF5 identifiers.\n        '
        return 0
    
    def __init__(self, *args, **kwargs):
        '\n        An HDF5 property list class.\n\n        * Hashable: Yes, by identifier\n        * Equality: Logical H5P comparison\n    '
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
    

class PropCopyID(PropInstanceID):
    '\n        Generic object copy property list\n    '
    __class__ = PropCopyID
    def __init__(self, *args, **kwargs):
        '\n        Generic object copy property list\n    '
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
    
    def get_copy_object(self, *args, **kwds):
        '() => UINT flags\n\n        Get copy process flags. Legal flags are h5o.COPY*.\n        '
        pass
    
    def set_copy_object(self, *args, **kwds):
        '(UINT flags)\n\n        Set flags for object copying process.  Legal flags are\n        from the h5o.COPY* family:\n\n        h5o.COPY_SHALLOW_HIERARCHY_FLAG\n            Copy only immediate members of a group.\n\n        h5o.COPY_EXPAND_SOFT_LINK_FLAG\n            Expand soft links into new objects.\n\n        h5o.COPY_EXPAND_EXT_LINK_FLAG\n            Expand external link into new objects.\n\n        h5o.COPY_EXPAND_REFERENCE_FLAG\n            Copy objects that are pointed to by references.\n\n        h5o.COPY_WITHOUT_ATTR_FLAG\n            Copy object without copying attributes.\n        '
        pass
    

class PropCreateID(PropInstanceID):
    '\n        Generic object creation property list.\n    '
    __class__ = PropCreateID
    def __init__(self, *args, **kwargs):
        '\n        Generic object creation property list.\n    '
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
    

class PropDAID(PropInstanceID):
    ' Dataset access property list '
    __class__ = PropDAID
    def __init__(self, *args, **kwargs):
        ' Dataset access property list '
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
    
    def get_chunk_cache(self, *args, **kwds):
        '() => TUPLE chunk cache info\n\n        Get the metadata and raw data chunk cache settings.  See the HDF5\n        docs for element definitions.  Return is a 3-tuple with entries:\n\n        0. size_t rdcc_nslots: Number of chunk slots in the raw data chunk cache hash table.\n        1. size_t rdcc_nbytes: Total size of the raw data chunk cache, in bytes.\n        2. DOUBLE rdcc_w0:     Preemption policy.\n        '
        pass
    
    def get_virtual_printf_gap(self, *args, **kwds):
        '() => LONG gap_size\n\n            Return the maximum number of missing source files and/or datasets\n            with the printf-style names when getting the extent for an\n            unlimited virtual dataset.\n            '
        pass
    
    def get_virtual_view(self, *args, **kwds):
        '() => UINT view\n\n            Retrieve the view of the virtual dataset.\n\n            Valid values are:\n\n            - h5d.VDS_FIRST_MISSING\n            - h5d.VDS_LAST_AVAILABLE\n            '
        pass
    
    def set_chunk_cache(self, *args, **kwds):
        '(size_t rdcc_nslots,size_t rdcc_nbytes, double rdcc_w0)\n\n        Sets the raw data chunk cache parameters.\n        '
        pass
    
    def set_virtual_printf_gap(self, *args, **kwds):
        '(LONG gap_size=0)\n\n            Set the maximum number of missing source files and/or datasets\n            with the printf-style names when getting the extent of an unlimited\n            virtual dataset.\n\n            Instruct the library to stop looking for the mapped data stored in\n            the files and/or datasets with the printf-style names after not\n            finding gap_size files and/or datasets. The found source files and\n            datasets will determine the extent of the unlimited virtual dataset\n            with the printf-style mappings. Default value: 0.\n            '
        pass
    
    def set_virtual_view(self, *args, **kwds):
        "(UINT view)\n\n            Set the view of the virtual dataset (VDS) to include or exclude\n            missing mapped elements.\n\n            If view is set to h5d.VDS_FIRST_MISSING, the view includes all data\n            before the first missing mapped data. This setting provides a view\n            containing only the continuous data starting with the dataset’s\n            first data element. Any break in continuity terminates the view.\n\n            If view is set to h5d.VDS_LAST_AVAILABLE, the view includes all\n            available mapped data.\n\n            Missing mapped data is filled with the fill value set in the\n            virtual dataset's creation property list.\n            "
        pass
    

class PropDCID(PropOCID):
    '\n        Dataset creation property list.\n    '
    __class__ = PropDCID
    def __init__(self, *args, **kwargs):
        '\n        Dataset creation property list.\n    '
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
    
    def _has_filter(self, *args, **kwds):
        '(INT filter_code)\n\n        Slow & stupid method to determine if a filter is used in this\n        property list.  Used because the HDF5 function H5Pget_filter_by_id\n        is broken.\n        '
        pass
    
    def all_filters_avail(self, *args, **kwds):
        '() => BOOL\n\n        Determine if all the filters in the pipelist are available to\n        the library.\n        '
        pass
    
    def fill_value_defined(self, *args, **kwds):
        '() => INT fill_status\n\n        Determine the status of the dataset fill value.  Return values are:\n\n        - h5d.FILL_VALUE_UNDEFINED\n        - h5d.FILL_VALUE_DEFAULT\n        - h5d.FILL_VALUE_USER_DEFINED\n        '
        pass
    
    def get_alloc_time(self, *args, **kwds):
        '() => INT alloc_time\n\n        Get the storage space allocation time.  One of h5d.ALLOC_TIME*.\n        '
        pass
    
    def get_chunk(self, *args, **kwds):
        '() => TUPLE chunk_dimensions\n\n        Obtain the dataset chunk size, as a tuple.\n        '
        pass
    
    def get_external(self, *args, **kwds):
        '(UINT idx=0) => TUPLE external_file_info\n\n        Returns information about the indexed external file.\n        Tuple elements are:\n\n        0. STRING name of file (256 chars max)\n        1. UINT offset\n        2. UINT size\n        '
        pass
    
    def get_external_count(self, *args, **kwds):
        '() => INT\n\n        Returns the number of external files for the dataset.\n        '
        pass
    
    def get_fill_time(self, *args, **kwds):
        ' () => INT\n\n        Determine when fill values are written to the dataset.  Legal\n        values (defined in module h5d) are:\n\n        - h5d.FILL_TIME_ALLOC\n        - h5d.FILL_TIME_NEVER\n        - h5d.FILL_TIME_IFSET\n        '
        pass
    
    def get_fill_value(self, *args, **kwds):
        '(NDARRAY value)\n\n        Read the dataset fill value into a NumPy array.  It will be\n        converted to match the array dtype.  If the array has nonzero\n        rank, only the first element will contain the value.\n        '
        pass
    
    def get_filter(self, *args, **kwds):
        '(UINT filter_idx) => TUPLE filter_info\n\n        Get information about a filter, identified by its index.  Tuple\n        elements are:\n\n        0. INT filter code (h5z.FILTER*)\n        1. UINT flags (h5z.FLAG*)\n        2. TUPLE of UINT values; filter aux data (16 values max)\n        3. STRING name of filter (256 chars max)\n        '
        pass
    
    def get_filter_by_id(self, *args, **kwds):
        "(INT filter_code) => TUPLE filter_info or None\n\n        Get information about a filter, identified by its code (one\n        of h5z.FILTER*).  If the filter doesn't exist, returns None.\n        Tuple elements are:\n\n        0. UINT flags (h5z.FLAG*)\n        1. TUPLE of UINT values; filter aux data (16 values max)\n        2. STRING name of filter (256 chars max)\n        "
        pass
    
    def get_layout(self, *args, **kwds):
        '() => INT layout_code\n\n        Determine the storage strategy of a dataset; legal values are:\n\n        - h5d.COMPACT\n        - h5d.CONTIGUOUS\n        - h5d.CHUNKED\n        - h5d.VIRTUAL (If using HDF5 library version 1.10 or later)\n        '
        pass
    
    def get_nfilters(self, *args, **kwds):
        '() => INT\n\n        Determine the number of filters in the pipeline.\n        '
        pass
    
    def get_virtual_count(self, *args, **kwds):
        '() => UINT\n\n            Get the number of mappings for the virtual dataset.\n            '
        pass
    
    def get_virtual_dsetname(self, *args, **kwds):
        '(UINT index=0) => STR\n\n            Get the name of a source dataset used in the mapping of the virtual\n            dataset at the position index.\n            '
        pass
    
    def get_virtual_filename(self, *args, **kwds):
        '(UINT index=0) => STR\n\n            Get the file name of a source dataset used in the mapping of the\n            virtual dataset at the position index.\n            '
        pass
    
    def get_virtual_srcspace(self, *args, **kwds):
        '(UINT index=0) => SpaceID\n\n            Get a dataspace for the selection within the source dataset used\n            in the mapping.\n            '
        pass
    
    def get_virtual_vspace(self, *args, **kwds):
        '(UINT index=0) => SpaceID\n\n            Get a dataspace for the selection within the virtual dataset used\n            in the mapping.\n            '
        pass
    
    def remove_filter(self, *args, **kwds):
        '(INT filter_class)\n\n        Remove a filter from the pipeline.  The class code is one of\n        h5z.FILTER*.\n        '
        pass
    
    def set_alloc_time(self, *args, **kwds):
        '(INT alloc_time)\n\n        Set the storage space allocation time.  One of h5d.ALLOC_TIME*.\n        '
        pass
    
    def set_chunk(self, *args, **kwds):
        "(TUPLE chunksize)\n\n        Set the dataset chunk size.  It's up to you to provide\n        values which are compatible with your dataset.\n        "
        pass
    
    def set_deflate(self, *args, **kwds):
        '(UINT level=5)\n\n        Enable deflate (gzip) compression, at the given level.\n        Valid levels are 0-9, default is 5.\n        '
        pass
    
    def set_external(self, *args, **kwds):
        '(STR name, UINT offset, UINT size)\n\n        Adds an external file to the list of external files for the dataset.\n\n        The first call sets the external storage property in the property list,\n        thus designating that the dataset will be stored in one or more non-HDF5\n        file(s) external to the HDF5 file.'
        pass
    
    def set_fill_time(self, *args, **kwds):
        '(INT fill_time)\n\n        Define when fill values are written to the dataset.  Legal\n        values (defined in module h5d) are:\n\n        - h5d.FILL_TIME_ALLOC\n        - h5d.FILL_TIME_NEVER\n        - h5d.FILL_TIME_IFSET\n        '
        pass
    
    def set_fill_value(self, *args, **kwds):
        '(NDARRAY value)\n\n        Set the dataset fill value.  The object provided should be an\n        0-dimensional NumPy array; otherwise, the value will be read from\n        the first element.\n        '
        pass
    
    def set_filter(self, *args, **kwds):
        '(INT filter_code, UINT flags=0, TUPLE values=None)\n\n        Set a filter in the pipeline.  Params are:\n\n        filter_code\n            One of the following:\n\n            - h5z.FILTER_DEFLATE\n            - h5z.FILTER_SHUFFLE\n            - h5z.FILTER_FLETCHER32\n            - h5z.FILTER_SZIP\n\n        flags\n            Bit flags (h5z.FLAG*) setting filter properties\n\n        values\n            TUPLE of UINTs giving auxiliary data for the filter\n        '
        pass
    
    def set_fletcher32(self, *args, **kwds):
        '()\n\n        Enable Fletcher32 error correction on this list.\n        '
        pass
    
    def set_layout(self, *args, **kwds):
        '(INT layout_code)\n\n        Set dataset storage strategy; legal values are:\n\n        - h5d.COMPACT\n        - h5d.CONTIGUOUS\n        - h5d.CHUNKED\n        - h5d.VIRTUAL (If using HDF5 library version 1.10 or later)\n        '
        pass
    
    def set_scaleoffset(self, *args, **kwds):
        '(H5Z_SO_scale_type_t scale_type, INT scale_factor)\n\n        Enable scale/offset (usually lossy) compression; lossless (e.g. gzip)\n        compression and other filters may be applied on top of this.\n\n        Note that error detection (i.e. fletcher32) cannot precede this in\n        the filter chain, or else all reads on lossily-compressed data will\n        fail.'
        pass
    
    def set_shuffle(self, *args, **kwds):
        '()\n\n        Enable to use of the shuffle filter.  Use this immediately before\n        the deflate filter to increase the compression ratio.\n        '
        pass
    
    def set_szip(self, *args, **kwds):
        '(UINT options, UINT pixels_per_block)\n\n        Enable SZIP compression.  See the HDF5 docs for argument meanings,\n        and general restrictions on use of the SZIP format.\n        '
        pass
    
    def set_virtual(self, *args, **kwds):
        '(SpaceID vspace, STR src_file_name, STR src_dset_name, SpaceID src_space)\n\n            Set the mapping between virtual and source datasets.\n\n            The virtual dataset is described by its virtual dataspace (vspace)\n            to the elements. The source dataset is described by the name of the\n            file where it is located (src_file_name), the name of the dataset\n            (src_dset_name) and its dataspace (src_space).\n            '
        pass
    

class PropDXID(PropInstanceID):
    ' Data transfer property list '
    __class__ = PropDXID
    def __init__(self, *args, **kwargs):
        ' Data transfer property list '
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
    

class PropFAID(PropInstanceID):
    '\n        File access property list\n    '
    __class__ = PropFAID
    def __init__(self, *args, **kwargs):
        '\n        File access property list\n    '
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
    
    def get_alignment(self):
        '\n        Retrieves the current settings for alignment properties from a file access property list.\n        '
        pass
    
    def get_cache(self, *args, **kwds):
        '() => TUPLE cache info\n\n        Get the metadata and raw data chunk cache settings.  See the HDF5\n        docs for element definitions.  Return is a 4-tuple with entries:\n\n        1. INT mdc:              Number of metadata objects\n        2. INT rdcc:             Number of raw data chunks\n        3. UINT rdcc_nbytes:     Size of raw data cache\n        4. DOUBLE rdcc_w0:       Preemption policy for data cache.\n        '
        pass
    
    def get_driver(self, *args, **kwds):
        '() => INT driver code\n\n        Return an integer identifier for the driver used by this list.\n        Although HDF5 implements these as full-fledged objects, they are\n        treated as integers by Python.  Built-in drivers identifiers are\n        listed in module h5fd; they are:\n\n        - h5fd.CORE\n        - h5fd.FAMILY\n        - h5fd.LOG\n        - h5fd.MPIO\n        - h5fd.MULTI\n        - h5fd.SEC2\n        - h5fd.STDIO\n        '
        pass
    
    def get_fapl_core(self, *args, **kwds):
        '() => TUPLE core_settings\n\n        Determine settings for the h5fd.CORE (memory-resident) file driver.\n        Tuple elements are:\n\n        0. UINT "increment": Chunk size for new memory requests\n        1. BOOL "backing_store": If True, write the memory contents to\n           disk when the file is closed.\n        '
        pass
    
    def get_fapl_family(self, *args, **kwds):
        '() => TUPLE info\n\n        Determine family driver settings. Tuple values are:\n\n        0. UINT memb_size\n        1. PropFAID memb_fapl or None\n        '
        pass
    
    def get_fclose_degree(self, *args, **kwds):
        '() => INT close_degree\n        - h5fd.\n        Get the file-close degree, which determines library behavior when\n        a file is closed when objects are still open.  Legal values:\n\n        * h5f.CLOSE_WEAK\n        * h5f.CLOSE_SEMI\n        * h5f.CLOSE_STRONG\n        * h5f.CLOSE_DEFAULT\n        '
        pass
    
    def get_libver_bounds(self, *args, **kwds):
        ' () => (INT low, INT high)\n\n        Get the compatibility level for file format. Returned values are from:\n\n        - h5f.LIBVER_EARLIEST\n        - h5f.LIBVER_LATEST\n        '
        pass
    
    def get_mdc_config(self, *args, **kwds):
        '() => CacheConfig\n        Returns an object that stores all the information about the meta-data cache\n        configuration\n        '
        pass
    
    def get_sieve_buf_size(self, *args, **kwds):
        ' () => UINT size\n\n        Get the current maximum size of the data sieve buffer (in bytes).\n        '
        pass
    
    def set_alignment(self):
        '\n        Sets alignment properties of a file access property list.\n        '
        pass
    
    def set_cache(self, *args, **kwds):
        '(INT mdc, INT rdcc, UINT rdcc_nbytes, DOUBLE rdcc_w0)\n\n        Set the metadata (mdc) and raw data chunk (rdcc) cache properties.\n        See the HDF5 docs for a full explanation.\n        '
        pass
    
    def set_driver(self, *args, **kwds):
        '(INT driver_id)\n\n        Sets the file driver identifier for this file access or data\n        transfer property list.\n        '
        pass
    
    def set_fapl_core(self, *args, **kwds):
        '(UINT increment=64k, BOOL backing_store=True)\n\n        Use the h5fd.CORE (memory-resident) file driver.\n\n        increment\n            Chunk size for new memory requests (default 1 meg)\n\n        backing_store\n            If True (default), memory contents are associated with an\n            on-disk file, which is updated when the file is closed.\n            Set to False for a purely in-memory file.\n        '
        pass
    
    def set_fapl_family(self, *args, **kwds):
        '(UINT memb_size=2**31-1, PropFAID memb_fapl=None)\n\n        Set up the family driver.\n\n        memb_size\n            Member file size\n\n        memb_fapl\n            File access property list for each member access\n        '
        pass
    
    def set_fapl_log(self, *args, **kwds):
        '(STRING logfile, UINT flags, UINT buf_size)\n\n        Enable the use of the logging driver.  See the HDF5 documentation\n        for details.  Flag constants are stored in module h5fd.\n        '
        pass
    
    def set_fapl_sec2(self, *args, **kwds):
        '()\n\n        Select the "section-2" driver (h5fd.SEC2).\n        '
        pass
    
    def set_fapl_stdio(self, *args, **kwds):
        '()\n\n        Select the "stdio" driver (h5fd.STDIO)\n        '
        pass
    
    def set_fclose_degree(self, *args, **kwds):
        '(INT close_degree)\n\n        Set the file-close degree, which determines library behavior when\n        a file is closed when objects are still open.  Legal values:\n\n        * h5f.CLOSE_WEAK\n        * h5f.CLOSE_SEMI\n        * h5f.CLOSE_STRONG\n        * h5f.CLOSE_DEFAULT\n        '
        pass
    
    def set_file_image(self, *args, **kwds):
        '\n            Copy a file image into the property list. Passing None releases\n            any image currently loaded. The parameter image must either be\n            None or support the buffer protocol.\n            '
        pass
    
    def set_fileobj_driver(self, *args, **kwds):
        '(INT driver_id, OBJECT fileobj)\n\n        Select the "fileobj" file driver (h5py-specific).\n        '
        pass
    
    def set_libver_bounds(self, *args, **kwds):
        ' (INT low, INT high)\n\n        Set the compatibility level for file format.  Legal values are:\n\n        - h5f.LIBVER_EARLIEST\n        - h5f.LIBVER_LATEST\n        '
        pass
    
    def set_mdc_config(self, *args, **kwds):
        '(CacheConfig) => None\n        Returns an object that stores all the information about the meta-data cache\n        configuration\n        '
        pass
    
    def set_sieve_buf_size(self, *args, **kwds):
        ' (UINT size)\n\n        Set the maximum size of the data sieve buffer (in bytes).  This\n        buffer can improve I/O performance for hyperslab I/O, by combining\n        reads and writes into blocks of the given size.  The default is 64k.\n        '
        pass
    

class PropFCID(PropOCID):
    '\n        File creation property list.\n    '
    __class__ = PropFCID
    def __init__(self, *args, **kwargs):
        '\n        File creation property list.\n    '
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
    
    def get_link_creation_order(self, *args, **kwds):
        ' () -> UINT flags\n\n        Get tracking and indexing of creation order for links added to this group\n        '
        pass
    
    def get_sizes(self, *args, **kwds):
        '() => TUPLE sizes\n\n        Determine addressing offsets and lengths for objects in an\n        HDF5 file, in bytes.  Return value is a 2-tuple with values:\n\n        0.  UINT Address offsets\n        1.  UINT Lengths\n        '
        pass
    
    def get_userblock(self, *args, **kwds):
        '() => LONG size\n\n        Determine the user block size, in bytes.\n        '
        pass
    
    def get_version(self, *args, **kwds):
        '() => TUPLE version_info\n\n        Determine version information of various file attributes.\n        Elements are:\n\n        0.  UINT Super block version number\n        1.  UINT Freelist version number\n        2.  UINT Symbol table version number\n        3.  UINT Shared object header version number\n        '
        pass
    
    def set_link_creation_order(self, *args, **kwds):
        ' (UINT flags)\n\n        Set tracking and indexing of creation order for links added to this group\n\n        flags -- h5p.CRT_ORDER_TRACKED, h5p.CRT_ORDER_INDEXED\n        '
        pass
    
    def set_sizes(self, *args, **kwds):
        '(UINT addr, UINT size)\n\n        Set the addressing offsets and lengths for objects\n        in an HDF5 file, in bytes.\n        '
        pass
    
    def set_userblock(self, *args, **kwds):
        '(INT/LONG size)\n\n        Set the file user block size, in bytes.\n        Must be a power of 2, and at least 512.\n        '
        pass
    

class PropGCID(PropOCID):
    ' Group creation property list '
    __class__ = PropGCID
    def __init__(self, *args, **kwargs):
        ' Group creation property list '
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
    
    def get_link_creation_order(self, *args, **kwds):
        ' () -> UINT flags\n\n        Get tracking and indexing of creation order for links added to this group\n        '
        pass
    
    def set_link_creation_order(self, *args, **kwds):
        ' (UINT flags)\n\n        Set tracking and indexing of creation order for links added to this group\n\n        flags -- h5p.CRT_ORDER_TRACKED, h5p.CRT_ORDER_INDEXED\n        '
        pass
    

class PropID(_mod_h5py__objects.ObjectID):
    '\n        Base class for all property lists and classes\n    '
    __class__ = PropID
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
        '\n        Base class for all property lists and classes\n    '
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
    
    def equal(self, *args, **kwds):
        '(PropID plist) => BOOL\n\n        Compare this property list (or class) to another for equality.\n        '
        pass
    

class PropInstanceID(PropID):
    '\n        Base class for property list instance objects.  Provides methods which\n        are common across all HDF5 property list classes.\n\n        * Hashable: No\n        * Equality: Logical H5P comparison\n    '
    __class__ = PropInstanceID
    def __init__(self, *args, **kwargs):
        '\n        Base class for property list instance objects.  Provides methods which\n        are common across all HDF5 property list classes.\n\n        * Hashable: No\n        * Equality: Logical H5P comparison\n    '
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
        '() => PropList newid\n\n         Create a new copy of an existing property list object.\n        '
        pass
    
    def get_class(self):
        '() => PropClassID\n\n        Determine the class of a property list object.\n        '
        pass
    

class PropLAID(PropInstanceID):
    ' Link access property list '
    __class__ = PropLAID
    def __init__(self, *args, **kwargs):
        ' Link access property list '
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
    
    def get_elink_fapl(self, *args, **kwds):
        ' () => PropFAID fapl\n\n        Get the file access property list used when opening external files.\n        '
        pass
    
    def get_elink_prefix(self, *args, **kwds):
        '() => STRING prefix\n\n        Get the external link prefix\n        '
        pass
    
    def get_nlinks(self, *args, **kwds):
        '() => UINT\n\n        Get the maximum traversal depth for soft links\n        '
        pass
    
    def set_elink_fapl(self, *args, **kwds):
        ' (PropFAID fapl)\n\n        Set the file access property list used when opening external files.\n        '
        pass
    
    def set_elink_prefix(self, *args, **kwds):
        '(STRING prefix)\n\n        Set the external link prefix.\n        '
        pass
    
    def set_nlinks(self, *args, **kwds):
        '(UINT nlinks)\n\n        Set the maximum traversal depth for soft links\n        '
        pass
    

class PropLCID(PropCreateID):
    ' Link creation property list '
    __class__ = PropLCID
    def __init__(self, *args, **kwargs):
        ' Link creation property list '
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
    
    def get_char_encoding(self, *args, **kwds):
        ' () => INT encoding\n\n        Get the character encoding for link names.  Legal values are:\n\n        - h5t.CSET_ASCII\n        - h5t.CSET_UTF8\n        '
        pass
    
    def get_create_intermediate_group(self, *args, **kwds):
        '() => BOOL\n\n        Determine if missing intermediate groups are automatically created.\n        '
        pass
    
    def set_char_encoding(self, *args, **kwds):
        ' (INT encoding)\n\n        Set the character encoding for link names.  Legal values are:\n\n        - h5t.CSET_ASCII\n        - h5t.CSET_UTF8\n        '
        pass
    
    def set_create_intermediate_group(self, *args, **kwds):
        '(BOOL create)\n\n        Set whether missing intermediate groups are automatically created.\n        '
        pass
    

class PropOCID(PropCreateID):
    ' Object creation property list\n\n    This seems to be a super class for dataset creation property list\n    and group creation property list.\n\n    The documentation is somewhat hazy\n    '
    __class__ = PropOCID
    def __init__(self, *args, **kwargs):
        ' Object creation property list\n\n    This seems to be a super class for dataset creation property list\n    and group creation property list.\n\n    The documentation is somewhat hazy\n    '
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
    
    def get_attr_creation_order(self, *args, **kwds):
        ' () -> UINT flags\n\n        Get tracking and indexing of creation order for object attributes\n        '
        pass
    
    def get_obj_track_times(self, *args, **kwds):
        '\n        Determines whether times associated with an object are being recorded.\n        '
        pass
    
    def set_attr_creation_order(self, *args, **kwds):
        ' (UINT flags)\n\n        Set tracking and indexing of creation order for object attributes\n\n        flags -- h5p.CRT_ORDER_TRACKED, h5p.CRT_ORDER_INDEXED\n        '
        pass
    
    def set_obj_track_times(self, *args, **kwds):
        'Sets the recording of times associated with an object.'
        pass
    

__builtins__ = {}
__doc__ = '\n    HDF5 property list interface.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5p.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5p'
__package__ = 'h5py'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_PropClassID():
    pass

def __pyx_unpickle_PropCopyID():
    pass

def __pyx_unpickle_PropCreateID():
    pass

def __pyx_unpickle_PropDAID():
    pass

def __pyx_unpickle_PropDCID():
    pass

def __pyx_unpickle_PropDXID():
    pass

def __pyx_unpickle_PropFAID():
    pass

def __pyx_unpickle_PropFCID():
    pass

def __pyx_unpickle_PropGCID():
    pass

def __pyx_unpickle_PropID():
    pass

def __pyx_unpickle_PropInstanceID():
    pass

def __pyx_unpickle_PropLCID():
    pass

def __pyx_unpickle_PropOCID():
    pass

__test__ = _mod_builtins.dict()
def create(*args, **kwds):
    '(PropClassID cls) => PropID\n\n    Create a new property list as an instance of a class; classes are:\n\n    - FILE_CREATE\n    - FILE_ACCESS\n    - DATASET_CREATE\n    - DATASET_XFER\n    - DATASET_ACCESS\n    - LINK_CREATE\n    - LINK_ACCESS\n    - GROUP_CREATE\n    - OBJECT_COPY\n    - OBJECT_CREATE\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def with_phil():
    ' Locking decorator '
    pass

