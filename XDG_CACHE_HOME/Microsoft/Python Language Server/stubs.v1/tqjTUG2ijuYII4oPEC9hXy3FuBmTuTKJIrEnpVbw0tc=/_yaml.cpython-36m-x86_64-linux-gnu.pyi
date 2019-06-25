import builtins as _mod_builtins
import yaml.composer as _mod_yaml_composer
import yaml.constructor as _mod_yaml_constructor
import yaml.emitter as _mod_yaml_emitter
import yaml.error as _mod_yaml_error
import yaml.events as _mod_yaml_events
import yaml.nodes as _mod_yaml_nodes
import yaml.parser as _mod_yaml_parser
import yaml.reader as _mod_yaml_reader
import yaml.representer as _mod_yaml_representer
import yaml.scanner as _mod_yaml_scanner
import yaml.serializer as _mod_yaml_serializer
import yaml.tokens as _mod_yaml_tokens

AliasEvent = _mod_yaml_events.AliasEvent
AliasToken = _mod_yaml_tokens.AliasToken
AnchorToken = _mod_yaml_tokens.AnchorToken
BlockEndToken = _mod_yaml_tokens.BlockEndToken
BlockEntryToken = _mod_yaml_tokens.BlockEntryToken
BlockMappingStartToken = _mod_yaml_tokens.BlockMappingStartToken
BlockSequenceStartToken = _mod_yaml_tokens.BlockSequenceStartToken
class CEmitter(_mod_builtins.object):
    __class__ = CEmitter
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        pass
    
    def dispose(self):
        pass
    
    def emit(self):
        pass
    
    def open(self):
        pass
    
    def serialize(self):
        pass
    

class CParser(_mod_builtins.object):
    __class__ = CParser
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def check_event(self):
        pass
    
    def check_node(self):
        pass
    
    def check_token(self):
        pass
    
    def dispose(self):
        pass
    
    def get_event(self):
        pass
    
    def get_node(self):
        pass
    
    def get_single_node(self):
        pass
    
    def get_token(self):
        pass
    
    def peek_event(self):
        pass
    
    def peek_token(self):
        pass
    
    def raw_parse(self):
        pass
    
    def raw_scan(self):
        pass
    

ComposerError = _mod_yaml_composer.ComposerError
ConstructorError = _mod_yaml_constructor.ConstructorError
DirectiveToken = _mod_yaml_tokens.DirectiveToken
DocumentEndEvent = _mod_yaml_events.DocumentEndEvent
DocumentEndToken = _mod_yaml_tokens.DocumentEndToken
DocumentStartEvent = _mod_yaml_events.DocumentStartEvent
DocumentStartToken = _mod_yaml_tokens.DocumentStartToken
EmitterError = _mod_yaml_emitter.EmitterError
FlowEntryToken = _mod_yaml_tokens.FlowEntryToken
FlowMappingEndToken = _mod_yaml_tokens.FlowMappingEndToken
FlowMappingStartToken = _mod_yaml_tokens.FlowMappingStartToken
FlowSequenceEndToken = _mod_yaml_tokens.FlowSequenceEndToken
FlowSequenceStartToken = _mod_yaml_tokens.FlowSequenceStartToken
KeyToken = _mod_yaml_tokens.KeyToken
MappingEndEvent = _mod_yaml_events.MappingEndEvent
MappingNode = _mod_yaml_nodes.MappingNode
MappingStartEvent = _mod_yaml_events.MappingStartEvent
class Mark(_mod_builtins.object):
    __class__ = Mark
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def buffer(self):
        pass
    
    @property
    def column(self):
        pass
    
    def get_snippet(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def line(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def pointer(self):
        pass
    

ParserError = _mod_yaml_parser.ParserError
ReaderError = _mod_yaml_reader.ReaderError
RepresenterError = _mod_yaml_representer.RepresenterError
ScalarEvent = _mod_yaml_events.ScalarEvent
ScalarNode = _mod_yaml_nodes.ScalarNode
ScalarToken = _mod_yaml_tokens.ScalarToken
ScannerError = _mod_yaml_scanner.ScannerError
SequenceEndEvent = _mod_yaml_events.SequenceEndEvent
SequenceNode = _mod_yaml_nodes.SequenceNode
SequenceStartEvent = _mod_yaml_events.SequenceStartEvent
SerializerError = _mod_yaml_serializer.SerializerError
StreamEndEvent = _mod_yaml_events.StreamEndEvent
StreamEndToken = _mod_yaml_tokens.StreamEndToken
StreamStartEvent = _mod_yaml_events.StreamStartEvent
StreamStartToken = _mod_yaml_tokens.StreamStartToken
TagToken = _mod_yaml_tokens.TagToken
ValueToken = _mod_yaml_tokens.ValueToken
YAMLError = _mod_yaml_error.YAMLError
__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/_yaml.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_yaml'
__package__ = ''
def __pyx_unpickle_Mark():
    pass

__test__ = _mod_builtins.dict()
def get_version():
    pass

def get_version_string():
    pass

