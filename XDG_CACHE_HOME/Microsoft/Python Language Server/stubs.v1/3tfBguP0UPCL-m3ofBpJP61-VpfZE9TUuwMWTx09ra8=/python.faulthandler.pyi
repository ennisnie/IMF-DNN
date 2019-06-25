__doc__ = 'faulthandler module.'
__name__ = 'faulthandler'
__package__ = ''
def _fatal_error(message):
    '_fatal_error(message): call Py_FatalError(message)'
    pass

def _fatal_error_c_thread():
    'fatal_error_c_thread(): call Py_FatalError() in a new C thread.'
    pass

def _read_null():
    '_read_null(): read from NULL, raise a SIGSEGV or SIGBUS signal depending on the platform'
    pass

def _sigabrt():
    '_sigabrt(): raise a SIGABRT signal'
    pass

def _sigfpe():
    '_sigfpe(): raise a SIGFPE signal'
    pass

def _sigsegv(release_gil=False):
    '_sigsegv(release_gil=False): raise a SIGSEGV signal'
    pass

def _stack_overflow():
    '_stack_overflow(): recursive call to raise a stack overflow'
    pass

def cancel_dump_traceback_later():
    'cancel_dump_traceback_later():\ncancel the previous call to dump_traceback_later().'
    pass

def disable():
    'disable(): disable the fault handler'
    pass

def dump_traceback(file=sys.stderr, all_threads=True):
    'dump_traceback(file=sys.stderr, all_threads=True): dump the traceback of the current thread, or of all threads if all_threads is True, into file'
    pass

def dump_traceback_later(timeout, repeat=False, file=sys.stderrn, exit=False):
    'dump_traceback_later(timeout, repeat=False, file=sys.stderrn, exit=False):\ndump the traceback of all threads in timeout seconds,\nor each timeout seconds if repeat is True. If exit is True, call _exit(1) which is not safe.'
    pass

def enable(file=sys.stderr, all_threads=True):
    'enable(file=sys.stderr, all_threads=True): enable the fault handler'
    pass

def is_enabled():
    'is_enabled()->bool: check if the handler is enabled'
    return True

def register(signum, file=sys.stderr, all_threads=True, chain=False):
    "register(signum, file=sys.stderr, all_threads=True, chain=False): register a handler for the signal 'signum': dump the traceback of the current thread, or of all threads if all_threads is True, into file"
    pass

def unregister(signum):
    "unregister(signum): unregister the handler of the signal 'signum' registered by register()"
    pass

