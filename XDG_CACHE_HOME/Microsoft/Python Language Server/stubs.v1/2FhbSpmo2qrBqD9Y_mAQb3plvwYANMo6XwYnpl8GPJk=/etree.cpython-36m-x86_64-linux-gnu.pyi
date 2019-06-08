import builtins as _mod_builtins

class _MemDebug(_mod_builtins.object):
    'Debugging support for the memory allocation in libxml2.\n    '
    __class__ = _MemDebug
    def __init__(self, *args, **kwargs):
        'Debugging support for the memory allocation in libxml2.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def blocks_used(self):
        'blocks_used(self)\n\n        Returns the total number of memory blocks currently allocated by libxml2.\n        Note that libxml2 constrains this value to a C int, which limits\n        the accuracy on 64 bit systems.\n        '
        pass
    
    def bytes_used(self):
        'bytes_used(self)\n\n        Returns the total amount of memory (in bytes) currently used by libxml2.\n        Note that libxml2 constrains this value to a C int, which limits\n        the accuracy on 64 bit systems.\n        '
        pass
    
    def dict_size(self):
        'dict_size(self)\n\n        Returns the current size of the global name dictionary used by libxml2\n        for the current thread.  Each thread has its own dictionary.\n        '
        pass
    
    def dump(self, output_file, byte_count):
        'dump(self, output_file=None, byte_count=None)\n\n        Dumps the current memory blocks allocated by libxml2 to a file.\n\n        The optional parameter \'output_file\' specifies the file path.  It defaults\n        to the file ".memorylist" in the current directory.\n\n        The optional parameter \'byte_count\' limits the number of bytes in the dump.\n        Note that this parameter is ignored when lxml is compiled against a libxml2\n        version before 2.7.0.\n        '
        pass
    
    def show(self, output_file, block_count):
        'show(self, output_file=None, block_count=None)\n\n        Dumps the current memory blocks allocated by libxml2 to a file.\n        The output file format is suitable for line diffing.\n\n        The optional parameter \'output_file\' specifies the file path.  It defaults\n        to the file ".memorydump" in the current directory.\n\n        The optional parameter \'block_count\' limits the number of blocks\n        in the dump.\n        '
        pass
    

class AncestorsIterator(_ElementMatchIterator):
    'AncestorsIterator(self, node, tag=None)\n    Iterates over the ancestors of an element (from parent to parent).\n    '
    __class__ = AncestorsIterator
    def __init__(self, fromparenttoparent):
        'AncestorsIterator(self, node, tag=None)\n    Iterates over the ancestors of an element (from parent to parent).\n    '
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
    

class AttributeBasedElementClassLookup(FallbackElementClassLookup):
    "AttributeBasedElementClassLookup(self, attribute_name, class_mapping, fallback=None)\n    Checks an attribute of an Element and looks up the value in a\n    class dictionary.\n\n    Arguments:\n      - attribute name - '{ns}name' style string\n      - class mapping  - Python dict mapping attribute values to Element classes\n      - fallback       - optional fallback lookup mechanism\n\n    A None key in the class mapping will be checked if the attribute is\n    missing.\n    "
    __class__ = AttributeBasedElementClassLookup
    def __init__(self, attribute_name, class_mapping, fallback=None):
        "AttributeBasedElementClassLookup(self, attribute_name, class_mapping, fallback=None)\n    Checks an attribute of an Element and looks up the value in a\n    class dictionary.\n\n    Arguments:\n      - attribute name - '{ns}name' style string\n      - class mapping  - Python dict mapping attribute values to Element classes\n      - fallback       - optional fallback lookup mechanism\n\n    A None key in the class mapping will be checked if the attribute is\n    missing.\n    "
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
    

class C14NError(LxmlError):
    'Error during C14N serialisation.\n    '
    __class__ = C14NError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error during C14N serialisation.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class CDATA(_mod_builtins.object):
    'CDATA(data)\n\n    CDATA factory.  This factory creates an opaque data object that\n    can be used to set Element text.  The usual way to use it is::\n\n        >>> el = Element(\'content\')\n        >>> el.text = CDATA(\'a string\')\n\n        >>> print(el.text)\n        a string\n        >>> print(tostring(el, encoding="unicode"))\n        <content><![CDATA[a string]]></content>\n    '
    __class__ = CDATA
    def __init__(self, data):
        'CDATA(data)\n\n    CDATA factory.  This factory creates an opaque data object that\n    can be used to set Element text.  The usual way to use it is::\n\n        >>> el = Element(\'content\')\n        >>> el.text = CDATA(\'a string\')\n\n        >>> print(el.text)\n        a string\n        >>> print(tostring(el, encoding="unicode"))\n        <content><![CDATA[a string]]></content>\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def Comment(text):
    'Comment(text=None)\n\n    Comment element factory. This factory function creates a special element that will\n    be serialized as an XML comment.\n    '
    pass

class CommentBase(_Comment):
    'All custom Comment classes must inherit from this one.\n\n    To create an XML Comment instance, use the ``Comment()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Comments must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
    __class__ = CommentBase
    def __init__(self, *args, **kwargs):
        'All custom Comment classes must inherit from this one.\n\n    To create an XML Comment instance, use the ``Comment()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Comments must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
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
    

class CustomElementClassLookup(FallbackElementClassLookup):
    "CustomElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    You can inherit from this class and override the method::\n\n        lookup(self, type, doc, namespace, name)\n\n    to lookup the element class for a node. Arguments of the method:\n    * type:      one of 'element', 'comment', 'PI', 'entity'\n    * doc:       document that the node is in\n    * namespace: namespace URI of the node (or None for comments/PIs/entities)\n    * name:      name of the element/entity, None for comments, target for PIs\n\n    If you return None from this method, the fallback will be called.\n    "
    __class__ = CustomElementClassLookup
    def __init__(self, fallback=None):
        "CustomElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    You can inherit from this class and override the method::\n\n        lookup(self, type, doc, namespace, name)\n\n    to lookup the element class for a node. Arguments of the method:\n    * type:      one of 'element', 'comment', 'PI', 'entity'\n    * doc:       document that the node is in\n    * namespace: namespace URI of the node (or None for comments/PIs/entities)\n    * name:      name of the element/entity, None for comments, target for PIs\n\n    If you return None from this method, the fallback will be called.\n    "
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
    
    def lookup(self, type, doc, namespace, name):
        'lookup(self, type, doc, namespace, name)'
        pass
    

DEBUG = 1
class DTD(_Validator):
    'DTD(self, file=None, external_id=None)\n    A DTD validator.\n\n    Can load from filesystem directly given a filename or file-like object.\n    Alternatively, pass the keyword parameter ``external_id`` to load from a\n    catalog.\n    '
    def __call__(self, etree):
        '__call__(self, etree)\n\n        Validate doc using the DTD.\n\n        Returns true if the document is valid, false if not.\n        '
        pass
    
    __class__ = DTD
    def __init__(self, file=None, external_id=None):
        'DTD(self, file=None, external_id=None)\n    A DTD validator.\n\n    Can load from filesystem directly given a filename or file-like object.\n    Alternatively, pass the keyword parameter ``external_id`` to load from a\n    catalog.\n    '
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
    
    def elements(self):
        pass
    
    def entities(self):
        pass
    
    @property
    def external_id(self):
        pass
    
    def iterelements(self):
        pass
    
    def iterentities(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def system_url(self):
        pass
    

class DTDError(LxmlError):
    'Base class for DTD errors.\n    '
    __class__ = DTDError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class for DTD errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DTDParseError(DTDError):
    'Error while parsing a DTD.\n    '
    __class__ = DTDParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while parsing a DTD.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DTDValidateError(DTDError):
    'Error while validating an XML document with a DTD.\n    '
    __class__ = DTDValidateError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while validating an XML document with a DTD.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class DocInfo(_mod_builtins.object):
    'Document information provided by parser and DTD.'
    @property
    def URL(self):
        'The source URL of the document (or None if unknown).'
        pass
    
    __class__ = DocInfo
    def __init__(self, *args, **kwargs):
        'Document information provided by parser and DTD.'
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
    
    def clear(self):
        'Removes DOCTYPE and internal subset from the document.'
        pass
    
    @property
    def doctype(self):
        'Returns a DOCTYPE declaration string for the document.'
        pass
    
    @property
    def encoding(self):
        'Returns the encoding name as declared by the document.'
        pass
    
    @property
    def externalDTD(self):
        'Returns a DTD validator based on the external subset of the document.'
        pass
    
    @property
    def internalDTD(self):
        'Returns a DTD validator based on the internal subset of the document.'
        pass
    
    @property
    def public_id(self):
        'Public ID of the DOCTYPE.\n\n        Mutable.  May be set to a valid string or None.  If a DTD does not\n        exist, setting this variable (even to None) will create one.\n        '
        pass
    
    @property
    def root_name(self):
        'Returns the name of the root node as defined by the DOCTYPE.'
        pass
    
    @property
    def standalone(self):
        "Returns the standalone flag as declared by the document.  The possible\n        values are True (``standalone='yes'``), False\n        (``standalone='no'`` or flag not provided in the declaration),\n        and None (unknown or no declaration found).  Note that a\n        normal truth test on this value will always tell if the\n        ``standalone`` flag was set to ``'yes'`` or not.\n        "
        pass
    
    @property
    def system_url(self):
        'System ID of the DOCTYPE.\n\n        Mutable.  May be set to a valid string or None.  If a DTD does not\n        exist, setting this variable (even to None) will create one.\n        '
        pass
    
    @property
    def xml_version(self):
        'Returns the XML version as declared by the document.'
        pass
    

class DocumentInvalid(LxmlError):
    'Validation error.\n\n    Raised by all document validators when their ``assertValid(tree)``\n    method fails.\n    '
    __class__ = DocumentInvalid
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Validation error.\n\n    Raised by all document validators when their ``assertValid(tree)``\n    method fails.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ETCompatXMLParser(XMLParser):
    'ETCompatXMLParser(self, encoding=None, attribute_defaults=False,                  dtd_validation=False, load_dtd=False, no_network=True,                  ns_clean=False, recover=False, schema=None,                  huge_tree=False, remove_blank_text=False, resolve_entities=True,                  remove_comments=True, remove_pis=True, strip_cdata=True,                  target=None, compact=True)\n\n    An XML parser with an ElementTree compatible default setup.\n\n    See the XMLParser class for details.\n\n    This parser has ``remove_comments`` and ``remove_pis`` enabled by default\n    and thus ignores comments and processing instructions.\n    '
    __class__ = ETCompatXMLParser
    def __init__(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema=None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=True, remove_pis=True, strip_cdata=True, target=None, compact=True):
        'ETCompatXMLParser(self, encoding=None, attribute_defaults=False,                  dtd_validation=False, load_dtd=False, no_network=True,                  ns_clean=False, recover=False, schema=None,                  huge_tree=False, remove_blank_text=False, resolve_entities=True,                  remove_comments=True, remove_pis=True, strip_cdata=True,                  target=None, compact=True)\n\n    An XML parser with an ElementTree compatible default setup.\n\n    See the XMLParser class for details.\n\n    This parser has ``remove_comments`` and ``remove_pis`` enabled by default\n    and thus ignores comments and processing instructions.\n    '
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
    

class ETXPath(XPath):
    'ETXPath(self, path, extensions=None, regexp=True, smart_strings=True)\n    Special XPath class that supports the ElementTree {uri} notation for namespaces.\n\n    Note that this class does not accept the ``namespace`` keyword\n    argument. All namespaces must be passed as part of the path\n    string.  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    '
    __class__ = ETXPath
    def __init__(self, path, extensions=None, regexp=True, smart_strings=True):
        'ETXPath(self, path, extensions=None, regexp=True, smart_strings=True)\n    Special XPath class that supports the ElementTree {uri} notation for namespaces.\n\n    Note that this class does not accept the ``namespace`` keyword\n    argument. All namespaces must be passed as part of the path\n    string.  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    '
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
    

def Element(_tag, attrib, nsmap, **_extra):
    'Element(_tag, attrib=None, nsmap=None, **_extra)\n\n    Element factory.  This function returns an object implementing the\n    Element interface.\n\n    Also look at the `_Element.makeelement()` and\n    `_BaseParser.makeelement()` methods, which provide a faster way to\n    create an Element within a specific document or parser context.\n    '
    pass

class ElementBase(_Element):
    'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n\n    The public Element class.  All custom Element classes must inherit\n    from this one.  To create an Element, use the `Element()` factory.\n\n    BIG FAT WARNING: Subclasses *must not* override __init__ or\n    __new__ as it is absolutely undefined when these objects will be\n    created or destroyed.  All persistent state of Elements must be\n    stored in the underlying XML.  If you really need to initialize\n    the object after creation, you can implement an ``_init(self)``\n    method that will be called directly after object creation.\n\n    Subclasses of this class can be instantiated to create a new\n    Element.  By default, the tag name will be the class name and the\n    namespace will be empty.  You can modify this with the following\n    class attributes:\n\n    * TAG - the tag name, possibly containing a namespace in Clark\n      notation\n\n    * NAMESPACE - the default namespace URI, unless provided as part\n      of the TAG attribute.\n\n    * HTML - flag if the class is an HTML tag, as opposed to an XML\n      tag.  This only applies to un-namespaced tags and defaults to\n      false (i.e. XML).\n\n    * PARSER - the parser that provides the configuration for the\n      newly created document.  Providing an HTML parser here will\n      default to creating an HTML element.\n\n    In user code, the latter three are commonly inherited in class\n    hierarchies that implement a common namespace.\n    '
    __class__ = ElementBase
    def __init__(self, *children, attrib=None, nsmap=None, **_extra):
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ElementChildIterator(_ElementMatchIterator):
    'ElementChildIterator(self, node, tag=None, reversed=False)\n    Iterates over the children of an element.\n    '
    __class__ = ElementChildIterator
    def __init__(self, node, tag=None, reversed=False):
        'ElementChildIterator(self, node, tag=None, reversed=False)\n    Iterates over the children of an element.\n    '
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
    

class ElementClassLookup(_mod_builtins.object):
    'ElementClassLookup(self)\n    Superclass of Element class lookups.\n    '
    __class__ = ElementClassLookup
    def __init__(self):
        'ElementClassLookup(self)\n    Superclass of Element class lookups.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ElementDefaultClassLookup(ElementClassLookup):
    'ElementDefaultClassLookup(self, element=None, comment=None, pi=None, entity=None)\n    Element class lookup scheme that always returns the default Element\n    class.\n\n    The keyword arguments ``element``, ``comment``, ``pi`` and ``entity``\n    accept the respective Element classes.\n    '
    __class__ = ElementDefaultClassLookup
    def __init__(self, element=None, comment=None, pi=None, entity=None):
        'ElementDefaultClassLookup(self, element=None, comment=None, pi=None, entity=None)\n    Element class lookup scheme that always returns the default Element\n    class.\n\n    The keyword arguments ``element``, ``comment``, ``pi`` and ``entity``\n    accept the respective Element classes.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def comment_class(self):
        pass
    
    @property
    def element_class(self):
        pass
    
    @property
    def entity_class(self):
        pass
    
    @property
    def pi_class(self):
        pass
    

class ElementDepthFirstIterator(_mod_builtins.object):
    "ElementDepthFirstIterator(self, node, tag=None, inclusive=True)\n    Iterates over an element and its sub-elements in document order (depth\n    first pre-order).\n\n    Note that this also includes comments, entities and processing\n    instructions.  To filter them out, check if the ``tag`` property\n    of the returned element is a string (i.e. not None and not a\n    factory function), or pass the ``Element`` factory for the ``tag``\n    argument to receive only Elements.\n\n    If the optional ``tag`` argument is not None, the iterator returns only\n    the elements that match the respective name and namespace.\n\n    The optional boolean argument 'inclusive' defaults to True and can be set\n    to False to exclude the start element itself.\n\n    Note that the behaviour of this iterator is completely undefined if the\n    tree it traverses is modified during iteration.\n    "
    __class__ = ElementDepthFirstIterator
    def __init__(self, node, tag=None, inclusive=True):
        "ElementDepthFirstIterator(self, node, tag=None, inclusive=True)\n    Iterates over an element and its sub-elements in document order (depth\n    first pre-order).\n\n    Note that this also includes comments, entities and processing\n    instructions.  To filter them out, check if the ``tag`` property\n    of the returned element is a string (i.e. not None and not a\n    factory function), or pass the ``Element`` factory for the ``tag``\n    argument to receive only Elements.\n\n    If the optional ``tag`` argument is not None, the iterator returns only\n    the elements that match the respective name and namespace.\n\n    The optional boolean argument 'inclusive' defaults to True and can be set\n    to False to exclude the start element itself.\n\n    Note that the behaviour of this iterator is completely undefined if the\n    tree it traverses is modified during iteration.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return ElementDepthFirstIterator()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class ElementNamespaceClassLookup(FallbackElementClassLookup):
    'ElementNamespaceClassLookup(self, fallback=None)\n\n    Element class lookup scheme that searches the Element class in the\n    Namespace registry.\n\n    Usage:\n\n    >>> lookup = ElementNamespaceClassLookup()\n    >>> ns_elements = lookup.get_namespace("http://schema.org/Movie")\n\n    >>> @ns_elements\n    ... class movie(ElementBase):\n    ...     "Element implementation for \'movie\' tag (using class name) in schema namespace."\n\n    >>> @ns_elements("movie")\n    ... class MovieElement(ElementBase):\n    ...     "Element implementation for \'movie\' tag (explicit tag name) in schema namespace."\n    '
    __class__ = ElementNamespaceClassLookup
    def __init__(self, fallback=None):
        'ElementNamespaceClassLookup(self, fallback=None)\n\n    Element class lookup scheme that searches the Element class in the\n    Namespace registry.\n\n    Usage:\n\n    >>> lookup = ElementNamespaceClassLookup()\n    >>> ns_elements = lookup.get_namespace("http://schema.org/Movie")\n\n    >>> @ns_elements\n    ... class movie(ElementBase):\n    ...     "Element implementation for \'movie\' tag (using class name) in schema namespace."\n\n    >>> @ns_elements("movie")\n    ... class MovieElement(ElementBase):\n    ...     "Element implementation for \'movie\' tag (explicit tag name) in schema namespace."\n    '
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
    
    def get_namespace(self, ns_uri):
        'get_namespace(self, ns_uri)\n\n        Retrieve the namespace object associated with the given URI.\n        Pass None for the empty namespace.\n\n        Creates a new namespace object if it does not yet exist.'
        pass
    

class ElementTextIterator(_mod_builtins.object):
    "ElementTextIterator(self, element, tag=None, with_tail=True)\n    Iterates over the text content of a subtree.\n\n    You can pass the ``tag`` keyword argument to restrict text content to a\n    specific tag name.\n\n    You can set the ``with_tail`` keyword argument to ``False`` to skip over\n    tail text (e.g. if you know that it's only whitespace from pretty-printing).\n    "
    __class__ = ElementTextIterator
    def __init__(self, element, tag=None, with_tail=True):
        "ElementTextIterator(self, element, tag=None, with_tail=True)\n    Iterates over the text content of a subtree.\n\n    You can pass the ``tag`` keyword argument to restrict text content to a\n    specific tag name.\n\n    You can set the ``with_tail`` keyword argument to ``False`` to skip over\n    tail text (e.g. if you know that it's only whitespace from pretty-printing).\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return ElementTextIterator()
    
    def __next__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def ElementTree(element):
    'ElementTree(element=None, file=None, parser=None)\n\n    ElementTree wrapper class.\n    '
    pass

def Entity(name):
    'Entity(name)\n\n    Entity factory.  This factory function creates a special element\n    that will be serialized as an XML entity reference or character\n    reference.  Note, however, that entities will not be automatically\n    declared in the document.  A document that uses entity references\n    requires a DTD to define the entities.\n    '
    pass

class EntityBase(_Entity):
    'All custom Entity classes must inherit from this one.\n\n    To create an XML Entity instance, use the ``Entity()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Entities must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
    __class__ = EntityBase
    def __init__(self, *args, **kwargs):
        'All custom Entity classes must inherit from this one.\n\n    To create an XML Entity instance, use the ``Entity()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Entities must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
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
    

class Error(_mod_builtins.Exception):
    __class__ = Error
    __dict__ = {}
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
    

class ErrorDomains(_mod_builtins.object):
    'Libxml2 error domains'
    BUFFER = 29
    C14N = 21
    CATALOG = 20
    CHECK = 24
    DATATYPE = 15
    DTD = 4
    FTP = 9
    HTML = 5
    HTTP = 10
    I18N = 27
    IO = 8
    MEMORY = 6
    MODULE = 26
    NAMESPACE = 3
    NONE = 0
    OUTPUT = 7
    PARSER = 1
    REGEXP = 14
    RELAXNGP = 18
    RELAXNGV = 19
    SCHEMASP = 16
    SCHEMASV = 17
    SCHEMATRONV = 28
    TREE = 2
    URI = 30
    VALID = 23
    WRITER = 25
    XINCLUDE = 11
    XPATH = 12
    XPOINTER = 13
    XSLT = 22
    __class__ = ErrorDomains
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Libxml2 error domains'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.etree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def _getName(cls):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        pass
    
    _names = _mod_builtins.dict()

class ErrorLevels(_mod_builtins.object):
    'Libxml2 error levels'
    ERROR = 2
    FATAL = 3
    NONE = 0
    WARNING = 1
    __class__ = ErrorLevels
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Libxml2 error levels'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.etree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def _getName(cls):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        pass
    
    _names = _mod_builtins.dict()

class ErrorTypes(_mod_builtins.object):
    'Libxml2 error types'
    BUF_OVERFLOW = 7000
    C14N_CREATE_CTXT = 1950
    C14N_CREATE_STACK = 1952
    C14N_INVALID_NODE = 1953
    C14N_RELATIVE_NAMESPACE = 1955
    C14N_REQUIRES_UTF8 = 1951
    C14N_UNKNOW_NODE = 1954
    CATALOG_ENTRY_BROKEN = 1651
    CATALOG_MISSING_ATTR = 1650
    CATALOG_NOT_CATALOG = 1653
    CATALOG_PREFER_VALUE = 1652
    CATALOG_RECURSION = 1654
    CHECK_ENTITY_TYPE = 5012
    CHECK_FOUND_ATTRIBUTE = 5001
    CHECK_FOUND_CDATA = 5003
    CHECK_FOUND_COMMENT = 5007
    CHECK_FOUND_DOCTYPE = 5008
    CHECK_FOUND_ELEMENT = 5000
    CHECK_FOUND_ENTITY = 5005
    CHECK_FOUND_ENTITYREF = 5004
    CHECK_FOUND_FRAGMENT = 5009
    CHECK_FOUND_NOTATION = 5010
    CHECK_FOUND_PI = 5006
    CHECK_FOUND_TEXT = 5002
    CHECK_NAME_NOT_NULL = 5037
    CHECK_NOT_ATTR = 5023
    CHECK_NOT_ATTR_DECL = 5024
    CHECK_NOT_DTD = 5022
    CHECK_NOT_ELEM_DECL = 5025
    CHECK_NOT_ENTITY_DECL = 5026
    CHECK_NOT_NCNAME = 5034
    CHECK_NOT_NS_DECL = 5027
    CHECK_NOT_UTF8 = 5032
    CHECK_NO_DICT = 5033
    CHECK_NO_DOC = 5014
    CHECK_NO_ELEM = 5016
    CHECK_NO_HREF = 5028
    CHECK_NO_NAME = 5015
    CHECK_NO_NEXT = 5020
    CHECK_NO_PARENT = 5013
    CHECK_NO_PREV = 5018
    CHECK_NS_ANCESTOR = 5031
    CHECK_NS_SCOPE = 5030
    CHECK_OUTSIDE_DICT = 5035
    CHECK_UNKNOWN_NODE = 5011
    CHECK_WRONG_DOC = 5017
    CHECK_WRONG_NAME = 5036
    CHECK_WRONG_NEXT = 5021
    CHECK_WRONG_PARENT = 5029
    CHECK_WRONG_PREV = 5019
    DTD_ATTRIBUTE_DEFAULT = 500
    DTD_ATTRIBUTE_REDEFINED = 501
    DTD_ATTRIBUTE_VALUE = 502
    DTD_CONTENT_ERROR = 503
    DTD_CONTENT_MODEL = 504
    DTD_CONTENT_NOT_DETERMINIST = 505
    DTD_DIFFERENT_PREFIX = 506
    DTD_DUP_TOKEN = 541
    DTD_ELEM_DEFAULT_NAMESPACE = 507
    DTD_ELEM_NAMESPACE = 508
    DTD_ELEM_REDEFINED = 509
    DTD_EMPTY_NOTATION = 510
    DTD_ENTITY_TYPE = 511
    DTD_ID_FIXED = 512
    DTD_ID_REDEFINED = 513
    DTD_ID_SUBSET = 514
    DTD_INVALID_CHILD = 515
    DTD_INVALID_DEFAULT = 516
    DTD_LOAD_ERROR = 517
    DTD_MISSING_ATTRIBUTE = 518
    DTD_MIXED_CORRUPT = 519
    DTD_MULTIPLE_ID = 520
    DTD_NOTATION_REDEFINED = 526
    DTD_NOTATION_VALUE = 527
    DTD_NOT_EMPTY = 528
    DTD_NOT_PCDATA = 529
    DTD_NOT_STANDALONE = 530
    DTD_NO_DOC = 521
    DTD_NO_DTD = 522
    DTD_NO_ELEM_NAME = 523
    DTD_NO_PREFIX = 524
    DTD_NO_ROOT = 525
    DTD_ROOT_NAME = 531
    DTD_STANDALONE_DEFAULTED = 538
    DTD_STANDALONE_WHITE_SPACE = 532
    DTD_UNKNOWN_ATTRIBUTE = 533
    DTD_UNKNOWN_ELEM = 534
    DTD_UNKNOWN_ENTITY = 535
    DTD_UNKNOWN_ID = 536
    DTD_UNKNOWN_NOTATION = 537
    DTD_XMLID_TYPE = 540
    DTD_XMLID_VALUE = 539
    ERR_ATTLIST_NOT_FINISHED = 51
    ERR_ATTLIST_NOT_STARTED = 50
    ERR_ATTRIBUTE_NOT_FINISHED = 40
    ERR_ATTRIBUTE_NOT_STARTED = 39
    ERR_ATTRIBUTE_REDEFINED = 42
    ERR_ATTRIBUTE_WITHOUT_VALUE = 41
    ERR_CDATA_NOT_FINISHED = 63
    ERR_CHARREF_AT_EOF = 10
    ERR_CHARREF_IN_DTD = 13
    ERR_CHARREF_IN_EPILOG = 12
    ERR_CHARREF_IN_PROLOG = 11
    ERR_COMMENT_NOT_FINISHED = 45
    ERR_CONDSEC_INVALID = 83
    ERR_CONDSEC_INVALID_KEYWORD = 95
    ERR_CONDSEC_NOT_FINISHED = 59
    ERR_CONDSEC_NOT_STARTED = 58
    ERR_DOCTYPE_NOT_FINISHED = 61
    ERR_DOCUMENT_EMPTY = 4
    ERR_DOCUMENT_END = 5
    ERR_DOCUMENT_START = 3
    ERR_ELEMCONTENT_NOT_FINISHED = 55
    ERR_ELEMCONTENT_NOT_STARTED = 54
    ERR_ENCODING_NAME = 79
    ERR_ENTITYREF_AT_EOF = 14
    ERR_ENTITYREF_IN_DTD = 17
    ERR_ENTITYREF_IN_EPILOG = 16
    ERR_ENTITYREF_IN_PROLOG = 15
    ERR_ENTITYREF_NO_NAME = 22
    ERR_ENTITYREF_SEMICOL_MISSING = 23
    ERR_ENTITY_BOUNDARY = 90
    ERR_ENTITY_CHAR_ERROR = 87
    ERR_ENTITY_IS_EXTERNAL = 29
    ERR_ENTITY_IS_PARAMETER = 30
    ERR_ENTITY_LOOP = 89
    ERR_ENTITY_NOT_FINISHED = 37
    ERR_ENTITY_NOT_STARTED = 36
    ERR_ENTITY_PE_INTERNAL = 88
    ERR_ENTITY_PROCESSING = 104
    ERR_EQUAL_REQUIRED = 75
    ERR_EXTRA_CONTENT = 86
    ERR_EXT_ENTITY_STANDALONE = 82
    ERR_EXT_SUBSET_NOT_FINISHED = 60
    ERR_GT_REQUIRED = 73
    ERR_HYPHEN_IN_COMMENT = 80
    ERR_INTERNAL_ERROR = 1
    ERR_INVALID_CHAR = 9
    ERR_INVALID_CHARREF = 8
    ERR_INVALID_DEC_CHARREF = 7
    ERR_INVALID_ENCODING = 81
    ERR_INVALID_HEX_CHARREF = 6
    ERR_INVALID_URI = 91
    ERR_LITERAL_NOT_FINISHED = 44
    ERR_LITERAL_NOT_STARTED = 43
    ERR_LTSLASH_REQUIRED = 74
    ERR_LT_IN_ATTRIBUTE = 38
    ERR_LT_REQUIRED = 72
    ERR_MISPLACED_CDATA_END = 62
    ERR_MISSING_ENCODING = 101
    ERR_MIXED_NOT_FINISHED = 53
    ERR_MIXED_NOT_STARTED = 52
    ERR_NAME_REQUIRED = 68
    ERR_NAME_TOO_LONG = 110
    ERR_NMTOKEN_REQUIRED = 67
    ERR_NOTATION_NOT_FINISHED = 49
    ERR_NOTATION_NOT_STARTED = 48
    ERR_NOTATION_PROCESSING = 105
    ERR_NOT_STANDALONE = 103
    ERR_NOT_WELL_BALANCED = 85
    ERR_NO_DTD = 94
    ERR_NO_MEMORY = 2
    ERR_NS_DECL_ERROR = 35
    ERR_OK = 0
    ERR_PCDATA_REQUIRED = 69
    ERR_PEREF_AT_EOF = 18
    ERR_PEREF_IN_EPILOG = 20
    ERR_PEREF_IN_INT_SUBSET = 21
    ERR_PEREF_IN_PROLOG = 19
    ERR_PEREF_NO_NAME = 24
    ERR_PEREF_SEMICOL_MISSING = 25
    ERR_PI_NOT_FINISHED = 47
    ERR_PI_NOT_STARTED = 46
    ERR_PUBID_REQUIRED = 71
    ERR_RESERVED_XML_NAME = 64
    ERR_SEPARATOR_REQUIRED = 66
    ERR_SPACE_REQUIRED = 65
    ERR_STANDALONE_VALUE = 78
    ERR_STRING_NOT_CLOSED = 34
    ERR_STRING_NOT_STARTED = 33
    ERR_TAG_NAME_MISMATCH = 76
    ERR_TAG_NOT_FINISHED = 77
    ERR_UNDECLARED_ENTITY = 26
    ERR_UNKNOWN_ENCODING = 31
    ERR_UNKNOWN_VERSION = 108
    ERR_UNPARSED_ENTITY = 28
    ERR_UNSUPPORTED_ENCODING = 32
    ERR_URI_FRAGMENT = 92
    ERR_URI_REQUIRED = 70
    ERR_USER_STOP = 111
    ERR_VALUE_REQUIRED = 84
    ERR_VERSION_MISMATCH = 109
    ERR_VERSION_MISSING = 96
    ERR_XMLDECL_NOT_FINISHED = 57
    ERR_XMLDECL_NOT_STARTED = 56
    FTP_ACCNT = 2002
    FTP_EPSV_ANSWER = 2001
    FTP_PASV_ANSWER = 2000
    FTP_URL_SYNTAX = 2003
    HTML_STRUCURE_ERROR = 800
    HTML_UNKNOWN_TAG = 801
    HTTP_UNKNOWN_HOST = 2022
    HTTP_URL_SYNTAX = 2020
    HTTP_USE_IP = 2021
    I18N_CONV_FAILED = 6003
    I18N_EXCESS_HANDLER = 6002
    I18N_NO_HANDLER = 6001
    I18N_NO_NAME = 6000
    I18N_NO_OUTPUT = 6004
    IO_BUFFER_FULL = 1548
    IO_EACCES = 1501
    IO_EADDRINUSE = 1554
    IO_EAFNOSUPPORT = 1556
    IO_EAGAIN = 1502
    IO_EALREADY = 1555
    IO_EBADF = 1503
    IO_EBADMSG = 1504
    IO_EBUSY = 1505
    IO_ECANCELED = 1506
    IO_ECHILD = 1507
    IO_ECONNREFUSED = 1552
    IO_EDEADLK = 1508
    IO_EDOM = 1509
    IO_EEXIST = 1510
    IO_EFAULT = 1511
    IO_EFBIG = 1512
    IO_EINPROGRESS = 1513
    IO_EINTR = 1514
    IO_EINVAL = 1515
    IO_EIO = 1516
    IO_EISCONN = 1551
    IO_EISDIR = 1517
    IO_EMFILE = 1518
    IO_EMLINK = 1519
    IO_EMSGSIZE = 1520
    IO_ENAMETOOLONG = 1521
    IO_ENCODER = 1544
    IO_ENETUNREACH = 1553
    IO_ENFILE = 1522
    IO_ENODEV = 1523
    IO_ENOENT = 1524
    IO_ENOEXEC = 1525
    IO_ENOLCK = 1526
    IO_ENOMEM = 1527
    IO_ENOSPC = 1528
    IO_ENOSYS = 1529
    IO_ENOTDIR = 1530
    IO_ENOTEMPTY = 1531
    IO_ENOTSOCK = 1550
    IO_ENOTSUP = 1532
    IO_ENOTTY = 1533
    IO_ENXIO = 1534
    IO_EPERM = 1535
    IO_EPIPE = 1536
    IO_ERANGE = 1537
    IO_EROFS = 1538
    IO_ESPIPE = 1539
    IO_ESRCH = 1540
    IO_ETIMEDOUT = 1541
    IO_EXDEV = 1542
    IO_FLUSH = 1545
    IO_LOAD_ERROR = 1549
    IO_NETWORK_ATTEMPT = 1543
    IO_NO_INPUT = 1547
    IO_UNKNOWN = 1500
    IO_WRITE = 1546
    MODULE_CLOSE = 4901
    MODULE_OPEN = 4900
    NS_ERR_ATTRIBUTE_REDEFINED = 203
    NS_ERR_COLON = 205
    NS_ERR_EMPTY = 204
    NS_ERR_QNAME = 202
    NS_ERR_UNDEFINED_NAMESPACE = 201
    NS_ERR_XML_NAMESPACE = 200
    REGEXP_COMPILE_ERROR = 1450
    RNGP_ANYNAME_ATTR_ANCESTOR = 1000
    RNGP_ATTRIBUTE_CHILDREN = 1002
    RNGP_ATTRIBUTE_CONTENT = 1003
    RNGP_ATTRIBUTE_EMPTY = 1004
    RNGP_ATTRIBUTE_NOOP = 1005
    RNGP_ATTR_CONFLICT = 1001
    RNGP_CHOICE_CONTENT = 1006
    RNGP_CHOICE_EMPTY = 1007
    RNGP_CREATE_FAILURE = 1008
    RNGP_DATA_CONTENT = 1009
    RNGP_DEFINE_CREATE_FAILED = 1011
    RNGP_DEFINE_EMPTY = 1012
    RNGP_DEFINE_MISSING = 1013
    RNGP_DEFINE_NAME_MISSING = 1014
    RNGP_DEF_CHOICE_AND_INTERLEAVE = 1010
    RNGP_ELEMENT_CONTENT = 1018
    RNGP_ELEMENT_EMPTY = 1017
    RNGP_ELEMENT_NAME = 1019
    RNGP_ELEMENT_NO_CONTENT = 1020
    RNGP_ELEM_CONTENT_EMPTY = 1015
    RNGP_ELEM_CONTENT_ERROR = 1016
    RNGP_ELEM_TEXT_CONFLICT = 1021
    RNGP_EMPTY = 1022
    RNGP_EMPTY_CONSTRUCT = 1023
    RNGP_EMPTY_CONTENT = 1024
    RNGP_EMPTY_NOT_EMPTY = 1025
    RNGP_ERROR_TYPE_LIB = 1026
    RNGP_EXCEPT_EMPTY = 1027
    RNGP_EXCEPT_MISSING = 1028
    RNGP_EXCEPT_MULTIPLE = 1029
    RNGP_EXCEPT_NO_CONTENT = 1030
    RNGP_EXTERNALREF_EMTPY = 1031
    RNGP_EXTERNALREF_RECURSE = 1033
    RNGP_EXTERNAL_REF_FAILURE = 1032
    RNGP_FORBIDDEN_ATTRIBUTE = 1034
    RNGP_FOREIGN_ELEMENT = 1035
    RNGP_GRAMMAR_CONTENT = 1036
    RNGP_GRAMMAR_EMPTY = 1037
    RNGP_GRAMMAR_MISSING = 1038
    RNGP_GRAMMAR_NO_START = 1039
    RNGP_GROUP_ATTR_CONFLICT = 1040
    RNGP_HREF_ERROR = 1041
    RNGP_INCLUDE_EMPTY = 1042
    RNGP_INCLUDE_FAILURE = 1043
    RNGP_INCLUDE_RECURSE = 1044
    RNGP_INTERLEAVE_ADD = 1045
    RNGP_INTERLEAVE_CREATE_FAILED = 1046
    RNGP_INTERLEAVE_EMPTY = 1047
    RNGP_INTERLEAVE_NO_CONTENT = 1048
    RNGP_INVALID_DEFINE_NAME = 1049
    RNGP_INVALID_URI = 1050
    RNGP_INVALID_VALUE = 1051
    RNGP_MISSING_HREF = 1052
    RNGP_NAME_MISSING = 1053
    RNGP_NEED_COMBINE = 1054
    RNGP_NOTALLOWED_NOT_EMPTY = 1055
    RNGP_NSNAME_ATTR_ANCESTOR = 1056
    RNGP_NSNAME_NO_NS = 1057
    RNGP_PARAM_FORBIDDEN = 1058
    RNGP_PARAM_NAME_MISSING = 1059
    RNGP_PARENTREF_CREATE_FAILED = 1060
    RNGP_PARENTREF_NAME_INVALID = 1061
    RNGP_PARENTREF_NOT_EMPTY = 1064
    RNGP_PARENTREF_NO_NAME = 1062
    RNGP_PARENTREF_NO_PARENT = 1063
    RNGP_PARSE_ERROR = 1065
    RNGP_PAT_ANYNAME_EXCEPT_ANYNAME = 1066
    RNGP_PAT_ATTR_ATTR = 1067
    RNGP_PAT_ATTR_ELEM = 1068
    RNGP_PAT_DATA_EXCEPT_ATTR = 1069
    RNGP_PAT_DATA_EXCEPT_ELEM = 1070
    RNGP_PAT_DATA_EXCEPT_EMPTY = 1071
    RNGP_PAT_DATA_EXCEPT_GROUP = 1072
    RNGP_PAT_DATA_EXCEPT_INTERLEAVE = 1073
    RNGP_PAT_DATA_EXCEPT_LIST = 1074
    RNGP_PAT_DATA_EXCEPT_ONEMORE = 1075
    RNGP_PAT_DATA_EXCEPT_REF = 1076
    RNGP_PAT_DATA_EXCEPT_TEXT = 1077
    RNGP_PAT_LIST_ATTR = 1078
    RNGP_PAT_LIST_ELEM = 1079
    RNGP_PAT_LIST_INTERLEAVE = 1080
    RNGP_PAT_LIST_LIST = 1081
    RNGP_PAT_LIST_REF = 1082
    RNGP_PAT_LIST_TEXT = 1083
    RNGP_PAT_NSNAME_EXCEPT_ANYNAME = 1084
    RNGP_PAT_NSNAME_EXCEPT_NSNAME = 1085
    RNGP_PAT_ONEMORE_GROUP_ATTR = 1086
    RNGP_PAT_ONEMORE_INTERLEAVE_ATTR = 1087
    RNGP_PAT_START_ATTR = 1088
    RNGP_PAT_START_DATA = 1089
    RNGP_PAT_START_EMPTY = 1090
    RNGP_PAT_START_GROUP = 1091
    RNGP_PAT_START_INTERLEAVE = 1092
    RNGP_PAT_START_LIST = 1093
    RNGP_PAT_START_ONEMORE = 1094
    RNGP_PAT_START_TEXT = 1095
    RNGP_PAT_START_VALUE = 1096
    RNGP_PREFIX_UNDEFINED = 1097
    RNGP_REF_CREATE_FAILED = 1098
    RNGP_REF_CYCLE = 1099
    RNGP_REF_NAME_INVALID = 1100
    RNGP_REF_NOT_EMPTY = 1103
    RNGP_REF_NO_DEF = 1101
    RNGP_REF_NO_NAME = 1102
    RNGP_START_CHOICE_AND_INTERLEAVE = 1104
    RNGP_START_CONTENT = 1105
    RNGP_START_EMPTY = 1106
    RNGP_START_MISSING = 1107
    RNGP_TEXT_EXPECTED = 1108
    RNGP_TEXT_HAS_CHILD = 1109
    RNGP_TYPE_MISSING = 1110
    RNGP_TYPE_NOT_FOUND = 1111
    RNGP_TYPE_VALUE = 1112
    RNGP_UNKNOWN_ATTRIBUTE = 1113
    RNGP_UNKNOWN_COMBINE = 1114
    RNGP_UNKNOWN_CONSTRUCT = 1115
    RNGP_UNKNOWN_TYPE_LIB = 1116
    RNGP_URI_FRAGMENT = 1117
    RNGP_URI_NOT_ABSOLUTE = 1118
    RNGP_VALUE_EMPTY = 1119
    RNGP_VALUE_NO_CONTENT = 1120
    RNGP_XMLNS_NAME = 1121
    RNGP_XML_NS = 1122
    SAVE_CHAR_INVALID = 1401
    SAVE_NOT_UTF8 = 1400
    SAVE_NO_DOCTYPE = 1402
    SAVE_UNKNOWN_ENCODING = 1403
    SCHEMAP_AG_PROPS_CORRECT = 3087
    SCHEMAP_ATTRFORMDEFAULT_VALUE = 1701
    SCHEMAP_ATTRGRP_NONAME_NOREF = 1702
    SCHEMAP_ATTR_NONAME_NOREF = 1703
    SCHEMAP_AU_PROPS_CORRECT = 3089
    SCHEMAP_AU_PROPS_CORRECT_2 = 3078
    SCHEMAP_A_PROPS_CORRECT_2 = 3079
    SCHEMAP_A_PROPS_CORRECT_3 = 3090
    SCHEMAP_COMPLEXTYPE_NONAME_NOREF = 1704
    SCHEMAP_COS_ALL_LIMITED = 3091
    SCHEMAP_COS_CT_EXTENDS_1_1 = 3063
    SCHEMAP_COS_CT_EXTENDS_1_2 = 3088
    SCHEMAP_COS_CT_EXTENDS_1_3 = 1800
    SCHEMAP_COS_ST_DERIVED_OK_2_1 = 3031
    SCHEMAP_COS_ST_DERIVED_OK_2_2 = 3032
    SCHEMAP_COS_ST_RESTRICTS_1_1 = 3011
    SCHEMAP_COS_ST_RESTRICTS_1_2 = 3012
    SCHEMAP_COS_ST_RESTRICTS_1_3_1 = 3013
    SCHEMAP_COS_ST_RESTRICTS_1_3_2 = 3014
    SCHEMAP_COS_ST_RESTRICTS_2_1 = 3015
    SCHEMAP_COS_ST_RESTRICTS_2_3_1_1 = 3016
    SCHEMAP_COS_ST_RESTRICTS_2_3_1_2 = 3017
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_1 = 3018
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_2 = 3019
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_3 = 3020
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_4 = 3021
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_5 = 3022
    SCHEMAP_COS_ST_RESTRICTS_3_1 = 3023
    SCHEMAP_COS_ST_RESTRICTS_3_3_1 = 3024
    SCHEMAP_COS_ST_RESTRICTS_3_3_1_2 = 3025
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_1 = 3027
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_2 = 3026
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_3 = 3028
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_4 = 3029
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_5 = 3030
    SCHEMAP_COS_VALID_DEFAULT_1 = 3058
    SCHEMAP_COS_VALID_DEFAULT_2_1 = 3059
    SCHEMAP_COS_VALID_DEFAULT_2_2_1 = 3060
    SCHEMAP_COS_VALID_DEFAULT_2_2_2 = 3061
    SCHEMAP_CT_PROPS_CORRECT_1 = 1782
    SCHEMAP_CT_PROPS_CORRECT_2 = 1783
    SCHEMAP_CT_PROPS_CORRECT_3 = 1784
    SCHEMAP_CT_PROPS_CORRECT_4 = 1785
    SCHEMAP_CT_PROPS_CORRECT_5 = 1786
    SCHEMAP_CVC_SIMPLE_TYPE = 3062
    SCHEMAP_C_PROPS_CORRECT = 3080
    SCHEMAP_DEF_AND_PREFIX = 1768
    SCHEMAP_DERIVATION_OK_RESTRICTION_1 = 1787
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_1_1 = 1788
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_1_2 = 1789
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_1_3 = 3077
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_2 = 1790
    SCHEMAP_DERIVATION_OK_RESTRICTION_3 = 1791
    SCHEMAP_DERIVATION_OK_RESTRICTION_4_1 = 1797
    SCHEMAP_DERIVATION_OK_RESTRICTION_4_2 = 1798
    SCHEMAP_DERIVATION_OK_RESTRICTION_4_3 = 1799
    SCHEMAP_ELEMFORMDEFAULT_VALUE = 1705
    SCHEMAP_ELEM_DEFAULT_FIXED = 1755
    SCHEMAP_ELEM_NONAME_NOREF = 1706
    SCHEMAP_EXTENSION_NO_BASE = 1707
    SCHEMAP_E_PROPS_CORRECT_2 = 3045
    SCHEMAP_E_PROPS_CORRECT_3 = 3046
    SCHEMAP_E_PROPS_CORRECT_4 = 3047
    SCHEMAP_E_PROPS_CORRECT_5 = 3048
    SCHEMAP_E_PROPS_CORRECT_6 = 3049
    SCHEMAP_FACET_NO_VALUE = 1708
    SCHEMAP_FAILED_BUILD_IMPORT = 1709
    SCHEMAP_FAILED_LOAD = 1757
    SCHEMAP_FAILED_PARSE = 1766
    SCHEMAP_GROUP_NONAME_NOREF = 1710
    SCHEMAP_IMPORT_NAMESPACE_NOT_URI = 1711
    SCHEMAP_IMPORT_REDEFINE_NSNAME = 1712
    SCHEMAP_IMPORT_SCHEMA_NOT_URI = 1713
    SCHEMAP_INCLUDE_SCHEMA_NOT_URI = 1770
    SCHEMAP_INCLUDE_SCHEMA_NO_URI = 1771
    SCHEMAP_INTERNAL = 3069
    SCHEMAP_INTERSECTION_NOT_EXPRESSIBLE = 1793
    SCHEMAP_INVALID_ATTR_COMBINATION = 1777
    SCHEMAP_INVALID_ATTR_INLINE_COMBINATION = 1778
    SCHEMAP_INVALID_ATTR_NAME = 1780
    SCHEMAP_INVALID_ATTR_USE = 1774
    SCHEMAP_INVALID_BOOLEAN = 1714
    SCHEMAP_INVALID_ENUM = 1715
    SCHEMAP_INVALID_FACET = 1716
    SCHEMAP_INVALID_FACET_VALUE = 1717
    SCHEMAP_INVALID_MAXOCCURS = 1718
    SCHEMAP_INVALID_MINOCCURS = 1719
    SCHEMAP_INVALID_REF_AND_SUBTYPE = 1720
    SCHEMAP_INVALID_WHITE_SPACE = 1721
    SCHEMAP_MG_PROPS_CORRECT_1 = 3074
    SCHEMAP_MG_PROPS_CORRECT_2 = 3075
    SCHEMAP_MISSING_SIMPLETYPE_CHILD = 1779
    SCHEMAP_NOATTR_NOREF = 1722
    SCHEMAP_NOROOT = 1759
    SCHEMAP_NOTATION_NO_NAME = 1723
    SCHEMAP_NOTHING_TO_PARSE = 1758
    SCHEMAP_NOTYPE_NOREF = 1724
    SCHEMAP_NOT_DETERMINISTIC = 3070
    SCHEMAP_NOT_SCHEMA = 1772
    SCHEMAP_NO_XMLNS = 3056
    SCHEMAP_NO_XSI = 3057
    SCHEMAP_PREFIX_UNDEFINED = 1700
    SCHEMAP_P_PROPS_CORRECT_1 = 3042
    SCHEMAP_P_PROPS_CORRECT_2_1 = 3043
    SCHEMAP_P_PROPS_CORRECT_2_2 = 3044
    SCHEMAP_RECURSIVE = 1775
    SCHEMAP_REDEFINED_ATTR = 1764
    SCHEMAP_REDEFINED_ATTRGROUP = 1763
    SCHEMAP_REDEFINED_ELEMENT = 1762
    SCHEMAP_REDEFINED_GROUP = 1760
    SCHEMAP_REDEFINED_NOTATION = 1765
    SCHEMAP_REDEFINED_TYPE = 1761
    SCHEMAP_REF_AND_CONTENT = 1781
    SCHEMAP_REF_AND_SUBTYPE = 1725
    SCHEMAP_REGEXP_INVALID = 1756
    SCHEMAP_RESTRICTION_NONAME_NOREF = 1726
    SCHEMAP_S4S_ATTR_INVALID_VALUE = 3037
    SCHEMAP_S4S_ATTR_MISSING = 3036
    SCHEMAP_S4S_ATTR_NOT_ALLOWED = 3035
    SCHEMAP_S4S_ELEM_MISSING = 3034
    SCHEMAP_S4S_ELEM_NOT_ALLOWED = 3033
    SCHEMAP_SIMPLETYPE_NONAME = 1727
    SCHEMAP_SRC_ATTRIBUTE_1 = 3051
    SCHEMAP_SRC_ATTRIBUTE_2 = 3052
    SCHEMAP_SRC_ATTRIBUTE_3_1 = 3053
    SCHEMAP_SRC_ATTRIBUTE_3_2 = 3054
    SCHEMAP_SRC_ATTRIBUTE_4 = 3055
    SCHEMAP_SRC_ATTRIBUTE_GROUP_1 = 3071
    SCHEMAP_SRC_ATTRIBUTE_GROUP_2 = 3072
    SCHEMAP_SRC_ATTRIBUTE_GROUP_3 = 3073
    SCHEMAP_SRC_CT_1 = 3076
    SCHEMAP_SRC_ELEMENT_1 = 3038
    SCHEMAP_SRC_ELEMENT_2_1 = 3039
    SCHEMAP_SRC_ELEMENT_2_2 = 3040
    SCHEMAP_SRC_ELEMENT_3 = 3041
    SCHEMAP_SRC_IMPORT = 3082
    SCHEMAP_SRC_IMPORT_1_1 = 3064
    SCHEMAP_SRC_IMPORT_1_2 = 3065
    SCHEMAP_SRC_IMPORT_2 = 3066
    SCHEMAP_SRC_IMPORT_2_1 = 3067
    SCHEMAP_SRC_IMPORT_2_2 = 3068
    SCHEMAP_SRC_IMPORT_3_1 = 1795
    SCHEMAP_SRC_IMPORT_3_2 = 1796
    SCHEMAP_SRC_INCLUDE = 3050
    SCHEMAP_SRC_LIST_ITEMTYPE_OR_SIMPLETYPE = 3006
    SCHEMAP_SRC_REDEFINE = 3081
    SCHEMAP_SRC_RESOLVE = 3004
    SCHEMAP_SRC_RESTRICTION_BASE_OR_SIMPLETYPE = 3005
    SCHEMAP_SRC_SIMPLE_TYPE_1 = 3000
    SCHEMAP_SRC_SIMPLE_TYPE_2 = 3001
    SCHEMAP_SRC_SIMPLE_TYPE_3 = 3002
    SCHEMAP_SRC_SIMPLE_TYPE_4 = 3003
    SCHEMAP_SRC_UNION_MEMBERTYPES_OR_SIMPLETYPES = 3007
    SCHEMAP_ST_PROPS_CORRECT_1 = 3008
    SCHEMAP_ST_PROPS_CORRECT_2 = 3009
    SCHEMAP_ST_PROPS_CORRECT_3 = 3010
    SCHEMAP_SUPERNUMEROUS_LIST_ITEM_TYPE = 1776
    SCHEMAP_TYPE_AND_SUBTYPE = 1728
    SCHEMAP_UNION_NOT_EXPRESSIBLE = 1794
    SCHEMAP_UNKNOWN_ALL_CHILD = 1729
    SCHEMAP_UNKNOWN_ANYATTRIBUTE_CHILD = 1730
    SCHEMAP_UNKNOWN_ATTRGRP_CHILD = 1732
    SCHEMAP_UNKNOWN_ATTRIBUTE_GROUP = 1733
    SCHEMAP_UNKNOWN_ATTR_CHILD = 1731
    SCHEMAP_UNKNOWN_BASE_TYPE = 1734
    SCHEMAP_UNKNOWN_CHOICE_CHILD = 1735
    SCHEMAP_UNKNOWN_COMPLEXCONTENT_CHILD = 1736
    SCHEMAP_UNKNOWN_COMPLEXTYPE_CHILD = 1737
    SCHEMAP_UNKNOWN_ELEM_CHILD = 1738
    SCHEMAP_UNKNOWN_EXTENSION_CHILD = 1739
    SCHEMAP_UNKNOWN_FACET_CHILD = 1740
    SCHEMAP_UNKNOWN_FACET_TYPE = 1741
    SCHEMAP_UNKNOWN_GROUP_CHILD = 1742
    SCHEMAP_UNKNOWN_IMPORT_CHILD = 1743
    SCHEMAP_UNKNOWN_INCLUDE_CHILD = 1769
    SCHEMAP_UNKNOWN_LIST_CHILD = 1744
    SCHEMAP_UNKNOWN_MEMBER_TYPE = 1773
    SCHEMAP_UNKNOWN_NOTATION_CHILD = 1745
    SCHEMAP_UNKNOWN_PREFIX = 1767
    SCHEMAP_UNKNOWN_PROCESSCONTENT_CHILD = 1746
    SCHEMAP_UNKNOWN_REF = 1747
    SCHEMAP_UNKNOWN_RESTRICTION_CHILD = 1748
    SCHEMAP_UNKNOWN_SCHEMAS_CHILD = 1749
    SCHEMAP_UNKNOWN_SEQUENCE_CHILD = 1750
    SCHEMAP_UNKNOWN_SIMPLECONTENT_CHILD = 1751
    SCHEMAP_UNKNOWN_SIMPLETYPE_CHILD = 1752
    SCHEMAP_UNKNOWN_TYPE = 1753
    SCHEMAP_UNKNOWN_UNION_CHILD = 1754
    SCHEMAP_WARN_ATTR_POINTLESS_PROH = 3086
    SCHEMAP_WARN_ATTR_REDECL_PROH = 3085
    SCHEMAP_WARN_SKIP_SCHEMA = 3083
    SCHEMAP_WARN_UNLOCATED_SCHEMA = 3084
    SCHEMAP_WILDCARD_INVALID_NS_MEMBER = 1792
    SCHEMATRONV_ASSERT = 4000
    SCHEMATRONV_REPORT = 4001
    SCHEMAV_ATTRINVALID = 1821
    SCHEMAV_ATTRUNKNOWN = 1820
    SCHEMAV_CONSTRUCT = 1817
    SCHEMAV_CVC_ATTRIBUTE_1 = 1861
    SCHEMAV_CVC_ATTRIBUTE_2 = 1862
    SCHEMAV_CVC_ATTRIBUTE_3 = 1863
    SCHEMAV_CVC_ATTRIBUTE_4 = 1864
    SCHEMAV_CVC_AU = 1874
    SCHEMAV_CVC_COMPLEX_TYPE_1 = 1873
    SCHEMAV_CVC_COMPLEX_TYPE_2_1 = 1841
    SCHEMAV_CVC_COMPLEX_TYPE_2_2 = 1842
    SCHEMAV_CVC_COMPLEX_TYPE_2_3 = 1843
    SCHEMAV_CVC_COMPLEX_TYPE_2_4 = 1844
    SCHEMAV_CVC_COMPLEX_TYPE_3_1 = 1865
    SCHEMAV_CVC_COMPLEX_TYPE_3_2_1 = 1866
    SCHEMAV_CVC_COMPLEX_TYPE_3_2_2 = 1867
    SCHEMAV_CVC_COMPLEX_TYPE_4 = 1868
    SCHEMAV_CVC_COMPLEX_TYPE_5_1 = 1869
    SCHEMAV_CVC_COMPLEX_TYPE_5_2 = 1870
    SCHEMAV_CVC_DATATYPE_VALID_1_2_1 = 1824
    SCHEMAV_CVC_DATATYPE_VALID_1_2_2 = 1825
    SCHEMAV_CVC_DATATYPE_VALID_1_2_3 = 1826
    SCHEMAV_CVC_ELT_1 = 1845
    SCHEMAV_CVC_ELT_2 = 1846
    SCHEMAV_CVC_ELT_3_1 = 1847
    SCHEMAV_CVC_ELT_3_2_1 = 1848
    SCHEMAV_CVC_ELT_3_2_2 = 1849
    SCHEMAV_CVC_ELT_4_1 = 1850
    SCHEMAV_CVC_ELT_4_2 = 1851
    SCHEMAV_CVC_ELT_4_3 = 1852
    SCHEMAV_CVC_ELT_5_1_1 = 1853
    SCHEMAV_CVC_ELT_5_1_2 = 1854
    SCHEMAV_CVC_ELT_5_2_1 = 1855
    SCHEMAV_CVC_ELT_5_2_2_1 = 1856
    SCHEMAV_CVC_ELT_5_2_2_2_1 = 1857
    SCHEMAV_CVC_ELT_5_2_2_2_2 = 1858
    SCHEMAV_CVC_ELT_6 = 1859
    SCHEMAV_CVC_ELT_7 = 1860
    SCHEMAV_CVC_ENUMERATION_VALID = 1840
    SCHEMAV_CVC_FACET_VALID = 1829
    SCHEMAV_CVC_FRACTIONDIGITS_VALID = 1838
    SCHEMAV_CVC_IDC = 1877
    SCHEMAV_CVC_LENGTH_VALID = 1830
    SCHEMAV_CVC_MAXEXCLUSIVE_VALID = 1836
    SCHEMAV_CVC_MAXINCLUSIVE_VALID = 1834
    SCHEMAV_CVC_MAXLENGTH_VALID = 1832
    SCHEMAV_CVC_MINEXCLUSIVE_VALID = 1835
    SCHEMAV_CVC_MININCLUSIVE_VALID = 1833
    SCHEMAV_CVC_MINLENGTH_VALID = 1831
    SCHEMAV_CVC_PATTERN_VALID = 1839
    SCHEMAV_CVC_TOTALDIGITS_VALID = 1837
    SCHEMAV_CVC_TYPE_1 = 1875
    SCHEMAV_CVC_TYPE_2 = 1876
    SCHEMAV_CVC_TYPE_3_1_1 = 1827
    SCHEMAV_CVC_TYPE_3_1_2 = 1828
    SCHEMAV_CVC_WILDCARD = 1878
    SCHEMAV_DOCUMENT_ELEMENT_MISSING = 1872
    SCHEMAV_ELEMCONT = 1810
    SCHEMAV_ELEMENT_CONTENT = 1871
    SCHEMAV_EXTRACONTENT = 1813
    SCHEMAV_FACET = 1823
    SCHEMAV_HAVEDEFAULT = 1811
    SCHEMAV_INTERNAL = 1818
    SCHEMAV_INVALIDATTR = 1814
    SCHEMAV_INVALIDELEM = 1815
    SCHEMAV_ISABSTRACT = 1808
    SCHEMAV_MISC = 1879
    SCHEMAV_MISSING = 1804
    SCHEMAV_NOROLLBACK = 1807
    SCHEMAV_NOROOT = 1801
    SCHEMAV_NOTDETERMINIST = 1816
    SCHEMAV_NOTEMPTY = 1809
    SCHEMAV_NOTNILLABLE = 1812
    SCHEMAV_NOTSIMPLE = 1819
    SCHEMAV_NOTTOPLEVEL = 1803
    SCHEMAV_NOTYPE = 1806
    SCHEMAV_UNDECLAREDELEM = 1802
    SCHEMAV_VALUE = 1822
    SCHEMAV_WRONGELEM = 1805
    TREE_INVALID_DEC = 1301
    TREE_INVALID_HEX = 1300
    TREE_NOT_UTF8 = 1303
    TREE_UNTERMINATED_ENTITY = 1302
    WAR_CATALOG_PI = 93
    WAR_ENTITY_REDEFINED = 107
    WAR_LANG_VALUE = 98
    WAR_NS_COLUMN = 106
    WAR_NS_URI = 99
    WAR_NS_URI_RELATIVE = 100
    WAR_SPACE_VALUE = 102
    WAR_UNDECLARED_ENTITY = 27
    WAR_UNKNOWN_VERSION = 97
    XINCLUDE_BUILD_FAILED = 1609
    XINCLUDE_DEPRECATED_NS = 1617
    XINCLUDE_ENTITY_DEF_MISMATCH = 1602
    XINCLUDE_FALLBACKS_IN_INCLUDE = 1615
    XINCLUDE_FALLBACK_NOT_IN_INCLUDE = 1616
    XINCLUDE_FRAGMENT_ID = 1618
    XINCLUDE_HREF_URI = 1605
    XINCLUDE_INCLUDE_IN_INCLUDE = 1614
    XINCLUDE_INVALID_CHAR = 1608
    XINCLUDE_MULTIPLE_ROOT = 1611
    XINCLUDE_NO_FALLBACK = 1604
    XINCLUDE_NO_HREF = 1603
    XINCLUDE_PARSE_VALUE = 1601
    XINCLUDE_RECURSION = 1600
    XINCLUDE_TEXT_DOCUMENT = 1607
    XINCLUDE_TEXT_FRAGMENT = 1606
    XINCLUDE_UNKNOWN_ENCODING = 1610
    XINCLUDE_XPTR_FAILED = 1612
    XINCLUDE_XPTR_RESULT = 1613
    XPATH_ENCODING_ERROR = 1220
    XPATH_EXPRESSION_OK = 1200
    XPATH_EXPR_ERROR = 1207
    XPATH_INVALID_ARITY = 1212
    XPATH_INVALID_CHAR_ERROR = 1221
    XPATH_INVALID_CTXT_POSITION = 1214
    XPATH_INVALID_CTXT_SIZE = 1213
    XPATH_INVALID_OPERAND = 1210
    XPATH_INVALID_PREDICATE_ERROR = 1206
    XPATH_INVALID_TYPE = 1211
    XPATH_MEMORY_ERROR = 1215
    XPATH_NUMBER_ERROR = 1201
    XPATH_START_LITERAL_ERROR = 1203
    XPATH_UNCLOSED_ERROR = 1208
    XPATH_UNDEF_PREFIX_ERROR = 1219
    XPATH_UNDEF_VARIABLE_ERROR = 1205
    XPATH_UNFINISHED_LITERAL_ERROR = 1202
    XPATH_UNKNOWN_FUNC_ERROR = 1209
    XPATH_VARIABLE_REF_ERROR = 1204
    XPTR_CHILDSEQ_START = 1901
    XPTR_EVAL_FAILED = 1902
    XPTR_EXTRA_OBJECTS = 1903
    XPTR_RESOURCE_ERROR = 1217
    XPTR_SUB_RESOURCE_ERROR = 1218
    XPTR_SYNTAX_ERROR = 1216
    XPTR_UNKNOWN_SCHEME = 1900
    __class__ = ErrorTypes
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Libxml2 error types'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.etree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def _getName(cls):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        pass
    
    _names = _mod_builtins.dict()

def Extension(module, function_mapping):
    'Extension(module, function_mapping=None, ns=None)\n\n    Build a dictionary of extension functions from the functions\n    defined in a module or the methods of an object.\n\n    As second argument, you can pass an additional mapping of\n    attribute names to XPath function names, or a list of function\n    names that should be taken.\n\n    The ``ns`` keyword argument accepts a namespace URI for the XPath\n    functions.\n    '
    pass

class FallbackElementClassLookup(ElementClassLookup):
    'FallbackElementClassLookup(self, fallback=None)\n\n    Superclass of Element class lookups with additional fallback.\n    '
    __class__ = FallbackElementClassLookup
    def __init__(self, fallback=None):
        'FallbackElementClassLookup(self, fallback=None)\n\n    Superclass of Element class lookups with additional fallback.\n    '
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
    def fallback(self):
        pass
    
    def set_fallback(self, lookup):
        'set_fallback(self, lookup)\n\n        Sets the fallback scheme for this lookup method.\n        '
        pass
    

def FunctionNamespace(ns_uri):
    'FunctionNamespace(ns_uri)\n\n    Retrieve the function namespace object associated with the given\n    URI.\n\n    Creates a new one if it does not yet exist. A function namespace\n    can only be used to register extension functions.\n\n    Usage:\n\n    >>> ns_functions = FunctionNamespace("http://schema.org/Movie")\n\n    >>> @ns_functions  # uses function name\n    ... def add2(x):\n    ...     return x + 2\n\n    >>> @ns_functions("add3")  # uses explicit name\n    ... def add_three(x):\n    ...     return x + 3\n    '
    pass

def HTML(text, parser):
    'HTML(text, parser=None, base_url=None)\n\n    Parses an HTML document from a string constant.  Returns the root\n    node (or the result returned by a parser target).  This function\n    can be used to embed "HTML literals" in Python code.\n\n    To override the parser with a different ``HTMLParser`` you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    pass

class HTMLParser(_FeedParser):
    "HTMLParser(self, encoding=None, remove_blank_text=False,                    remove_comments=False, remove_pis=False, strip_cdata=True,                    no_network=True, target=None, schema: XMLSchema =None,                    recover=True, compact=True, collect_ids=True, huge_tree=False)\n\n    The HTML parser.\n\n    This parser allows reading HTML into a normal XML tree.  By\n    default, it can read broken (non well-formed) HTML, depending on\n    the capabilities of libxml2.  Use the 'recover' option to switch\n    this off.\n\n    Available boolean keyword arguments:\n\n    - recover            - try hard to parse through broken HTML (default: True)\n    - no_network         - prevent network access for related files (default: True)\n    - remove_blank_text  - discard empty text nodes that are ignorable (i.e. not actual text content)\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - default_doctype    - add a default doctype even if it is not found in the HTML (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads for performance\n    reasons.\n    "
    __class__ = HTMLParser
    def __init__(self, encoding=None, remove_blank_text=False, remove_comments=False, remove_pis=False, strip_cdata=True, no_network=True, target=None, schema: XMLSchema=None, recover=True, compact=True, collect_ids=True, huge_tree=False):
        "HTMLParser(self, encoding=None, remove_blank_text=False,                    remove_comments=False, remove_pis=False, strip_cdata=True,                    no_network=True, target=None, schema: XMLSchema =None,                    recover=True, compact=True, collect_ids=True, huge_tree=False)\n\n    The HTML parser.\n\n    This parser allows reading HTML into a normal XML tree.  By\n    default, it can read broken (non well-formed) HTML, depending on\n    the capabilities of libxml2.  Use the 'recover' option to switch\n    this off.\n\n    Available boolean keyword arguments:\n\n    - recover            - try hard to parse through broken HTML (default: True)\n    - no_network         - prevent network access for related files (default: True)\n    - remove_blank_text  - discard empty text nodes that are ignorable (i.e. not actual text content)\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - default_doctype    - add a default doctype even if it is not found in the HTML (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads for performance\n    reasons.\n    "
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
    

class HTMLPullParser(HTMLParser):
    "HTMLPullParser(self, events=None, *, tag=None, base_url=None, **kwargs)\n\n    HTML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
    __class__ = HTMLPullParser
    def __init__(self, events=None, *, tag=None, base_url=None, **kwargs):
        "HTMLPullParser(self, events=None, *, tag=None, base_url=None, **kwargs)\n\n    HTML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
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
    
    def read_events(self):
        pass
    

LIBXML_COMPILED_VERSION = _mod_builtins.tuple()
LIBXML_VERSION = _mod_builtins.tuple()
LIBXSLT_COMPILED_VERSION = _mod_builtins.tuple()
LIBXSLT_VERSION = _mod_builtins.tuple()
LXML_VERSION = _mod_builtins.tuple()
class LxmlError(Error):
    'Main exception base class for lxml.  All other exceptions inherit from\n    this one.\n    '
    __class__ = LxmlError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Main exception base class for lxml.  All other exceptions inherit from\n    this one.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class LxmlRegistryError(LxmlError):
    'Base class of lxml registry errors.\n    '
    __class__ = LxmlRegistryError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class of lxml registry errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class LxmlSyntaxError(LxmlError,_mod_builtins.SyntaxError):
    'Base class for all syntax errors.\n    '
    __class__ = LxmlSyntaxError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class for all syntax errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class NamespaceRegistryError(LxmlRegistryError):
    'Error registering a namespace extension.\n    '
    __class__ = NamespaceRegistryError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error registering a namespace extension.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def PI(target, text):
    'ProcessingInstruction(target, text=None)\n\n    ProcessingInstruction element factory. This factory function creates a\n    special element that will be serialized as an XML processing instruction.\n    '
    pass

class PIBase(_ProcessingInstruction):
    'All custom Processing Instruction classes must inherit from this one.\n\n    To create an XML ProcessingInstruction instance, use the ``PI()``\n    factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of PIs must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
    __class__ = PIBase
    def __init__(self, *args, **kwargs):
        'All custom Processing Instruction classes must inherit from this one.\n\n    To create an XML ProcessingInstruction instance, use the ``PI()``\n    factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of PIs must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
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
    

class ParseError(LxmlSyntaxError):
    'Syntax error while parsing an XML document.\n\n    For compatibility with ElementTree 1.3 and later.\n    '
    __class__ = ParseError
    __dict__ = {}
    def __init__(self, message, code, line, column, filename):
        'Syntax error while parsing an XML document.\n\n    For compatibility with ElementTree 1.3 and later.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    position = _mod_builtins.property()

class ParserBasedElementClassLookup(FallbackElementClassLookup):
    'ParserBasedElementClassLookup(self, fallback=None)\n    Element class lookup based on the XML parser.\n    '
    __class__ = ParserBasedElementClassLookup
    def __init__(self, fallback=None):
        'ParserBasedElementClassLookup(self, fallback=None)\n    Element class lookup based on the XML parser.\n    '
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
    

class ParserError(LxmlError):
    'Internal lxml parser error.\n    '
    __class__ = ParserError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Internal lxml parser error.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def ProcessingInstruction(target, text):
    'ProcessingInstruction(target, text=None)\n\n    ProcessingInstruction element factory. This factory function creates a\n    special element that will be serialized as an XML processing instruction.\n    '
    pass

class PyErrorLog(_BaseErrorLog):
    "PyErrorLog(self, logger_name=None, logger=None)\n    A global error log that connects to the Python stdlib logging package.\n\n    The constructor accepts an optional logger name or a readily\n    instantiated logger instance.\n\n    If you want to change the mapping between libxml2's ErrorLevels and Python\n    logging levels, you can modify the level_map dictionary from a subclass.\n\n    The default mapping is::\n\n            ErrorLevels.WARNING = logging.WARNING\n            ErrorLevels.ERROR   = logging.ERROR\n            ErrorLevels.FATAL   = logging.CRITICAL\n\n    You can also override the method ``receive()`` that takes a LogEntry\n    object and calls ``self.log(log_entry, format_string, arg1, arg2, ...)``\n    with appropriate data.\n    "
    __class__ = PyErrorLog
    def __init__(self, logger_name=None, logger=None):
        "PyErrorLog(self, logger_name=None, logger=None)\n    A global error log that connects to the Python stdlib logging package.\n\n    The constructor accepts an optional logger name or a readily\n    instantiated logger instance.\n\n    If you want to change the mapping between libxml2's ErrorLevels and Python\n    logging levels, you can modify the level_map dictionary from a subclass.\n\n    The default mapping is::\n\n            ErrorLevels.WARNING = logging.WARNING\n            ErrorLevels.ERROR   = logging.ERROR\n            ErrorLevels.FATAL   = logging.CRITICAL\n\n    You can also override the method ``receive()`` that takes a LogEntry\n    object and calls ``self.log(log_entry, format_string, arg1, arg2, ...)``\n    with appropriate data.\n    "
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
    
    def copy(self):
        'Dummy method that returns an empty error log.\n        '
        pass
    
    @property
    def level_map(self):
        pass
    
    def log(self, log_entry, message, *args):
        'log(self, log_entry, message, *args)\n\n        Called by the .receive() method to log a _LogEntry instance to\n        the Python logging system.  This handles the error level\n        mapping.\n\n        In the default implementation, the ``message`` argument\n        receives a complete log line, and there are no further\n        ``args``.  To change the message format, it is best to\n        override the .receive() method instead of this one.\n        '
        pass
    
    def receive(self, log_entry):
        'receive(self, log_entry)\n\n        Receive a _LogEntry instance from the logging system.  Calls\n        the .log() method with appropriate parameters::\n\n            self.log(log_entry, repr(log_entry))\n\n        You can override this method to provide your own log output\n        format.\n        '
        pass
    

class PythonElementClassLookup(FallbackElementClassLookup):
    'PythonElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    This class lookup scheme allows access to the entire XML tree in\n    read-only mode.  To use it, re-implement the ``lookup(self, doc,\n    root)`` method in a subclass::\n\n        from lxml import etree, pyclasslookup\n\n        class MyElementClass(etree.ElementBase):\n            honkey = True\n\n        class MyLookup(pyclasslookup.PythonElementClassLookup):\n            def lookup(self, doc, root):\n                if root.tag == "sometag":\n                    return MyElementClass\n                else:\n                    for child in root:\n                        if child.tag == "someothertag":\n                            return MyElementClass\n                # delegate to default\n                return None\n\n    If you return None from this method, the fallback will be called.\n\n    The first argument is the opaque document instance that contains\n    the Element.  The second argument is a lightweight Element proxy\n    implementation that is only valid during the lookup.  Do not try\n    to keep a reference to it.  Once the lookup is done, the proxy\n    will be invalid.\n\n    Also, you cannot wrap such a read-only Element in an ElementTree,\n    and you must take care not to keep a reference to them outside of\n    the `lookup()` method.\n\n    Note that the API of the Element objects is not complete.  It is\n    purely read-only and does not support all features of the normal\n    `lxml.etree` API (such as XPath, extended slicing or some\n    iteration methods).\n\n    See http://codespeak.net/lxml/element_classes.html\n    '
    __class__ = PythonElementClassLookup
    def __init__(self, fallback=None):
        'PythonElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    This class lookup scheme allows access to the entire XML tree in\n    read-only mode.  To use it, re-implement the ``lookup(self, doc,\n    root)`` method in a subclass::\n\n        from lxml import etree, pyclasslookup\n\n        class MyElementClass(etree.ElementBase):\n            honkey = True\n\n        class MyLookup(pyclasslookup.PythonElementClassLookup):\n            def lookup(self, doc, root):\n                if root.tag == "sometag":\n                    return MyElementClass\n                else:\n                    for child in root:\n                        if child.tag == "someothertag":\n                            return MyElementClass\n                # delegate to default\n                return None\n\n    If you return None from this method, the fallback will be called.\n\n    The first argument is the opaque document instance that contains\n    the Element.  The second argument is a lightweight Element proxy\n    implementation that is only valid during the lookup.  Do not try\n    to keep a reference to it.  Once the lookup is done, the proxy\n    will be invalid.\n\n    Also, you cannot wrap such a read-only Element in an ElementTree,\n    and you must take care not to keep a reference to them outside of\n    the `lookup()` method.\n\n    Note that the API of the Element objects is not complete.  It is\n    purely read-only and does not support all features of the normal\n    `lxml.etree` API (such as XPath, extended slicing or some\n    iteration methods).\n\n    See http://codespeak.net/lxml/element_classes.html\n    '
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
    
    def lookup(self, doc, element):
        'lookup(self, doc, element)\n\n        Override this method to implement your own lookup scheme.\n        '
        pass
    

class QName(_mod_builtins.object):
    'QName(text_or_uri_or_element, tag=None)\n\n    QName wrapper for qualified XML names.\n\n    Pass a tag name by itself or a namespace URI and a tag name to\n    create a qualified name.  Alternatively, pass an Element to\n    extract its tag name.  ``None`` as first argument is ignored in\n    order to allow for generic 2-argument usage.\n\n    The ``text`` property holds the qualified name in\n    ``{namespace}tagname`` notation.  The ``namespace`` and\n    ``localname`` properties hold the respective parts of the tag\n    name.\n\n    You can pass QName objects wherever a tag name is expected.  Also,\n    setting Element text from a QName will resolve the namespace prefix\n    on assignment and set a qualified text value.  This is helpful in XML\n    languages like SOAP or XML-Schema that use prefixed tag names in\n    their text content.\n    '
    __class__ = QName
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, text_or_uri_or_element, tag=None):
        'QName(text_or_uri_or_element, tag=None)\n\n    QName wrapper for qualified XML names.\n\n    Pass a tag name by itself or a namespace URI and a tag name to\n    create a qualified name.  Alternatively, pass an Element to\n    extract its tag name.  ``None`` as first argument is ignored in\n    order to allow for generic 2-argument usage.\n\n    The ``text`` property holds the qualified name in\n    ``{namespace}tagname`` notation.  The ``namespace`` and\n    ``localname`` properties hold the respective parts of the tag\n    name.\n\n    You can pass QName objects wherever a tag name is expected.  Also,\n    setting Element text from a QName will resolve the namespace prefix\n    on assignment and set a qualified text value.  This is helpful in XML\n    languages like SOAP or XML-Schema that use prefixed tag names in\n    their text content.\n    '
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
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def localname(self):
        pass
    
    @property
    def namespace(self):
        pass
    
    @property
    def text(self):
        pass
    

class RelaxNG(_Validator):
    'RelaxNG(self, etree=None, file=None)\n    Turn a document into a Relax NG validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n    '
    def __call__(self, etree):
        '__call__(self, etree)\n\n        Validate doc using Relax NG.\n\n        Returns true if document is valid, false if not.'
        pass
    
    __class__ = RelaxNG
    def __init__(self, etree=None, file=None):
        'RelaxNG(self, etree=None, file=None)\n    Turn a document into a Relax NG validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n    '
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
    
    def from_rnc_string(self, cls, src, base_url):
        "Parse a RelaxNG schema in compact syntax from a text string\n\n        Requires the rnc2rng package to be installed.\n\n        Passing the source URL or file path of the source as 'base_url'\n        will enable resolving resource references relative to the source.\n        "
        pass
    

class RelaxNGError(LxmlError):
    'Base class for RelaxNG errors.\n    '
    __class__ = RelaxNGError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class for RelaxNG errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class RelaxNGErrorTypes(_mod_builtins.object):
    'Libxml2 RelaxNG error types'
    RELAXNG_ERR_ATTREXTRANS = 20
    RELAXNG_ERR_ATTRNAME = 14
    RELAXNG_ERR_ATTRNONS = 16
    RELAXNG_ERR_ATTRVALID = 24
    RELAXNG_ERR_ATTRWRONGNS = 18
    RELAXNG_ERR_CONTENTVALID = 25
    RELAXNG_ERR_DATAELEM = 28
    RELAXNG_ERR_DATATYPE = 31
    RELAXNG_ERR_DUPID = 4
    RELAXNG_ERR_ELEMEXTRANS = 19
    RELAXNG_ERR_ELEMNAME = 13
    RELAXNG_ERR_ELEMNONS = 15
    RELAXNG_ERR_ELEMNOTEMPTY = 21
    RELAXNG_ERR_ELEMWRONG = 38
    RELAXNG_ERR_ELEMWRONGNS = 17
    RELAXNG_ERR_EXTRACONTENT = 26
    RELAXNG_ERR_EXTRADATA = 35
    RELAXNG_ERR_INTEREXTRA = 12
    RELAXNG_ERR_INTERNAL = 37
    RELAXNG_ERR_INTERNODATA = 10
    RELAXNG_ERR_INTERSEQ = 11
    RELAXNG_ERR_INVALIDATTR = 27
    RELAXNG_ERR_LACKDATA = 36
    RELAXNG_ERR_LIST = 33
    RELAXNG_ERR_LISTELEM = 30
    RELAXNG_ERR_LISTEMPTY = 9
    RELAXNG_ERR_LISTEXTRA = 8
    RELAXNG_ERR_MEMORY = 1
    RELAXNG_ERR_NODEFINE = 7
    RELAXNG_ERR_NOELEM = 22
    RELAXNG_ERR_NOGRAMMAR = 34
    RELAXNG_ERR_NOSTATE = 6
    RELAXNG_ERR_NOTELEM = 23
    RELAXNG_ERR_TEXTWRONG = 39
    RELAXNG_ERR_TYPE = 2
    RELAXNG_ERR_TYPECMP = 5
    RELAXNG_ERR_TYPEVAL = 3
    RELAXNG_ERR_VALELEM = 29
    RELAXNG_ERR_VALUE = 32
    RELAXNG_OK = 0
    __class__ = RelaxNGErrorTypes
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Libxml2 RelaxNG error types'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.etree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def _getName(cls):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        pass
    
    _names = _mod_builtins.dict()

class RelaxNGParseError(RelaxNGError):
    'Error while parsing an XML document as RelaxNG.\n    '
    __class__ = RelaxNGParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while parsing an XML document as RelaxNG.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class RelaxNGValidateError(RelaxNGError):
    'Error while validating an XML document with a RelaxNG schema.\n    '
    __class__ = RelaxNGValidateError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while validating an XML document with a RelaxNG schema.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Resolver(_mod_builtins.object):
    'This is the base class of all resolvers.'
    __class__ = Resolver
    def __init__(self, *args, **kwargs):
        'This is the base class of all resolvers.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def resolve(self, system_url, public_id, context):
        'resolve(self, system_url, public_id, context)\n\n        Override this method to resolve an external source by\n        ``system_url`` and ``public_id``.  The third argument is an\n        opaque context object.\n\n        Return the result of one of the ``resolve_*()`` methods.\n        '
        pass
    
    def resolve_empty(self, context):
        'resolve_empty(self, context)\n\n        Return an empty input document.\n\n        Pass context as parameter.\n        '
        pass
    
    def resolve_file(self, f, context):
        'resolve_file(self, f, context, base_url=None, close=True)\n\n        Return an open file-like object as input document.\n\n        Pass open file and context as parameters.  You can pass the\n        base URL or filename of the file through the ``base_url``\n        keyword argument.  If the ``close`` flag is True (the\n        default), the file will be closed after reading.\n\n        Note that using ``.resolve_filename()`` is more efficient,\n        especially in threaded environments.\n        '
        pass
    
    def resolve_filename(self, filename, context):
        'resolve_filename(self, filename, context)\n\n        Return the name of a parsable file as input document.\n\n        Pass filename and context as parameters.  You can also pass a\n        URL with an HTTP, FTP or file target.\n        '
        pass
    
    def resolve_string(self, string, context):
        'resolve_string(self, string, context, base_url=None)\n\n        Return a parsable string as input document.\n\n        Pass data string and context as parameters.  You can pass the\n        source URL or filename through the ``base_url`` keyword\n        argument.\n        '
        pass
    

class Schematron(_Validator):
    'Schematron(self, etree=None, file=None)\n    A Schematron validator.\n\n    Pass a root Element or an ElementTree to turn it into a validator.\n    Alternatively, pass a filename as keyword argument \'file\' to parse from\n    the file system.\n\n    Schematron is a less well known, but very powerful schema language.  The main\n    idea is to use the capabilities of XPath to put restrictions on the structure\n    and the content of XML documents.  Here is a simple example::\n\n      >>> schematron = Schematron(XML(\'\'\'\n      ... <schema xmlns="http://www.ascc.net/xml/schematron" >\n      ...   <pattern name="id is the only permited attribute name">\n      ...     <rule context="*">\n      ...       <report test="@*[not(name()=\'id\')]">Attribute\n      ...         <name path="@*[not(name()=\'id\')]"/> is forbidden<name/>\n      ...       </report>\n      ...     </rule>\n      ...   </pattern>\n      ... </schema>\n      ... \'\'\'))\n\n      >>> xml = XML(\'\'\'\n      ... <AAA name="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC color="ccc"/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      0\n\n      >>> xml = XML(\'\'\'\n      ... <AAA id="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      1\n\n    Schematron was added to libxml2 in version 2.6.21.  Before version 2.6.32,\n    however, Schematron lacked support for error reporting other than to stderr.\n    This version is therefore required to retrieve validation warnings and\n    errors in lxml.\n    '
    def __call__(self, etree):
        '__call__(self, etree)\n\n        Validate doc using Schematron.\n\n        Returns true if document is valid, false if not.'
        pass
    
    __class__ = Schematron
    def __init__(self, etree=None, file=None):
        'Schematron(self, etree=None, file=None)\n    A Schematron validator.\n\n    Pass a root Element or an ElementTree to turn it into a validator.\n    Alternatively, pass a filename as keyword argument \'file\' to parse from\n    the file system.\n\n    Schematron is a less well known, but very powerful schema language.  The main\n    idea is to use the capabilities of XPath to put restrictions on the structure\n    and the content of XML documents.  Here is a simple example::\n\n      >>> schematron = Schematron(XML(\'\'\'\n      ... <schema xmlns="http://www.ascc.net/xml/schematron" >\n      ...   <pattern name="id is the only permited attribute name">\n      ...     <rule context="*">\n      ...       <report test="@*[not(name()=\'id\')]">Attribute\n      ...         <name path="@*[not(name()=\'id\')]"/> is forbidden<name/>\n      ...       </report>\n      ...     </rule>\n      ...   </pattern>\n      ... </schema>\n      ... \'\'\'))\n\n      >>> xml = XML(\'\'\'\n      ... <AAA name="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC color="ccc"/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      0\n\n      >>> xml = XML(\'\'\'\n      ... <AAA id="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      1\n\n    Schematron was added to libxml2 in version 2.6.21.  Before version 2.6.32,\n    however, Schematron lacked support for error reporting other than to stderr.\n    This version is therefore required to retrieve validation warnings and\n    errors in lxml.\n    '
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
    

class SchematronError(LxmlError):
    'Base class of all Schematron errors.\n    '
    __class__ = SchematronError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class of all Schematron errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class SchematronParseError(SchematronError):
    'Error while parsing an XML document as Schematron schema.\n    '
    __class__ = SchematronParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while parsing an XML document as Schematron schema.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class SchematronValidateError(SchematronError):
    'Error while validating an XML document with a Schematron schema.\n    '
    __class__ = SchematronValidateError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while validating an XML document with a Schematron schema.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class SerialisationError(LxmlError):
    'A libxml2 error that occurred during serialisation.\n    '
    __class__ = SerialisationError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'A libxml2 error that occurred during serialisation.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class SiblingsIterator(_ElementMatchIterator):
    'SiblingsIterator(self, node, tag=None, preceding=False)\n    Iterates over the siblings of an element.\n\n    You can pass the boolean keyword ``preceding`` to specify the direction.\n    '
    __class__ = SiblingsIterator
    def __init__(self, node, tag=None, preceding=False):
        'SiblingsIterator(self, node, tag=None, preceding=False)\n    Iterates over the siblings of an element.\n\n    You can pass the boolean keyword ``preceding`` to specify the direction.\n    '
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
    

def SubElement(_parent, _tag, attrib, nsmap, **_extra):
    'SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra)\n\n    Subelement factory.  This function creates an element instance, and\n    appends it to an existing element.\n    '
    pass

class TreeBuilder(_SaxParserTarget):
    'TreeBuilder(self, element_factory=None, parser=None)\n    Parser target that builds a tree.\n\n    The final tree is returned by the ``close()`` method.\n    '
    __class__ = TreeBuilder
    def __init__(self, element_factory=None, parser=None):
        'TreeBuilder(self, element_factory=None, parser=None)\n    Parser target that builds a tree.\n\n    The final tree is returned by the ``close()`` method.\n    '
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
    
    def close(self):
        'close(self)\n\n        Flushes the builder buffers, and returns the toplevel document\n        element.\n        '
        pass
    
    def comment(self, comment):
        'comment(self, comment)\n        '
        pass
    
    def data(self, data):
        'data(self, data)\n\n        Adds text to the current element.  The value should be either an\n        8-bit string containing ASCII text, or a Unicode string.\n        '
        pass
    
    def end(self, tag):
        'end(self, tag)\n\n        Closes the current element.\n        '
        pass
    
    def pi(self, target, data):
        'pi(self, target, data)\n        '
        pass
    
    def start(self, tag, attrs, nsmap):
        'start(self, tag, attrs, nsmap=None)\n\n        Opens a new element.\n        '
        pass
    

class XInclude(_mod_builtins.object):
    'XInclude(self)\n    XInclude processor.\n\n    Create an instance and call it on an Element to run XInclude\n    processing.\n    '
    def __call__(self, node):
        '__call__(self, node)'
        pass
    
    __class__ = XInclude
    def __init__(self):
        'XInclude(self)\n    XInclude processor.\n\n    Create an instance and call it on an Element to run XInclude\n    processing.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def error_log(self):
        pass
    

class XIncludeError(LxmlError):
    'Error during XInclude processing.\n    '
    __class__ = XIncludeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error during XInclude processing.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def XML(text, parser):
    'XML(text, parser=None, base_url=None)\n\n    Parses an XML document or fragment from a string constant.\n    Returns the root node (or the result returned by a parser target).\n    This function can be used to embed "XML literals" in Python code,\n    like in\n\n       >>> root = XML("<root><test/></root>")\n       >>> print(root.tag)\n       root\n\n    To override the parser with a different ``XMLParser`` you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    pass

def XMLDTDID(text, parser):
    'XMLDTDID(text, parser=None, base_url=None)\n\n    Parse the text and return a tuple (root node, ID dictionary).  The root\n    node is the same as returned by the XML() function.  The dictionary\n    contains string-element pairs.  The dictionary keys are the values of ID\n    attributes as defined by the DTD.  The elements referenced by the ID are\n    stored as dictionary values.\n\n    Note that you must not modify the XML tree if you use the ID dictionary.\n    The results are undefined.\n    '
    pass

def XMLID(text, parser):
    "XMLID(text, parser=None, base_url=None)\n\n    Parse the text and return a tuple (root node, ID dictionary).  The root\n    node is the same as returned by the XML() function.  The dictionary\n    contains string-element pairs.  The dictionary keys are the values of 'id'\n    attributes.  The elements referenced by the ID are stored as dictionary\n    values.\n    "
    pass

class XMLParser(_FeedParser):
    "XMLParser(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema: XMLSchema =None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True)\n\n    The XML parser.\n\n    Parsers can be supplied as additional argument to various parse\n    functions of the lxml API.  A default parser is always available\n    and can be replaced by a call to the global function\n    'set_default_parser'.  New parsers can be created at any time\n    without a major run-time overhead.\n\n    The keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if DTD\n    validation or attribute default values are requested (unless you\n    additionally provide an XMLSchema from which the default\n    attributes can be read).\n\n    Available boolean keyword arguments:\n\n    - attribute_defaults - inject default attributes from DTD or XMLSchema\n    - dtd_validation     - validate against a DTD referenced by the document\n    - load_dtd           - use DTD for parsing\n    - no_network         - prevent network access for related files (default: True)\n    - ns_clean           - clean up redundant namespace declarations\n    - recover            - try hard to parse through broken XML\n    - remove_blank_text  - discard blank text nodes that appear ignorable\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True, always True with DTD validation)\n    - resolve_entities   - replace entities by their text value (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads.  While this is\n    not harmful, it is more efficient to use separate parsers.  This does not\n    apply to the default parser.\n    "
    __class__ = XMLParser
    def __init__(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema: XMLSchema=None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True):
        "XMLParser(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema: XMLSchema =None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True)\n\n    The XML parser.\n\n    Parsers can be supplied as additional argument to various parse\n    functions of the lxml API.  A default parser is always available\n    and can be replaced by a call to the global function\n    'set_default_parser'.  New parsers can be created at any time\n    without a major run-time overhead.\n\n    The keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if DTD\n    validation or attribute default values are requested (unless you\n    additionally provide an XMLSchema from which the default\n    attributes can be read).\n\n    Available boolean keyword arguments:\n\n    - attribute_defaults - inject default attributes from DTD or XMLSchema\n    - dtd_validation     - validate against a DTD referenced by the document\n    - load_dtd           - use DTD for parsing\n    - no_network         - prevent network access for related files (default: True)\n    - ns_clean           - clean up redundant namespace declarations\n    - recover            - try hard to parse through broken XML\n    - remove_blank_text  - discard blank text nodes that appear ignorable\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True, always True with DTD validation)\n    - resolve_entities   - replace entities by their text value (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads.  While this is\n    not harmful, it is more efficient to use separate parsers.  This does not\n    apply to the default parser.\n    "
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
    

class XMLPullParser(XMLParser):
    "XMLPullParser(self, events=None, *, tag=None, **kwargs)\n\n    XML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
    __class__ = XMLPullParser
    def __init__(self, events=None, *, tag=None, **kwargs):
        "XMLPullParser(self, events=None, *, tag=None, **kwargs)\n\n    XML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
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
    
    def read_events(self):
        pass
    

class XMLSchema(_Validator):
    'XMLSchema(self, etree=None, file=None)\n    Turn a document into an XML Schema validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n\n    Passing the ``attribute_defaults`` boolean option will make the\n    schema insert default/fixed attributes into validated documents.\n    '
    def __call__(self, etree):
        '__call__(self, etree)\n\n        Validate doc using XML Schema.\n\n        Returns true if document is valid, false if not.\n        '
        pass
    
    __class__ = XMLSchema
    def __init__(self, etree=None, file=None):
        'XMLSchema(self, etree=None, file=None)\n    Turn a document into an XML Schema validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n\n    Passing the ``attribute_defaults`` boolean option will make the\n    schema insert default/fixed attributes into validated documents.\n    '
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
    

class XMLSchemaError(LxmlError):
    'Base class of all XML Schema errors\n    '
    __class__ = XMLSchemaError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class of all XML Schema errors\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XMLSchemaParseError(XMLSchemaError):
    'Error while parsing an XML document as XML Schema.\n    '
    __class__ = XMLSchemaParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while parsing an XML document as XML Schema.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XMLSchemaValidateError(XMLSchemaError):
    'Error while validating an XML document with an XML Schema.\n    '
    __class__ = XMLSchemaValidateError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error while validating an XML document with an XML Schema.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XMLSyntaxError(ParseError):
    'Syntax error while parsing an XML document.\n    '
    __class__ = XMLSyntaxError
    __dict__ = {}
    def __init__(self, message, code, line, column, filename):
        'Syntax error while parsing an XML document.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

XMLTreeBuilder = ETCompatXMLParser()
class XPath(_XPathEvaluatorBase):
    "XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    A compiled XPath expression that can be called on Elements and ElementTrees.\n\n    Besides the XPath expression, you can pass prefix-namespace\n    mappings and extension functions to the constructor through the\n    keyword arguments ``namespaces`` and ``extensions``.  EXSLT\n    regular expression support can be disabled with the 'regexp'\n    boolean keyword (defaults to True).  Smart strings will be\n    returned for string results unless you pass\n    ``smart_strings=False``.\n    "
    def __call__(self, _etree_or_element, **_variables):
        '__call__(self, _etree_or_element, **_variables)'
        pass
    
    __class__ = XPath
    def __init__(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True):
        "XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    A compiled XPath expression that can be called on Elements and ElementTrees.\n\n    Besides the XPath expression, you can pass prefix-namespace\n    mappings and extension functions to the constructor through the\n    keyword arguments ``namespaces`` and ``extensions``.  EXSLT\n    regular expression support can be disabled with the 'regexp'\n    boolean keyword (defaults to True).  Smart strings will be\n    returned for string results unless you pass\n    ``smart_strings=False``.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def path(self):
        'The literal XPath expression.\n        '
        pass
    

class XPathDocumentEvaluator(XPathElementEvaluator):
    "XPathDocumentEvaluator(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an ElementTree.\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
    def __call__(self, _path, **_variables):
        '__call__(self, _path, **_variables)\n\n        Evaluate an XPath expression on the document.\n\n        Variables may be provided as keyword arguments.  Note that namespaces\n        are currently not supported for variables.\n        '
        pass
    
    __class__ = XPathDocumentEvaluator
    def __init__(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True):
        "XPathDocumentEvaluator(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an ElementTree.\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
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
    

class XPathElementEvaluator(_XPathEvaluatorBase):
    "XPathElementEvaluator(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an element.\n\n    Absolute XPath expressions (starting with '/') will be evaluated against\n    the ElementTree as returned by getroottree().\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
    def __call__(self, _path, **_variables):
        "__call__(self, _path, **_variables)\n\n        Evaluate an XPath expression on the document.\n\n        Variables may be provided as keyword arguments.  Note that namespaces\n        are currently not supported for variables.\n\n        Absolute XPath expressions (starting with '/') will be evaluated\n        against the ElementTree as returned by getroottree().\n        "
        pass
    
    __class__ = XPathElementEvaluator
    def __init__(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True):
        "XPathElementEvaluator(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an element.\n\n    Absolute XPath expressions (starting with '/') will be evaluated against\n    the ElementTree as returned by getroottree().\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
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
    
    def register_namespace(self, prefix, uri):
        'Register a namespace with the XPath context.\n        '
        pass
    
    def register_namespaces(self, namespaces):
        'Register a prefix -> uri dict.\n        '
        pass
    

class XPathError(LxmlError):
    'Base class of all XPath errors.\n    '
    __class__ = XPathError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class of all XPath errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XPathEvalError(XPathError):
    'Error during XPath evaluation.\n    '
    __class__ = XPathEvalError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error during XPath evaluation.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def XPathEvaluator(etree_or_element):
    "XPathEvaluator(etree_or_element, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n\n    Creates an XPath evaluator for an ElementTree or an Element.\n\n    The resulting object can be called with an XPath expression as argument\n    and XPath variables provided as keyword arguments.\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
    pass

class XPathFunctionError(XPathEvalError):
    'Internal error looking up an XPath extension function.\n    '
    __class__ = XPathFunctionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Internal error looking up an XPath extension function.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XPathResultError(XPathEvalError):
    'Error handling an XPath result.\n    '
    __class__ = XPathResultError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error handling an XPath result.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XPathSyntaxError(LxmlSyntaxError,XPathError):
    __class__ = XPathSyntaxError
    __dict__ = {}
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
    

class XSLT(_mod_builtins.object):
    'XSLT(self, xslt_input, extensions=None, regexp=True, access_control=None)\n\n    Turn an XSL document into an XSLT object.\n\n    Calling this object on a tree or Element will execute the XSLT::\n\n        transform = etree.XSLT(xsl_tree)\n        result = transform(xml_tree)\n\n    Keyword arguments of the constructor:\n\n    - extensions: a dict mapping ``(namespace, name)`` pairs to\n      extension functions or extension elements\n    - regexp: enable exslt regular expression support in XPath\n      (default: True)\n    - access_control: access restrictions for network or file\n      system (see `XSLTAccessControl`)\n\n    Keyword arguments of the XSLT call:\n\n    - profile_run: enable XSLT profiling (default: False)\n\n    Other keyword arguments of the call are passed to the stylesheet\n    as parameters.\n    '
    def __call__(self, _input, profile_run=False, **kw):
        '__call__(self, _input, profile_run=False, **kw)\n\n        Execute the XSL transformation on a tree or Element.\n\n        Pass the ``profile_run`` option to get profile information\n        about the XSLT.  The result of the XSLT will have a property\n        xslt_profile that holds an XML tree with profiling data.\n        '
        pass
    
    __class__ = XSLT
    def __copy__(self):
        pass
    
    def __deepcopy__(self, memo):
        pass
    
    def __init__(self, xslt_input, extensions=None, regexp=True, access_control=None):
        'XSLT(self, xslt_input, extensions=None, regexp=True, access_control=None)\n\n    Turn an XSL document into an XSLT object.\n\n    Calling this object on a tree or Element will execute the XSLT::\n\n        transform = etree.XSLT(xsl_tree)\n        result = transform(xml_tree)\n\n    Keyword arguments of the constructor:\n\n    - extensions: a dict mapping ``(namespace, name)`` pairs to\n      extension functions or extension elements\n    - regexp: enable exslt regular expression support in XPath\n      (default: True)\n    - access_control: access restrictions for network or file\n      system (see `XSLTAccessControl`)\n\n    Keyword arguments of the XSLT call:\n\n    - profile_run: enable XSLT profiling (default: False)\n\n    Other keyword arguments of the call are passed to the stylesheet\n    as parameters.\n    '
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
    
    def apply(self, _input, **kw):
        'apply(self, _input,  profile_run=False, **kw)\n        \n        :deprecated: call the object, not this method.'
        pass
    
    @property
    def error_log(self):
        'The log of errors and warnings of an XSLT execution.'
        pass
    
    def set_global_max_depth(self, max_depth):
        'set_global_max_depth(max_depth)\n\n        The maximum traversal depth that the stylesheet engine will allow.\n        This does not only count the template recursion depth but also takes\n        the number of variables/parameters into account.  The required setting\n        for a run depends on both the stylesheet and the input data.\n\n        Example::\n\n            XSLT.set_global_max_depth(5000)\n\n        Note that this is currently a global, module-wide setting because\n        libxslt does not support it at a per-stylesheet level.\n        '
        pass
    
    def strparam(self, strval):
        'strparam(strval)\n\n        Mark an XSLT string parameter that requires quote escaping\n        before passing it into the transformation.  Use it like this::\n\n            result = transform(doc, some_strval = XSLT.strparam(\n                \'\'\'it\'s "Monty Python\'s" ...\'\'\'))\n\n        Escaped string parameters can be reused without restriction.\n        '
        pass
    
    def tostring(self, result_tree):
        'tostring(self, result_tree)\n\n        Save result doc to string based on stylesheet output method.\n\n        :deprecated: use str(result_tree) instead.\n        '
        pass
    

class XSLTAccessControl(_mod_builtins.object):
    'XSLTAccessControl(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True)\n\n    Access control for XSLT: reading/writing files, directories and\n    network I/O.  Access to a type of resource is granted or denied by\n    passing any of the following boolean keyword arguments.  All of\n    them default to True to allow access.\n\n    - read_file\n    - write_file\n    - create_dir\n    - read_network\n    - write_network\n\n    For convenience, there is also a class member `DENY_ALL` that\n    provides an XSLTAccessControl instance that is readily configured\n    to deny everything, and a `DENY_WRITE` member that denies all\n    write access but allows read access.\n\n    See `XSLT`.\n    '
    DENY_ALL = XSLTAccessControl()
    DENY_WRITE = XSLTAccessControl()
    __class__ = XSLTAccessControl
    def __init__(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True):
        'XSLTAccessControl(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True)\n\n    Access control for XSLT: reading/writing files, directories and\n    network I/O.  Access to a type of resource is granted or denied by\n    passing any of the following boolean keyword arguments.  All of\n    them default to True to allow access.\n\n    - read_file\n    - write_file\n    - create_dir\n    - read_network\n    - write_network\n\n    For convenience, there is also a class member `DENY_ALL` that\n    provides an XSLTAccessControl instance that is readily configured\n    to deny everything, and a `DENY_WRITE` member that denies all\n    write access but allows read access.\n\n    See `XSLT`.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def options(self):
        'The access control configuration as a map of options.'
        pass
    

class XSLTApplyError(XSLTError):
    'Error running an XSL transformation.\n    '
    __class__ = XSLTApplyError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error running an XSL transformation.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XSLTError(LxmlError):
    'Base class of all XSLT errors.\n    '
    __class__ = XSLTError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Base class of all XSLT errors.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XSLTExtension(_mod_builtins.object):
    'Base class of an XSLT extension element.\n    '
    __class__ = XSLTExtension
    def __init__(self, *args, **kwargs):
        'Base class of an XSLT extension element.\n    '
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
    
    def apply_templates(self, context, node, output_parent):
        'apply_templates(self, context, node, output_parent=None, elements_only=False, remove_blank_text=False)\n\n        Call this method to retrieve the result of applying templates\n        to an element.\n\n        The return value is a list of elements or text strings that\n        were generated by the XSLT processor.  If you pass\n        ``elements_only=True``, strings will be discarded from the result\n        list.  The option ``remove_blank_text=True`` will only discard\n        strings that consist entirely of whitespace (e.g. formatting).\n        These options do not apply to Elements, only to bare string results.\n\n        If you pass an Element as `output_parent` parameter, the result\n        will instead be appended to the element (including attributes\n        etc.) and the return value will be `None`.  This is a safe way\n        to generate content into the output document directly, without\n        having to take care of special values like text or attributes.\n        Note that the string discarding options will be ignored in this\n        case.\n        '
        pass
    
    def execute(self, context, self_node, input_node, output_parent):
        'execute(self, context, self_node, input_node, output_parent)\n        Execute this extension element.\n\n        Subclasses must override this method.  They may append\n        elements to the `output_parent` element here, or set its text\n        content.  To this end, the `input_node` provides read-only\n        access to the current node in the input document, and the\n        `self_node` points to the extension element in the stylesheet.\n\n        Note that the `output_parent` parameter may be `None` if there\n        is no parent element in the current context (e.g. no content\n        was added to the output tree yet).\n        '
        pass
    
    def process_children(self, context, output_parent):
        'process_children(self, context, output_parent=None, elements_only=False, remove_blank_text=False)\n\n        Call this method to process the XSLT content of the extension\n        element itself.\n\n        The return value is a list of elements or text strings that\n        were generated by the XSLT processor.  If you pass\n        ``elements_only=True``, strings will be discarded from the result\n        list.  The option ``remove_blank_text=True`` will only discard\n        strings that consist entirely of whitespace (e.g. formatting).\n        These options do not apply to Elements, only to bare string results.\n\n        If you pass an Element as `output_parent` parameter, the result\n        will instead be appended to the element (including attributes\n        etc.) and the return value will be `None`.  This is a safe way\n        to generate content into the output document directly, without\n        having to take care of special values like text or attributes.\n        Note that the string discarding options will be ignored in this\n        case.\n        '
        pass
    

class XSLTExtensionError(XSLTError):
    'Error registering an XSLT extension.\n    '
    __class__ = XSLTExtensionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error registering an XSLT extension.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XSLTParseError(XSLTError):
    'Error parsing a stylesheet document.\n    '
    __class__ = XSLTParseError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error parsing a stylesheet document.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class XSLTSaveError(XSLTError,SerialisationError):
    'Error serialising an XSLT result.\n    '
    __class__ = XSLTSaveError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Error serialising an XSLT result.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class _Attrib(_mod_builtins.object):
    'A dict-like proxy for the ``Element.attrib`` property.\n    '
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = _Attrib
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __copy__(self):
        pass
    
    def __deepcopy__(self, memo):
        pass
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        'A dict-like proxy for the ``Element.attrib`` property.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _Attrib()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        pass
    
    def get(self, key, default):
        pass
    
    def has_key(self, key):
        pass
    
    def items(self):
        pass
    
    def iteritems(self):
        pass
    
    def iterkeys(self):
        pass
    
    def itervalues(self):
        pass
    
    def keys(self):
        pass
    
    def pop(self, key, *default):
        pass
    
    def update(self, sequence_or_dict):
        pass
    
    def values(self):
        pass
    

class _BaseErrorLog(_mod_builtins.object):
    __class__ = _BaseErrorLog
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def copy(self):
        pass
    
    @property
    def last_error(self):
        pass
    
    def receive(self, entry):
        pass
    

class _Comment(__ContentOnlyElement):
    __class__ = _Comment
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def tag(self):
        pass
    

class _Document(_mod_builtins.object):
    'Internal base class to reference a libxml document.\n\n    When instances of this class are garbage collected, the libxml\n    document is cleaned up.\n    '
    __class__ = _Document
    def __init__(self, *args, **kwargs):
        'Internal base class to reference a libxml document.\n\n    When instances of this class are garbage collected, the libxml\n    document is cleaned up.\n    '
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
    

class _DomainErrorLog(_ErrorLog):
    __class__ = _DomainErrorLog
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
    
    def receive(self, entry):
        pass
    

class _Element(_mod_builtins.object):
    'Element class.\n\n    References a document object and a libxml node.\n\n    By pointing to a Document instance, a reference is kept to\n    _Document as long as there is some pointer to a node in it.\n    '
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = _Element
    def __contains__(self, value):
        '__contains__(self, element)'
        return False
    
    def __copy__(self):
        '__copy__(self)'
        pass
    
    def __deepcopy__(self, memo):
        '__deepcopy__(self, memo)'
        pass
    
    def __delitem__(self, x):
        '__delitem__(self, x)\n\n        Deletes the given subelement or a slice.\n        '
        return None
    
    def __getitem__(self, index):
        'Returns the subelement at the given position or the requested\n        slice.\n        '
        pass
    
    def __init__(self, *args, **kwargs):
        'Element class.\n\n    References a document object and a libxml node.\n\n    By pointing to a Document instance, a reference is kept to\n    _Document as long as there is some pointer to a node in it.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        '__iter__(self)'
        return _Element()
    
    def __len__(self):
        '__len__(self)\n\n        Returns the number of subelements.\n        '
        return 0
    
    def __repr__(self):
        '__repr__(self)'
        return ''
    
    def __reversed__(self):
        '__reversed__(self)'
        pass
    
    def __setitem__(self, index, value):
        '__setitem__(self, x, value)\n\n        Replaces the given subelement index or slice.\n        '
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _init(self):
        '_init(self)\n\n        Called after object initialisation.  Custom subclasses may override\n        this if they recursively call _init() in the superclasses.\n        '
        pass
    
    def addnext(self, element):
        'addnext(self, element)\n\n        Adds the element as a following sibling directly after this\n        element.\n\n        This is normally used to set a processing instruction or comment after\n        the root node of a document.  Note that tail text is automatically\n        discarded when adding at the root level.\n        '
        pass
    
    def addprevious(self, element):
        'addprevious(self, element)\n\n        Adds the element as a preceding sibling directly before this\n        element.\n\n        This is normally used to set a processing instruction or comment\n        before the root node of a document.  Note that tail text is\n        automatically discarded when adding at the root level.\n        '
        pass
    
    def append(self, element):
        'append(self, element)\n\n        Adds a subelement to the end of this element.\n        '
        pass
    
    @property
    def attrib(self):
        'Element attribute dictionary. Where possible, use get(), set(),\n        keys(), values() and items() to access element attributes.\n        '
        pass
    
    @property
    def base(self):
        'The base URI of the Element (xml:base or HTML base URL).\n        None if the base URI is unknown.\n\n        Note that the value depends on the URL of the document that\n        holds the Element if there is no xml:base attribute on the\n        Element or its ancestors.\n\n        Setting this property will set an xml:base attribute on the\n        Element, regardless of the document type (XML or HTML).\n        '
        pass
    
    def clear(self):
        'clear(self)\n\n        Resets an element.  This function removes all subelements, clears\n        all attributes and sets the text and tail properties to None.\n        '
        pass
    
    def cssselect(self, expr):
        '\n        Run the CSS expression on this element and its children,\n        returning a list of the results.\n\n        Equivalent to lxml.cssselect.CSSSelect(expr)(self) -- note\n        that pre-compiling the expression can provide a substantial\n        speedup.\n        '
        pass
    
    def extend(self, elements):
        'extend(self, elements)\n\n        Extends the current children by the elements in the iterable.\n        '
        pass
    
    def find(self, path, namespaces):
        'find(self, path, namespaces=None)\n\n        Finds the first matching subelement, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def findall(self, path, namespaces):
        'findall(self, path, namespaces=None)\n\n        Finds all matching subelements, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def findtext(self, path, default, namespaces):
        'findtext(self, path, default=None, namespaces=None)\n\n        Finds text for the first matching subelement, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def get(self, key, default):
        'get(self, key, default=None)\n\n        Gets an element attribute.\n        '
        pass
    
    def getchildren(self):
        'getchildren(self)\n\n        Returns all direct children.  The elements are returned in document\n        order.\n\n        :deprecated: Note that this method has been deprecated as of\n          ElementTree 1.3 and lxml 2.0.  New code should use\n          ``list(element)`` or simply iterate over elements.\n        '
        pass
    
    def getiterator(self, tag, *tags):
        'getiterator(self, tag=None, *tags)\n\n        Returns a sequence or iterator of all elements in the subtree in\n        document order (depth first pre-order), starting with this\n        element.\n\n        Can be restricted to find only elements with specific tags,\n        see `iter`.\n\n        :deprecated: Note that this method is deprecated as of\n          ElementTree 1.3 and lxml 2.0.  It returns an iterator in\n          lxml, which diverges from the original ElementTree\n          behaviour.  If you want an efficient iterator, use the\n          ``element.iter()`` method instead.  You should only use this\n          method in new code if you require backwards compatibility\n          with older versions of lxml or ElementTree.\n        '
        pass
    
    def getnext(self):
        'getnext(self)\n\n        Returns the following sibling of this element or None.\n        '
        pass
    
    def getparent(self):
        'getparent(self)\n\n        Returns the parent of this element or None for the root element.\n        '
        pass
    
    def getprevious(self):
        'getprevious(self)\n\n        Returns the preceding sibling of this element or None.\n        '
        pass
    
    def getroottree(self):
        'getroottree(self)\n\n        Return an ElementTree for the root node of the document that\n        contains this element.\n\n        This is the same as following element.getparent() up the tree until it\n        returns None (for the root element) and then build an ElementTree for\n        the last parent that was returned.'
        pass
    
    def index(self, child, start, stop):
        'index(self, child, start=None, stop=None)\n\n        Find the position of the child within the parent.\n\n        This method is not part of the original ElementTree API.\n        '
        pass
    
    def insert(self, index, element):
        'insert(self, index, element)\n\n        Inserts a subelement at the given position in this element\n        '
        pass
    
    def items(self):
        'items(self)\n\n        Gets element attributes, as a sequence. The attributes are returned in\n        an arbitrary order.\n        '
        pass
    
    def iter(self, tag, *tags):
        'iter(self, tag=None, *tags)\n\n        Iterate over all elements in the subtree in document order (depth\n        first pre-order), starting with this element.\n\n        Can be restricted to find only elements with specific tags:\n        pass ``"{ns}localname"`` as tag. Either or both of ``ns`` and\n        ``localname`` can be ``*`` for a wildcard; ``ns`` can be empty\n        for no namespace. ``"localname"`` is equivalent to ``"{}localname"``\n        (i.e. no namespace) but ``"*"`` is ``"{*}*"`` (any or no namespace),\n        not ``"{}*"``.\n\n        You can also pass the Element, Comment, ProcessingInstruction and\n        Entity factory functions to look only for the specific element type.\n\n        Passing multiple tags (or a sequence of tags) instead of a single tag\n        will let the iterator return all elements matching any of these tags,\n        in document order.\n        '
        pass
    
    def iterancestors(self, tag, *tags):
        'iterancestors(self, tag=None, *tags)\n\n        Iterate over the ancestors of this element (from parent to parent).\n\n        Can be restricted to find only elements with specific tags,\n        see `iter`.\n        '
        pass
    
    def iterchildren(self, tag, *tags):
        "iterchildren(self, tag=None, *tags, reversed=False)\n\n        Iterate over the children of this element.\n\n        As opposed to using normal iteration on this element, the returned\n        elements can be reversed with the 'reversed' keyword and restricted\n        to find only elements with specific tags, see `iter`.\n        "
        pass
    
    def iterdescendants(self, tag, *tags):
        'iterdescendants(self, tag=None, *tags)\n\n        Iterate over the descendants of this element in document order.\n\n        As opposed to ``el.iter()``, this iterator does not yield the element\n        itself.  The returned elements can be restricted to find only elements\n        with specific tags, see `iter`.\n        '
        pass
    
    def iterfind(self, path, namespaces):
        'iterfind(self, path, namespaces=None)\n\n        Iterates over all matching subelements, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def itersiblings(self, tag, *tags):
        "itersiblings(self, tag=None, *tags, preceding=False)\n\n        Iterate over the following or preceding siblings of this element.\n\n        The direction is determined by the 'preceding' keyword which\n        defaults to False, i.e. forward iteration over the following\n        siblings.  When True, the iterator yields the preceding\n        siblings in reverse document order, i.e. starting right before\n        the current element and going backwards.\n\n        Can be restricted to find only elements with specific tags,\n        see `iter`.\n        "
        pass
    
    def itertext(self, tag, *tags):
        'itertext(self, tag=None, *tags, with_tail=True)\n\n        Iterates over the text content of a subtree.\n\n        You can pass tag names to restrict text content to specific elements,\n        see `iter`.\n\n        You can set the ``with_tail`` keyword argument to ``False`` to skip\n        over tail text.\n        '
        pass
    
    def keys(self):
        'keys(self)\n\n        Gets a list of attribute names.  The names are returned in an\n        arbitrary order (just like for an ordinary Python dictionary).\n        '
        pass
    
    def makeelement(self, _tag, attrib, nsmap, **_extra):
        'makeelement(self, _tag, attrib=None, nsmap=None, **_extra)\n\n        Creates a new element associated with the same document.\n        '
        pass
    
    @property
    def nsmap(self):
        'Namespace prefix->URI mapping known in the context of this\n        Element.  This includes all namespace declarations of the\n        parents.\n\n        Note that changing the returned dict has no effect on the Element.\n        '
        pass
    
    @property
    def prefix(self):
        'Namespace prefix or None.\n        '
        pass
    
    def remove(self, element):
        'remove(self, element)\n\n        Removes a matching subelement. Unlike the find methods, this\n        method compares elements based on identity, not on tag value\n        or contents.\n        '
        pass
    
    def replace(self, old_element, new_element):
        'replace(self, old_element, new_element)\n\n        Replaces a subelement with the element passed as second argument.\n        '
        pass
    
    def set(self, key, value):
        'set(self, key, value)\n\n        Sets an element attribute.\n        '
        pass
    
    @property
    def sourceline(self):
        'Original line number as found by the parser or None if unknown.\n        '
        pass
    
    @property
    def tag(self):
        'Element tag\n        '
        pass
    
    @property
    def tail(self):
        "Text after this element's end tag, but before the next sibling\n        element's start tag. This is either a string or the value None, if\n        there was no text.\n        "
        pass
    
    @property
    def text(self):
        'Text before the first subelement. This is either a string or\n        the value None, if there was no text.\n        '
        pass
    
    def values(self):
        'values(self)\n\n        Gets element attribute values as a sequence of strings.  The\n        attributes are returned in an arbitrary order.\n        '
        pass
    
    def xpath(self, _path, **_variables):
        'xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)\n\n        Evaluate an xpath expression using the element as context node.\n        '
        pass
    

class _ElementIterator(_ElementTagMatcher):
    '\n    Dead but public. :)\n    '
    __class__ = _ElementIterator
    def __init__(self, *args, **kwargs):
        '\n    Dead but public. :)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _ElementIterator()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _ElementMatchIterator(_mod_builtins.object):
    __class__ = _ElementMatchIterator
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _ElementMatchIterator()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _ElementStringResult(_mod_builtins.bytes):
    __class__ = _ElementStringResult
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.etree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def fromhex(cls, type, string):
        "Create a bytes object from a string of hexadecimal numbers.\n\nSpaces between two numbers are accepted.\nExample: bytes.fromhex('B9 01EF') -> b'\\\\xb9\\\\x01\\\\xef'."
        pass
    
    def getparent(self):
        pass
    

class _ElementTagMatcher(_mod_builtins.object):
    '\n    Dead but public. :)\n    '
    __class__ = _ElementTagMatcher
    def __init__(self, *args, **kwargs):
        '\n    Dead but public. :)\n    '
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
    

class _ElementTree(_mod_builtins.object):
    __class__ = _ElementTree
    def __copy__(self):
        pass
    
    def __deepcopy__(self, memo):
        pass
    
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
    
    def _setroot(self, root):
        '_setroot(self, root)\n\n        Relocate the ElementTree to a new root node.\n        '
        pass
    
    @property
    def docinfo(self):
        'Information about the document provided by parser and DTD.'
        pass
    
    def find(self, path, namespaces):
        'find(self, path, namespaces=None)\n\n        Finds the first toplevel element with given tag.  Same as\n        ``tree.getroot().find(path)``.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def findall(self, path, namespaces):
        'findall(self, path, namespaces=None)\n\n        Finds all elements matching the ElementPath expression.  Same as\n        getroot().findall(path).\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def findtext(self, path, default, namespaces):
        'findtext(self, path, default=None, namespaces=None)\n\n        Finds the text for the first element matching the ElementPath\n        expression.  Same as getroot().findtext(path)\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def getelementpath(self, element):
        'getelementpath(self, element)\n\n        Returns a structural, absolute ElementPath expression to find the\n        element.  This path can be used in the .find() method to look up\n        the element, provided that the elements along the path and their\n        list of immediate children were not modified in between.\n\n        ElementPath has the advantage over an XPath expression (as returned\n        by the .getpath() method) that it does not require additional prefix\n        declarations.  It is always self-contained.\n        '
        pass
    
    def getiterator(self, tag, *tags):
        'getiterator(self, *tags, tag=None)\n\n        Returns a sequence or iterator of all elements in document order\n        (depth first pre-order), starting with the root element.\n\n        Can be restricted to find only elements with specific tags,\n        see `_Element.iter`.\n\n        :deprecated: Note that this method is deprecated as of\n          ElementTree 1.3 and lxml 2.0.  It returns an iterator in\n          lxml, which diverges from the original ElementTree\n          behaviour.  If you want an efficient iterator, use the\n          ``tree.iter()`` method instead.  You should only use this\n          method in new code if you require backwards compatibility\n          with older versions of lxml or ElementTree.\n        '
        pass
    
    def getpath(self, element):
        'getpath(self, element)\n\n        Returns a structural, absolute XPath expression to find the element.\n\n        For namespaced elements, the expression uses prefixes from the\n        document, which therefore need to be provided in order to make any\n        use of the expression in XPath.\n\n        Also see the method getelementpath(self, element), which returns a\n        self-contained ElementPath expression.\n        '
        pass
    
    def getroot(self):
        'getroot(self)\n\n        Gets the root element for this tree.\n        '
        pass
    
    def iter(self, tag, *tags):
        'iter(self, tag=None, *tags)\n\n        Creates an iterator for the root element.  The iterator loops over\n        all elements in this tree, in document order.  Note that siblings\n        of the root element (comments or processing instructions) are not\n        returned by the iterator.\n\n        Can be restricted to find only elements with specific tags,\n        see `_Element.iter`.\n        '
        pass
    
    def iterfind(self, path, namespaces):
        'iterfind(self, path, namespaces=None)\n\n        Iterates over all elements matching the ElementPath expression.\n        Same as getroot().iterfind(path).\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        pass
    
    def parse(self, source, parser):
        'parse(self, source, parser=None, base_url=None)\n\n        Updates self with the content of source and returns its root\n        '
        pass
    
    @property
    def parser(self):
        'The parser that was used to parse the document in this ElementTree.\n        '
        pass
    
    def relaxng(self, relaxng):
        'relaxng(self, relaxng)\n\n        Validate this document using other document.\n\n        The relaxng argument is a tree that should contain a Relax NG schema.\n\n        Returns True or False, depending on whether validation\n        succeeded.\n\n        Note: if you are going to apply the same Relax NG schema against\n        multiple documents, it is more efficient to use the RelaxNG\n        class directly.\n        '
        pass
    
    def write(self, file):
        'write(self, file, encoding=None, method="xml",\n                  pretty_print=False, xml_declaration=None, with_tail=True,\n                  standalone=None, doctype=None, compression=0,\n                  exclusive=False, with_comments=True, inclusive_ns_prefixes=None)\n\n        Write the tree to a filename, file or file-like object.\n\n        Defaults to ASCII encoding and writing a declaration as needed.\n\n        The keyword argument \'method\' selects the output method:\n        \'xml\', \'html\', \'text\' or \'c14n\'.  Default is \'xml\'.\n\n        The ``exclusive`` and ``with_comments`` arguments are only\n        used with C14N output, where they request exclusive and\n        uncommented C14N serialisation respectively.\n\n        Passing a boolean value to the ``standalone`` option will\n        output an XML declaration with the corresponding\n        ``standalone`` flag.\n\n        The ``doctype`` option allows passing in a plain string that will\n        be serialised before the XML tree.  Note that passing in non\n        well-formed content here will make the XML output non well-formed.\n        Also, an existing doctype in the document tree will not be removed\n        when serialising an ElementTree instance.\n\n        The ``compression`` option enables GZip compression level 1-9.\n\n        The ``inclusive_ns_prefixes`` should be a list of namespace strings\n        (i.e. [\'xs\', \'xsi\']) that will be promoted to the top-level element\n        during exclusive C14N serialisation.  This parameter is ignored if\n        exclusive mode=False.\n\n        If exclusive=True and no list is provided, a namespace will only be\n        rendered if it is used by the immediate parent or one of its attributes\n        and its prefix and values have not already been rendered by an ancestor\n        of the namespace node\'s parent element.\n        '
        pass
    
    def write_c14n(self, file):
        "write_c14n(self, file, exclusive=False, with_comments=True,\n                       compression=0, inclusive_ns_prefixes=None)\n\n        C14N write of document. Always writes UTF-8.\n\n        The ``compression`` option enables GZip compression level 1-9.\n\n        The ``inclusive_ns_prefixes`` should be a list of namespace strings\n        (i.e. ['xs', 'xsi']) that will be promoted to the top-level element\n        during exclusive C14N serialisation.  This parameter is ignored if\n        exclusive mode=False.\n\n        If exclusive=True and no list is provided, a namespace will only be\n        rendered if it is used by the immediate parent or one of its attributes\n        and its prefix and values have not already been rendered by an ancestor\n        of the namespace node's parent element.\n        "
        pass
    
    def xinclude(self):
        'xinclude(self)\n\n        Process the XInclude nodes in this document and include the\n        referenced XML fragments.\n\n        There is support for loading files through the file system, HTTP and\n        FTP.\n\n        Note that XInclude does not support custom resolvers in Python space\n        due to restrictions of libxml2 <= 2.6.29.\n        '
        pass
    
    def xmlschema(self, xmlschema):
        'xmlschema(self, xmlschema)\n\n        Validate this document using other document.\n\n        The xmlschema argument is a tree that should contain an XML Schema.\n\n        Returns True or False, depending on whether validation\n        succeeded.\n\n        Note: If you are going to apply the same XML Schema against\n        multiple documents, it is more efficient to use the XMLSchema\n        class directly.\n        '
        pass
    
    def xpath(self, _path, **_variables):
        'xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)\n\n        XPath evaluate in context of document.\n\n        ``namespaces`` is an optional dictionary with prefix to namespace URI\n        mappings, used by XPath.  ``extensions`` defines additional extension\n        functions.\n\n        Returns a list (nodeset), or bool, float or string.\n\n        In case of a list result, return Element for element nodes,\n        string for text and attribute values.\n\n        Note: if you are going to apply multiple XPath expressions\n        against the same document, it is more efficient to use\n        XPathEvaluator directly.\n        '
        pass
    
    def xslt(self, _xslt, extensions, access_control, **_kw):
        'xslt(self, _xslt, extensions=None, access_control=None, **_kw)\n\n        Transform this document using other document.\n\n        xslt is a tree that should be XSLT\n        keyword parameters are XSLT transformation parameters.\n\n        Returns the transformed tree.\n\n        Note: if you are going to apply the same XSLT stylesheet against\n        multiple documents, it is more efficient to use the XSLT\n        class directly.\n        '
        pass
    

class _ElementUnicodeResult(_mod_builtins.str):
    __class__ = _ElementUnicodeResult
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
    
    @property
    def attrname(self):
        pass
    
    def getparent(self):
        pass
    
    @property
    def is_attribute(self):
        pass
    
    @property
    def is_tail(self):
        pass
    
    @property
    def is_text(self):
        pass
    

class _Entity(__ContentOnlyElement):
    __class__ = _Entity
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def name(self):
        pass
    
    @property
    def tag(self):
        pass
    
    @property
    def text(self):
        pass
    

class _ErrorLog(_ListErrorLog):
    __class__ = _ErrorLog
    def __exit__(self, *args):
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _ErrorLog()
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def clear(self):
        pass
    
    def copy(self):
        'Creates a shallow copy of this error log and the list of entries.\n        '
        pass
    
    def receive(self, entry):
        pass
    

class _FeedParser(_BaseParser):
    __class__ = _FeedParser
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
    
    def close(self):
        'close(self)\n\n        Terminates feeding data to this parser.  This tells the parser to\n        process any remaining data in the feed buffer, and then returns the\n        root Element of the tree that was parsed.\n\n        This method must be called after passing the last chunk of data into\n        the ``feed()`` method.  It should only be called when using the feed\n        parser interface, all other usage is undefined.\n        '
        pass
    
    def feed(self, data):
        'feed(self, data)\n\n        Feeds data to the parser.  The argument should be an 8-bit string\n        buffer containing encoded data, although Unicode is supported as long\n        as both string types are not mixed.\n\n        This is the main entry point to the consumer interface of a\n        parser.  The parser will parse as much of the XML stream as it\n        can on each call.  To finish parsing or to reset the parser,\n        call the ``close()`` method.  Both methods may raise\n        ParseError if errors occur in the input data.  If an error is\n        raised, there is no longer a need to call ``close()``.\n\n        The feed parser interface is independent of the normal parser\n        usage.  You can use the same parser as a feed parser and in\n        the ``parse()`` function concurrently.\n        '
        pass
    
    @property
    def feed_error_log(self):
        'The error log of the last (or current) run of the feed parser.\n\n        Note that this is local to the feed parser and thus is\n        different from what the ``error_log`` property returns.\n        '
        pass
    

class _IDDict(_mod_builtins.object):
    "IDDict(self, etree)\n    A dictionary-like proxy class that mapps ID attributes to elements.\n\n    The dictionary must be instantiated with the root element of a parsed XML\n    document, otherwise the behaviour is undefined.  Elements and XML trees\n    that were created or modified 'by hand' are not supported.\n    "
    __class__ = _IDDict
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, etree):
        "IDDict(self, etree)\n    A dictionary-like proxy class that mapps ID attributes to elements.\n\n    The dictionary must be instantiated with the root element of a parsed XML\n    document, otherwise the behaviour is undefined.  Elements and XML trees\n    that were created or modified 'by hand' are not supported.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _IDDict()
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def copy(self):
        pass
    
    def get(self, id_name):
        pass
    
    def has_key(self, id_name):
        pass
    
    def items(self):
        pass
    
    def iteritems(self):
        pass
    
    def iterkeys(self):
        pass
    
    def itervalues(self):
        pass
    
    def keys(self):
        pass
    
    def values(self):
        pass
    

class _ListErrorLog(_BaseErrorLog):
    'Immutable base version of a list based error log.'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = _ListErrorLog
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'Immutable base version of a list based error log.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return _ListErrorLog()
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def copy(self):
        'Creates a shallow copy of this error log.  Reuses the list of\n        entries.\n        '
        pass
    
    def filter_domains(self, domains):
        'Filter the errors by the given domains and return a new error log\n        containing the matches.\n        '
        pass
    
    def filter_from_errors(self):
        'filter_from_errors(self)\n\n        Convenience method to get all error messages or worse.\n        '
        pass
    
    def filter_from_fatals(self):
        'filter_from_fatals(self)\n\n        Convenience method to get all fatal error messages.\n        '
        pass
    
    def filter_from_level(self, level):
        'filter_from_level(self, level)\n\n        Return a log with all messages of the requested level of worse.\n        '
        pass
    
    def filter_from_warnings(self):
        'filter_from_warnings(self)\n\n        Convenience method to get all warnings or worse.\n        '
        pass
    
    def filter_levels(self, levels):
        'filter_levels(self, levels)\n\n        Filter the errors by the given error levels and return a new\n        error log containing the matches.\n        '
        pass
    
    def filter_types(self, types):
        'filter_types(self, types)\n\n        Filter the errors by the given types and return a new error\n        log containing the matches.\n        '
        pass
    

class _LogEntry(_mod_builtins.object):
    'A log message entry from an error log.\n\n    Attributes:\n\n    - message: the message text\n    - domain: the domain ID (see lxml.etree.ErrorDomains)\n    - type: the message type ID (see lxml.etree.ErrorTypes)\n    - level: the log level ID (see lxml.etree.ErrorLevels)\n    - line: the line at which the message originated (if applicable)\n    - column: the character column at which the message originated (if applicable)\n    - filename: the name of the file in which the message originated (if applicable)\n    - path: the location in which the error was found (if available)\n    '
    __class__ = _LogEntry
    def __init__(self, *args, **kwargs):
        'A log message entry from an error log.\n\n    Attributes:\n\n    - message: the message text\n    - domain: the domain ID (see lxml.etree.ErrorDomains)\n    - type: the message type ID (see lxml.etree.ErrorTypes)\n    - level: the log level ID (see lxml.etree.ErrorLevels)\n    - line: the line at which the message originated (if applicable)\n    - column: the character column at which the message originated (if applicable)\n    - filename: the name of the file in which the message originated (if applicable)\n    - path: the location in which the error was found (if available)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def column(self):
        pass
    
    @property
    def domain(self):
        pass
    
    @property
    def domain_name(self):
        'The name of the error domain.  See lxml.etree.ErrorDomains\n        '
        pass
    
    @property
    def filename(self):
        'The file path where the report originated, if any.\n        '
        pass
    
    @property
    def level(self):
        pass
    
    @property
    def level_name(self):
        'The name of the error level.  See lxml.etree.ErrorLevels\n        '
        pass
    
    @property
    def line(self):
        pass
    
    @property
    def message(self):
        'The log message string.\n        '
        pass
    
    @property
    def path(self):
        'The XPath for the node where the error was detected.\n        '
        pass
    
    @property
    def type(self):
        pass
    
    @property
    def type_name(self):
        'The name of the error type.  See lxml.etree.ErrorTypes\n        '
        pass
    

class _ProcessingInstruction(__ContentOnlyElement):
    __class__ = _ProcessingInstruction
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def attrib(self):
        'Returns a dict containing all pseudo-attributes that can be\n        parsed from the text content of this processing instruction.\n        Note that modifying the dict currently has no effect on the\n        XML node, although this is not guaranteed to stay this way.\n        '
        pass
    
    def get(self, key, default):
        'get(self, key, default=None)\n\n        Try to parse pseudo-attributes from the text content of the\n        processing instruction, search for one with the given key as\n        name and return its associated value.\n\n        Note that this is only a convenience method for the most\n        common case that all text content is structured in\n        attribute-like name-value pairs with properly quoted values.\n        It is not guaranteed to work for all possible text content.\n        '
        pass
    
    @property
    def tag(self):
        pass
    
    @property
    def target(self):
        pass
    

class _RotatingErrorLog(_ErrorLog):
    __class__ = _RotatingErrorLog
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
    
    def receive(self, entry):
        pass
    

class _SaxParserTarget(_mod_builtins.object):
    __class__ = _SaxParserTarget
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
    

class _TargetParserResult(_mod_builtins.Exception):
    __class__ = _TargetParserResult
    __dict__ = {}
    def __init__(self, result):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'lxml.etree'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class _Validator(_mod_builtins.object):
    'Base class for XML validators.'
    __class__ = _Validator
    def __init__(self, *args, **kwargs):
        'Base class for XML validators.'
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
    
    def _append_log_message(self, domain, type, level, line, message, filename):
        pass
    
    def _clear_error_log(self):
        pass
    
    def assertValid(self, etree):
        'assertValid(self, etree)\n\n        Raises `DocumentInvalid` if the document does not comply with the schema.\n        '
        pass
    
    def assert_(self, etree):
        'assert_(self, etree)\n\n        Raises `AssertionError` if the document does not comply with the schema.\n        '
        pass
    
    @property
    def error_log(self):
        'The log of validation errors and warnings.'
        pass
    
    def validate(self, etree):
        'validate(self, etree)\n\n        Validate the document using this schema.\n\n        Returns true if document is valid, false if not.\n        '
        pass
    

class _XPathEvaluatorBase(_mod_builtins.object):
    __class__ = _XPathEvaluatorBase
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
    def error_log(self):
        pass
    
    def evaluate(self, _eval_arg, **_variables):
        'evaluate(self, _eval_arg, **_variables)\n\n        Evaluate an XPath expression.\n\n        Instead of calling this method, you can also call the evaluator object\n        itself.\n\n        Variables may be provided as keyword arguments.  Note that namespaces\n        are currently not supported for variables.\n\n        :deprecated: call the object, not its method.\n        '
        pass
    

class _XSLTProcessingInstruction(PIBase):
    __class__ = _XSLTProcessingInstruction
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
    
    def parseXSL(self, parser):
        'parseXSL(self, parser=None)\n\n        Try to parse the stylesheet referenced by this PI and return\n        an ElementTree for it.  If the stylesheet is embedded in the\n        same document (referenced via xml:id), find and return an\n        ElementTree for the stylesheet Element.\n\n        The optional ``parser`` keyword argument can be passed to specify the\n        parser used to read from external stylesheet URLs.\n        '
        pass
    
    def set(self, key, value):
        "set(self, key, value)\n\n        Supports setting the 'href' pseudo-attribute in the text of\n        the processing instruction.\n        "
        pass
    

class _XSLTResultTree(_ElementTree):
    'The result of an XSLT evaluation.\n\n    Use ``str()`` or ``bytes()`` (or ``unicode()`` in Python 2.x) to serialise to a string,\n    and the ``.write_output()`` method to write serialise to a file.\n    '
    __class__ = _XSLTResultTree
    def __init__(self, *args, **kwargs):
        'The result of an XSLT evaluation.\n\n    Use ``str()`` or ``bytes()`` (or ``unicode()`` in Python 2.x) to serialise to a string,\n    and the ``.write_output()`` method to write serialise to a file.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    def write_output(self, file):
        'write_output(self, file, *, compression=0)\n\n        Serialise the XSLT output to a file or file-like object.\n\n        As opposed to the generic ``.write()`` method, ``.write_output()`` serialises\n        the result as defined by the ``<xsl:output>`` tag.\n        '
        pass
    
    @property
    def xslt_profile(self):
        'Return an ElementTree with profiling data for the stylesheet run.\n        '
        pass
    

__all__ = _mod_builtins.list()
__builtins__ = {}
__doc__ = '\nThe ``lxml.etree`` module implements the extended ElementTree API for XML.\n'
__docformat__ = 'restructuredtext en'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/lxml/etree.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'lxml.etree'
__package__ = 'lxml'
__pyx_capi__ = _mod_builtins.dict()
__test__ = _mod_builtins.dict()
__version__ = '4.3.2'
def adopt_external_document(capsule, parser):
    'adopt_external_document(capsule, parser=None)\n\n    Unpack a libxml2 document pointer from a PyCapsule and wrap it in an\n    lxml ElementTree object.\n\n    This allows external libraries to build XML/HTML trees using libxml2\n    and then pass them efficiently into lxml for further processing.\n\n    If a ``parser`` is provided, it will be used for configuring the\n    lxml document.  No parsing will be done.\n\n    The capsule must have the name ``"libxml2:xmlDoc"`` and its pointer\n    value must reference a correct libxml2 document of type ``xmlDoc*``.\n    The creator of the capsule must take care to correctly clean up the\n    document using an appropriate capsule destructor.  By default, the\n    libxml2 document will be copied to let lxml safely own the memory\n    of the internal tree that it uses.\n\n    If the capsule context is non-NULL, it must point to a C string that\n    can be compared using ``strcmp()``.  If the context string equals\n    ``"destructor:xmlFreeDoc"``, the libxml2 document will not be copied\n    but the capsule invalidated instead by clearing its destructor and\n    name.  That way, lxml takes ownership of the libxml2 document in memory\n    without creating a copy first, and the capsule destructor will not be\n    called.  The document will then eventually be cleaned up by lxml using\n    the libxml2 API function ``xmlFreeDoc()`` once it is no longer used.\n\n    If no copy is made, later modifications of the tree outside of lxml\n    should not be attempted after transferring the ownership.\n    '
    pass

def cleanup_namespaces(tree_or_element, top_nsmap, keep_ns_prefixes):
    "cleanup_namespaces(tree_or_element, top_nsmap=None, keep_ns_prefixes=None)\n\n    Remove all namespace declarations from a subtree that are not used\n    by any of the elements or attributes in that tree.\n\n    If a 'top_nsmap' is provided, it must be a mapping from prefixes\n    to namespace URIs.  These namespaces will be declared on the top\n    element of the subtree before running the cleanup, which allows\n    moving namespace declarations to the top of the tree.\n\n    If a 'keep_ns_prefixes' is provided, it must be a list of prefixes.\n    These prefixes will not be removed as part of the cleanup.\n    "
    pass

def clear_error_log():
    'clear_error_log()\n\n    Clear the global error log.  Note that this log is already bound to a\n    fixed size.\n\n    Note: since lxml 2.2, the global error log is local to a thread\n    and this function will only clear the global error log of the\n    current thread.\n    '
    pass

def dump(elem):
    'dump(elem, pretty_print=True, with_tail=True)\n\n    Writes an element tree or element structure to sys.stdout. This function\n    should be used for debugging only.\n    '
    pass

def fromstring(text, parser):
    'fromstring(text, parser=None, base_url=None)\n\n    Parses an XML document or fragment from a string.  Returns the\n    root node (or the result returned by a parser target).\n\n    To override the default parser with a different parser you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    pass

def fromstringlist(strings, parser):
    'fromstringlist(strings, parser=None)\n\n    Parses an XML document from a sequence of strings.  Returns the\n    root node (or the result returned by a parser target).\n\n    To override the default parser with a different parser you can pass it to\n    the ``parser`` keyword argument.\n    '
    pass

def get_default_parser():
    'get_default_parser()'
    pass

class htmlfile(xmlfile):
    'htmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental HTML serialisation.  Works the same as\n    xmlfile.\n    '
    __class__ = htmlfile
    def __init__(self, output_file, encoding=None, compression=None, close=False, buffered=True):
        'htmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental HTML serialisation.  Works the same as\n    xmlfile.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def iselement(element):
    'iselement(element)\n\n    Checks if an object appears to be a valid element object.\n    '
    pass

class iterparse(_mod_builtins.object):
    'iterparse(self, source, events=("end",), tag=None,                   attribute_defaults=False, dtd_validation=False,                   load_dtd=False, no_network=True, remove_blank_text=False,                   remove_comments=False, remove_pis=False, encoding=None,                   html=False, recover=None, huge_tree=False, schema=None)\n\n    Incremental parser.\n\n    Parses XML into a tree and generates tuples (event, element) in a\n    SAX-like fashion. ``event`` is any of \'start\', \'end\', \'start-ns\',\n    \'end-ns\'.\n\n    For \'start\' and \'end\', ``element`` is the Element that the parser just\n    found opening or closing.  For \'start-ns\', it is a tuple (prefix, URI) of\n    a new namespace declaration.  For \'end-ns\', it is simply None.  Note that\n    all start and end events are guaranteed to be properly nested.\n\n    The keyword argument ``events`` specifies a sequence of event type names\n    that should be generated.  By default, only \'end\' events will be\n    generated.\n\n    The additional ``tag`` argument restricts the \'start\' and \'end\' events to\n    those elements that match the given tag.  The ``tag`` argument can also be\n    a sequence of tags to allow matching more than one tag.  By default,\n    events are generated for all elements.  Note that the \'start-ns\' and\n    \'end-ns\' events are not impacted by this restriction.\n\n    The other keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if validation or\n    attribute default values are requested.\n\n    Available boolean keyword arguments:\n     - attribute_defaults: read default attributes from DTD\n     - dtd_validation: validate (if DTD is available)\n     - load_dtd: use DTD for parsing\n     - no_network: prevent network access for related files\n     - remove_blank_text: discard blank text nodes\n     - remove_comments: discard comments\n     - remove_pis: discard processing instructions\n     - strip_cdata: replace CDATA sections by normal text content (default: True)\n     - compact: safe memory for short text content (default: True)\n     - resolve_entities: replace entities by their text value (default: True)\n     - huge_tree: disable security restrictions and support very deep trees\n                  and very long text content (only affects libxml2 2.7+)\n     - html: parse input as HTML (default: XML)\n     - recover: try hard to parse through broken input (default: True for HTML,\n                False otherwise)\n\n    Other keyword arguments:\n     - encoding: override the document encoding\n     - schema: an XMLSchema to validate against\n    '
    __class__ = iterparse
    def __init__(self, source, events=("end",), tag=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, remove_blank_text=False, remove_comments=False, remove_pis=False, encoding=None, html=False, recover=None, huge_tree=False, schema=None):
        'iterparse(self, source, events=("end",), tag=None,                   attribute_defaults=False, dtd_validation=False,                   load_dtd=False, no_network=True, remove_blank_text=False,                   remove_comments=False, remove_pis=False, encoding=None,                   html=False, recover=None, huge_tree=False, schema=None)\n\n    Incremental parser.\n\n    Parses XML into a tree and generates tuples (event, element) in a\n    SAX-like fashion. ``event`` is any of \'start\', \'end\', \'start-ns\',\n    \'end-ns\'.\n\n    For \'start\' and \'end\', ``element`` is the Element that the parser just\n    found opening or closing.  For \'start-ns\', it is a tuple (prefix, URI) of\n    a new namespace declaration.  For \'end-ns\', it is simply None.  Note that\n    all start and end events are guaranteed to be properly nested.\n\n    The keyword argument ``events`` specifies a sequence of event type names\n    that should be generated.  By default, only \'end\' events will be\n    generated.\n\n    The additional ``tag`` argument restricts the \'start\' and \'end\' events to\n    those elements that match the given tag.  The ``tag`` argument can also be\n    a sequence of tags to allow matching more than one tag.  By default,\n    events are generated for all elements.  Note that the \'start-ns\' and\n    \'end-ns\' events are not impacted by this restriction.\n\n    The other keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if validation or\n    attribute default values are requested.\n\n    Available boolean keyword arguments:\n     - attribute_defaults: read default attributes from DTD\n     - dtd_validation: validate (if DTD is available)\n     - load_dtd: use DTD for parsing\n     - no_network: prevent network access for related files\n     - remove_blank_text: discard blank text nodes\n     - remove_comments: discard comments\n     - remove_pis: discard processing instructions\n     - strip_cdata: replace CDATA sections by normal text content (default: True)\n     - compact: safe memory for short text content (default: True)\n     - resolve_entities: replace entities by their text value (default: True)\n     - huge_tree: disable security restrictions and support very deep trees\n                  and very long text content (only affects libxml2 2.7+)\n     - html: parse input as HTML (default: XML)\n     - recover: try hard to parse through broken input (default: True for HTML,\n                False otherwise)\n\n    Other keyword arguments:\n     - encoding: override the document encoding\n     - schema: an XMLSchema to validate against\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return iterparse()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def error_log(self):
        'The error log of the last (or current) parser run.\n        '
        pass
    
    def makeelement(self, _tag, attrib, nsmap, **_extra):
        'makeelement(self, _tag, attrib=None, nsmap=None, **_extra)\n\n        Creates a new element associated with this parser.\n        '
        pass
    
    @property
    def resolvers(self):
        'The custom resolver registry of the last (or current) parser run.\n        '
        pass
    
    @property
    def root(self):
        pass
    
    def set_element_class_lookup(self, lookup):
        'set_element_class_lookup(self, lookup = None)\n\n        Set a lookup scheme for element classes generated from this parser.\n\n        Reset it by passing None or nothing.\n        '
        pass
    
    @property
    def version(self):
        'The version of the underlying XML parser.'
        pass
    

class iterwalk(_mod_builtins.object):
    'iterwalk(self, element_or_tree, events=("end",), tag=None)\n\n    A tree walker that generates events from an existing tree as if it\n    was parsing XML data with ``iterparse()``.\n\n    Just as for ``iterparse()``, the ``tag`` argument can be a single tag or a\n    sequence of tags.\n\n    After receiving a \'start\' or \'start-ns\' event, the children and\n    descendants of the current element can be excluded from iteration\n    by calling the ``skip_subtree()`` method.\n    '
    __class__ = iterwalk
    def __init__(self, element_or_tree, events=("end",), tag=None):
        'iterwalk(self, element_or_tree, events=("end",), tag=None)\n\n    A tree walker that generates events from an existing tree as if it\n    was parsing XML data with ``iterparse()``.\n\n    Just as for ``iterparse()``, the ``tag`` argument can be a single tag or a\n    sequence of tags.\n\n    After receiving a \'start\' or \'start-ns\' event, the children and\n    descendants of the current element can be excluded from iteration\n    by calling the ``skip_subtree()`` method.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return iterwalk()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def skip_subtree(self):
        "Prevent descending into the current subtree.\n        Instead, the next returned event will be the 'end' event of the current element\n        (if included), ignoring any children or descendants.\n\n        This has no effect right after an 'end' or 'end-ns' event.\n        "
        pass
    

memory_debugger = _MemDebug()
def parse(source, parser):
    'parse(source, parser=None, base_url=None)\n\n    Return an ElementTree object loaded with source elements.  If no parser\n    is provided as second argument, the default parser is used.\n\n    The ``source`` can be any of the following:\n\n    - a file name/path\n    - a file object\n    - a file-like object\n    - a URL using the HTTP or FTP protocol\n\n    To parse from a string, use the ``fromstring()`` function instead.\n\n    Note that it is generally faster to parse from a file path or URL\n    than from an open file object or file-like object.  Transparent\n    decompression from gzip compressed sources is supported (unless\n    explicitly disabled in libxml2).\n\n    The ``base_url`` keyword allows setting a URL for the document\n    when parsing from a file-like object.  This is needed when looking\n    up external entities (DTD, XInclude, ...) with relative paths.\n    '
    pass

def parseid(source, parser):
    'parseid(source, parser=None)\n\n    Parses the source into a tuple containing an ElementTree object and an\n    ID dictionary.  If no parser is provided as second argument, the default\n    parser is used.\n\n    Note that you must not modify the XML tree if you use the ID dictionary.\n    The results are undefined.\n    '
    pass

def register_namespace(prefix, uri):
    'Registers a namespace prefix that newly created Elements in that\n    namespace will use.  The registry is global, and any existing\n    mapping for either the given prefix or the namespace URI will be\n    removed.\n    '
    pass

def set_default_parser(parser):
    'set_default_parser(parser=None)\n\n    Set a default parser for the current thread.  This parser is used\n    globally whenever no parser is supplied to the various parse functions of\n    the lxml API.  If this function is called without a parser (or if it is\n    None), the default parser is reset to the original configuration.\n\n    Note that the pre-installed default parser is not thread-safe.  Avoid the\n    default parser in multi-threaded environments.  You can create a separate\n    parser for each thread explicitly or use a parser pool.\n    '
    pass

def set_element_class_lookup(lookup):
    'set_element_class_lookup(lookup = None)\n\n    Set the global default element class lookup method.\n    '
    pass

def strip_attributes(tree_or_element, *attribute_names):
    "strip_attributes(tree_or_element, *attribute_names)\n\n    Delete all attributes with the provided attribute names from an\n    Element (or ElementTree) and its descendants.\n\n    Attribute names can contain wildcards as in `_Element.iter`.\n\n    Example usage::\n\n        strip_attributes(root_element,\n                         'simpleattr',\n                         '{http://some/ns}attrname',\n                         '{http://other/ns}*')\n    "
    pass

def strip_elements(tree_or_element, *tag_names):
    "strip_elements(tree_or_element, *tag_names, with_tail=True)\n\n    Delete all elements with the provided tag names from a tree or\n    subtree.  This will remove the elements and their entire subtree,\n    including all their attributes, text content and descendants.  It\n    will also remove the tail text of the element unless you\n    explicitly set the ``with_tail`` keyword argument option to False.\n\n    Tag names can contain wildcards as in `_Element.iter`.\n\n    Note that this will not delete the element (or ElementTree root\n    element) that you passed even if it matches.  It will only treat\n    its descendants.  If you want to include the root element, check\n    its tag name directly before even calling this function.\n\n    Example usage::\n\n        strip_elements(some_element,\n            'simpletagname',             # non-namespaced tag\n            '{http://some/ns}tagname',   # namespaced tag\n            '{http://some/other/ns}*'    # any tag from a namespace\n            lxml.etree.Comment           # comments\n            )\n    "
    pass

def strip_tags(tree_or_element, *tag_names):
    "strip_tags(tree_or_element, *tag_names)\n\n    Delete all elements with the provided tag names from a tree or\n    subtree.  This will remove the elements and their attributes, but\n    *not* their text/tail content or descendants.  Instead, it will\n    merge the text content and children of the element into its\n    parent.\n\n    Tag names can contain wildcards as in `_Element.iter`.\n\n    Note that this will not delete the element (or ElementTree root\n    element) that you passed even if it matches.  It will only treat\n    its descendants.\n\n    Example usage::\n\n        strip_tags(some_element,\n            'simpletagname',             # non-namespaced tag\n            '{http://some/ns}tagname',   # namespaced tag\n            '{http://some/other/ns}*'    # any tag from a namespace\n            Comment                      # comments (including their text!)\n            )\n    "
    pass

def tostring(element_or_tree):
    'tostring(element_or_tree, encoding=None, method="xml",\n                 xml_declaration=None, pretty_print=False, with_tail=True,\n                 standalone=None, doctype=None,\n                 exclusive=False, with_comments=True, inclusive_ns_prefixes=None)\n\n    Serialize an element to an encoded string representation of its XML\n    tree.\n\n    Defaults to ASCII encoding without XML declaration.  This\n    behaviour can be configured with the keyword arguments \'encoding\'\n    (string) and \'xml_declaration\' (bool).  Note that changing the\n    encoding to a non UTF-8 compatible encoding will enable a\n    declaration by default.\n\n    You can also serialise to a Unicode string without declaration by\n    passing the name ``\'unicode\'`` as encoding (or the ``str`` function\n    in Py3 or ``unicode`` in Py2).  This changes the return value from\n    a byte string to an unencoded unicode string.\n\n    The keyword argument \'pretty_print\' (bool) enables formatted XML.\n\n    The keyword argument \'method\' selects the output method: \'xml\',\n    \'html\', plain \'text\' (text content without tags) or \'c14n\'.\n    Default is \'xml\'.\n\n    The ``exclusive`` and ``with_comments`` arguments are only used\n    with C14N output, where they request exclusive and uncommented\n    C14N serialisation respectively.\n\n    Passing a boolean value to the ``standalone`` option will output\n    an XML declaration with the corresponding ``standalone`` flag.\n\n    The ``doctype`` option allows passing in a plain string that will\n    be serialised before the XML tree.  Note that passing in non\n    well-formed content here will make the XML output non well-formed.\n    Also, an existing doctype in the document tree will not be removed\n    when serialising an ElementTree instance.\n\n    You can prevent the tail text of the element from being serialised\n    by passing the boolean ``with_tail`` option.  This has no impact\n    on the tail text of children, which will always be serialised.\n    '
    pass

def tostringlist(element_or_tree, *args, **kwargs):
    'tostringlist(element_or_tree, *args, **kwargs)\n\n    Serialize an element to an encoded string representation of its XML\n    tree, stored in a list of partial strings.\n\n    This is purely for ElementTree 1.3 compatibility.  The result is a\n    single string wrapped in a list.\n    '
    pass

def tounicode(element_or_tree):
    'tounicode(element_or_tree, method="xml", pretty_print=False,\n                  with_tail=True, doctype=None)\n\n    Serialize an element to the Python unicode representation of its XML\n    tree.\n\n    :deprecated: use ``tostring(el, encoding=\'unicode\')`` instead.\n\n    Note that the result does not carry an XML encoding declaration and is\n    therefore not necessarily suited for serialization to byte streams without\n    further treatment.\n\n    The boolean keyword argument \'pretty_print\' enables formatted XML.\n\n    The keyword argument \'method\' selects the output method: \'xml\',\n    \'html\' or plain \'text\'.\n\n    You can prevent the tail text of the element from being serialised\n    by passing the boolean ``with_tail`` option.  This has no impact\n    on the tail text of children, which will always be serialised.\n    '
    pass

def use_global_python_log(log):
    'use_global_python_log(log)\n\n    Replace the global error log by an etree.PyErrorLog that uses the\n    standard Python logging package.\n\n    Note that this disables access to the global error log from exceptions.\n    Parsers, XSLT etc. will continue to provide their normal local error log.\n\n    Note: prior to lxml 2.2, this changed the error log globally.\n    Since lxml 2.2, the global error log is local to a thread and this\n    function will only set the global error log of the current thread.\n    '
    pass

class xmlfile(_mod_builtins.object):
    'xmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental XML serialisation.\n\n    Usage example::\n\n         with xmlfile("somefile.xml", encoding=\'utf-8\') as xf:\n             xf.write_declaration(standalone=True)\n             xf.write_doctype(\'<!DOCTYPE root SYSTEM "some.dtd">\')\n\n             # generate an element (the root element)\n             with xf.element(\'root\'):\n                  # write a complete Element into the open root element\n                  xf.write(etree.Element(\'test\'))\n\n                  # generate and write more Elements, e.g. through iterparse\n                  for element in generate_some_elements():\n                      # serialise generated elements into the XML file\n                      xf.write(element)\n\n                  # or write multiple Elements or strings at once\n                  xf.write(etree.Element(\'start\'), "text", etree.Element(\'end\'))\n\n    If \'output_file\' is a file(-like) object, passing ``close=True`` will\n    close it when exiting the context manager.  By default, it is left\n    to the owner to do that.  When a file path is used, lxml will take care\n    of opening and closing the file itself.  Also, when a compression level\n    is set, lxml will deliberately close the file to make sure all data gets\n    compressed and written.\n\n    Setting ``buffered=False`` will flush the output after each operation,\n    such as opening or closing an ``xf.element()`` block or calling\n    ``xf.write()``.  Alternatively, calling ``xf.flush()`` can be used to\n    explicitly flush any pending output when buffering is enabled.\n    '
    def __aenter__(self):
        pass
    
    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
    
    __class__ = xmlfile
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __init__(self, output_file, encoding=None, compression=None, close=False, buffered=True):
        'xmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental XML serialisation.\n\n    Usage example::\n\n         with xmlfile("somefile.xml", encoding=\'utf-8\') as xf:\n             xf.write_declaration(standalone=True)\n             xf.write_doctype(\'<!DOCTYPE root SYSTEM "some.dtd">\')\n\n             # generate an element (the root element)\n             with xf.element(\'root\'):\n                  # write a complete Element into the open root element\n                  xf.write(etree.Element(\'test\'))\n\n                  # generate and write more Elements, e.g. through iterparse\n                  for element in generate_some_elements():\n                      # serialise generated elements into the XML file\n                      xf.write(element)\n\n                  # or write multiple Elements or strings at once\n                  xf.write(etree.Element(\'start\'), "text", etree.Element(\'end\'))\n\n    If \'output_file\' is a file(-like) object, passing ``close=True`` will\n    close it when exiting the context manager.  By default, it is left\n    to the owner to do that.  When a file path is used, lxml will take care\n    of opening and closing the file itself.  Also, when a compression level\n    is set, lxml will deliberately close the file to make sure all data gets\n    compressed and written.\n\n    Setting ``buffered=False`` will flush the output after each operation,\n    such as opening or closing an ``xf.element()`` block or calling\n    ``xf.write()``.  Alternatively, calling ``xf.flush()`` can be used to\n    explicitly flush any pending output when buffering is enabled.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

