import builtins as _mod_builtins

class PickleError(_mod_builtins.Exception):
    __class__ = PickleError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_pickle'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Pickler(_mod_builtins.object):
    'This takes a binary file for writing a pickle data stream.\n\nThe optional *protocol* argument tells the pickler to use the given\nprotocol; supported protocols are 0, 1, 2, 3 and 4.  The default\nprotocol is 3; a backward-incompatible protocol designed for Python 3.\n\nSpecifying a negative protocol version selects the highest protocol\nversion supported.  The higher the protocol used, the more recent the\nversion of Python needed to read the pickle produced.\n\nThe *file* argument must have a write() method that accepts a single\nbytes argument. It can thus be a file object opened for binary\nwriting, an io.BytesIO instance, or any other custom object that meets\nthis interface.\n\nIf *fix_imports* is True and protocol is less than 3, pickle will try\nto map the new Python 3 names to the old module names used in Python\n2, so that the pickle data stream is readable with Python 2.'
    __class__ = Pickler
    def __init__(self, *args, **kwargs):
        'This takes a binary file for writing a pickle data stream.\n\nThe optional *protocol* argument tells the pickler to use the given\nprotocol; supported protocols are 0, 1, 2, 3 and 4.  The default\nprotocol is 3; a backward-incompatible protocol designed for Python 3.\n\nSpecifying a negative protocol version selects the highest protocol\nversion supported.  The higher the protocol used, the more recent the\nversion of Python needed to read the pickle produced.\n\nThe *file* argument must have a write() method that accepts a single\nbytes argument. It can thus be a file object opened for binary\nwriting, an io.BytesIO instance, or any other custom object that meets\nthis interface.\n\nIf *fix_imports* is True and protocol is less than 3, pickle will try\nto map the new Python 3 names to the old module names used in Python\n2, so that the pickle data stream is readable with Python 2.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __sizeof__(self):
        'Returns size in memory, in bytes.'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def bin(self):
        pass
    
    def clear_memo(self):
        'Clears the pickler\'s "memo".\n\nThe memo is the data structure that remembers which objects the\npickler has already seen, so that shared or recursive objects are\npickled by reference and not by value.  This method is useful when\nre-using picklers.'
        pass
    
    @property
    def dispatch_table(self):
        pass
    
    def dump(self, obj):
        'Write a pickled representation of the given object to the open file.'
        pass
    
    @property
    def fast(self):
        pass
    
    @property
    def memo(self):
        pass
    
    @property
    def persistent_id(self):
        pass
    

class PicklingError(PickleError):
    __class__ = PicklingError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_pickle'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Unpickler(_mod_builtins.object):
    "This takes a binary file for reading a pickle data stream.\n\nThe protocol version of the pickle is detected automatically, so no\nprotocol argument is needed.  Bytes past the pickled object's\nrepresentation are ignored.\n\nThe argument *file* must have two methods, a read() method that takes\nan integer argument, and a readline() method that requires no\narguments.  Both methods should return bytes.  Thus *file* can be a\nbinary file object opened for reading, an io.BytesIO object, or any\nother custom object that meets this interface.\n\nOptional keyword arguments are *fix_imports*, *encoding* and *errors*,\nwhich are used to control compatibility support for pickle stream\ngenerated by Python 2.  If *fix_imports* is True, pickle will try to\nmap the old Python 2 names to the new names used in Python 3.  The\n*encoding* and *errors* tell pickle how to decode 8-bit string\ninstances pickled by Python 2; these default to 'ASCII' and 'strict',\nrespectively.  The *encoding* can be 'bytes' to read these 8-bit\nstring instances as bytes objects."
    __class__ = Unpickler
    def __init__(self, *args, **kwargs):
        "This takes a binary file for reading a pickle data stream.\n\nThe protocol version of the pickle is detected automatically, so no\nprotocol argument is needed.  Bytes past the pickled object's\nrepresentation are ignored.\n\nThe argument *file* must have two methods, a read() method that takes\nan integer argument, and a readline() method that requires no\narguments.  Both methods should return bytes.  Thus *file* can be a\nbinary file object opened for reading, an io.BytesIO object, or any\nother custom object that meets this interface.\n\nOptional keyword arguments are *fix_imports*, *encoding* and *errors*,\nwhich are used to control compatibility support for pickle stream\ngenerated by Python 2.  If *fix_imports* is True, pickle will try to\nmap the old Python 2 names to the new names used in Python 3.  The\n*encoding* and *errors* tell pickle how to decode 8-bit string\ninstances pickled by Python 2; these default to 'ASCII' and 'strict',\nrespectively.  The *encoding* can be 'bytes' to read these 8-bit\nstring instances as bytes objects."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __sizeof__(self):
        'Returns size in memory, in bytes.'
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def find_class(self, module_name, global_name):
        'Return an object from a specified module.\n\nIf necessary, the module will be imported. Subclasses may override\nthis method (e.g. to restrict unpickling of arbitrary classes and\nfunctions).\n\nThis method is called whenever a class or a function object is\nneeded.  Both arguments passed are str objects.'
        pass
    
    def load(self):
        'Load a pickle.\n\nRead a pickled object representation from the open file object given\nin the constructor, and return the reconstituted object hierarchy\nspecified therein.'
        pass
    
    @property
    def memo(self):
        pass
    
    @property
    def persistent_load(self):
        pass
    

class UnpicklingError(PickleError):
    __class__ = UnpicklingError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_pickle'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__doc__ = 'Optimized C implementation for the Python pickle module.'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/_pickle.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_pickle'
__package__ = ''
def dump(obj, file, protocol):
    'Write a pickled representation of obj to the open file object file.\n\nThis is equivalent to ``Pickler(file, protocol).dump(obj)``, but may\nbe more efficient.\n\nThe optional *protocol* argument tells the pickler to use the given\nprotocol supported protocols are 0, 1, 2, 3 and 4.  The default\nprotocol is 3; a backward-incompatible protocol designed for Python 3.\n\nSpecifying a negative protocol version selects the highest protocol\nversion supported.  The higher the protocol used, the more recent the\nversion of Python needed to read the pickle produced.\n\nThe *file* argument must have a write() method that accepts a single\nbytes argument.  It can thus be a file object opened for binary\nwriting, an io.BytesIO instance, or any other custom object that meets\nthis interface.\n\nIf *fix_imports* is True and protocol is less than 3, pickle will try\nto map the new Python 3 names to the old module names used in Python\n2, so that the pickle data stream is readable with Python 2.'
    pass

def dumps(obj, protocol):
    'Return the pickled representation of the object as a bytes object.\n\nThe optional *protocol* argument tells the pickler to use the given\nprotocol; supported protocols are 0, 1, 2, 3 and 4.  The default\nprotocol is 3; a backward-incompatible protocol designed for Python 3.\n\nSpecifying a negative protocol version selects the highest protocol\nversion supported.  The higher the protocol used, the more recent the\nversion of Python needed to read the pickle produced.\n\nIf *fix_imports* is True and *protocol* is less than 3, pickle will\ntry to map the new Python 3 names to the old module names used in\nPython 2, so that the pickle data stream is readable with Python 2.'
    pass

def load(file):
    "Read and return an object from the pickle data stored in a file.\n\nThis is equivalent to ``Unpickler(file).load()``, but may be more\nefficient.\n\nThe protocol version of the pickle is detected automatically, so no\nprotocol argument is needed.  Bytes past the pickled object's\nrepresentation are ignored.\n\nThe argument *file* must have two methods, a read() method that takes\nan integer argument, and a readline() method that requires no\narguments.  Both methods should return bytes.  Thus *file* can be a\nbinary file object opened for reading, an io.BytesIO object, or any\nother custom object that meets this interface.\n\nOptional keyword arguments are *fix_imports*, *encoding* and *errors*,\nwhich are used to control compatibility support for pickle stream\ngenerated by Python 2.  If *fix_imports* is True, pickle will try to\nmap the old Python 2 names to the new names used in Python 3.  The\n*encoding* and *errors* tell pickle how to decode 8-bit string\ninstances pickled by Python 2; these default to 'ASCII' and 'strict',\nrespectively.  The *encoding* can be 'bytes' to read these 8-bit\nstring instances as bytes objects."
    pass

def loads(data):
    "Read and return an object from the given pickle data.\n\nThe protocol version of the pickle is detected automatically, so no\nprotocol argument is needed.  Bytes past the pickled object's\nrepresentation are ignored.\n\nOptional keyword arguments are *fix_imports*, *encoding* and *errors*,\nwhich are used to control compatibility support for pickle stream\ngenerated by Python 2.  If *fix_imports* is True, pickle will try to\nmap the old Python 2 names to the new names used in Python 3.  The\n*encoding* and *errors* tell pickle how to decode 8-bit string\ninstances pickled by Python 2; these default to 'ASCII' and 'strict',\nrespectively.  The *encoding* can be 'bytes' to read these 8-bit\nstring instances as bytes objects."
    pass

