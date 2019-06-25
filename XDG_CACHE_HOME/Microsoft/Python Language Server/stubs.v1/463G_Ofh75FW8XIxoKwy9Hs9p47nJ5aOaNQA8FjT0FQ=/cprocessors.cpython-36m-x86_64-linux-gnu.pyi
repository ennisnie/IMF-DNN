import builtins as _mod_builtins
import sqlalchemy as _mod_sqlalchemy

DecimalResultProcessor = _mod_sqlalchemy.DecimalResultProcessor
class UnicodeResultProcessor(_mod_builtins.object):
    'UnicodeResultProcessor objects'
    __class__ = UnicodeResultProcessor
    def __init__(self, *args, **kwargs):
        'UnicodeResultProcessor objects'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def conditional_process(self):
        'Conditional version of the value processor.'
        pass
    
    def process(self):
        'The value processor itself.'
        pass
    

__doc__ = 'Module containing C versions of data processing functions.'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/sqlalchemy/cprocessors.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'sqlalchemy.cprocessors'
__package__ = 'sqlalchemy'
def int_to_boolean():
    'Convert an integer to a boolean.'
    pass

def str_to_date():
    'Convert an ISO string to a datetime.date object.'
    pass

def str_to_datetime():
    'Convert an ISO string to a datetime.datetime object.'
    pass

def str_to_time():
    'Convert an ISO string to a datetime.time object.'
    pass

def to_float():
    'Convert any value to its floating point representation.'
    pass

def to_str():
    'Convert any value to its string representation.'
    pass

