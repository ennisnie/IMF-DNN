class Element(object):
    __class__ = Element
    def __copy__(self):
        pass
    
    def __deepcopy__(self, memo):
        pass
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __getstate__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    def __sizeof__(self):
        return 0
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self, subelement):
        pass
    
    @property
    def attrib(self):
        "A dictionary containing the element's attributes"
        pass
    
    def clear(self):
        pass
    
    def extend(self, elements):
        pass
    
    def find(self, path, namespaces):
        pass
    
    def findall(self, path, namespaces):
        pass
    
    def findtext(self, path, default, namespaces):
        pass
    
    def get(self, key, default):
        pass
    
    def getchildren(self):
        pass
    
    def getiterator(self):
        'iter($self, /, tag=None)\n--\n\n'
        pass
    
    def insert(self, index, subelement):
        pass
    
    def items(self):
        pass
    
    def iter(self, tag):
        pass
    
    def iterfind(self, path, namespaces):
        pass
    
    def itertext(self):
        pass
    
    def keys(self):
        pass
    
    def makeelement(self, tag, attrib):
        pass
    
    def remove(self, subelement):
        pass
    
    def set(self, key, value):
        pass
    
    @property
    def tag(self):
        'A string identifying what kind of data this element represents'
        pass
    
    @property
    def tail(self):
        'A string of text directly after the end tag, or None'
        pass
    
    @property
    def text(self):
        'A string of text directly after the start tag, or None'
        pass
    

class ParseError(SyntaxError):
    __class__ = ParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'xml.etree.ElementTree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def SubElement():
    pass

class TreeBuilder(object):
    __class__ = TreeBuilder
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
    
    def close(self):
        pass
    
    def data(self, data):
        pass
    
    def end(self, tag):
        pass
    
    def start(self, tag, attrs):
        pass
    

class XMLParser(object):
    __class__ = XMLParser
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
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
    
    def _parse_whole(self, file):
        pass
    
    def _setevents(self, events_queue, events_to_report):
        pass
    
    def close(self):
        pass
    
    def doctype(self, name, pubid, system):
        pass
    
    def feed(self, data):
        pass
    

__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/_elementtree.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_elementtree'
__package__ = ''
