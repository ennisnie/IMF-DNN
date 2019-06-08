import builtins as _mod_builtins

RLIMIT_AS = 9
RLIMIT_CORE = 4
RLIMIT_CPU = 0
RLIMIT_DATA = 2
RLIMIT_FSIZE = 1
RLIMIT_MEMLOCK = 8
RLIMIT_MSGQUEUE = 12
RLIMIT_NICE = 13
RLIMIT_NOFILE = 7
RLIMIT_NPROC = 6
RLIMIT_OFILE = 7
RLIMIT_RSS = 5
RLIMIT_RTPRIO = 14
RLIMIT_SIGPENDING = 11
RLIMIT_STACK = 3
RLIM_INFINITY = -1
RUSAGE_CHILDREN = -1
RUSAGE_SELF = 0
RUSAGE_THREAD = 1
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/resource.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'resource'
__package__ = ''
error = _mod_builtins.OSError
def getpagesize():
    pass

def getrlimit():
    pass

def getrusage():
    pass

def setrlimit():
    pass

class struct_rusage(_mod_builtins.tuple):
    'struct_rusage: Result from getrusage.\n\nThis object may be accessed either as a tuple of\n    (utime,stime,maxrss,ixrss,idrss,isrss,minflt,majflt,\n    nswap,inblock,oublock,msgsnd,msgrcv,nsignals,nvcsw,nivcsw)\nor via the attributes ru_utime, ru_stime, ru_maxrss, and so on.'
    __class__ = struct_rusage
    def __init__(self, *args, **kwargs):
        'struct_rusage: Result from getrusage.\n\nThis object may be accessed either as a tuple of\n    (utime,stime,maxrss,ixrss,idrss,isrss,minflt,majflt,\n    nswap,inblock,oublock,msgsnd,msgrcv,nsignals,nvcsw,nivcsw)\nor via the attributes ru_utime, ru_stime, ru_maxrss, and so on.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    n_fields = 16
    n_sequence_fields = 16
    n_unnamed_fields = 0
    @property
    def ru_idrss(self):
        'unshared data size'
        pass
    
    @property
    def ru_inblock(self):
        'block input operations'
        pass
    
    @property
    def ru_isrss(self):
        'unshared stack size'
        pass
    
    @property
    def ru_ixrss(self):
        'shared memory size'
        pass
    
    @property
    def ru_majflt(self):
        'page faults requiring I/O'
        pass
    
    @property
    def ru_maxrss(self):
        'max. resident set size'
        pass
    
    @property
    def ru_minflt(self):
        'page faults not requiring I/O'
        pass
    
    @property
    def ru_msgrcv(self):
        'IPC messages received'
        pass
    
    @property
    def ru_msgsnd(self):
        'IPC messages sent'
        pass
    
    @property
    def ru_nivcsw(self):
        'involuntary context switches'
        pass
    
    @property
    def ru_nsignals(self):
        'signals received'
        pass
    
    @property
    def ru_nswap(self):
        'number of swap outs'
        pass
    
    @property
    def ru_nvcsw(self):
        'voluntary context switches'
        pass
    
    @property
    def ru_oublock(self):
        'block output operations'
        pass
    
    @property
    def ru_stime(self):
        'system time used'
        pass
    
    @property
    def ru_utime(self):
        'user time used'
        pass
    

