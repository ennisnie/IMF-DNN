import functools as _mod_functools

__doc__ = 'Tools that operate on functions.'
__name__ = '_functools'
__package__ = ''
_lru_cache_wrapper = _mod_functools._lru_cache_wrapper
def cmp_to_key():
    'Convert a cmp= function into a key= function.'
    pass

partial = _mod_functools.partial
def reduce(function, sequence, initial=None):
    'reduce(function, sequence[, initial]) -> value\n\nApply a function of two arguments cumulatively to the items of a sequence,\nfrom left to right, so as to reduce the sequence to a single value.\nFor example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates\n((((1+2)+3)+4)+5).  If initial is present, it is placed before the items\nof the sequence in the calculation, and serves as a default when the\nsequence is empty.'
    pass

