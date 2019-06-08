import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csr as _mod_scipy_sparse_csr

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
__builtins__ = {}
__doc__ = '\nRoutines for traversing graphs in compressed sparse format\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/sparse/csgraph/_traversal.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.csgraph._traversal'
__package__ = 'scipy.sparse.csgraph'
__test__ = _mod_builtins.dict()
def breadth_first_order():
    '\n    breadth_first_order(csgraph, i_start, directed=True, return_predecessors=True)\n\n    Return a breadth-first ordering starting with specified node.\n\n    Note that a breadth-first order is not unique, but the tree which it\n    generates is unique.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N compressed sparse graph.  The input csgraph will be\n        converted to csr format for the calculation.\n    i_start : int\n        The index of starting node.\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only\n        move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i].\n    return_predecessors : bool, optional\n        If True (default), then return the predecesor array (see below).\n\n    Returns\n    -------\n    node_array : ndarray, one dimension\n        The breadth-first list of nodes, starting with specified node.  The\n        length of node_array is the number of nodes reachable from the\n        specified node.\n    predecessors : ndarray, one dimension\n        Returned only if return_predecessors is True.\n        The length-N list of predecessors of each node in a breadth-first\n        tree.  If node i is in the tree, then its parent is given by\n        predecessors[i]. If node i is not in the tree (and for the parent\n        node) then predecessors[i] = -9999.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import breadth_first_order\n\n    >>> graph = [\n    ... [0, 1 , 2, 0],\n    ... [0, 0, 0, 1],\n    ... [2, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)    1\n      (0, 2)    2\n      (1, 3)    1\n      (2, 0)    2\n      (2, 3)    3\n\n    >>> breadth_first_order(graph,0)\n    (array([0, 1, 2, 3], dtype=int32), array([-9999,     0,     0,     1], dtype=int32))\n\n    '
    pass

def breadth_first_tree():
    '\n    breadth_first_tree(csgraph, i_start, directed=True)\n\n    Return the tree generated by a breadth-first search\n\n    Note that a breadth-first tree from a specified node is unique.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N matrix representing the compressed sparse graph.  The input\n        csgraph will be converted to csr format for the calculation.\n    i_start : int\n        The index of starting node.\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only\n        move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i].\n\n    Returns\n    -------\n    cstree : csr matrix\n        The N x N directed compressed-sparse representation of the breadth-\n        first tree drawn from csgraph, starting at the specified node.\n\n    Examples\n    --------\n    The following example shows the computation of a depth-first tree\n    over a simple four-component graph, starting at node 0::\n\n         input graph          breadth first tree from (0)\n\n             (0)                         (0)\n            /   \\                       /   \\\n           3     8                     3     8\n          /       \\                   /       \\\n        (3)---5---(1)               (3)       (1)\n          \\       /                           /\n           6     2                           2\n            \\   /                           /\n             (2)                         (2)\n\n    In compressed sparse representation, the solution looks like this:\n\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import breadth_first_tree\n    >>> X = csr_matrix([[0, 8, 0, 3],\n    ...                 [0, 0, 2, 5],\n    ...                 [0, 0, 0, 6],\n    ...                 [0, 0, 0, 0]])\n    >>> Tcsr = breadth_first_tree(X, 0, directed=False)\n    >>> Tcsr.toarray().astype(int)\n    array([[0, 8, 0, 3],\n           [0, 0, 2, 0],\n           [0, 0, 0, 0],\n           [0, 0, 0, 0]])\n\n    Note that the resulting graph is a Directed Acyclic Graph which spans\n    the graph.  A breadth-first tree from a given node is unique.\n    '
    pass

def connected_components():
    '\n    connected_components(csgraph, directed=True, connection=\'weak\',\n                         return_labels=True)\n\n    Analyze the connected components of a sparse graph\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N matrix representing the compressed sparse graph.  The input\n        csgraph will be converted to csr format for the calculation.\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only\n        move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i].\n    connection : str, optional\n        [\'weak\'|\'strong\'].  For directed graphs, the type of connection to\n        use.  Nodes i and j are strongly connected if a path exists both\n        from i to j and from j to i.  Nodes i and j are weakly connected if\n        only one of these paths exists.  If directed == False, this keyword\n        is not referenced.\n    return_labels : bool, optional\n        If True (default), then return the labels for each of the connected\n        components.\n\n    Returns\n    -------\n    n_components: int\n        The number of connected components.\n    labels: ndarray\n        The length-N array of labels of the connected components.\n\n    References\n    ----------\n    .. [1] D. J. Pearce, "An Improved Algorithm for Finding the Strongly\n           Connected Components of a Directed Graph", Technical Report, 2005\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import connected_components\n\n    >>> graph = [\n    ... [ 0, 1 , 1, 0 , 0 ],\n    ... [ 0, 0 , 1 , 0 ,0 ],\n    ... [ 0, 0, 0, 0, 0],\n    ... [0, 0 , 0, 0, 1],\n    ... [0, 0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t1\n      (1, 2)\t1\n      (3, 4)\t1\n\n    >>> n_components, labels = connected_components(csgraph=graph, directed=False, return_labels=True)\n    >>> n_components\n    2\n    >>> labels\n    array([0, 0, 0, 1, 1], dtype=int32)\n\n    '
    pass

csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def depth_first_order():
    '\n    depth_first_order(csgraph, i_start, directed=True, return_predecessors=True)\n\n    Return a depth-first ordering starting with specified node.\n\n    Note that a depth-first order is not unique.  Furthermore, for graphs\n    with cycles, the tree generated by a depth-first search is not\n    unique either.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N compressed sparse graph.  The input csgraph will be\n        converted to csr format for the calculation.\n    i_start : int\n        The index of starting node.\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only\n        move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i].\n    return_predecessors : bool, optional\n        If True (default), then return the predecesor array (see below).\n\n    Returns\n    -------\n    node_array : ndarray, one dimension\n        The depth-first list of nodes, starting with specified node.  The\n        length of node_array is the number of nodes reachable from the\n        specified node.\n    predecessors : ndarray, one dimension\n        Returned only if return_predecessors is True.\n        The length-N list of predecessors of each node in a depth-first\n        tree.  If node i is in the tree, then its parent is given by\n        predecessors[i]. If node i is not in the tree (and for the parent\n        node) then predecessors[i] = -9999.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import depth_first_order\n\n    >>> graph = [\n    ... [0, 1 , 2, 0],\n    ... [0, 0, 0, 1],\n    ... [2, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 3)\t1\n      (2, 0)\t2\n      (2, 3)\t3\n\n    >>> depth_first_order(graph,0)\n    (array([0, 1, 3, 2], dtype=int32), array([-9999,     0,     0,     1], dtype=int32))\n\n    '
    pass

def depth_first_tree():
    '\n    depth_first_tree(csgraph, i_start, directed=True)\n\n    Return a tree generated by a depth-first search.\n\n    Note that a tree generated by a depth-first search is not unique:\n    it depends on the order that the children of each node are searched.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N matrix representing the compressed sparse graph.  The input\n        csgraph will be converted to csr format for the calculation.\n    i_start : int\n        The index of starting node.\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only\n        move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i].\n\n    Returns\n    -------\n    cstree : csr matrix\n        The N x N directed compressed-sparse representation of the depth-\n        first tree drawn from csgraph, starting at the specified node.\n\n    Examples\n    --------\n    The following example shows the computation of a depth-first tree\n    over a simple four-component graph, starting at node 0::\n\n         input graph           depth first tree from (0)\n\n             (0)                         (0)\n            /   \\                           \\\n           3     8                           8\n          /       \\                           \\\n        (3)---5---(1)               (3)       (1)\n          \\       /                   \\       /\n           6     2                     6     2\n            \\   /                       \\   /\n             (2)                         (2)\n\n    In compressed sparse representation, the solution looks like this:\n\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import depth_first_tree\n    >>> X = csr_matrix([[0, 8, 0, 3],\n    ...                 [0, 0, 2, 5],\n    ...                 [0, 0, 0, 6],\n    ...                 [0, 0, 0, 0]])\n    >>> Tcsr = depth_first_tree(X, 0, directed=False)\n    >>> Tcsr.toarray().astype(int)\n    array([[0, 8, 0, 0],\n           [0, 0, 2, 0],\n           [0, 0, 0, 6],\n           [0, 0, 0, 0]])\n\n    Note that the resulting graph is a Directed Acyclic Graph which spans\n    the graph.  Unlike a breadth-first tree, a depth-first tree of a given\n    graph is not unique if the graph contains cycles.  If the above solution\n    had begun with the edge connecting nodes 0 and 3, the result would have\n    been different.\n    '
    pass

def isspmatrix(x):
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    pass

def isspmatrix_csc(x):
    'Is x of csc_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csc matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csc matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csc_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csc_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csr_matrix([[5]]))\n    False\n    '
    pass

def isspmatrix_csr(x):
    'Is x of csr_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csr matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csr matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix_csr\n    >>> isspmatrix_csr(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csr(csc_matrix([[5]]))\n    False\n    '
    pass

def reconstruct_path():
    '\n    reconstruct_path(csgraph, predecessors, directed=True)\n\n    Construct a tree from a graph and a predecessor list.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N matrix representing the directed or undirected graph\n        from which the predecessors are drawn.\n    predecessors : array_like, one dimension\n        The length-N array of indices of predecessors for the tree.  The\n        index of the parent of node i is given by predecessors[i].\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only move from\n        point i to point j along paths csgraph[i, j].\n        If False, then operate on an undirected graph: the algorithm can\n        progress from point i to j along csgraph[i, j] or csgraph[j, i].\n\n    Returns\n    -------\n    cstree : csr matrix\n        The N x N directed compressed-sparse representation of the tree drawn\n        from csgraph which is encoded by the predecessor list.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import reconstruct_path\n\n    >>> graph = [\n    ... [0, 1 , 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 3)\t1\n      (2, 3)\t3\n\n    >>> pred = np.array([-9999, 0, 0, 1], dtype=np.int32)\n\n    >>> cstree = reconstruct_path(csgraph=graph, predecessors=pred, directed=False)\n    >>> cstree.todense()\n    matrix([[ 0.,  1.,  2.,  0.],\n            [ 0.,  0.,  0.,  1.],\n            [ 0.,  0.,  0.,  0.],\n            [ 0.,  0.,  0.,  0.]])\n\n    '
    pass

def validate_graph(csgraph, directed, dtype, csr_output, dense_output, copy_if_dense, copy_if_sparse, null_value_in, null_value_out, infinity_null, nan_null):
    'Routine for validation and conversion of csgraph inputs'
    pass
