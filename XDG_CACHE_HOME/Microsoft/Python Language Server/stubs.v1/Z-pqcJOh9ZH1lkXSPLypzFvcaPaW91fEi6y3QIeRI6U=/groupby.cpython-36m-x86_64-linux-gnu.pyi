import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/groupby.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.groupby'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
_int64_max = 9223372036854775807
def group_add_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_add_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_any_all():
    "Aggregated boolean values to show truthfulness of group elements\n\n    Parameters\n    ----------\n    out : array of values which this method will write its results to\n    labels : array containing unique label for each group, with its\n        ordering matching up to the corresponding record in `values`\n    values : array containing the truth value of each element\n    mask : array indicating whether a value is na or not\n    val_test : str {'any', 'all'}\n        String object dictating whether to use any or all truth testing\n    skipna : boolean\n        Flag to ignore nan values during truth testing\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object.\n    The returned values will either be 0 or 1 (False or True, respectively).\n    "
    pass

def group_cummax(out, values, labels, is_datetimelike):
    '\n    Only transforms on axis=0\n    '
    pass

def group_cummin(out, values, labels, is_datetimelike):
    '\n    Only transforms on axis=0\n    '
    pass

def group_cumprod_float64():
    '\n    Only transforms on axis=0\n    '
    pass

def group_cumsum():
    '\n    Only transforms on axis=0\n    '
    pass

def group_fillna_indexer():
    "Indexes how to fill values forwards or backwards within a group\n\n    Parameters\n    ----------\n    out : array of int64_t values which this method will write its results to\n        Missing values will be written to with a value of -1\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    mask : array of int64_t values where a 1 indicates a missing value\n    direction : {'ffill', 'bfill'}\n        Direction for fill to be applied (forwards or backwards, respectively)\n    limit : Consecutive values to fill before stopping, or -1 for no limit\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    pass

def group_last_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_last_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_last_int64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_last_object():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_max():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_mean_float32():
    pass

def group_mean_float64():
    pass

def group_median_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_min():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_nth_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_nth_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_nth_int64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_nth_object():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_ohlc_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_ohlc_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_prod_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_prod_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_rank_float32():
    "\n    Provides the rank of values within each group.\n\n    Parameters\n    ----------\n    out : array of float64_t values which this method will write its results to\n    values : array of float32_t values to be ranked\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    is_datetimelike : bool, default False\n        unused in this method but provided for call compatibility with other\n        Cython transformations\n    ties_method : {'average', 'min', 'max', 'first', 'dense'}, default\n        'average'\n        * average: average rank of group\n        * min: lowest rank in group\n        * max: highest rank in group\n        * first: ranks assigned in order they appear in the array\n        * dense: like 'min', but rank always increases by 1 between groups\n    ascending : boolean, default True\n        False for ranks by high (1) to low (N)\n        na_option : {'keep', 'top', 'bottom'}, default 'keep'\n    pct : boolean, default False\n        Compute percentage rank of data within each group\n    na_option : {'keep', 'top', 'bottom'}, default 'keep'\n        * keep: leave NA values where they are\n        * top: smallest rank if ascending\n        * bottom: smallest rank if descending\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    pass

def group_rank_float64():
    "\n    Provides the rank of values within each group.\n\n    Parameters\n    ----------\n    out : array of float64_t values which this method will write its results to\n    values : array of float64_t values to be ranked\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    is_datetimelike : bool, default False\n        unused in this method but provided for call compatibility with other\n        Cython transformations\n    ties_method : {'average', 'min', 'max', 'first', 'dense'}, default\n        'average'\n        * average: average rank of group\n        * min: lowest rank in group\n        * max: highest rank in group\n        * first: ranks assigned in order they appear in the array\n        * dense: like 'min', but rank always increases by 1 between groups\n    ascending : boolean, default True\n        False for ranks by high (1) to low (N)\n        na_option : {'keep', 'top', 'bottom'}, default 'keep'\n    pct : boolean, default False\n        Compute percentage rank of data within each group\n    na_option : {'keep', 'top', 'bottom'}, default 'keep'\n        * keep: leave NA values where they are\n        * top: smallest rank if ascending\n        * bottom: smallest rank if descending\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    pass

def group_rank_int64():
    "\n    Provides the rank of values within each group.\n\n    Parameters\n    ----------\n    out : array of float64_t values which this method will write its results to\n    values : array of int64_t values to be ranked\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    is_datetimelike : bool, default False\n        unused in this method but provided for call compatibility with other\n        Cython transformations\n    ties_method : {'average', 'min', 'max', 'first', 'dense'}, default\n        'average'\n        * average: average rank of group\n        * min: lowest rank in group\n        * max: highest rank in group\n        * first: ranks assigned in order they appear in the array\n        * dense: like 'min', but rank always increases by 1 between groups\n    ascending : boolean, default True\n        False for ranks by high (1) to low (N)\n        na_option : {'keep', 'top', 'bottom'}, default 'keep'\n    pct : boolean, default False\n        Compute percentage rank of data within each group\n    na_option : {'keep', 'top', 'bottom'}, default 'keep'\n        * keep: leave NA values where they are\n        * top: smallest rank if ascending\n        * bottom: smallest rank if descending\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    pass

def group_shift_indexer():
    pass

def group_var_float32():
    pass

def group_var_float64():
    pass

def groupsort_indexer():
    '\n    compute a 1-d indexer that is an ordering of the passed index,\n    ordered by the groups. This is a reverse of the label\n    factorization process.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        mappings from group -> position\n    ngroups: int64\n        number of groups\n\n    return a tuple of (1-d indexer ordered by groups, group counts)\n    '
    pass

def take_2d_axis1_float64_float64():
    pass

tiebreakers = _mod_builtins.dict()
