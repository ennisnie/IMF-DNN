import Cython.Compiler.Scanning as _mod_Cython_Compiler_Scanning
import _io as _mod__io
import builtins as _mod_builtins

class Ctx(_mod_builtins.object):
    def __call__(self, **kwds):
        pass
    
    __class__ = Ctx
    __dict__ = {}
    def __init__(self, **kwds):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Parsing'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    allow_struct_enum_decorator = False
    api = 0
    cdef_flag = 0
    level = 'other'
    namespace = None
    nogil = 0
    overridable = 0
    templates = None
    typedef_flag = 0
    visibility = 'private'

StringIO = _mod__io.StringIO
StringSourceDescriptor = _mod_Cython_Compiler_Scanning.StringSourceDescriptor
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/Cython/Compiler/Parsing.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Compiler.Parsing'
__package__ = 'Cython.Compiler'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
def make_slice_node(pos, start, stop, step):
    pass

def p_c_arg_list(s, ctx, in_pyfunc, cmethod_flag, nonempty_declarators, kw_only, annotated):
    pass

def p_c_base_type(s, self_flag, nonempty, templates):
    pass

def p_c_declarator(s, ctx, empty, is_type, cmethod_flag, assignable, nonempty, calling_convention_allowed):
    pass

def p_code(s, level, ctx):
    pass

def p_module(s, pxd, full_module_name, ctx):
    pass

def print_parse_tree(f, node, level, key):
    pass

