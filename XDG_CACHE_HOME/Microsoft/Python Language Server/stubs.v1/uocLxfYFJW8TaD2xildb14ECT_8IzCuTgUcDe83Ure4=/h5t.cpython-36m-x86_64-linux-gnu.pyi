import builtins as _mod_builtins
import collections as _mod_collections
import collections.abc as _mod_collections_abc
import h5py._objects as _mod_h5py__objects
import h5py.h5 as _mod_h5py_h5
import h5py.h5py_warnings as _mod_h5py_h5py_warnings
import numpy as _mod_numpy

ARRAY = 10
BITFIELD = 4
BKG_NO = 0
BKG_TEMP = 1
BKG_YES = 2
COMPOUND = 6
CSET_ASCII = 0
CSET_UTF8 = 1
C_S1 = TypeStringID()
DIR_ASCEND = 1
DIR_DEFAULT = 0
DIR_DESCEND = 2
ENUM = 8
FLOAT = 1
FORTRAN_S1 = TypeStringID()
H5pyDeprecationWarning = _mod_h5py_h5py_warnings.H5pyDeprecationWarning
IEEE_F128BE = TypeFloatID()
IEEE_F128LE = TypeFloatID()
IEEE_F16BE = TypeFloatID()
IEEE_F16LE = TypeFloatID()
IEEE_F32BE = TypeFloatID()
IEEE_F32LE = TypeFloatID()
IEEE_F64BE = TypeFloatID()
IEEE_F64LE = TypeFloatID()
INTEGER = 0
LDOUBLE_BE = TypeFloatID()
LDOUBLE_LE = TypeFloatID()
MACHINE = 'x86_64'
Mapping = _mod_collections_abc.Mapping
NATIVE_DOUBLE = TypeFloatID()
NATIVE_FLOAT = TypeFloatID()
NATIVE_INT16 = TypeIntegerID()
NATIVE_INT32 = TypeIntegerID()
NATIVE_INT64 = TypeIntegerID()
NATIVE_INT8 = TypeIntegerID()
NATIVE_LDOUBLE = TypeFloatID()
NATIVE_UINT16 = TypeIntegerID()
NATIVE_UINT32 = TypeIntegerID()
NATIVE_UINT64 = TypeIntegerID()
NATIVE_UINT8 = TypeIntegerID()
NORM_IMPLIED = 0
NORM_MSBSET = 1
NORM_NONE = 2
NO_CLASS = -1
OPAQUE = 5
ORDER_BE = 1
ORDER_LE = 0
ORDER_NATIVE = 0
ORDER_NONE = 4
ORDER_VAX = 2
PAD_BACKGROUND = 2
PAD_ONE = 1
PAD_ZERO = 0
PY3 = True
PYTHON_OBJECT = TypeOpaqueID()
REFERENCE = 7
SGN_2 = 1
SGN_NONE = 0
STD_I16BE = TypeIntegerID()
STD_I16LE = TypeIntegerID()
STD_I32BE = TypeIntegerID()
STD_I32LE = TypeIntegerID()
STD_I64BE = TypeIntegerID()
STD_I64LE = TypeIntegerID()
STD_I8BE = TypeIntegerID()
STD_I8LE = TypeIntegerID()
STD_REF_DSETREG = TypeReferenceID()
STD_REF_OBJ = TypeReferenceID()
STD_U16BE = TypeIntegerID()
STD_U16LE = TypeIntegerID()
STD_U32BE = TypeIntegerID()
STD_U32LE = TypeIntegerID()
STD_U64BE = TypeIntegerID()
STD_U64LE = TypeIntegerID()
STD_U8BE = TypeIntegerID()
STD_U8LE = TypeIntegerID()
STRING = 3
STR_NULLPAD = 1
STR_NULLTERM = 0
STR_SPACEPAD = 2
TIME = 2
class TypeArrayID(TypeID):
    '\n        Represents an array datatype\n    '
    __class__ = TypeArrayID
    def __init__(self, *args, **kwargs):
        '\n        Represents an array datatype\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_array_dims(self, *args, **kwds):
        '() => TUPLE dimensions\n\n        Get the dimensions of the given array datatype as\n        a tuple of integers.\n        '
        pass
    
    def get_array_ndims(self, *args, **kwds):
        '() => INT rank\n\n        Get the rank of the given array datatype.\n        '
        pass
    

class TypeAtomicID(TypeID):
    '\n        Base class for atomic datatypes (float or integer)\n    '
    __class__ = TypeAtomicID
    def __init__(self, *args, **kwargs):
        '\n        Base class for atomic datatypes (float or integer)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_offset(self, *args, **kwds):
        '() => INT offset\n\n        Get the offset of the first significant bit.\n        '
        pass
    
    def get_order(self, *args, **kwds):
        '() => INT order\n\n        Obtain the byte order of the datatype; one of:\n\n        - ORDER_LE\n        - ORDER_BE\n        '
        pass
    
    def get_pad(self, *args, **kwds):
        '() => (INT lsb_pad_code, INT msb_pad_code)\n\n        Determine the padding type.  Possible values are:\n\n        - PAD_ZERO\n        - PAD_ONE\n        - PAD_BACKGROUND\n        '
        pass
    
    def get_precision(self, *args, **kwds):
        '() => UINT precision\n\n        Get the number of significant bits (excludes padding).\n        '
        pass
    
    def set_offset(self, *args, **kwds):
        '(UINT offset)\n\n        Set the offset of the first significant bit.\n        '
        pass
    
    def set_order(self, *args, **kwds):
        '(INT order)\n\n        Set the byte order of the datatype; one of:\n\n        - ORDER_LE\n        - ORDER_BE\n        '
        pass
    
    def set_pad(self, *args, **kwds):
        '(INT lsb_pad_code, INT msb_pad_code)\n\n        Set the padding type.  Possible values are:\n\n        - PAD_ZERO\n        - PAD_ONE\n        - PAD_BACKGROUND\n        '
        pass
    
    def set_precision(self, *args, **kwds):
        '(UINT precision)\n\n        Set the number of significant bits (excludes padding).\n        '
        pass
    

class TypeBitfieldID(TypeID):
    '\n        HDF5 bitfield type\n    '
    __class__ = TypeBitfieldID
    def __init__(self, *args, **kwargs):
        '\n        HDF5 bitfield type\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class TypeCompositeID(TypeID):
    '\n        Base class for enumerated and compound types.\n    '
    __class__ = TypeCompositeID
    def __init__(self, *args, **kwargs):
        '\n        Base class for enumerated and compound types.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_member_index(self, *args, **kwds):
        '(STRING name) => INT index\n\n        Determine the index of a member of a compound or enumerated datatype\n        identified by a string name.\n        '
        pass
    
    def get_member_name(self, *args, **kwds):
        '(INT member) => STRING name\n\n        Determine the name of a member of a compound or enumerated type,\n        identified by its index (0 <= member < nmembers).\n        '
        pass
    
    def get_nmembers(self, *args, **kwds):
        '() => INT number_of_members\n\n        Determine the number of members in a compound or enumerated type.\n        '
        pass
    

class TypeCompoundID(TypeCompositeID):
    '\n        Represents a compound datatype\n    '
    __class__ = TypeCompoundID
    def __init__(self, *args, **kwargs):
        '\n        Represents a compound datatype\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_member_class(self, *args, **kwds):
        '(INT member) => INT class\n\n        Determine the datatype class of the member of a compound type,\n        identified by its index (0 <= member < nmembers).\n        '
        pass
    
    def get_member_offset(self, *args, **kwds):
        '(INT member) => INT offset\n\n        Determine the offset, in bytes, of the beginning of the specified\n        member of a compound datatype.\n        '
        pass
    
    def get_member_type(self, *args, **kwds):
        '(INT member) => TypeID\n\n        Create a copy of a member of a compound datatype, identified by its\n        index.\n        '
        pass
    
    def insert(self, *args, **kwds):
        '(STRING name, UINT offset, TypeID field)\n\n        Add a named member datatype to a compound datatype.  The parameter\n        offset indicates the offset from the start of the compound datatype,\n        in bytes.\n        '
        pass
    
    def pack(self, *args, **kwds):
        '()\n\n        Recursively removes padding (introduced on account of e.g. compiler\n        alignment rules) from a compound datatype.\n        '
        pass
    

class TypeEnumID(TypeCompositeID):
    '\n        Represents an enumerated type\n    '
    __class__ = TypeEnumID
    def __init__(self, *args, **kwargs):
        '\n        Represents an enumerated type\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def enum_insert(self, *args, **kwds):
        '(STRING name, INT/LONG value)\n\n        Define a new member of an enumerated type.  The value will be\n        automatically converted to the base type defined for this enum.  If\n        the conversion results in overflow, the value will be silently\n        clipped.\n        '
        pass
    
    def enum_nameof(self, *args, **kwds):
        '(LONG value) => STRING name\n\n        Determine the name associated with the given value.  Due to a\n        limitation of the HDF5 library, this can only retrieve names up to\n        1023 characters in length.\n        '
        pass
    
    def enum_valueof(self, *args, **kwds):
        '(STRING name) => LONG value\n\n        Get the value associated with an enum name.\n        '
        pass
    
    def get_member_value(self, *args, **kwds):
        '(UINT index) => LONG value\n\n        Determine the value for the member at the given zero-based index.\n        '
        pass
    

class TypeFloatID(TypeAtomicID):
    '\n        Floating-point atomic datatypes\n    '
    __class__ = TypeFloatID
    def __init__(self, *args, **kwargs):
        '\n        Floating-point atomic datatypes\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_ebias(self, *args, **kwds):
        '() => UINT ebias\n\n        Get the exponent bias.\n        '
        pass
    
    def get_fields(self, *args, **kwds):
        '() => TUPLE field_info\n\n        Get information about floating-point bit fields.  See the HDF5\n        docs for a full description.  Tuple has the following members:\n\n        0. UINT spos\n        1. UINT epos\n        2. UINT esize\n        3. UINT mpos\n        4. UINT msize\n        '
        pass
    
    def get_inpad(self, *args, **kwds):
        '() => INT pad_code\n\n        Determine the internal padding strategy.  Legal values are:\n\n        - PAD_ZERO\n        - PAD_ONE\n        - PAD_BACKGROUND\n        '
        pass
    
    def get_norm(self, *args, **kwds):
        '() => INT normalization_code\n\n        Get the normalization strategy.  Legal values are:\n\n        - NORM_IMPLIED\n        - NORM_MSBSET\n        - NORM_NONE\n        '
        pass
    
    def set_ebias(self, *args, **kwds):
        '(UINT ebias)\n\n        Set the exponent bias.\n        '
        pass
    
    def set_fields(self, *args, **kwds):
        '(UINT spos, UINT epos, UINT esize, UINT mpos, UINT msize)\n\n        Set floating-point bit fields.  Refer to the HDF5 docs for\n        argument definitions.\n        '
        pass
    
    def set_inpad(self, *args, **kwds):
        '(INT pad_code)\n\n        Set the internal padding strategy.  Legal values are:\n\n        - PAD_ZERO\n        - PAD_ONE\n        - PAD_BACKGROUND\n        '
        pass
    
    def set_norm(self, *args, **kwds):
        '(INT normalization_code)\n\n        Set the normalization strategy.  Legal values are:\n\n        - NORM_IMPLIED\n        - NORM_MSBSET\n        - NORM_NONE\n        '
        pass
    

class TypeID(_mod_h5py__objects.ObjectID):
    '\n        Base class for type identifiers (implements common operations)\n\n        * Hashable: If committed; in HDF5 1.8.X, also if locked\n        * Equality: Logical H5T comparison\n    '
    __class__ = TypeID
    def __copy__(self):
        pass
    
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
        '\n        Base class for type identifiers (implements common operations)\n\n        * Hashable: If committed; in HDF5 1.8.X, also if locked\n        * Equality: Logical H5T comparison\n    '
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
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def commit(self, *args, **kwds):
        '(ObjectID group, STRING name, PropID lcpl=None)\n\n        Commit this (transient) datatype to a named datatype in a file.\n        If present, lcpl may be a link creation property list.\n        '
        pass
    
    def committed(self, *args, **kwds):
        '() => BOOL is_comitted\n\n        Determine if a given type object is named (T) or transient (F).\n        '
        pass
    
    def copy(self, *args, **kwds):
        '() => TypeID\n\n        Create a copy of this type object.\n        '
        pass
    
    def detect_class(self, *args, **kwds):
        '(INT classtype) => BOOL class_is_present\n\n        Determine if a member of the given class exists in a compound\n        datatype.  The search is recursive.\n        '
        pass
    
    @property
    def dtype(self):
        ' A Numpy-style dtype object representing this object.\n        '
        pass
    
    def encode(self, *args, **kwds):
        '() => STRING\n\n        Serialize an HDF5 type.  Bear in mind you can also use the\n        native Python pickle/unpickle machinery to do this.  The\n        returned string may contain binary values, including NULLs.\n        '
        pass
    
    def equal(self, *args, **kwds):
        '(TypeID typeid) => BOOL\n\n        Logical comparison between datatypes.  Also called by\n        Python\'s "==" operator.\n        '
        pass
    
    def get_class(self, *args, **kwds):
        "() => INT classcode\n\n        Determine the datatype's class code.\n        "
        pass
    
    def get_size(self, *args, **kwds):
        ' () => INT size\n\n            Determine the total size of a datatype, in bytes.\n        '
        pass
    
    def get_super(self, *args, **kwds):
        '() => TypeID\n\n        Determine the parent type of an array, enumeration or vlen datatype.\n        '
        pass
    
    def lock(self, *args, **kwds):
        "()\n\n        Lock this datatype, which makes it immutable and indestructible.\n        Once locked, it can't be unlocked.\n        "
        pass
    
    def set_size(self, *args, **kwds):
        '(UINT size)\n\n        Set the total size of the datatype, in bytes.\n        '
        pass
    

class TypeIntegerID(TypeAtomicID):
    '\n        Integer atomic datatypes\n    '
    __class__ = TypeIntegerID
    def __init__(self, *args, **kwargs):
        '\n        Integer atomic datatypes\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_sign(self, *args, **kwds):
        '() => INT sign\n\n        Get the "signedness" of the datatype; one of:\n\n        SGN_NONE\n            Unsigned\n\n        SGN_2\n            Signed 2\'s complement\n        '
        pass
    
    def set_sign(self, *args, **kwds):
        '(INT sign)\n\n        Set the "signedness" of the datatype; one of:\n\n        SGN_NONE\n            Unsigned\n\n        SGN_2\n            Signed 2\'s complement\n        '
        pass
    

class TypeOpaqueID(TypeID):
    '\n        Represents an opaque type\n    '
    __class__ = TypeOpaqueID
    def __init__(self, *args, **kwargs):
        '\n        Represents an opaque type\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_tag(self, *args, **kwds):
        '() => STRING tag\n\n        Get the tag associated with an opaque datatype.\n        '
        pass
    
    def set_tag(self, *args, **kwds):
        '(STRING tag)\n\n        Set a string describing the contents of an opaque datatype.\n        Limited to 256 characters.\n        '
        pass
    

class TypeReferenceID(TypeID):
    '\n        HDF5 object or region reference\n    '
    __class__ = TypeReferenceID
    def __init__(self, *args, **kwargs):
        '\n        HDF5 object or region reference\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class TypeStringID(TypeID):
    '\n        String datatypes, both fixed and vlen.\n    '
    __class__ = TypeStringID
    def __init__(self, *args, **kwargs):
        '\n        String datatypes, both fixed and vlen.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_cset(self, *args, **kwds):
        '() => INT character_set\n\n        Retrieve the character set used for a string.\n        '
        pass
    
    def get_strpad(self, *args, **kwds):
        '() => INT padding_type\n\n        Get the padding type.  Legal values are:\n\n        STR_NULLTERM\n            NULL termination only (C style)\n\n        STR_NULLPAD\n            Pad buffer with NULLs\n\n        STR_SPACEPAD\n            Pad buffer with spaces (FORTRAN style)\n        '
        pass
    
    def is_variable_str(self, *args, **kwds):
        '() => BOOL is_variable\n\n        Determine if the given string datatype is a variable-length string.\n        '
        pass
    
    def set_cset(self, *args, **kwds):
        '(INT character_set)\n\n        Set the character set used for a string.\n        '
        pass
    
    def set_strpad(self, *args, **kwds):
        '(INT pad)\n\n        Set the padding type.  Legal values are:\n\n        STR_NULLTERM\n            NULL termination only (C style)\n\n        STR_NULLPAD\n            Pad buffer with NULLs\n\n        STR_SPACEPAD\n            Pad buffer with spaces (FORTRAN style)\n        '
        pass
    

class TypeTimeID(TypeID):
    '\n        Unix-style time_t (deprecated)\n    '
    __class__ = TypeTimeID
    def __init__(self, *args, **kwargs):
        '\n        Unix-style time_t (deprecated)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class TypeVlenID(TypeID):
    '\n        Non-string vlen datatypes.\n    '
    __class__ = TypeVlenID
    def __init__(self, *args, **kwargs):
        '\n        Non-string vlen datatypes.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

UNIX_D32BE = TypeTimeID()
UNIX_D32LE = TypeTimeID()
UNIX_D64BE = TypeTimeID()
UNIX_D64LE = TypeTimeID()
VARIABLE = 18446744073709551615
VLEN = 9
class _DeprecatedMapping(_mod_collections_abc.Mapping):
    '\n    Mapping class which warns when members are accessed\n    '
    __abstractmethods__ = _mod_builtins.frozenset()
    __class__ = _DeprecatedMapping
    __dict__ = {}
    def __getitem__(self, key):
        pass
    
    def __init__(self, mapping, message):
        '\n    Mapping class which warns when members are accessed\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        return _DeprecatedMapping()
    
    def __len__(self):
        return 0
    
    __module__ = 'h5py.h5t'
    def __subclasshook__(self, cls, C):
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    _abc_cache = _mod__weakrefset.WeakSet()
    _abc_negative_cache = _mod__weakrefset.WeakSet()
    _abc_negative_cache_version = 43
    _abc_registry = _mod__weakrefset.WeakSet()

__builtins__ = {}
__doc__ = '\n    HDF5 "H5T" data-type API\n\n    This module contains the datatype identifier class TypeID, and its\n    subclasses which represent things like integer/float/compound identifiers.\n    The majority of the H5T API is presented as methods on these identifiers.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/h5py/h5t.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'h5py.h5t'
__package__ = 'h5py'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
_available_ftypes = _mod_builtins.tuple()
def _get_available_ftypes():
    pass

def _get_float_dtype_to_hdf5():
    pass

def array_create(*args, **kwds):
    '(TypeID base, TUPLE dimensions) => TypeArrayID\n\n    Create a new array datatype, using and HDF5 parent type and\n    dimensions given via a tuple of positive integers.  "Unlimited"\n    dimensions are not allowed.\n    '
    pass

available_ftypes = _DeprecatedMapping()
cfg = _mod_h5py_h5.H5PYConfig()
def check_dtype(*args, **kwds):
    ' Check a dtype for h5py special type "hint" information.  Only one\n    keyword may be given.\n\n    vlen = dtype\n        If the dtype represents an HDF5 vlen, returns the Python base class.\n        Currently only builting string vlens (str) are supported.  Returns\n        None if the dtype does not represent an HDF5 vlen.\n\n    enum = dtype\n        If the dtype represents an HDF5 enumerated type, returns the dictionary\n        mapping string names to integer values.  Returns None if the dtype does\n        not represent an HDF5 enumerated type.\n\n    ref = dtype\n        If the dtype represents an HDF5 reference type, returns the reference\n        class (either Reference or RegionReference).  Returns None if the dtype\n        does not represent an HDF5 reference type.\n    '
    pass

def convert(*args, **kwds):
    ' (TypeID src, TypeID dst, UINT n, NDARRAY buf, NDARRAY bkg=None,\n    PropID dxpl=None)\n\n    Convert n contiguous elements of a buffer in-place.  The array dtype\n    is ignored.  The backing buffer is optional; for conversion of compound\n    types, a temporary copy of conversion buffer will used for backing if\n    one is not supplied.\n    '
    pass

def create(*args, **kwds):
    '(INT classtype, UINT size) => TypeID\n\n    Create a new HDF5 type object.  Legal class values are\n    COMPOUND and OPAQUE.  Use enum_create for enums.\n    '
    pass

def decode(*args, **kwds):
    '(STRING buf) => TypeID\n\n    Unserialize an HDF5 type.  You can also do this with the native\n    Python pickling machinery.\n    '
    pass

defaultdict = _mod_collections.defaultdict
def enum_create(*args, **kwds):
    '(TypeID base) => TypeID\n\n    Create a new enumerated type based on an (integer) parent type.\n    '
    pass

def find(*args, **kwds):
    ' (TypeID src, TypeID dst) => TUPLE or None\n\n    Determine if a conversion path exists from src to dst.  Result is None\n    or a tuple describing the conversion path.  Currently tuple entries are:\n\n    1. INT need_bkg:    Whether this routine requires a backing buffer.\n                        Values are BKG_NO, BKG_TEMP and BKG_YES.\n    '
    pass

ftype = _mod_numpy.bytes_
def get_config():
    '() => H5PYConfig\n\n    Get a reference to the global library configuration object.\n    '
    pass

def open(*args, **kwds):
    '(ObjectID group, STRING name) => TypeID\n\n    Open a named datatype from a file.\n    '
    pass

phil = _mod_h5py__objects.FastRLock()
def py_create():
    '(OBJECT dtype_in, BOOL logical=False) => TypeID\n\n    Given a Numpy dtype object, generate a byte-for-byte memory-compatible\n    HDF5 datatype object.  The result is guaranteed to be transient and\n    unlocked.\n\n    Argument dtype_in may be a dtype object, or anything which can be\n    converted to a dtype, including strings like \'<i4\'.\n\n    logical\n        If this flag is set, instead of returning a byte-for-byte identical\n        representation of the type, the function returns the closest logically\n        appropriate HDF5 type.  For example, in the case of a "hinted" dtype\n        of kind "O" representing a string, it would return an HDF5 variable-\n        length string type.\n    '
    pass

def py_get_enum():
    ' (DTYPE dt_in) => DICT\n\n    Deprecated; use check_dtype() instead.\n    '
    pass

def py_get_vlen():
    ' (OBJECT dt_in) => TYPE\n\n    Deprecated; use check_dtype() instead.\n    '
    pass

def py_new_enum():
    ' (DTYPE dt_in, DICT enum_vals) => DTYPE\n\n    Deprecated; use special_dtype() instead.\n    '
    pass

def py_new_vlen():
    ' (OBJECT kind) => DTYPE\n\n    Deprecated; use special_dtype() instead.\n    '
    pass

def special_dtype(*args, **kwds):
    ' Create a new h5py "special" type.  Only one keyword may be given.\n\n    Legal keywords are:\n\n    vlen = basetype\n        Base type for HDF5 variable-length datatype. This can be Python\n        str type or instance of np.dtype.\n        Example: special_dtype( vlen=str )\n\n    enum = (basetype, values_dict)\n        Create a NumPy representation of an HDF5 enumerated type.  Provide\n        a 2-tuple containing an (integer) base dtype and a dict mapping\n        string names to integer values.\n\n    ref = Reference | RegionReference\n        Create a NumPy representation of an HDF5 object or region reference\n        type.\n    '
    pass

def typewrap():
    pass

def vlen_create(*args, **kwds):
    '(TypeID base) => TypeID\n\n    Create a new variable-length datatype, using any HDF5 type as a base.\n\n    Although the Python interface can manipulate these types, there is no\n    provision for reading/writing vlen data.\n    '
    pass

def warn():
    'Issue a warning, or maybe ignore it or raise an exception.'
    pass

def with_phil():
    ' Locking decorator '
    pass

