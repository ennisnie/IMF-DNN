import builtins as _mod_builtins
import tables.atom as _mod_tables_atom
import tables.description as _mod_tables_description
import tables.exceptions as _mod_tables_exceptions
import tables.misc.enum as _mod_tables_misc_enum

Atom = _mod_tables_atom.Atom
Col = _mod_tables_description.Col
Description = _mod_tables_description.Description
Enum = _mod_tables_misc_enum.Enum
EnumAtom = _mod_tables_atom.EnumAtom
H5T_IEEE_F32 = 216172782113783862
H5T_IEEE_F64 = 216172782113783864
H5T_STD_B8 = 216172782113783884
H5T_STD_I16 = 216172782113783870
H5T_STD_I32 = 216172782113783872
H5T_STD_I64 = 216172782113783874
H5T_STD_I8 = 216172782113783868
H5T_STD_U16 = 216172782113783878
H5T_STD_U32 = 216172782113783880
H5T_STD_U64 = 216172782113783882
H5T_STD_U8 = 216172782113783876
H5T_UNIX_D32 = 216172782113783892
H5T_UNIX_D64 = 216172782113783894
HDF5ClassToString = _mod_builtins.dict()
HDF5ExtError = _mod_tables_exceptions.HDF5ExtError
NPExtPrefixesToPTKinds = _mod_builtins.dict()
PTSpecialKinds = _mod_builtins.list()
PTTypeToHDF5 = _mod_builtins.dict()
ReferenceAtom = _mod_tables_atom.ReferenceAtom
__builtins__ = {}
__doc__ = 'Cython utilities for PyTables and HDF5 library.'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/tables/utilsextension.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'tables.utilsextension'
__package__ = 'tables'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def _arch_without_blosc():
    pass

def _broken_hdf5_long_double():
    pass

def _dump_h5_backtrace():
    pass

def atom_from_hdf5_type():
    'Get an atom from a type_id.\n\n  See `hdf5_to_np_ext_type` for an explanation of the `pure_numpy_types`\n  parameter.\n\n  '
    pass

def atom_to_hdf5_type():
    pass

def bisect_left():
    'Return the index where to insert item x in list a, assuming a is sorted.\n\n  The return value i is such that all e in a[:i] have e < x, and all e in\n  a[i:] have e >= x.  So if x already appears in the list, i points just\n  before the leftmost x already there.\n\n  '
    pass

def bisect_right():
    'Return the index where to insert item x in list a, assuming a is sorted.\n\n  The return value i is such that all e in a[:i] have e <= x, and all e in\n  a[i:] have e > x.  So if x already appears in the list, i points just\n  beyond the rightmost x already there.\n\n  '
    pass

def blosc_compcode_to_compname_():
    '\n  blosc_compcode_to_compname()\n\n  Returns the compressor name associated with compressor code.\n\n  Parameters\n  ----------\n  None\n\n  Returns\n  -------\n  out : string\n      The name of the compressor.\n  '
    pass

def blosc_compressor_list():
    '\n  blosc_compressor_list()\n\n  Returns a list of compressors available in the Blosc build.\n\n  Parameters\n  ----------\n  None\n\n  Returns\n  -------\n  out : list\n      The list of names.\n  '
    pass

def blosc_get_complib_info_():
    'Get info from compression libraries included in the current build\n  of blosc.\n\n  Returns a mapping containing the compressor names as keys and the\n  tuple (complib, version) as values.\n\n  '
    pass

blosc_version = _mod_builtins.tuple()
bzip2_version = _mod_builtins.tuple()
def check_file_access(filename, mode):
    'Check for file access in the specified `mode`.\n\n    `mode` is one of the modes supported by `File` objects.  If the file\n    indicated by `filename` can be accessed using that `mode`, the\n    function ends successfully.  Else, an ``IOError`` is raised\n    explaining the reason of the failure.\n\n    All this paraphernalia is used to avoid the lengthy and scaring HDF5\n    messages produced when there are problems opening a file.  No\n    changes are ever made to the file system.\n\n    '
    pass

def create_nested_type():
    'Create a nested type based on a description and return an HDF5 type.'
    pass

def encode_filename():
    'Return the encoded filename in the filesystem encoding.'
    pass

def enum_from_hdf5(enumId):
    'enum_from_hdf5(enumId) -> (Enum, npType)\n\n  Convert an HDF5 enumerated type to a PyTables one.\n\n  This function takes an HDF5 enumerated type and returns an `Enum`\n  instance built from that, and the NumPy type used to encode it.\n\n  '
    return tuple()

def enum_to_hdf5():
    'Convert a PyTables enumerated type to an HDF5 one.\n\n  This function creates an HDF5 enumerated type from the information\n  contained in `enumAtom` (an ``Atom`` object), with the specified\n  `byteorder` (a string).  The resulting HDF5 enumerated type is\n  returned.\n\n  '
    pass

def get_filters():
    'Get a dictionary with the filter names and cd_values'
    pass

def get_hdf5_version():
    'Get the underlying HDF5 library version'
    pass

def get_nested_field():
    'Get the maybe nested field named `fieldname` from the `recarray`.\n\n  The `fieldname` may be a simple field name or a nested field name\n  with slah-separated components.\n\n  '
    pass

def get_pytables_version():
    'Return this extension version.'
    pass

def get_type_enum():
    '_getTypeEnum(h5type) -> hid_t\n\n  Get the native HDF5 enumerated type of `h5type`.\n\n  If `h5type` is an enumerated type, it is returned.  If it is a\n  variable-length type with an enumerated base type, this is returned.  If it\n  is a multi-dimensional type with an enumerated base type, this is returned.\n  Else, a ``TypeError`` is raised.\n\n  '
    pass

hdf5_class_to_string = _mod_builtins.dict()
def hdf5_to_np_ext_type():
    'Map the atomic HDF5 type to a string repr of NumPy extended codes.\n\n  If `pure_numpy_types` is true, detected HDF5 types that does not match pure\n  NumPy types will raise a ``TypeError`` exception.  If not, HDF5 types like\n  TIME, VLEN or ENUM are passed through.\n\n  If `atom` is true, the resulting repr is meant for atoms.  If not, the\n  result is meant for attributes.\n\n  Returns the string repr of type and its shape.  The exception is for\n  compounds types, that returns a NumPy dtype and shape instead.\n\n  '
    pass

def hdf5_to_np_nested_type():
    'Given a HDF5 `type_id`, return a dtype string representation of it.'
    pass

def is_hdf5_file(filename):
    'is_hdf5_file(filename)\n\n  Determine whether a file is in the HDF5 format.\n\n  When successful, it returns a true value if the file is an HDF5\n  file, false otherwise.  If there were problems identifying the file,\n  an HDF5ExtError is raised.\n\n  '
    pass

def is_pytables_file(filename):
    'is_pytables_file(filename)\n\n  Determine whether a file is in the PyTables format.\n\n  When successful, it returns the format version string if the file is a\n  PyTables file, None otherwise.  If there were problems identifying the\n  file, an HDF5ExtError is raised.\n\n  '
    pass

def load_enum():
    'load_enum() -> (Enum, npType)\n\n  Load the enumerated HDF5 type associated with this type_id.\n\n  It returns an `Enum` instance built from that, and the\n  NumPy type used to encode it.\n\n  '
    return tuple()

lzo_version = _mod_builtins.tuple()
def nan_aware_ge():
    pass

def nan_aware_gt():
    pass

def nan_aware_le():
    pass

def nan_aware_lt():
    pass

npext_prefixes_to_ptkinds = _mod_builtins.dict()
platform_byteorder = 0
pt_special_kinds = _mod_builtins.list()
pttype_to_hdf5 = _mod_builtins.dict()
def read_f_attr():
    'Read PyTables file attributes (i.e. in root group).\n\n  Returns the value of the `attr_name` attribute in root group, or `None`\n  if it does not exist.  This call cannot fail.\n\n  '
    pass

def set_blosc_max_threads(nthreads):
    'set_blosc_max_threads(nthreads)\n\n  Set the maximum number of threads that Blosc can use.\n\n  This actually overrides the :data:`tables.parameters.MAX_BLOSC_THREADS`\n  setting in :mod:`tables.parameters`, so the new value will be effective until\n  this function is called again or a new file with a different\n  :data:`tables.parameters.MAX_BLOSC_THREADS` value is specified.\n\n  Returns the previous setting for maximum threads.\n\n  '
    pass

def silence_hdf5_messages(silence=True):
    'silence_hdf5_messages(silence=True)\n\n    Silence (or re-enable) messages from the HDF5 C library.\n\n    The *silence* parameter can be used control the behaviour and reset\n    the standard HDF5 logging.\n\n    .. versionadded:: 2.4\n\n    '
    pass

typeDict = _mod_builtins.dict()
def which_class():
    'Detects a class ID using heuristics.'
    pass

def which_lib_version(name):
    'which_lib_version(name)\n\n  Get version information about a C library.\n\n  If the library indicated by name is available, this function returns a\n  3-tuple containing the major library version as an integer, its full version\n  as a string, and the version date as a string. If the library is not\n  available, None is returned.\n\n  The currently supported library names are hdf5, zlib, lzo, bzip2, and blosc. If\n  another name is given, a ValueError is raised.\n\n  '
    pass

zlib_imported = True
