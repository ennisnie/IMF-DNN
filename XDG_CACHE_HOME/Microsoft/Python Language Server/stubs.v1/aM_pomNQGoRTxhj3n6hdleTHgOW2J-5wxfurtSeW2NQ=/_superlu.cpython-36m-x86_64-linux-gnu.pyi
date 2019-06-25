import builtins as _mod_builtins

SuperLU = _mod_builtins.SuperLU
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/sparse/linalg/dsolve/_superlu.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.linalg.dsolve._superlu'
__package__ = 'scipy.sparse.linalg.dsolve'
def gssv():
    'Direct inversion of sparse matrix.\n\nX = gssv(A,B) solves A*X = B for X.'
    pass

def gstrf():
    "gstrf(A, ...)\n\nperforms a factorization of the sparse matrix A=*(N,nnz,nzvals,rowind,colptr) and \nreturns a factored_lu object.\n\narguments\n---------\n\nMatrix to be factorized is represented as N,nnz,nzvals,rowind,colptr\n  as separate arguments.  This is compressed sparse column representation.\n\nN         number of rows and columns \nnnz       number of non-zero elements\nnzvals    non-zero values \nrowind    row-index for this column (same size as nzvals)\ncolptr    index into rowind for first non-zero value in this column\n          size is (N+1).  Last value should be nnz. \n\nadditional keyword arguments:\n-----------------------------\noptions             specifies additional options for SuperLU\n                    (same keys and values as in superlu_options_t C structure,\n                    and additionally 'Relax' and 'PanelSize')\n\nilu                 whether to perform an incomplete LU decomposition\n                    (default: false)\n"
    pass

