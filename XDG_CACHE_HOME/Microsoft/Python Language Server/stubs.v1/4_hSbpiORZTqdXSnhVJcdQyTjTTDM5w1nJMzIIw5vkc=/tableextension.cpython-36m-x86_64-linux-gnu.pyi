import builtins as _mod_builtins
import numpy as _mod_numpy
import tables.description as _mod_tables_description
import tables.exceptions as _mod_tables_exceptions
import tables.hdf5extension as _mod_tables_hdf5extension

Col = _mod_tables_description.Col
H5T_STD_I64 = 216172782113783874
HDF5ExtError = _mod_tables_exceptions.HDF5ExtError
class Row(_mod_builtins.object):
    'Table row iterator and field accessor.\n\n  Instances of this class are used to fetch and set the values\n  of individual table fields.  It works very much like a dictionary,\n  where keys are the pathnames or positions (extended slicing is\n  supported) of the fields in the associated table in a specific row.\n\n  This class provides an *iterator interface*\n  so that you can use the same Row instance to\n  access successive table rows one after the other.  There are also\n  some important methods that are useful for accessing, adding and\n  modifying values in tables.\n\n  .. rubric:: Row attributes\n\n  .. attribute:: nrow\n\n      The current row number.\n\n      This property is useful for knowing which row is being dealt with in the\n      middle of a loop or iterator.\n\n  '
    __class__ = Row
    def __contains__(self, value):
        '__contains__(item)\n\n    A true value is returned if item is found in current row, false\n    otherwise.\n\n    '
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, index):
        "__getitem__(key)\n\n    Get the row field specified by the `key`.\n\n    The key can be a string (the name of the field), an integer (the\n    position of the field) or a slice (the range of field positions). When\n    key is a slice, the returned value is a *tuple* containing the values\n    of the specified fields.\n\n    Examples\n    --------\n\n    ::\n\n        res = [row['var3'] for row in table.where('var2 < 20')]\n\n    which selects the var3 field for all the rows that fulfil the\n    condition. Or::\n\n        res = [row[4] for row in table if row[1] < 20]\n\n    which selects the field in the *4th* position for all the rows that\n    fulfil the condition. Or::\n\n        res = [row[:] for row in table if row['var2'] < 20]\n\n    which selects the all the fields (in the form of a *tuple*) for all the\n    rows that fulfil the condition. Or::\n\n        res = [row[1::2] for row in table.iterrows(2, 3000, 3)]\n\n    which selects all the fields in even positions (in the form of a\n    *tuple*) for all the rows in the slice [2:3000:3].\n\n    "
        pass
    
    def __init__(self, *args, **kwargs):
        'Table row iterator and field accessor.\n\n  Instances of this class are used to fetch and set the values\n  of individual table fields.  It works very much like a dictionary,\n  where keys are the pathnames or positions (extended slicing is\n  supported) of the fields in the associated table in a specific row.\n\n  This class provides an *iterator interface*\n  so that you can use the same Row instance to\n  access successive table rows one after the other.  There are also\n  some important methods that are useful for accessing, adding and\n  modifying values in tables.\n\n  .. rubric:: Row attributes\n\n  .. attribute:: nrow\n\n      The current row number.\n\n      This property is useful for knowing which row is being dealt with in the\n      middle of a loop or iterator.\n\n  '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Iterator that traverses all the data in the Table'
        return Row()
    
    def __next__(self):
        'next() method for __iter__() that is called on each iteration'
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Represent the record as an string'
        return ''
    
    def __setitem__(self, index, value):
        "__setitem__(key, value)\n\n    Set the key row field to the specified value.\n\n    Differently from its __getitem__() counterpart, in this case key can\n    only be a string (the name of the field). The changes done via\n    __setitem__() will not take effect on the data on disk until any of the\n    :meth:`Row.append` or :meth:`Row.update` methods are called.\n\n    Examples\n    --------\n\n    ::\n\n        for row in table.iterrows(step=10):\n            row['col1'] = row.nrow\n            row['col2'] = 'b'\n            row['col3'] = 0.0\n            row.update()\n        table.flush()\n\n    which modifies every tenth row in the table.\n\n    "
        return None
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Represent the record as an string'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _fill_col(self):
        'Read a field from a table on disk and put the result in result'
        pass
    
    def _flush_buffered_rows(self):
        pass
    
    def _flush_mod_rows(self):
        'Flush any possible modified row using Row.update()'
        pass
    
    def _get_unsaved_nrows(self):
        pass
    
    def _iter(self):
        'Return an iterator for traversiong the data in table.'
        pass
    
    def append(self):
        "Add a new row of data to the end of the dataset.\n\n    Once you have filled the proper fields for the current\n    row, calling this method actually appends the new data to the\n    *output buffer* (which will eventually be\n    dumped to disk).  If you have not set the value of a field, the\n    default value of the column will be used.\n\n    .. warning::\n\n        After completion of the loop in which :meth:`Row.append` has\n        been called, it is always convenient to make a call to\n        :meth:`Table.flush` in order to avoid losing the last rows that\n        may still remain in internal buffers.\n\n    Examples\n    --------\n\n    ::\n\n        row = table.row\n        for i in xrange(nrows):\n            row['col1'] = i-1\n            row['col2'] = 'a'\n            row['col3'] = -1.0\n            row.append()\n        table.flush()\n\n    "
        pass
    
    def fetch_all_fields(self):
        "Retrieve all the fields in the current row.\n\n    Contrarily to row[:] (see :ref:`RowSpecialMethods`), this returns row\n    data as a NumPy void scalar.  For instance::\n\n        [row.fetch_all_fields() for row in table.where('col1 < 3')]\n\n    will select all the rows that fulfill the given condition\n    as a list of NumPy records.\n\n    "
        pass
    
    @property
    def nrow(self):
        'The current row number.\n\n    This property is useful for knowing which row is being dealt with in the\n    middle of a loop or iterator.\n\n    '
        pass
    
    @property
    def table(self):
        pass
    
    def update(self):
        "Change the data of the current row in the dataset.\n\n    This method allows you to modify values in a table when you are in the\n    middle of a table iterator like :meth:`Table.iterrows` or\n    :meth:`Table.where`.\n\n    Once you have filled the proper fields for the current row, calling\n    this method actually changes data in the *output buffer* (which will\n    eventually be dumped to disk).  If you have not set the value of a\n    field, its original value will be used.\n\n    .. warning::\n\n        After completion of the loop in which :meth:`Row.update` has\n        been called, it is always convenient to make a call to\n        :meth:`Table.flush` in order to avoid losing changed rows that\n        may still remain in internal buffers.\n\n    Examples\n    --------\n\n    ::\n\n        for row in table.iterrows(step=10):\n            row['col1'] = row.nrow\n            row['col2'] = 'b'\n            row['col3'] = 0.0\n            row.update()\n        table.flush()\n\n    which modifies every tenth row in table.  Or::\n\n        for row in table.where('col1 > 3'):\n            row['col1'] = row.nrow\n            row['col2'] = 'b'\n            row['col3'] = 0.0\n            row.update()\n        table.flush()\n\n    which just updates the rows with values bigger than 3 in the first\n    column.\n\n    "
        pass
    

SizeType = _mod_numpy.int64
class Table(_mod_tables_hdf5extension.Leaf):
    __class__ = Table
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _append_records(self):
        pass
    
    def _close_append(self):
        pass
    
    def _convert_types(self):
        "Converts columns in 'recarr' between NumPy and HDF5 formats.\n\n    NumPy to HDF5 conversion is performed when 'sense' is 0.  Otherwise, HDF5\n    to NumPy conversion is performed.  The conversion is done in place,\n    i.e. 'recarr' is modified.\n\n    "
        pass
    
    def _create_table(self):
        pass
    
    def _get_info(self):
        'Get info from a table on disk.'
        pass
    
    def _open_append(self):
        pass
    
    def _read_elements(self):
        pass
    
    def _read_records(self):
        pass
    
    def _remove_rows(self):
        pass
    
    def _update_elements(self):
        pass
    
    def _update_records(self):
        pass
    

__builtins__ = {}
__doc__ = 'Here is where Table and Row extension types live.\n\nClasses (type extensions):\n\n    Table\n    Row\n\nFunctions:\n\nMisc variables:\n\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/tables/tableextension.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'tables.tableextension'
__package__ = 'tables'
__test__ = _mod_builtins.dict()
def atom_from_hdf5_type():
    'Get an atom from a type_id.\n\n  See `hdf5_to_np_ext_type` for an explanation of the `pure_numpy_types`\n  parameter.\n\n  '
    pass

def call_on_recarr(func, params, recarr, param2arg, **kwargs):
    'Call `func` with `params` over `recarr`.\n\n    The `param2arg` function, when specified, is used to get an argument\n    given a parameter name; otherwise, the parameter itself is used as\n    an argument.  When the argument is a `Column` object, the proper\n    column from `recarr` is used as its value.\n\n    '
    pass

def create_nested_type():
    'Create a nested type based on a description and return an HDF5 type.'
    pass

def get_nested_field():
    'Get the maybe nested field named `fieldname` from the `recarray`.\n\n  The `fieldname` may be a simple field name or a nested field name\n  with slah-separated components.\n\n  '
    pass

hdf5_class_to_string = _mod_builtins.dict()
def hdf5_to_np_ext_type():
    'Map the atomic HDF5 type to a string repr of NumPy extended codes.\n\n  If `pure_numpy_types` is true, detected HDF5 types that does not match pure\n  NumPy types will raise a ``TypeError`` exception.  If not, HDF5 types like\n  TIME, VLEN or ENUM are passed through.\n\n  If `atom` is true, the resulting repr is meant for atoms.  If not, the\n  result is meant for attributes.\n\n  Returns the string repr of type and its shape.  The exception is for\n  compounds types, that returns a NumPy dtype and shape instead.\n\n  '
    pass

npext_prefixes_to_ptkinds = _mod_builtins.dict()
platform_byteorder = 0
pt_special_kinds = _mod_builtins.list()
pttype_to_hdf5 = _mod_builtins.dict()
def time():
    'time() -> floating point number\n\nReturn the current time in seconds since the Epoch.\nFractions of a second may be present if the system clock provides them.'
    return 1.0

