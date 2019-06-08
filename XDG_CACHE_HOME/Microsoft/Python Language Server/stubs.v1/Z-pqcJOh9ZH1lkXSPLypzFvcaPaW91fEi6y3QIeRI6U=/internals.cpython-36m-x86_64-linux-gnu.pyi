import builtins as _mod_builtins

class BlockPlacement(_mod_builtins.object):
    __class__ = BlockPlacement
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return BlockPlacement()
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def add(self):
        pass
    
    def append(self):
        pass
    
    @property
    def as_array(self):
        pass
    
    @property
    def as_slice(self):
        pass
    
    def delete(self):
        pass
    
    @property
    def indexer(self):
        pass
    
    @property
    def is_slice_like(self):
        pass
    
    def isin(self):
        pass
    
    def sub(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/internals.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.internals'
__package__ = 'pandas._libs'
def __pyx_unpickle_BlockPlacement():
    pass

def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def ensure_int64():
    pass

def get_blkno_indexers():
    '\n    Enumerate contiguous runs of integers in ndarray.\n\n    Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``\n    pairs for each contiguous run found.\n\n    If `group` is True and there is more than one run for a certain blkno,\n    ``(blkno, array)`` with an array containing positions of all elements equal\n    to blkno.\n\n    Returns\n    -------\n    iter : iterator of (int, slice or array)\n\n    '
    pass

def get_blkno_placements():
    '\n\n    Parameters\n    ----------\n    blknos : array of int64\n    blk_count : int\n    group : bool\n\n    Returns\n    -------\n    iterator\n        yield (BlockPlacement, blkno)\n\n    '
    pass

def indexer_as_slice():
    pass

def slice_getitem():
    pass

def slice_len():
    '\n    Get length of a bounded slice.\n\n    The slice must not have any "open" bounds that would create dependency on\n    container size, i.e.:\n    - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``\n    - if ``s.step < 0``, ``s.start`` is not ``None``\n\n    Otherwise, the result is unreliable.\n\n    '
    pass

