import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/optimize/_lsq/givens_elimination.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize._lsq.givens_elimination'
__package__ = 'scipy.optimize._lsq'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def givens_elimination():
    'Zero out a diagonal block of a matrix by series of Givens rotations.\n\n    The matrix has the structure::\n\n        [ S ]\n        [ D ]\n\n    Where S is an upper triangular matrix with shape (n, n) and D is a\n    diagonal matrix with shape (n, n) with elements from `diag`. This function\n    applies Givens rotations to it such that the resulting matrix has zeros\n    in place of D.\n\n    Array `S` will be modified in-place.\n\n    Array `v` of shape (n,) is the part of the full vector with shape (2*n,)::\n\n        [ v ]\n        [ 0 ]\n\n    to which Givens rotations are applied. This array is modified in place,\n    such that on exit it contains the first n components of the above\n    mentioned vector after rotations were applied.\n    '
    pass

