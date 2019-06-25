import builtins as _mod_builtins

tkapp = _mod_builtins.type
tktimertoken = _mod_builtins.type
ALL_EVENTS = -3
DONT_WAIT = 2
EXCEPTION = 8
FILE_EVENTS = 8
IDLE_EVENTS = 32
READABLE = 2
TCL_VERSION = '8.6'
TIMER_EVENTS = 16
TK_VERSION = '8.6'
class TclError(_mod_builtins.Exception):
    __class__ = TclError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_tkinter'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Tcl_Obj(_mod_builtins.object):
    __class__ = Tcl_Obj
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
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
    
    __module__ = '_tkinter'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def string(self):
        'the string representation of this object, either as str or bytes'
        pass
    
    @property
    def typename(self):
        'name of the Tcl type'
        pass
    

TkappType = tkapp()
TkttType = tktimertoken()
WINDOW_EVENTS = 4
WRITABLE = 4
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/_tkinter.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_tkinter'
__package__ = ''
def _flatten(item):
    pass

def create(screenName, baseName, className, interactive, wantobjects, wantTk, sync, use):
    "\n\n  wantTk\n    if false, then Tk_Init() doesn't get called\n  sync\n    if true, then pass -sync to wish\n  use\n    if not None, then pass -use to wish"
    pass

def getbusywaitinterval():
    'Return the current busy-wait interval between successive calls to Tcl_DoOneEvent in a threaded Python interpreter.'
    pass

def setbusywaitinterval(new_val):
    'Set the busy-wait interval in milliseconds between successive calls to Tcl_DoOneEvent in a threaded Python interpreter.\n\nIt should be set to a divisor of the maximum time between frames in an animation.'
    pass

