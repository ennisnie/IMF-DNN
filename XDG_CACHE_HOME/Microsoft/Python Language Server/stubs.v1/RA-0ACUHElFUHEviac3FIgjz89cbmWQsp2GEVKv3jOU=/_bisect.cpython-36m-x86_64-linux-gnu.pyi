__doc__ = 'Bisection algorithms.\n\nThis module provides support for maintaining a list in sorted order without\nhaving to sort the list after each insertion. For long lists of items with\nexpensive comparison operations, this can be an improvement over the more\ncommon approach.\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/_bisect.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_bisect'
__package__ = ''
def bisect():
    'Alias for bisect_right().\n'
    pass

def bisect_left(a, x, lo=None, hi=None):
    'bisect_left(a, x[, lo[, hi]]) -> index\n\nReturn the index where to insert item x in list a, assuming a is sorted.\n\nThe return value i is such that all e in a[:i] have e < x, and all e in\na[i:] have e >= x.  So if x already appears in the list, i points just\nbefore the leftmost x already there.\n\nOptional args lo (default 0) and hi (default len(a)) bound the\nslice of a to be searched.\n'
    pass

def bisect_right(a, x, lo=None, hi=None):
    'bisect_right(a, x[, lo[, hi]]) -> index\n\nReturn the index where to insert item x in list a, assuming a is sorted.\n\nThe return value i is such that all e in a[:i] have e <= x, and all e in\na[i:] have e > x.  So if x already appears in the list, i points just\nbeyond the rightmost x already there\n\nOptional args lo (default 0) and hi (default len(a)) bound the\nslice of a to be searched.\n'
    pass

def insort():
    'Alias for insort_right().\n'
    pass

def insort_left(a, x, lo=None, hi=None):
    'insort_left(a, x[, lo[, hi]])\n\nInsert item x in list a, and keep it sorted assuming a is sorted.\n\nIf x is already in a, insert it to the left of the leftmost x.\n\nOptional args lo (default 0) and hi (default len(a)) bound the\nslice of a to be searched.\n'
    pass

def insort_right(a, x, lo=None, hi=None):
    'insort_right(a, x[, lo[, hi]])\n\nInsert item x in list a, and keep it sorted assuming a is sorted.\n\nIf x is already in a, insert it to the right of the rightmost x.\n\nOptional args lo (default 0) and hi (default len(a)) bound the\nslice of a to be searched.\n'
    pass

