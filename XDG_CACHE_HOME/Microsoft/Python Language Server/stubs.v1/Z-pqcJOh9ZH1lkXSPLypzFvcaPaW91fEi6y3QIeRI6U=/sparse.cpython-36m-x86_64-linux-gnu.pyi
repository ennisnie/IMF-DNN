import builtins as _mod_builtins

class BlockIndex(SparseIndex):
    '\n    Object for holding block-based sparse indexing information\n\n    Parameters\n    ----------\n    '
    __class__ = BlockIndex
    def __init__(self, *args, **kwargs):
        '\n    Object for holding block-based sparse indexing information\n\n    Parameters\n    ----------\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def blengths(self):
        pass
    
    @property
    def blocs(self):
        pass
    
    def check_integrity(self):
        '\n        Check:\n        - Locations are in ascending order\n        - No overlapping blocks\n        - Blocks to not start after end of index, nor extend beyond end\n        '
        pass
    
    def equals(self):
        pass
    
    def intersect(self):
        '\n        Intersect two BlockIndex objects\n\n        Parameters\n        ----------\n\n        Returns\n        -------\n        intersection : BlockIndex\n        '
        pass
    
    @property
    def length(self):
        pass
    
    def lookup(self):
        '\n        Return the internal location if value exists on given index.\n        Return -1 otherwise.\n        '
        pass
    
    def lookup_array(self):
        '\n        Vectorized lookup, returns ndarray[int32_t]\n        '
        pass
    
    def make_union(self):
        '\n        Combine together two BlockIndex objects, accepting indices if contained\n        in one or the other\n\n        Parameters\n        ----------\n        other : SparseIndex\n\n        Notes\n        -----\n        union is a protected keyword in Cython, hence make_union\n\n        Returns\n        -------\n        union : BlockIndex\n        '
        pass
    
    @property
    def nblocks(self):
        pass
    
    @property
    def nbytes(self):
        pass
    
    @property
    def ngaps(self):
        pass
    
    @property
    def npoints(self):
        pass
    
    def put(self):
        pass
    
    def reindex(self):
        pass
    
    def take(self):
        pass
    
    def to_block_index(self):
        pass
    
    def to_int_index(self):
        pass
    

class BlockMerge(_mod_builtins.object):
    '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
    __class__ = BlockMerge
    def __init__(self, *args, **kwargs):
        '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
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
    

class BlockUnion(BlockMerge):
    '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
    __class__ = BlockUnion
    def __init__(self, *args, **kwargs):
        '\n    Object-oriented approach makes sharing state between recursive functions a\n    lot easier and reduces code duplication\n    '
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
    

class IntIndex(SparseIndex):
    '\n    Object for holding exact integer sparse indexing information\n\n    Parameters\n    ----------\n    length : integer\n    indices : array-like\n        Contains integers corresponding to the indices.\n    '
    __class__ = IntIndex
    def __init__(self, *args, **kwargs):
        '\n    Object for holding exact integer sparse indexing information\n\n    Parameters\n    ----------\n    length : integer\n    indices : array-like\n        Contains integers corresponding to the indices.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def check_integrity(self):
        '\n        Checks the following:\n\n        - Indices are strictly ascending\n        - Number of indices is at most self.length\n        - Indices are at least 0 and at most the total length less one\n\n        A ValueError is raised if any of these conditions is violated.\n        '
        pass
    
    def equals(self):
        pass
    
    @property
    def indices(self):
        pass
    
    def intersect(self):
        pass
    
    @property
    def length(self):
        pass
    
    def lookup(self):
        '\n        Return the internal location if value exists on given index.\n        Return -1 otherwise.\n        '
        pass
    
    def lookup_array(self):
        '\n        Vectorized lookup, returns ndarray[int32_t]\n        '
        pass
    
    def make_union(self):
        pass
    
    @property
    def nbytes(self):
        pass
    
    @property
    def ngaps(self):
        pass
    
    @property
    def npoints(self):
        pass
    
    def put(self):
        pass
    
    def reindex(self):
        pass
    
    def take(self):
        pass
    
    def to_block_index(self):
        pass
    
    def to_int_index(self):
        pass
    

class SparseIndex(_mod_builtins.object):
    '\n    Abstract superclass for sparse index types.\n    '
    __class__ = SparseIndex
    def __init__(self, *args, **kwargs):
        '\n    Abstract superclass for sparse index types.\n    '
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
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/sparse.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.sparse'
__package__ = 'pandas._libs'
def __pyx_unpickle_BlockMerge():
    pass

def __pyx_unpickle_BlockUnion():
    pass

def __pyx_unpickle_SparseIndex():
    pass

__test__ = _mod_builtins.dict()
def get_blocks():
    pass

def make_mask_object_ndarray():
    pass

def sparse_add_float64():
    pass

def sparse_add_int64():
    pass

def sparse_and_int64():
    pass

def sparse_and_uint8():
    pass

def sparse_div_float64():
    pass

def sparse_div_int64():
    pass

def sparse_eq_float64():
    pass

def sparse_eq_int64():
    pass

def sparse_fill_add_float64():
    pass

def sparse_fill_add_int64():
    pass

def sparse_fill_and_int64():
    pass

def sparse_fill_and_uint8():
    pass

def sparse_fill_div_float64():
    pass

def sparse_fill_div_int64():
    pass

def sparse_fill_eq_float64():
    pass

def sparse_fill_eq_int64():
    pass

def sparse_fill_floordiv_float64():
    pass

def sparse_fill_floordiv_int64():
    pass

def sparse_fill_ge_float64():
    pass

def sparse_fill_ge_int64():
    pass

def sparse_fill_gt_float64():
    pass

def sparse_fill_gt_int64():
    pass

def sparse_fill_le_float64():
    pass

def sparse_fill_le_int64():
    pass

def sparse_fill_lt_float64():
    pass

def sparse_fill_lt_int64():
    pass

def sparse_fill_mod_float64():
    pass

def sparse_fill_mod_int64():
    pass

def sparse_fill_mul_float64():
    pass

def sparse_fill_mul_int64():
    pass

def sparse_fill_ne_float64():
    pass

def sparse_fill_ne_int64():
    pass

def sparse_fill_or_int64():
    pass

def sparse_fill_or_uint8():
    pass

def sparse_fill_pow_float64():
    pass

def sparse_fill_pow_int64():
    pass

def sparse_fill_sub_float64():
    pass

def sparse_fill_sub_int64():
    pass

def sparse_fill_truediv_float64():
    pass

def sparse_fill_truediv_int64():
    pass

def sparse_floordiv_float64():
    pass

def sparse_floordiv_int64():
    pass

def sparse_ge_float64():
    pass

def sparse_ge_int64():
    pass

def sparse_gt_float64():
    pass

def sparse_gt_int64():
    pass

def sparse_le_float64():
    pass

def sparse_le_int64():
    pass

def sparse_lt_float64():
    pass

def sparse_lt_int64():
    pass

def sparse_mod_float64():
    pass

def sparse_mod_int64():
    pass

def sparse_mul_float64():
    pass

def sparse_mul_int64():
    pass

def sparse_ne_float64():
    pass

def sparse_ne_int64():
    pass

def sparse_or_int64():
    pass

def sparse_or_uint8():
    pass

def sparse_pow_float64():
    pass

def sparse_pow_int64():
    pass

def sparse_sub_float64():
    pass

def sparse_sub_int64():
    pass

def sparse_truediv_float64():
    pass

def sparse_truediv_int64():
    pass

