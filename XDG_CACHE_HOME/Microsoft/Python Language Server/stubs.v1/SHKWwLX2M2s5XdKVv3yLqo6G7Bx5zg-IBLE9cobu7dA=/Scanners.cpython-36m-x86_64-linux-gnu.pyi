import builtins as _mod_builtins

class Scanner(_mod_builtins.object):
    "\n    A Scanner is used to read tokens from a stream of characters\n    using the token set specified by a Plex.Lexicon.\n\n    Constructor:\n\n      Scanner(lexicon, stream, name = '')\n\n        See the docstring of the __init__ method for details.\n\n    Methods:\n\n      See the docstrings of the individual methods for more\n      information.\n\n      read() --> (value, text)\n        Reads the next lexical token from the stream.\n\n      position() --> (name, line, col)\n        Returns the position of the last token read using the\n        read() method.\n\n      begin(state_name)\n        Causes scanner to change state.\n\n      produce(value [, text])\n        Causes return of a token value to the caller of the\n        Scanner.\n\n    "
    __class__ = Scanner
    def __init__(self):
        "\n        Scanner(lexicon, stream, name = '')\n\n          |lexicon| is a Plex.Lexicon instance specifying the lexical tokens\n          to be recognised.\n\n          |stream| can be a file object or anything which implements a\n          compatible read() method.\n\n          |name| is optional, and may be the name of the file being\n          scanned or any other identifying string.\n        "
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
    def buf_start_pos(self):
        pass
    
    @property
    def buffer(self):
        pass
    
    @property
    def cur_char(self):
        pass
    
    @property
    def cur_line(self):
        pass
    
    @property
    def cur_line_start(self):
        pass
    
    @property
    def cur_pos(self):
        pass
    
    def eof(self):
        '\n        Override this method if you want something to be done at\n        end of file.\n        '
        pass
    
    def get_position(self):
        'Python accessible wrapper around position(), only for error reporting.\n        '
        pass
    
    @property
    def initial_state(self):
        pass
    
    @property
    def input_state(self):
        pass
    
    @property
    def level(self):
        pass
    
    @property
    def lexicon(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def next_pos(self):
        pass
    
    @property
    def queue(self):
        pass
    
    def read(self):
        "\n        Read the next lexical token from the stream and return a\n        tuple (value, text), where |value| is the value associated with\n        the token as specified by the Lexicon, and |text| is the actual\n        string read from the stream. Returns (None, '') on end of file.\n        "
        pass
    
    @property
    def start_col(self):
        pass
    
    @property
    def start_line(self):
        pass
    
    @property
    def start_pos(self):
        pass
    
    @property
    def state_name(self):
        pass
    
    @property
    def stream(self):
        pass
    
    @property
    def text(self):
        pass
    
    @property
    def trace(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/Cython/Plex/Scanners.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Plex.Scanners'
__package__ = 'Cython.Plex'
__test__ = _mod_builtins.dict()
