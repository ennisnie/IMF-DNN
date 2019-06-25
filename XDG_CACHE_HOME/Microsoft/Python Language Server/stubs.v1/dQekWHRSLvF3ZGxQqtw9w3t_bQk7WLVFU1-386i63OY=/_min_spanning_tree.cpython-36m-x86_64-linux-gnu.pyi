import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csr as _mod_scipy_sparse_csr

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/sparse/csgraph/_min_spanning_tree.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.csgraph._min_spanning_tree'
__package__ = 'scipy.sparse.csgraph'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def isspmatrix(x):
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    pass

def isspmatrix_csc(x):
    'Is x of csc_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csc matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csc matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csc_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csc_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csr_matrix([[5]]))\n    False\n    '
    pass

def minimum_spanning_tree():
    '\n    minimum_spanning_tree(csgraph, overwrite=False)\n\n    Return a minimum spanning tree of an undirected graph\n\n    A minimum spanning tree is a graph consisting of the subset of edges\n    which together connect all connected nodes, while minimizing the total\n    sum of weights on the edges.  This is computed using the Kruskal algorithm.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix, 2 dimensions\n        The N x N matrix representing an undirected graph over N nodes\n        (see notes below).\n    overwrite : bool, optional\n        if true, then parts of the input graph will be overwritten for\n        efficiency.\n\n    Returns\n    -------\n    span_tree : csr matrix\n        The N x N compressed-sparse representation of the undirected minimum\n        spanning tree over the input (see notes below).\n\n    Notes\n    -----\n    This routine uses undirected graphs as input and output.  That is, if\n    graph[i, j] and graph[j, i] are both zero, then nodes i and j do not\n    have an edge connecting them.  If either is nonzero, then the two are\n    connected by the minimum nonzero value of the two.\n\n    Examples\n    --------\n    The following example shows the computation of a minimum spanning tree\n    over a simple four-component graph::\n\n         input graph             minimum spanning tree\n\n             (0)                         (0)\n            /   \\                       /\n           3     8                     3\n          /       \\                   /\n        (3)---5---(1)               (3)---5---(1)\n          \\       /                           /\n           6     2                           2\n            \\   /                           /\n             (2)                         (2)\n\n    It is easy to see from inspection that the minimum spanning tree involves\n    removing the edges with weights 8 and 6.  In compressed sparse\n    representation, the solution looks like this:\n\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import minimum_spanning_tree\n    >>> X = csr_matrix([[0, 8, 0, 3],\n    ...                 [0, 0, 2, 5],\n    ...                 [0, 0, 0, 6],\n    ...                 [0, 0, 0, 0]])\n    >>> Tcsr = minimum_spanning_tree(X)\n    >>> Tcsr.toarray().astype(int)\n    array([[0, 0, 0, 3],\n           [0, 0, 2, 5],\n           [0, 0, 0, 0],\n           [0, 0, 0, 0]])\n    '
    pass

def validate_graph(csgraph, directed, dtype, csr_output, dense_output, copy_if_dense, copy_if_sparse, null_value_in, null_value_out, infinity_null, nan_null):
    'Routine for validation and conversion of csgraph inputs'
    pass

