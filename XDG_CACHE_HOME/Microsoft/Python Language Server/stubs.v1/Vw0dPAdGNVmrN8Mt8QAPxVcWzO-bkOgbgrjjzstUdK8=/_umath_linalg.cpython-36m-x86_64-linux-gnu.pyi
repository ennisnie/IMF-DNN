__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/numpy/linalg/_umath_linalg.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'numpy.linalg._umath_linalg'
__package__ = 'numpy.linalg'
__version__ = b'0.1.5'
def cholesky_lo(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'cholesky_lo(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\ncholesky decomposition of hermitian positive-definite matrices. \nBroadcast to all outer dimensions. \n    "(m,m)->(m,m)" \n'
    pass

def det(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'det(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\ndet of the last two dimensions and broadcast on the rest. \n    "(m,m)->()" \n'
    pass

def eig(x, out1=None, out2=None, out=(None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'eig(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neig on the last two dimension and broadcast to the rest. \nResults in a vector with the  eigenvalues and a matrix with the eigenvectors. \n    "(m,m)->(m),(m,m)" \n'
    pass

def eigh_lo(x, out1=None, out2=None, out=(None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'eigh_lo(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigh on the last two dimension and broadcast to the rest, using lower triangle \nResults in a vector of eigenvalues and a matrix with theeigenvectors. \n    "(m,m)->(m),(m,m)" \n'
    pass

def eigh_up(x, out1=None, out2=None, out=(None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'eigh_up(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigh on the last two dimension and broadcast to the rest, using upper triangle. \nResults in a vector of eigenvalues and a matrix with the eigenvectors. \n    "(m,m)->(m),(m,m)" \n'
    pass

def eigvals(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "eigvals(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\neigvals on the last two dimension and broadcast to the rest. \nResults in a vector of eigenvalues. \n"
    pass

def eigvalsh_lo(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'eigvalsh_lo(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigh on the last two dimension and broadcast to the rest, using lower triangle. \nResults in a vector of eigenvalues and a matrix with theeigenvectors. \n    "(m,m)->(m)" \n'
    pass

def eigvalsh_up(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'eigvalsh_up(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\neigvalsh on the last two dimension and broadcast to the rest, using upper triangle. \nResults in a vector of eigenvalues and a matrix with theeigenvectors.\n    "(m,m)->(m)" \n'
    pass

def inv(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'inv(x, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\ncompute the inverse of the last two dimensions and broadcast to the rest. \nResults in the inverse matrices. \n    "(m,m)->(m,m)" \n'
    pass

def lstsq_m(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, out=(None,None,None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "lstsq_m(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nleast squares on the last two dimensions and broadcast to the rest. \nFor m <= n. \n"
    pass

def lstsq_n(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, out=(None,None,None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "lstsq_n(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nleast squares on the last two dimensions and broadcast to the rest. \nFor m >= n, meaning that residuals are produced. \n"
    pass

def slogdet(x, out1=None, out2=None, out=(None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'slogdet(x[, out1, out2], / [, out=(None, None)], *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\nslogdet on the last two dimensions and broadcast on the rest. \nResults in two arrays, one with sign and the other with log of the determinants. \n    "(m,m)->(),()" \n'
    pass

def solve(x1, x2, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'solve(x1, x2, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\nsolve the system a x = b, on the last two dimensions, broadcast to the rest. \nResults in a matrices with the solutions. \n    "(m,m),(m,n)->(m,n)" \n'
    pass

def solve1(x1, x2, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    'solve1(x1, x2, /, out=None, *, casting=\'same_kind\', order=\'K\', dtype=None, subok=True[, signature, extobj])\n\nsolve the system a x = b, for b being a vector, broadcast in the outer dimensions. \nResults in vectors with the solutions. \n    "(m,m),(m)->(m)" \n'
    pass

def svd_m(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "svd_m(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when n>=m. "
    pass

def svd_m_f(x, out1=None, out2=None, out3=None, out=(None,None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "svd_m_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m<=n"
    pass

def svd_m_s(x, out1=None, out2=None, out3=None, out=(None,None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "svd_m_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m<=n"
    pass

def svd_n(x, out=None, *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "svd_n(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when n<=m"
    pass

def svd_n_f(x, out1=None, out2=None, out3=None, out=(None,None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "svd_n_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m>=n"
    pass

def svd_n_s(x, out1=None, out2=None, out3=None, out=(None,None,None), *, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "svd_n_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\nsvd when m>=n"
    pass

