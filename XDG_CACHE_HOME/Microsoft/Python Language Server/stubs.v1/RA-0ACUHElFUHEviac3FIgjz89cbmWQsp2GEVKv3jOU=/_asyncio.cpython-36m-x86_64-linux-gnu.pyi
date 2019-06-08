class Future(object):
    "This class is *almost* compatible with concurrent.futures.Future.\n\n    Differences:\n\n    - result() and exception() do not take a timeout argument and\n      raise an exception when the future isn't done yet.\n\n    - Callbacks registered with add_done_callback() are always called\n      via the event loop's call_soon_threadsafe().\n\n    - This class is not compatible with the wait() and as_completed()\n      methods in the concurrent.futures package."
    def __await__(self):
        'Return an iterator to be used in await expression.'
        pass
    
    __class__ = Future
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        "This class is *almost* compatible with concurrent.futures.Future.\n\n    Differences:\n\n    - result() and exception() do not take a timeout argument and\n      raise an exception when the future isn't done yet.\n\n    - Callbacks registered with add_done_callback() are always called\n      via the event loop's call_soon_threadsafe().\n\n    - This class is not compatible with the wait() and as_completed()\n      methods in the concurrent.futures package."
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Future()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _asyncio_future_blocking(self):
        pass
    
    @property
    def _callbacks(self):
        pass
    
    @property
    def _exception(self):
        pass
    
    @property
    def _log_traceback(self):
        pass
    
    @property
    def _loop(self):
        pass
    
    def _repr_info(self):
        pass
    
    @property
    def _result(self):
        pass
    
    def _schedule_callbacks(self):
        pass
    
    @property
    def _source_traceback(self):
        pass
    
    @property
    def _state(self):
        pass
    
    def add_done_callback(self, fn):
        'Add a callback to be run when the future becomes done.\n\nThe callback is called with a single argument - the future object. If\nthe future is already done when this is called, the callback is\nscheduled with call_soon.'
        pass
    
    def cancel(self):
        "Cancel the future and schedule callbacks.\n\nIf the future is already done or cancelled, return False.  Otherwise,\nchange the future's state to cancelled, schedule the callbacks and\nreturn True."
        pass
    
    def cancelled(self):
        'Return True if the future was cancelled.'
        pass
    
    def done(self):
        'Return True if the future is done.\n\nDone means either that a result / exception are available, or that the\nfuture was cancelled.'
        pass
    
    def exception(self):
        "Return the exception that was set on this future.\n\nThe exception (or None if no exception was set) is returned only if\nthe future is done.  If the future has been cancelled, raises\nCancelledError.  If the future isn't done yet, raises\nInvalidStateError."
        pass
    
    def remove_done_callback(self, fn):
        'Remove all instances of a callback from the "call when done" list.\n\nReturns the number of callbacks removed.'
        pass
    
    def result(self):
        "Return the result this future represents.\n\nIf the future has been cancelled, raises CancelledError.  If the\nfuture's result isn't yet available, raises InvalidStateError.  If\nthe future is done and has an exception set, this exception is raised."
        pass
    
    def set_exception(self, exception):
        'Mark the future done and set an exception.\n\nIf the future is already done when this method is called, raises\nInvalidStateError.'
        pass
    
    def set_result(self, res):
        'Mark the future done and set its result.\n\nIf the future is already done when this method is called, raises\nInvalidStateError.'
        pass
    

class Task(Future):
    'A coroutine wrapped in a Future.'
    def __await__(self):
        'Return an iterator to be used in await expression.'
        pass
    
    __class__ = Task
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        'A coroutine wrapped in a Future.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Task()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def _asyncio_future_blocking(self):
        pass
    
    @property
    def _callbacks(self):
        pass
    
    @property
    def _coro(self):
        pass
    
    @property
    def _exception(self):
        pass
    
    @property
    def _fut_waiter(self):
        pass
    
    @property
    def _log_destroy_pending(self):
        pass
    
    @property
    def _log_traceback(self):
        pass
    
    @property
    def _loop(self):
        pass
    
    @property
    def _must_cancel(self):
        pass
    
    def _repr_info(self):
        pass
    
    @property
    def _result(self):
        pass
    
    @property
    def _source_traceback(self):
        pass
    
    @property
    def _state(self):
        pass
    
    def _step(self, exc):
        pass
    
    def _wakeup(self, fut):
        pass
    
    def add_done_callback(self, fn):
        'Add a callback to be run when the future becomes done.\n\nThe callback is called with a single argument - the future object. If\nthe future is already done when this is called, the callback is\nscheduled with call_soon.'
        pass
    
    @classmethod
    def all_tasks(cls, type, loop):
        'Return a set of all tasks for an event loop.\n\nBy default all tasks for the current event loop are returned.'
        pass
    
    def cancel(self):
        'Request that this task cancel itself.\n\nThis arranges for a CancelledError to be thrown into the\nwrapped coroutine on the next cycle through the event loop.\nThe coroutine then has a chance to clean up or even deny\nthe request using try/except/finally.\n\nUnlike Future.cancel, this does not guarantee that the\ntask will be cancelled: the exception might be caught and\nacted upon, delaying cancellation of the task or preventing\ncancellation completely.  The task may also return a value or\nraise a different exception.\n\nImmediately after this method is called, Task.cancelled() will\nnot return True (unless the task was already cancelled).  A\ntask will be marked as cancelled when the wrapped coroutine\nterminates with a CancelledError exception (even if cancel()\nwas not called).'
        pass
    
    def cancelled(self):
        'Return True if the future was cancelled.'
        pass
    
    @classmethod
    def current_task(cls, type, loop):
        'Return the currently running task in an event loop or None.\n\nBy default the current task for the current event loop is returned.\n\nNone is returned when called not in the context of a Task.'
        pass
    
    def done(self):
        'Return True if the future is done.\n\nDone means either that a result / exception are available, or that the\nfuture was cancelled.'
        pass
    
    def exception(self):
        "Return the exception that was set on this future.\n\nThe exception (or None if no exception was set) is returned only if\nthe future is done.  If the future has been cancelled, raises\nCancelledError.  If the future isn't done yet, raises\nInvalidStateError."
        pass
    
    def get_stack(self):
        "Return the list of stack frames for this task's coroutine.\n\nIf the coroutine is not done, this returns the stack where it is\nsuspended.  If the coroutine has completed successfully or was\ncancelled, this returns an empty list.  If the coroutine was\nterminated by an exception, this returns the list of traceback\nframes.\n\nThe frames are always ordered from oldest to newest.\n\nThe optional limit gives the maximum number of frames to\nreturn; by default all available frames are returned.  Its\nmeaning differs depending on whether a stack or a traceback is\nreturned: the newest frames of a stack are returned, but the\noldest frames of a traceback are returned.  (This matches the\nbehavior of the traceback module.)\n\nFor reasons beyond our control, only one stack frame is\nreturned for a suspended coroutine."
        pass
    
    def print_stack(self):
        "Print the stack or traceback for this task's coroutine.\n\nThis produces output similar to that of the traceback module,\nfor the frames retrieved by get_stack().  The limit argument\nis passed to get_stack().  The file argument is an I/O stream\nto which the output is written; by default output is written\nto sys.stderr."
        pass
    
    def remove_done_callback(self, fn):
        'Remove all instances of a callback from the "call when done" list.\n\nReturns the number of callbacks removed.'
        pass
    
    def result(self):
        "Return the result this future represents.\n\nIf the future has been cancelled, raises CancelledError.  If the\nfuture's result isn't yet available, raises InvalidStateError.  If\nthe future is done and has an exception set, this exception is raised."
        pass
    
    def set_exception(self, exception):
        'Mark the future done and set an exception.\n\nIf the future is already done when this method is called, raises\nInvalidStateError.'
        pass
    
    def set_result(self, res):
        'Mark the future done and set its result.\n\nIf the future is already done when this method is called, raises\nInvalidStateError.'
        pass
    

__doc__ = 'Accelerator module for asyncio'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/_asyncio.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_asyncio'
__package__ = ''
