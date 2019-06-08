import builtins as _mod_builtins

class BadRequiredStrength(_mod_builtins.Exception):
    __class__ = BadRequiredStrength
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kiwisolver'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Constraint(_mod_builtins.object):
    __class__ = Constraint
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __or__(self, value):
        'Return self|value.'
        return Constraint()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __ror__(self, value):
        'Return value|self.'
        return Constraint()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def expression(self):
        'Get the expression object for the constraint.'
        pass
    
    def op(self):
        'Get the relational operator for the constraint.'
        pass
    
    def strength(self):
        'Get the strength for the constraint.'
        pass
    

class DuplicateConstraint(_mod_builtins.Exception):
    __class__ = DuplicateConstraint
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kiwisolver'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class DuplicateEditVariable(_mod_builtins.Exception):
    __class__ = DuplicateEditVariable
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kiwisolver'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Expression(_mod_builtins.object):
    def __add__(self, value):
        'Return self+value.'
        return Expression()
    
    __class__ = Expression
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return Expression()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return Expression()
    
    def __radd__(self, value):
        'Return value+self.'
        return Expression()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return Expression()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Expression()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Expression()
    
    def __sub__(self, value):
        'Return self-value.'
        return Expression()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def constant(self):
        'Get the constant for the expression.'
        pass
    
    def terms(self):
        'Get the tuple of terms for the expression.'
        pass
    
    def value(self):
        'Get the value for the expression.'
        pass
    

class Solver(_mod_builtins.object):
    __class__ = Solver
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def addConstraint(self):
        'Add a constraint to the solver.'
        pass
    
    def addEditVariable(self):
        'Add an edit variable to the solver.'
        pass
    
    def dump(self):
        pass
    
    def hasConstraint(self):
        'Check whether the solver contains a constraint.'
        pass
    
    def hasEditVariable(self):
        'Check whether the solver contains an edit variable.'
        pass
    
    def removeConstraint(self):
        'Remove a constraint from the solver.'
        pass
    
    def removeEditVariable(self):
        'Remove an edit variable from the solver.'
        pass
    
    def reset(self):
        'Reset the solver to the initial empty starting condition.'
        pass
    
    def suggestValue(self):
        'Suggest a desired value for an edit variable.'
        pass
    
    def updateVariables(self):
        'Update the values of the solver variables.'
        pass
    

class Term(_mod_builtins.object):
    def __add__(self, value):
        'Return self+value.'
        return Term()
    
    __class__ = Term
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return Term()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return Term()
    
    def __radd__(self, value):
        'Return value+self.'
        return Term()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return Term()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Term()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Term()
    
    def __sub__(self, value):
        'Return self-value.'
        return Term()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def coefficient(self):
        'Get the coefficient for the term.'
        pass
    
    def value(self):
        'Get the value for the term.'
        pass
    
    def variable(self):
        'Get the variable for the term.'
        pass
    

class UnknownConstraint(_mod_builtins.Exception):
    __class__ = UnknownConstraint
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kiwisolver'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class UnknownEditVariable(_mod_builtins.Exception):
    __class__ = UnknownEditVariable
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kiwisolver'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class UnsatisfiableConstraint(_mod_builtins.Exception):
    __class__ = UnsatisfiableConstraint
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'kiwisolver'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Variable(_mod_builtins.object):
    def __add__(self, value):
        'Return self+value.'
        return Variable()
    
    __class__ = Variable
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return Variable()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return Variable()
    
    def __radd__(self, value):
        'Return value+self.'
        return Variable()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return Variable()
    
    def __rsub__(self, value):
        'Return value-self.'
        return Variable()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return Variable()
    
    def __sub__(self, value):
        'Return self-value.'
        return Variable()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    def context(self):
        'Get the context object associated with the variable.'
        pass
    
    def name(self):
        'Get the name of the variable.'
        pass
    
    def setContext(self):
        'Set the context object associated with the variable.'
        pass
    
    def setName(self):
        'Set the name of the variable.'
        pass
    
    def value(self):
        'Get the current value of the variable.'
        pass
    

__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/kiwisolver.cpython-36m-x86_64-linux-gnu.so'
__kiwi_version__ = '1.0.0'
__name__ = 'kiwisolver'
__package__ = ''
__version__ = '1.0.1'
class strength(_mod_builtins.object):
    __class__ = strength
    @staticmethod
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    @staticmethod
    def __dir__(self):
        '__dir__() -> list\ndefault dir() implementation'
        return ['']
    
    @staticmethod
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    @staticmethod
    def __format__(self, format_spec):
        'default object formatter'
        return ''
    
    @staticmethod
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    @staticmethod
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    @staticmethod
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    @staticmethod
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    @staticmethod
    def __init__(self, *args, **kwargs):
        pass
    
    @staticmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @staticmethod
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    @staticmethod
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    @staticmethod
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @staticmethod
    def __reduce__(self):
        'helper for pickle'
        return ''; return ()
    
    @staticmethod
    def __reduce_ex__(self, protocol):
        'helper for pickle'
        return ''; return ()
    
    @staticmethod
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @staticmethod
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @staticmethod
    def __sizeof__(self):
        '__sizeof__() -> int\nsize of object in memory, in bytes'
        return 0
    
    @staticmethod
    def __str__(self):
        'Return str(self).'
        return ''
    
    @staticmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @staticmethod
    def create():
        'Create a strength from constituent values and optional weight.'
        pass
    
    medium = 1000.0
    required = 1001001000.0
    strong = 1000000.0
    weak = 1.0

