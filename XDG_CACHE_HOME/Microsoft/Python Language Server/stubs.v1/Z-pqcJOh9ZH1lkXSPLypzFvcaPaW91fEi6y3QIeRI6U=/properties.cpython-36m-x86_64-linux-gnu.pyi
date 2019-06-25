import builtins as _mod_builtins

class AxisProperty(_mod_builtins.object):
    __class__ = AxisProperty
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return AxisProperty()
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def axis(self):
        pass
    

class CachedProperty(_mod_builtins.object):
    __class__ = CachedProperty
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return CachedProperty()
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
        return None
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def func(self):
        pass
    
    @property
    def name(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/pandas/_libs/properties.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'pandas._libs.properties'
__package__ = 'pandas._libs'
def __pyx_unpickle_AxisProperty():
    pass

def __pyx_unpickle_CachedProperty():
    pass

__test__ = _mod_builtins.dict()
cache_readonly = CachedProperty()
