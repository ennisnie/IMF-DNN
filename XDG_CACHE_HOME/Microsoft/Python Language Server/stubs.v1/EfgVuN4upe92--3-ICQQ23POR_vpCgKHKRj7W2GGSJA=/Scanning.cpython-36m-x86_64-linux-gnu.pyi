import Cython.Plex.Errors as _mod_Cython_Plex_Errors
import Cython.Plex.Scanners as _mod_Cython_Plex_Scanners
import builtins as _mod_builtins

class CompileTimeScope(_mod_builtins.object):
    __class__ = CompileTimeScope
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def entries(self):
        pass
    
    def lookup(self, name):
        pass
    
    @property
    def outer(self):
        pass
    
    def update(self, other):
        pass
    

class FileSourceDescriptor(SourceDescriptor):
    '\n    Represents a code source. A code source is a more generic abstraction\n    for a "filename" (as sometimes the code doesn\'t come from a file).\n    Instances of code sources are passed to Scanner.__init__ as the\n    optional name argument and will be passed back when asking for\n    the position()-tuple.\n    '
    __class__ = FileSourceDescriptor
    __dict__ = {}
    def __eq__(self, other):
        return False
    
    def __gt__(self, other):
        return False
    
    def __hash__(self):
        return 0
    
    def __init__(self, filename, path_description):
        '\n    Represents a code source. A code source is a more generic abstraction\n    for a "filename" (as sometimes the code doesn\'t come from a file).\n    Instances of code sources are passed to Scanner.__init__ as the\n    optional name argument and will be passed back when asking for\n    the position()-tuple.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, other):
        return False
    
    def __lt__(self, other):
        return False
    
    def __repr__(self):
        return ''
    
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_description(self):
        pass
    
    def get_error_description(self):
        pass
    
    def get_escaped_description(self):
        pass
    
    def get_filenametable_entry(self):
        pass
    
    def get_lines(self, encoding, error_handling):
        pass
    
    def is_cython_file(self):
        pass
    
    def is_python_file(self):
        pass
    
    def set_file_type_from_name(self, filename):
        pass
    

class Method(_mod_builtins.object):
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = Method
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __name__ = 'Method'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class PyrexScanner(_mod_Cython_Plex_Scanners.Scanner):
    __class__ = PyrexScanner
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def begin_string_action(self, text):
        pass
    
    @property
    def bracket_nesting_level(self):
        pass
    
    def close_bracket_action(self, text):
        pass
    
    def commentline(self, text):
        pass
    
    @property
    def compile_time_env(self):
        pass
    
    @property
    def compile_time_eval(self):
        pass
    
    @property
    def compile_time_expr(self):
        pass
    
    @property
    def context(self):
        pass
    
    def end_string_action(self, text):
        pass
    
    def eof(self):
        '\n        Override this method if you want something to be done at\n        end of file.\n        '
        pass
    
    def eof_action(self, text):
        pass
    
    def error(self, message, pos, fatal):
        pass
    
    def get_position(self):
        'Python accessible wrapper around position(), only for error reporting.\n        '
        pass
    
    @property
    def in_python_file(self):
        pass
    
    @property
    def included_files(self):
        pass
    
    def indentation_action(self, text):
        pass
    
    @property
    def indentation_char(self):
        pass
    
    @property
    def indentation_stack(self):
        pass
    
    def newline_action(self, text):
        pass
    
    def open_bracket_action(self, text):
        pass
    
    @property
    def parse_comments(self):
        pass
    
    def put_back(self, sy, systring):
        pass
    
    def read(self):
        "\n        Read the next lexical token from the stream and return a\n        tuple (value, text), where |value| is the value associated with\n        the token as specified by the Lexicon, and |text| is the actual\n        string read from the stream. Returns (None, '') on end of file.\n        "
        pass
    
    @property
    def source_encoding(self):
        pass
    
    string_states = _mod_builtins.dict()
    def strip_underscores(self, text, symbol):
        pass
    
    @property
    def sy(self):
        pass
    
    @property
    def systring(self):
        pass
    
    def unclosed_string_action(self, text):
        pass
    
    def unread(self, token, value):
        pass
    

class SourceDescriptor(_mod_builtins.object):
    '\n    A SourceDescriptor should be considered immutable.\n    '
    __class__ = SourceDescriptor
    __dict__ = {}
    def __gt__(self, other):
        return False
    
    def __init__(self, *args, **kwargs):
        '\n    A SourceDescriptor should be considered immutable.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, other):
        return False
    
    def __lt__(self, other):
        return False
    
    __module__ = 'Cython.Compiler.Scanning'
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    _cmp_name = ''
    _escaped_description = None
    _file_type = 'pyx'
    def get_escaped_description(self):
        pass
    
    def is_cython_file(self):
        pass
    
    def is_python_file(self):
        pass
    
    def set_file_type_from_name(self, filename):
        pass
    

class StringSourceDescriptor(SourceDescriptor):
    '\n    Instances of this class can be used instead of a filenames if the\n    code originates from a string object.\n    '
    __class__ = StringSourceDescriptor
    __dict__ = {}
    def __eq__(self, other):
        return False
    
    def __gt__(self, other):
        return False
    
    def __hash__(self):
        return 0
    
    def __init__(self, name, code):
        '\n    Instances of this class can be used instead of a filenames if the\n    code originates from a string object.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, other):
        return False
    
    def __lt__(self, other):
        return False
    
    def __repr__(self):
        return ''
    
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    filename = None
    def get_description(self):
        pass
    
    def get_error_description(self):
        pass
    
    def get_escaped_description(self):
        pass
    
    def get_filenametable_entry(self):
        pass
    
    def get_lines(self, encoding, error_handling):
        pass
    
    def is_cython_file(self):
        pass
    
    def is_python_file(self):
        pass
    
    def set_file_type_from_name(self, filename):
        pass
    

UnrecognizedInput = _mod_Cython_Plex_Errors.UnrecognizedInput
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/Cython/Compiler/Scanning.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Compiler.Scanning'
__package__ = 'Cython.Compiler'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
debug_scanner = 0
py_reserved_words = _mod_builtins.list()
pyx_reserved_words = _mod_builtins.list()
scanner_debug_flags = 0
scanner_dump_file = None
trace_scanner = 0
