import builtins as _mod_builtins
import datetime as _mod_datetime
import dateutil.tz.tz as _mod_dateutil_tz_tz
import pandas._libs.tslibs.np_datetime as _mod_pandas__libs_tslibs_np_datetime
import pytz as _mod_pytz
import pytz.tzinfo as _mod_pytz_tzinfo

class dtype(_mod_builtins.object):
    'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = dtype
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, obj, align=False, copy=False):
        'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return dtype()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return dtype()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def alignment(self):
        'The required alignment (bytes) of this data-type according to the compiler.\n\n    More information is available in the C-API section of the manual.'
        pass
    
    @property
    def base(self):
        pass
    
    @property
    def byteorder(self):
        "A character indicating the byte-order of this data-type object.\n\n    One of:\n\n    ===  ==============\n    '='  native\n    '<'  little-endian\n    '>'  big-endian\n    '|'  not applicable\n    ===  ==============\n\n    All built-in data-type objects have byteorder either '=' or '|'.\n\n    Examples\n    --------\n\n    >>> dt = np.dtype('i2')\n    >>> dt.byteorder\n    '='\n    >>> # endian is not relevant for 8 bit numbers\n    >>> np.dtype('i1').byteorder\n    '|'\n    >>> # or ASCII strings\n    >>> np.dtype('S2').byteorder\n    '|'\n    >>> # Even if specific code is given, and it is native\n    >>> # '=' is the byteorder\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> dt = np.dtype(native_code + 'i2')\n    >>> dt.byteorder\n    '='\n    >>> # Swapped code shows up as itself\n    >>> dt = np.dtype(swapped_code + 'i2')\n    >>> dt.byteorder == swapped_code\n    True"
        pass
    
    @property
    def char(self):
        'A unique character code for each of the 21 different built-in types.'
        pass
    
    @property
    def descr(self):
        "`__array_interface__` description of the data-type.\n\n    The format is that required by the 'descr' key in the\n    `__array_interface__` attribute.\n\n    Warning: This attribute exists specifically for `__array_interface__`,\n    and is not a datatype description compatible with `np.dtype`."
        pass
    
    @property
    def fields(self):
        "Dictionary of named fields defined for this data type, or ``None``.\n\n    The dictionary is indexed by keys that are the names of the fields.\n    Each entry in the dictionary is a tuple fully describing the field::\n\n      (dtype, offset[, title])\n\n    Offset is limited to C int, which is signed and usually 32 bits.\n    If present, the optional title can be any object (if it is a string\n    or unicode then it will also be a key in the fields dictionary,\n    otherwise it's meta-data). Notice also that the first two elements\n    of the tuple can be passed directly as arguments to the ``ndarray.getfield``\n    and ``ndarray.setfield`` methods.\n\n    See Also\n    --------\n    ndarray.getfield, ndarray.setfield\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> print(dt.fields)\n    {'grades': (dtype(('float64',(2,))), 16), 'name': (dtype('|S16'), 0)}"
        pass
    
    @property
    def flags(self):
        'Bit-flags describing how this data type is to be interpreted.\n\n    Bit-masks are in `numpy.core.multiarray` as the constants\n    `ITEM_HASOBJECT`, `LIST_PICKLE`, `ITEM_IS_POINTER`, `NEEDS_INIT`,\n    `NEEDS_PYAPI`, `USE_GETITEM`, `USE_SETITEM`. A full explanation\n    of these flags is in C-API documentation; they are largely useful\n    for user-defined data-types.'
        pass
    
    @property
    def hasobject(self):
        "Boolean indicating whether this dtype contains any reference-counted\n    objects in any fields or sub-dtypes.\n\n    Recall that what is actually in the ndarray memory representing\n    the Python object is the memory address of that object (a pointer).\n    Special handling may be required, and this attribute is useful for\n    distinguishing data types that may contain arbitrary Python objects\n    and data-types that won't."
        pass
    
    @property
    def isalignedstruct(self):
        'Boolean indicating whether the dtype is a struct which maintains\n    field alignment. This flag is sticky, so when combining multiple\n    structs together, it is preserved and produces new dtypes which\n    are also aligned.'
        pass
    
    @property
    def isbuiltin(self):
        "Integer indicating how this dtype relates to the built-in dtypes.\n\n    Read-only.\n\n    =  ========================================================================\n    0  if this is a structured array type, with fields\n    1  if this is a dtype compiled into numpy (such as ints, floats etc)\n    2  if the dtype is for a user-defined numpy type\n       A user-defined type uses the numpy C-API machinery to extend\n       numpy to handle a new array type. See\n       :ref:`user.user-defined-data-types` in the NumPy manual.\n    =  ========================================================================\n\n    Examples\n    --------\n    >>> dt = np.dtype('i2')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype('f8')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype([('field1', 'f8')])\n    >>> dt.isbuiltin\n    0"
        pass
    
    @property
    def isnative(self):
        'Boolean indicating whether the byte order of this dtype is native\n    to the platform.'
        pass
    
    @property
    def itemsize(self):
        'The element size of this data-type object.\n\n    For 18 of the 21 types this number is fixed by the data-type.\n    For the flexible data-types, this number can be anything.'
        pass
    
    @property
    def kind(self):
        "A character code (one of 'biufcmMOSUV') identifying the general kind of data.\n\n    =  ======================\n    b  boolean\n    i  signed integer\n    u  unsigned integer\n    f  floating-point\n    c  complex floating-point\n    m  timedelta\n    M  datetime\n    O  object\n    S  (byte-)string\n    U  Unicode\n    V  void\n    =  ======================"
        pass
    
    @property
    def metadata(self):
        pass
    
    @property
    def name(self):
        'A bit-width name for this data-type.\n\n    Un-sized flexible data-type objects do not have this attribute.'
        pass
    
    @property
    def names(self):
        "Ordered list of field names, or ``None`` if there are no fields.\n\n    The names are ordered according to increasing byte offset. This can be\n    used, for example, to walk through all of the named fields in offset order.\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> dt.names\n    ('name', 'grades')"
        pass
    
    @property
    def ndim(self):
        'Number of dimensions of the sub-array if this data type describes a\n    sub-array, and ``0`` otherwise.\n\n    .. versionadded:: 1.13.0'
        pass
    
    def newbyteorder(self, new_order='S'):
        "newbyteorder(new_order='S')\n\n    Return a new dtype with a different byte order.\n\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Parameters\n    ----------\n    new_order : string, optional\n        Byte order to force; a value from the byte order specifications\n        below.  The default value ('S') results in swapping the current\n        byte order.  `new_order` codes can be any of:\n\n        * 'S' - swap dtype from current to opposite endian\n        * {'<', 'L'} - little endian\n        * {'>', 'B'} - big endian\n        * {'=', 'N'} - native order\n        * {'|', 'I'} - ignore (no change to byte order)\n\n        The code does a case-insensitive check on the first letter of\n        `new_order` for these alternatives.  For example, any of '>'\n        or 'B' or 'b' or 'brian' are valid to specify big-endian.\n\n    Returns\n    -------\n    new_dtype : dtype\n        New dtype object with the given change to the byte order.\n\n    Notes\n    -----\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Examples\n    --------\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> native_dt = np.dtype(native_code+'i2')\n    >>> swapped_dt = np.dtype(swapped_code+'i2')\n    >>> native_dt.newbyteorder('S') == swapped_dt\n    True\n    >>> native_dt.newbyteorder() == swapped_dt\n    True\n    >>> native_dt == swapped_dt.newbyteorder('S')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('=')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('N')\n    True\n    >>> native_dt == native_dt.newbyteorder('|')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('<')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('L')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('>')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('B')\n    True"
        pass
    
    @property
    def num(self):
        'A unique number for each of the 21 different built-in types.\n\n    These are roughly ordered from least-to-most precision.'
        pass
    
    @property
    def shape(self):
        'Shape tuple of the sub-array if this data type describes a sub-array,\n    and ``()`` otherwise.'
        pass
    
    @property
    def str(self):
        'The array-protocol typestring of this data-type object.'
        pass
    
    @property
    def subdtype(self):
        'Tuple ``(item_dtype, shape)`` if this `dtype` describes a sub-array, and\n    None otherwise.\n\n    The *shape* is the fixed shape of the sub-array described by this\n    data type, and *item_dtype* the data type of the array.\n\n    If a field whose dtype object has this attribute is retrieved,\n    then the extra dimensions implied by *shape* are tacked on to\n    the end of the retrieved array.'
        pass
    
    @property
    def type(self):
        'The type object used to instantiate a scalar of this data-type.'
        pass
    

class dtype(_mod_builtins.object):
    'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = dtype
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, obj, align=False, copy=False):
        'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return dtype()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return dtype()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def alignment(self):
        'The required alignment (bytes) of this data-type according to the compiler.\n\n    More information is available in the C-API section of the manual.'
        pass
    
    @property
    def base(self):
        pass
    
    @property
    def byteorder(self):
        "A character indicating the byte-order of this data-type object.\n\n    One of:\n\n    ===  ==============\n    '='  native\n    '<'  little-endian\n    '>'  big-endian\n    '|'  not applicable\n    ===  ==============\n\n    All built-in data-type objects have byteorder either '=' or '|'.\n\n    Examples\n    --------\n\n    >>> dt = np.dtype('i2')\n    >>> dt.byteorder\n    '='\n    >>> # endian is not relevant for 8 bit numbers\n    >>> np.dtype('i1').byteorder\n    '|'\n    >>> # or ASCII strings\n    >>> np.dtype('S2').byteorder\n    '|'\n    >>> # Even if specific code is given, and it is native\n    >>> # '=' is the byteorder\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> dt = np.dtype(native_code + 'i2')\n    >>> dt.byteorder\n    '='\n    >>> # Swapped code shows up as itself\n    >>> dt = np.dtype(swapped_code + 'i2')\n    >>> dt.byteorder == swapped_code\n    True"
        pass
    
    @property
    def char(self):
        'A unique character code for each of the 21 different built-in types.'
        pass
    
    @property
    def descr(self):
        "`__array_interface__` description of the data-type.\n\n    The format is that required by the 'descr' key in the\n    `__array_interface__` attribute.\n\n    Warning: This attribute exists specifically for `__array_interface__`,\n    and is not a datatype description compatible with `np.dtype`."
        pass
    
    @property
    def fields(self):
        "Dictionary of named fields defined for this data type, or ``None``.\n\n    The dictionary is indexed by keys that are the names of the fields.\n    Each entry in the dictionary is a tuple fully describing the field::\n\n      (dtype, offset[, title])\n\n    Offset is limited to C int, which is signed and usually 32 bits.\n    If present, the optional title can be any object (if it is a string\n    or unicode then it will also be a key in the fields dictionary,\n    otherwise it's meta-data). Notice also that the first two elements\n    of the tuple can be passed directly as arguments to the ``ndarray.getfield``\n    and ``ndarray.setfield`` methods.\n\n    See Also\n    --------\n    ndarray.getfield, ndarray.setfield\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> print(dt.fields)\n    {'grades': (dtype(('float64',(2,))), 16), 'name': (dtype('|S16'), 0)}"
        pass
    
    @property
    def flags(self):
        'Bit-flags describing how this data type is to be interpreted.\n\n    Bit-masks are in `numpy.core.multiarray` as the constants\n    `ITEM_HASOBJECT`, `LIST_PICKLE`, `ITEM_IS_POINTER`, `NEEDS_INIT`,\n    `NEEDS_PYAPI`, `USE_GETITEM`, `USE_SETITEM`. A full explanation\n    of these flags is in C-API documentation; they are largely useful\n    for user-defined data-types.'
        pass
    
    @property
    def hasobject(self):
        "Boolean indicating whether this dtype contains any reference-counted\n    objects in any fields or sub-dtypes.\n\n    Recall that what is actually in the ndarray memory representing\n    the Python object is the memory address of that object (a pointer).\n    Special handling may be required, and this attribute is useful for\n    distinguishing data types that may contain arbitrary Python objects\n    and data-types that won't."
        pass
    
    @property
    def isalignedstruct(self):
        'Boolean indicating whether the dtype is a struct which maintains\n    field alignment. This flag is sticky, so when combining multiple\n    structs together, it is preserved and produces new dtypes which\n    are also aligned.'
        pass
    
    @property
    def isbuiltin(self):
        "Integer indicating how this dtype relates to the built-in dtypes.\n\n    Read-only.\n\n    =  ========================================================================\n    0  if this is a structured array type, with fields\n    1  if this is a dtype compiled into numpy (such as ints, floats etc)\n    2  if the dtype is for a user-defined numpy type\n       A user-defined type uses the numpy C-API machinery to extend\n       numpy to handle a new array type. See\n       :ref:`user.user-defined-data-types` in the NumPy manual.\n    =  ========================================================================\n\n    Examples\n    --------\n    >>> dt = np.dtype('i2')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype('f8')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype([('field1', 'f8')])\n    >>> dt.isbuiltin\n    0"
        pass
    
    @property
    def isnative(self):
        'Boolean indicating whether the byte order of this dtype is native\n    to the platform.'
        pass
    
    @property
    def itemsize(self):
        'The element size of this data-type object.\n\n    For 18 of the 21 types this number is fixed by the data-type.\n    For the flexible data-types, this number can be anything.'
        pass
    
    @property
    def kind(self):
        "A character code (one of 'biufcmMOSUV') identifying the general kind of data.\n\n    =  ======================\n    b  boolean\n    i  signed integer\n    u  unsigned integer\n    f  floating-point\n    c  complex floating-point\n    m  timedelta\n    M  datetime\n    O  object\n    S  (byte-)string\n    U  Unicode\n    V  void\n    =  ======================"
        pass
    
    @property
    def metadata(self):
        pass
    
    @property
    def name(self):
        'A bit-width name for this data-type.\n\n    Un-sized flexible data-type objects do not have this attribute.'
        pass
    
    @property
    def names(self):
        "Ordered list of field names, or ``None`` if there are no fields.\n\n    The names are ordered according to increasing byte offset. This can be\n    used, for example, to walk through all of the named fields in offset order.\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> dt.names\n    ('name', 'grades')"
        pass
    
    @property
    def ndim(self):
        'Number of dimensions of the sub-array if this data type describes a\n    sub-array, and ``0`` otherwise.\n\n    .. versionadded:: 1.13.0'
        pass
    
    def newbyteorder(self, new_order='S'):
        "newbyteorder(new_order='S')\n\n    Return a new dtype with a different byte order.\n\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Parameters\n    ----------\n    new_order : string, optional\n        Byte order to force; a value from the byte order specifications\n        below.  The default value ('S') results in swapping the current\n        byte order.  `new_order` codes can be any of:\n\n        * 'S' - swap dtype from current to opposite endian\n        * {'<', 'L'} - little endian\n        * {'>', 'B'} - big endian\n        * {'=', 'N'} - native order\n        * {'|', 'I'} - ignore (no change to byte order)\n\n        The code does a case-insensitive check on the first letter of\n        `new_order` for these alternatives.  For example, any of '>'\n        or 'B' or 'b' or 'brian' are valid to specify big-endian.\n\n    Returns\n    -------\n    new_dtype : dtype\n        New dtype object with the given change to the byte order.\n\n    Notes\n    -----\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Examples\n    --------\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> native_dt = np.dtype(native_code+'i2')\n    >>> swapped_dt = np.dtype(swapped_code+'i2')\n    >>> native_dt.newbyteorder('S') == swapped_dt\n    True\n    >>> native_dt.newbyteorder() == swapped_dt\n    True\n    >>> native_dt == swapped_dt.newbyteorder('S')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('=')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('N')\n    True\n    >>> native_dt == native_dt.newbyteorder('|')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('<')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('L')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('>')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('B')\n    True"
        pass
    
    @property
    def num(self):
        'A unique number for each of the 21 different built-in types.\n\n    These are roughly ordered from least-to-most precision.'
        pass
    
    @property
    def shape(self):
        'Shape tuple of the sub-array if this data type describes a sub-array,\n    and ``()`` otherwise.'
        pass
    
    @property
    def str(self):
        'The array-protocol typestring of this data-type object.'
        pass
    
    @property
    def subdtype(self):
        'Tuple ``(item_dtype, shape)`` if this `dtype` describes a sub-array, and\n    None otherwise.\n\n    The *shape* is the fixed shape of the sub-array described by this\n    data type, and *item_dtype* the data type of the array.\n\n    If a field whose dtype object has this attribute is retrieved,\n    then the extra dimensions implied by *shape* are tacked on to\n    the end of the retrieved array.'
        pass
    
    @property
    def type(self):
        'The type object used to instantiate a scalar of this data-type.'
        pass
    

DAY_SECONDS = 86400
HOUR_SECONDS = 3600
NS_DTYPE = dtype()
OutOfBoundsDatetime = _mod_pandas__libs_tslibs_np_datetime.OutOfBoundsDatetime
TD_DTYPE = dtype()
UTC = _mod_pytz.UTC()
class _TSObject(_mod_builtins.object):
    __class__ = _TSObject
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
    def value(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/tslibs/conversion.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.tslibs.conversion'
__package__ = 'pandas._libs.tslibs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
datetime_time = _mod_datetime.time
def datetime_to_datetime64():
    '\n    Convert ndarray of datetime-like objects to int64 array representing\n    nanosecond timestamps.\n\n    Parameters\n    ----------\n    values : ndarray[object]\n\n    Returns\n    -------\n    result : ndarray[int64_t]\n    inferred_tz : tzinfo or None\n    '
    pass

def ensure_datetime64ns():
    "\n    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'\n\n    Parameters\n    ----------\n    arr : ndarray\n    copy : boolean, default True\n\n    Returns\n    -------\n    result : ndarray with dtype datetime64[ns]\n\n    "
    pass

def ensure_timedelta64ns():
    "\n    Ensure a np.timedelta64 array has dtype specifically 'timedelta64[ns]'\n\n    Parameters\n    ----------\n    arr : ndarray\n    copy : boolean, default True\n\n    Returns\n    -------\n    result : ndarray with dtype timedelta64[ns]\n\n    "
    pass

def is_date_array_normalized():
    '\n    Check if all of the given (nanosecond) timestamps are normalized to\n    midnight, i.e. hour == minute == second == 0.  If the optional timezone\n    `tz` is not None, then this is midnight for this timezone.\n\n    Parameters\n    ----------\n    stamps : int64 ndarray\n    tz : tzinfo or None\n\n    Returns\n    -------\n    is_normalized : bool True if all stamps are normalized\n    '
    pass

def localize_pydatetime():
    '\n    Take a datetime/Timestamp in UTC and localizes to timezone tz.\n\n    Parameters\n    ----------\n    dt : datetime or Timestamp\n    tz : tzinfo, "UTC", or None\n\n    Returns\n    -------\n    localized : datetime or Timestamp\n    '
    pass

nat_strings = _mod_builtins.set()
def normalize_date():
    '\n    Normalize datetime.datetime value to midnight. Returns datetime.date as a\n    datetime.datetime at midnight\n\n    Parameters\n    ----------\n    dt : date, datetime, or Timestamp\n\n    Returns\n    -------\n    normalized : datetime.datetime or Timestamp\n\n    Raises\n    ------\n    TypeError : if input is not datetime.date, datetime.datetime, or Timestamp\n    '
    pass

def normalize_i8_timestamps():
    '\n    Normalize each of the (nanosecond) timezone aware timestamps in the given\n    array by rounding down to the beginning of the day (i.e. midnight).\n    This is midnight for timezone, `tz`.\n\n    Parameters\n    ----------\n    stamps : int64 ndarray\n    tz : tzinfo or None\n\n    Returns\n    -------\n    result : int64 ndarray of converted of normalized nanosecond timestamps\n    '
    pass

def parse_datetime_string():
    'parse datetime string, only returns datetime.\n    Also cares special handling matching time patterns.\n\n    Returns\n    -------\n    datetime\n    '
    pass

def pydt_to_i8():
    '\n    Convert to int64 representation compatible with numpy datetime64; converts\n    to UTC\n\n    Parameters\n    ----------\n    pydt : object\n\n    Returns\n    -------\n    i8value : np.int64\n    '
    pass

def tz_convert():
    '\n    Convert the values (in i8) from timezone1 to timezone2\n\n    Parameters\n    ----------\n    vals : int64 ndarray\n    tz1 : string / timezone object\n    tz2 : string / timezone object\n\n    Returns\n    -------\n    int64 ndarray of converted\n    '
    pass

def tz_convert_single():
    '\n    Convert the val (in i8) from timezone1 to timezone2\n\n    This is a single timezone version of tz_convert\n\n    Parameters\n    ----------\n    val : int64\n    tz1 : string / timezone object\n    tz2 : string / timezone object\n\n    Returns\n    -------\n    converted: int64\n    '
    pass

def tz_localize_to_utc():
    '\n    Localize tzinfo-naive i8 to given time zone (using pytz). If\n    there are ambiguities in the values, raise AmbiguousTimeError.\n\n    Parameters\n    ----------\n    vals : ndarray[int64_t]\n    tz : tzinfo or None\n    ambiguous : str, bool, or arraylike\n        When clocks moved backward due to DST, ambiguous times may arise.\n        For example in Central European Time (UTC+01), when going from 03:00\n        DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC\n        and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter\n        dictates how ambiguous times should be handled.\n\n        - \'infer\' will attempt to infer fall dst-transition hours based on\n          order\n        - bool-ndarray where True signifies a DST time, False signifies a\n          non-DST time (note that this flag is only applicable for ambiguous\n          times, but the array must have the same length as vals)\n        - bool if True, treat all vals as DST. If False, treat them as non-DST\n        - \'NaT\' will return NaT where there are ambiguous times\n\n    nonexistent : {None, "NaT", "shift_forward", "shift_backward", "raise",\n                   timedelta-like}\n        How to handle non-existent times when converting wall times to UTC\n\n        .. versionadded:: 0.24.0\n\n    Returns\n    -------\n    localized : ndarray[int64_t]\n    '
    pass

tzutc = _mod_dateutil_tz_tz.tzutc
