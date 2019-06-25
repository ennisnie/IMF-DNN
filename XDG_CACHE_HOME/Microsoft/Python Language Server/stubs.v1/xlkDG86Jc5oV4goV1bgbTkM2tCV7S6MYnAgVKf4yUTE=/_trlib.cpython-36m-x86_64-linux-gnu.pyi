import builtins as _mod_builtins
import scipy.optimize._trustregion as _mod_scipy_optimize__trustregion

BaseQuadraticSubproblem = _mod_scipy_optimize__trustregion.BaseQuadraticSubproblem
class TRLIBQuadraticSubproblem(_mod_scipy_optimize__trustregion.BaseQuadraticSubproblem):
    __class__ = TRLIBQuadraticSubproblem
    __dict__ = {}
    def __init__(self, x, fun, jac, hess, hessp, tol_rel_i, tol_rel_b, disp):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'scipy.optimize._trlib._trlib'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def solve(self, trust_radius):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/scipy/optimize/_trlib/_trlib.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.optimize._trlib._trlib'
__package__ = 'scipy.optimize._trlib'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _minimize_trust_region(fun, x0, args, jac, hess, hessp, subproblem, initial_trust_radius, max_trust_radius, eta, gtol, maxiter, disp, return_all, callback, inexact, **unknown_options):
    '\n    Minimization of scalar function of one or more variables using a\n    trust-region algorithm.\n\n    Options for the trust-region algorithm are:\n        initial_trust_radius : float\n            Initial trust radius.\n        max_trust_radius : float\n            Never propose steps that are longer than this value.\n        eta : float\n            Trust region related acceptance stringency for proposed steps.\n        gtol : float\n            Gradient norm must be less than `gtol`\n            before successful termination.\n        maxiter : int\n            Maximum number of iterations to perform.\n        disp : bool\n            If True, print convergence message.\n        inexact : bool\n            Accuracy to solve subproblems. If True requires less nonlinear\n            iterations, but more vector products. Only effective for method\n            trust-krylov.\n\n    This function is called by the `minimize` function.\n    It is not supposed to be called directly.\n    '
    pass

