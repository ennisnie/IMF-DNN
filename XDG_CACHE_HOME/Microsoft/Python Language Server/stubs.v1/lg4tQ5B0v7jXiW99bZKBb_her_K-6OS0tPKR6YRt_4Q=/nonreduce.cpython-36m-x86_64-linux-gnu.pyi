__doc__ = 'Bottleneck nonreducing functions.'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/bottleneck/nonreduce.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'bottleneck.nonreduce'
__package__ = 'bottleneck'
def replace(a, old, new):
    'replace(a, old, new)\n\nReplace (inplace) given scalar values of an array with new values.\n\nThe equivalent numpy function:\n\n    a[a==old] = new\n\nOr in the case where old=np.nan:\n\n    a[np.isnan(old)] = new\n\nParameters\n----------\na : numpy.ndarray\n    The input array, which is also the output array since this functions\n    works inplace.\nold : scalar\n    All elements in `a` with this value will be replaced by `new`.\nnew : scalar\n    All elements in `a` with a value of `old` will be replaced by `new`.\n\nReturns\n-------\nReturns a view of the input array after performing the replacements,\nif any.\n\nExamples\n--------\nReplace zero with 3 (note that the input array is modified):\n\n>>> a = np.array([1, 2, 0])\n>>> bn.replace(a, 0, 3)\n>>> a\narray([1, 2, 3])\n\nReplace np.nan with 0:\n\n>>> a = np.array([1, 2, np.nan])\n>>> bn.replace(a, np.nan, 0)\n>>> a\narray([ 1.,  2.,  0.])\n\n'
    pass

