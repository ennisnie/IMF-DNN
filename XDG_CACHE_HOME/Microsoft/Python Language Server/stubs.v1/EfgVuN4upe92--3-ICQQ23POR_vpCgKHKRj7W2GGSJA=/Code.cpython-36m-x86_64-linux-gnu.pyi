import builtins as _mod_builtins
import collections as _mod_collections
import contextlib as _mod_contextlib
import functools as _mod_functools
import string as _mod_string

class CCodeConfig(_mod_builtins.object):
    __class__ = CCodeConfig
    __dict__ = {}
    def __init__(self, emit_linenums, emit_code_comments, c_line_in_traceback):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class CCodeWriter(_mod_builtins.object):
    '\n    Utility class to output C code.\n\n    When creating an insertion point one must care about the state that is\n    kept:\n    - formatting state (level, bol) is cloned and used in insertion points\n      as well\n    - labels, temps, exc_vars: One must construct a scope in which these can\n      exist by calling enter_cfunc_scope/exit_cfunc_scope (these are for\n      sanity checking and forward compatabilty). Created insertion points\n      looses this scope and cannot access it.\n    - marker: Not copied to insertion point\n    - filename_table, filename_list, input_file_contents: All codewriters\n      coming from the same root share the same instances simultaneously.\n    '
    __class__ = CCodeWriter
    __dict__ = {}
    def __init__(self, create_from, buffer, copy_formatting):
        '\n    Utility class to output C code.\n\n    When creating an insertion point one must care about the state that is\n    kept:\n    - formatting state (level, bol) is cloned and used in insertion points\n      as well\n    - labels, temps, exc_vars: One must construct a scope in which these can\n      exist by calling enter_cfunc_scope/exit_cfunc_scope (these are for\n      sanity checking and forward compatabilty). Created insertion points\n      looses this scope and cannot access it.\n    - marker: Not copied to insertion point\n    - filename_table, filename_list, input_file_contents: All codewriters\n      coming from the same root share the same instances simultaneously.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _build_marker(self, pos):
        pass
    
    def _put_decref(self, cname, type, nanny, null_check, have_gil, clear, clear_before_decref):
        pass
    
    def _put_var_decref_clear(self, entry, null_check):
        pass
    
    def all_new_labels(self):
        pass
    
    def as_pyobject(self, cname, type):
        pass
    
    def begin_block(self):
        pass
    
    break_label = _mod_builtins.property()
    def build_function_modifiers(self, modifiers, mapper):
        pass
    
    code_config = None
    continue_label = _mod_builtins.property()
    def copyto(self, f):
        pass
    
    def create_new(self, create_from, buffer, copy_formatting):
        pass
    
    def declare_gilstate(self):
        pass
    
    def decrease_indent(self):
        pass
    
    def emit_marker(self):
        pass
    
    def end_block(self):
        pass
    
    def enter_cfunc_scope(self, scope):
        pass
    
    def entry_as_pyobject(self, entry):
        pass
    
    def error_goto(self, pos):
        pass
    
    def error_goto_if(self, cond, pos):
        pass
    
    def error_goto_if_PyErr(self, pos):
        pass
    
    def error_goto_if_neg(self, cname, pos):
        pass
    
    def error_goto_if_null(self, cname, pos):
        pass
    
    error_label = _mod_builtins.property()
    def exit_cfunc_scope(self):
        pass
    
    def get_all_labels(self):
        pass
    
    def get_argument_default_const(self, type):
        pass
    
    def get_cached_constants_writer(self):
        pass
    
    def get_loop_labels(self):
        pass
    
    def get_py_const(self, type, prefix, cleanup_level):
        pass
    
    def get_py_float(self, str_value, value_code):
        pass
    
    def get_py_int(self, str_value, longness):
        pass
    
    def get_py_string_const(self, text, identifier, is_str, unicode_value):
        pass
    
    def get_py_version_hex(self, pyversion):
        pass
    
    def get_pyunicode_ptr_const(self, text):
        pass
    
    def get_string_const(self, text):
        pass
    
    def getvalue(self):
        pass
    
    globalstate = None
    def increase_indent(self):
        pass
    
    def indent(self):
        pass
    
    def insert(self, writer):
        '\n        Inserts the contents of another code writer (created with\n        the same global state) in the current location.\n\n        It is ok to write to the inserted writer also after insertion.\n        '
        pass
    
    def insertion_point(self):
        pass
    
    def intern(self, text):
        pass
    
    def intern_identifier(self, text):
        pass
    
    label_counter = _mod_builtins.property()
    def label_used(self, lbl):
        pass
    
    labels_used = _mod_builtins.property()
    def lookup_filename(self, filename):
        pass
    
    def mark_pos(self, pos, trace):
        pass
    
    def new_error_label(self):
        pass
    
    def new_label(self, name):
        pass
    
    def new_loop_labels(self):
        pass
    
    def new_writer(self):
        '\n        Creates a new CCodeWriter connected to the same global state, which\n        can later be inserted using insert.\n        '
        pass
    
    def new_yield_label(self):
        pass
    
    def put(self, code):
        pass
    
    def put_acquire_gil(self, variable):
        "\n        Acquire the GIL. The thread's thread state must have been initialized\n        by a previous `put_release_gil`\n        "
        pass
    
    def put_add_traceback(self, qualified_name):
        '\n        Build a Python traceback for propagating exceptions.\n\n        qualified_name should be the qualified name of the function.\n        '
        pass
    
    def put_declare_refcount_context(self):
        pass
    
    def put_decref(self, cname, type, nanny):
        pass
    
    def put_decref_clear(self, cname, type, nanny, clear_before_decref):
        pass
    
    def put_decref_set(self, cname, rhs_cname):
        pass
    
    def put_ensure_gil(self, declare_gilstate, variable):
        '\n        Acquire the GIL. The generated code is safe even when no PyThreadState\n        has been allocated for this thread (for threads not initialized by\n        using the Python API). Additionally, the code generated by this method\n        may be called recursively.\n        '
        pass
    
    def put_error_if_neg(self, pos, value):
        pass
    
    def put_error_if_unbound(self, pos, entry, in_nogil_context):
        pass
    
    def put_finish_refcount_context(self):
        pass
    
    def put_generated_by(self):
        pass
    
    def put_giveref(self, cname):
        pass
    
    def put_goto(self, lbl):
        pass
    
    def put_gotref(self, cname):
        pass
    
    def put_h_guard(self, guard):
        pass
    
    def put_incref(self, cname, type, nanny):
        pass
    
    def put_incref_memoryviewslice(self, slice_cname, have_gil):
        pass
    
    def put_init_to_py_none(self, cname, type, nanny):
        pass
    
    def put_init_var_to_py_none(self, entry, template, nanny):
        pass
    
    def put_label(self, lbl):
        pass
    
    def put_or_include(self, code, name):
        pass
    
    def put_pymethoddef(self, entry, term, allow_skip):
        pass
    
    def put_release_ensured_gil(self, variable):
        '\n        Releases the GIL, corresponds to `put_ensure_gil`.\n        '
        pass
    
    def put_release_gil(self, variable):
        'Release the GIL, corresponds to `put_acquire_gil`.'
        pass
    
    def put_safe(self, code):
        pass
    
    def put_setup_refcount_context(self, name, acquire_gil):
        pass
    
    def put_temp_declarations(self, func_context):
        pass
    
    def put_tempita(self, code, **context):
        pass
    
    def put_trace_call(self, name, pos, nogil):
        pass
    
    def put_trace_declarations(self):
        pass
    
    def put_trace_exception(self):
        pass
    
    def put_trace_frame_init(self, codeobj):
        pass
    
    def put_trace_return(self, retvalue_cname, nogil):
        pass
    
    def put_unraisable(self, qualified_name, nogil):
        '\n        Generate code to print a Python warning for an unraisable exception.\n\n        qualified_name should be the qualified name of the function.\n        '
        pass
    
    def put_var_declaration(self, entry, storage_class, dll_linkage, definition):
        pass
    
    def put_var_decref(self, entry):
        pass
    
    def put_var_decref_clear(self, entry):
        pass
    
    def put_var_decrefs(self, entries, used_only):
        pass
    
    def put_var_giveref(self, entry):
        pass
    
    def put_var_gotref(self, entry):
        pass
    
    def put_var_incref(self, entry):
        pass
    
    def put_var_xdecref(self, entry):
        pass
    
    def put_var_xdecref_clear(self, entry):
        pass
    
    def put_var_xdecrefs(self, entries):
        pass
    
    def put_var_xdecrefs_clear(self, entries):
        pass
    
    def put_var_xgiveref(self, entry):
        pass
    
    def put_var_xgotref(self, entry):
        pass
    
    def put_var_xincref(self, entry):
        pass
    
    def put_xdecref(self, cname, type, nanny, have_gil):
        pass
    
    def put_xdecref_clear(self, cname, type, nanny, clear_before_decref):
        pass
    
    def put_xdecref_memoryviewslice(self, slice_cname, have_gil):
        pass
    
    def put_xdecref_set(self, cname, rhs_cname):
        pass
    
    def put_xgiveref(self, cname):
        pass
    
    def put_xgiveref_memoryviewslice(self, slice_cname):
        pass
    
    def put_xgotref(self, cname):
        pass
    
    def putln(self, code, safe):
        pass
    
    def putln_openmp(self, string):
        pass
    
    def putln_tempita(self, code, **context):
        pass
    
    def redef_builtin_expect(self, cond):
        pass
    
    return_from_error_cleanup_label = _mod_builtins.property()
    return_label = _mod_builtins.property()
    def set_all_labels(self, labels):
        pass
    
    def set_error_info(self, pos, used):
        pass
    
    def set_global_state(self, global_state):
        pass
    
    def set_loop_labels(self, labels):
        pass
    
    def undef_builtin_expect(self, cond):
        "\n        Redefine the macros likely() and unlikely to no-ops, depending on\n        condition 'cond'\n        "
        pass
    
    def unlikely(self, cond):
        pass
    
    def use_label(self, lbl):
        pass
    
    def write(self, s):
        pass
    
    yield_labels = _mod_builtins.property()

class ClosureTempAllocator(_mod_builtins.object):
    __class__ = ClosureTempAllocator
    __dict__ = {}
    def __init__(self, klass):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def allocate_temp(self, type):
        pass
    
    def reset(self):
        pass
    

class FunctionState(_mod_builtins.object):
    __class__ = FunctionState
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
    
    def all_free_managed_temps(self):
        'Return a list of (cname, type) tuples of refcount-managed Python\n        objects that are not currently in use.  This is used by\n        try-except and try-finally blocks to clean up temps in the\n        error case.\n        '
        pass
    
    def all_managed_temps(self):
        'Return a list of (cname, type) tuples of refcount-managed Python objects.\n        '
        pass
    
    def all_new_labels(self):
        pass
    
    def allocate_temp(self, type, manage_ref, static):
        '\n        Allocates a temporary (which may create a new one or get a previously\n        allocated and released one of the same type). Type is simply registered\n        and handed back, but will usually be a PyrexType.\n\n        If type.is_pyobject, manage_ref comes into play. If manage_ref is set to\n        True, the temp will be decref-ed on return statements and in exception\n        handling clauses. Otherwise the caller has to deal with any reference\n        counting of the variable.\n\n        If not type.is_pyobject, then manage_ref will be ignored, but it\n        still has to be passed. It is recommended to pass False by convention\n        if it is known that type will never be a Python object.\n\n        static=True marks the temporary declaration with "static".\n        This is only used when allocating backing store for a module-level\n        C array literals.\n\n        A C string referring to the variable is returned.\n        '
        pass
    
    @property
    def break_label(self):
        pass
    
    @property
    def can_trace(self):
        pass
    
    @property
    def closure_temps(self):
        pass
    
    @property
    def collect_temps_stack(self):
        pass
    
    @property
    def continue_label(self):
        pass
    
    @property
    def error_label(self):
        pass
    
    @property
    def exc_vars(self):
        pass
    
    def get_all_labels(self):
        pass
    
    def get_loop_labels(self):
        pass
    
    @property
    def gil_owned(self):
        pass
    
    @property
    def in_try_finally(self):
        pass
    
    def init_closure_temps(self, scope):
        pass
    
    @property
    def label_counter(self):
        pass
    
    def label_used(self, lbl):
        pass
    
    @property
    def labels_used(self):
        pass
    
    @property
    def names_taken(self):
        pass
    
    def new_error_label(self):
        pass
    
    def new_label(self, name):
        pass
    
    def new_loop_labels(self):
        pass
    
    def new_yield_label(self):
        pass
    
    @property
    def owner(self):
        pass
    
    def release_temp(self, name):
        '\n        Releases a temporary so that it can be reused by other code needing\n        a temp of the same type.\n        '
        pass
    
    @property
    def return_from_error_cleanup_label(self):
        pass
    
    @property
    def return_label(self):
        pass
    
    @property
    def scope(self):
        pass
    
    def set_all_labels(self, labels):
        pass
    
    def set_loop_labels(self, labels):
        pass
    
    @property
    def should_declare_error_indicator(self):
        pass
    
    def start_collecting_temps(self):
        '\n        Useful to find out which temps were used in a code block\n        '
        pass
    
    def stop_collecting_temps(self):
        pass
    
    @property
    def temp_counter(self):
        pass
    
    @property
    def temps_allocated(self):
        pass
    
    @property
    def temps_free(self):
        pass
    
    def temps_holding_reference(self):
        'Return a list of (cname,type) tuples of temp names and their type\n        that are currently in use. This includes only temps of a\n        Python object type which owns its reference.\n        '
        pass
    
    def temps_in_use(self):
        'Return a list of (cname,type,manage_ref) tuples of temp names and their type\n        that are currently in use.\n        '
        pass
    
    @property
    def temps_used_type(self):
        pass
    
    def use_label(self, lbl):
        pass
    
    @property
    def uses_error_indicator(self):
        pass
    
    @property
    def yield_labels(self):
        pass
    

class GlobalState(_mod_builtins.object):
    __class__ = GlobalState
    __dict__ = {}
    def __getitem__(self, key):
        pass
    
    def __init__(self, writer, module_node, code_config, common_utility_include_dir):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def add_cached_builtin_decl(self, entry):
        pass
    
    def close_global_decls(self):
        pass
    
    code_layout = _mod_builtins.list()
    def commented_file_contents(self, source_desc):
        pass
    
    directives = _mod_builtins.dict()
    def finalize_main_c_code(self):
        pass
    
    def generate_cached_methods_decls(self):
        pass
    
    def generate_const_declarations(self):
        pass
    
    def generate_num_constants(self):
        pass
    
    def generate_object_constant_decls(self):
        pass
    
    def generate_string_constants(self):
        pass
    
    def get_cached_constants_writer(self):
        pass
    
    def get_cached_unbound_method(self, type_cname, method_name, args_count):
        pass
    
    def get_float_const(self, str_value, value_code):
        pass
    
    def get_int_const(self, str_value, longness):
        pass
    
    def get_interned_identifier(self, text):
        pass
    
    def get_py_const(self, type, prefix, cleanup_level):
        pass
    
    def get_py_string_const(self, text, identifier, is_str, unicode_value):
        pass
    
    def get_pyunicode_ptr_const(self, text):
        pass
    
    def get_string_const(self, text, py_version):
        pass
    
    def initialize_main_c_code(self):
        pass
    
    def lookup_filename(self, source_desc):
        pass
    
    def new_const_cname(self, prefix, value):
        pass
    
    def new_num_const(self, value, py_type, value_code):
        pass
    
    def new_num_const_cname(self, value, py_type):
        pass
    
    def new_py_const(self, type, prefix):
        pass
    
    def new_string_const(self, text, byte_string):
        pass
    
    def new_string_const_cname(self, bytes_value):
        pass
    
    def put_cached_builtin_init(self, pos, name, cname):
        pass
    
    def put_pyobject_decl(self, entry):
        pass
    
    def should_declare(self, cname, entry):
        pass
    
    def use_entry_utility_code(self, entry):
        pass
    
    def use_utility_code(self, utility_code):
        '\n        Adds code to the C file. utility_code should\n        a) implement __eq__/__hash__ for the purpose of knowing whether the same\n           code has already been included\n        b) implement put_code, which takes a globalstate instance\n\n        See UtilityCode.\n        '
        pass
    

class IntConst(_mod_builtins.object):
    __class__ = IntConst
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
    

KEYWORDS_MUST_BE_BYTES = False
class LazyUtilityCode(UtilityCodeBase):
    "\n    Utility code that calls a callback with the root code writer when\n    available. Useful when you only have 'env' but not 'code'.\n    "
    __class__ = LazyUtilityCode
    __dict__ = {}
    def __init__(self, callback):
        "\n    Utility code that calls a callback with the root code writer when\n    available. Useful when you only have 'env' but not 'code'.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __name__ = 'LazyUtilityCode'
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_utility(self, cls, utility, type, lines, begin_lineno, tags):
        pass
    
    def format_code(self, code_string, replace_empty_lines):
        '\n        Format a code section for output.\n        '
        pass
    
    def get_tree(self, **kwargs):
        pass
    
    def load(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load utility code from a file specified by from_file (relative to\n        Cython/Utility) and name util_code_name.  If from_file is not given,\n        load it from the file util_code_name.*.  There should be only one\n        file matched by this pattern.\n        '
        pass
    
    def load_as_string(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load a utility code as a string. Returns (proto, implementation)\n        '
        pass
    
    def load_cached(self, cls, utility_code_name, from_file, __cache):
        '\n        Calls .load(), but using a per-type cache based on utility name and file name.\n        '
        pass
    
    def load_utilities_from_file(self, cls, path):
        pass
    
    def put_code(self, globalstate):
        pass
    

class NumConst(_mod_builtins.object):
    'Global info about a Python number constant held by GlobalState.\n\n    cname       string\n    value       string\n    py_type     string     int, long, float\n    value_code  string     evaluation code if different from value\n    '
    __class__ = NumConst
    __dict__ = {}
    def __init__(self, cname, value, py_type, value_code):
        'Global info about a Python number constant held by GlobalState.\n\n    cname       string\n    value       string\n    py_type     string     int, long, float\n    value_code  string     evaluation code if different from value\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class PyObjectConst(_mod_builtins.object):
    'Global info about a generic constant held by GlobalState.\n    '
    __class__ = PyObjectConst
    def __init__(self, *args, **kwargs):
        'Global info about a generic constant held by GlobalState.\n    '
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
    def cname(self):
        pass
    
    @property
    def type(self):
        pass
    

class PyStringConst(_mod_builtins.object):
    'Global info about a Python string constant held by GlobalState.\n    '
    __class__ = PyStringConst
    __dict__ = {}
    def __init__(self, cname, encoding, is_unicode, is_str, py3str_cstring, intern):
        'Global info about a Python string constant held by GlobalState.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __lt__(self, other):
        return False
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class PyrexCodeWriter(_mod_builtins.object):
    __class__ = PyrexCodeWriter
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
    
    def dedent(self):
        pass
    
    @property
    def f(self):
        pass
    
    def indent(self):
        pass
    
    @property
    def level(self):
        pass
    
    def putln(self, code):
        pass
    

class PyxCodeWriter(_mod_builtins.object):
    '\n    Can be used for writing out some Cython code. To use the indenter\n    functionality, the Cython.Compiler.Importer module will have to be used\n    to load the code to support python 2.4\n    '
    __class__ = PyxCodeWriter
    __dict__ = {}
    def __init__(self, buffer, indent_level, context, encoding):
        '\n    Can be used for writing out some Cython code. To use the indenter\n    functionality, the Cython.Compiler.Importer module will have to be used\n    to load the code to support python 2.4\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _putln(self, line):
        pass
    
    def dedent(self, levels):
        pass
    
    def getvalue(self):
        pass
    
    def indent(self, levels):
        pass
    
    def indenter(self, line):
        '\n        Instead of\n\n            with pyx_code.indenter("for i in range(10):"):\n                pyx_code.putln("print i")\n\n        write\n\n            if pyx_code.indenter("for i in range(10);"):\n                pyx_code.putln("print i")\n                pyx_code.dedent()\n        '
        pass
    
    def insertion_point(self):
        pass
    
    def named_insertion_point(self, name):
        pass
    
    def put_chunk(self, chunk, context):
        pass
    
    def putln(self, line, context):
        pass
    

class StringConst(_mod_builtins.object):
    'Global info about a C string constant held by GlobalState.\n    '
    __class__ = StringConst
    def __init__(self, *args, **kwargs):
        'Global info about a C string constant held by GlobalState.\n    '
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
    
    def add_py_version(self, version):
        pass
    
    @property
    def cname(self):
        pass
    
    @property
    def escaped_value(self):
        pass
    
    def get_py_string_const(self, encoding, identifier, is_str, py3str_cstring):
        pass
    
    @property
    def py_strings(self):
        pass
    
    @property
    def py_versions(self):
        pass
    
    @property
    def text(self):
        pass
    

class TempitaUtilityCode(UtilityCode):
    __class__ = TempitaUtilityCode
    __dict__ = {}
    def __eq__(self, other):
        return False
    
    def __hash__(self):
        return 0
    
    def __init__(self, name, proto, impl, init, file, context, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_utility(self, cls, utility, type, lines, begin_lineno, tags):
        pass
    
    def format_code(self, code_string, replace_empty_lines):
        '\n        Format a code section for output.\n        '
        pass
    
    def get_tree(self, **kwargs):
        pass
    
    def inject_string_constants(self, impl, output):
        'Replace \'PYIDENT("xyz")\' by a constant Python identifier cname.\n        '
        pass
    
    def inject_unbound_methods(self, impl, output):
        'Replace \'UNBOUND_METHOD(type, "name")\' by a constant Python identifier cname.\n        '
        pass
    
    def load(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load utility code from a file specified by from_file (relative to\n        Cython/Utility) and name util_code_name.  If from_file is not given,\n        load it from the file util_code_name.*.  There should be only one\n        file matched by this pattern.\n        '
        pass
    
    def load_as_string(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load a utility code as a string. Returns (proto, implementation)\n        '
        pass
    
    def load_cached(self, cls, utility_code_name, from_file, context, __cache):
        pass
    
    def load_utilities_from_file(self, cls, path):
        pass
    
    def none_or_sub(self, s, context):
        '\n        Format a string in this utility code with context. If None, do nothing.\n        '
        pass
    
    def put_code(self, output):
        pass
    
    def specialize(self, pyrex_type, **data):
        pass
    
    def wrap_c_strings(self, impl):
        "Replace CSTRING('''xyz''') by a C compatible string\n        "
        pass
    

Template = _mod_string.Template
class UtilityCode(UtilityCodeBase):
    '\n    Stores utility code to add during code generation.\n\n    See GlobalState.put_utility_code.\n\n    hashes/equals by instance\n\n    proto           C prototypes\n    impl            implemenation code\n    init            code to call on module initialization\n    requires        utility code dependencies\n    proto_block     the place in the resulting file where the prototype should\n                    end up\n    name            name of the utility code (or None)\n    file            filename of the utility code file this utility was loaded\n                    from (or None)\n    '
    __class__ = UtilityCode
    __dict__ = {}
    def __eq__(self, other):
        return False
    
    def __hash__(self):
        return 0
    
    def __init__(self, proto, impl, init, cleanup, requires, proto_block, name, file):
        '\n    Stores utility code to add during code generation.\n\n    See GlobalState.put_utility_code.\n\n    hashes/equals by instance\n\n    proto           C prototypes\n    impl            implemenation code\n    init            code to call on module initialization\n    requires        utility code dependencies\n    proto_block     the place in the resulting file where the prototype should\n                    end up\n    name            name of the utility code (or None)\n    file            filename of the utility code file this utility was loaded\n                    from (or None)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _add_utility(self, cls, utility, type, lines, begin_lineno, tags):
        pass
    
    def format_code(self, code_string, replace_empty_lines):
        '\n        Format a code section for output.\n        '
        pass
    
    def get_tree(self, **kwargs):
        pass
    
    def inject_string_constants(self, impl, output):
        'Replace \'PYIDENT("xyz")\' by a constant Python identifier cname.\n        '
        pass
    
    def inject_unbound_methods(self, impl, output):
        'Replace \'UNBOUND_METHOD(type, "name")\' by a constant Python identifier cname.\n        '
        pass
    
    def load(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load utility code from a file specified by from_file (relative to\n        Cython/Utility) and name util_code_name.  If from_file is not given,\n        load it from the file util_code_name.*.  There should be only one\n        file matched by this pattern.\n        '
        pass
    
    def load_as_string(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load a utility code as a string. Returns (proto, implementation)\n        '
        pass
    
    def load_cached(self, cls, utility_code_name, from_file, __cache):
        '\n        Calls .load(), but using a per-type cache based on utility name and file name.\n        '
        pass
    
    def load_utilities_from_file(self, cls, path):
        pass
    
    def none_or_sub(self, s, context):
        '\n        Format a string in this utility code with context. If None, do nothing.\n        '
        pass
    
    def put_code(self, output):
        pass
    
    def specialize(self, pyrex_type, **data):
        pass
    
    def wrap_c_strings(self, impl):
        "Replace CSTRING('''xyz''') by a C compatible string\n        "
        pass
    

class UtilityCodeBase(_mod_builtins.object):
    "\n    Support for loading utility code from a file.\n\n    Code sections in the file can be specified as follows:\n\n        ##### MyUtility.proto #####\n\n        [proto declarations]\n\n        ##### MyUtility.init #####\n\n        [code run at module initialization]\n\n        ##### MyUtility #####\n        #@requires: MyOtherUtility\n        #@substitute: naming\n\n        [definitions]\n\n    for prototypes and implementation respectively.  For non-python or\n    -cython files backslashes should be used instead.  5 to 30 comment\n    characters may be used on either side.\n\n    If the @cname decorator is not used and this is a CythonUtilityCode,\n    one should pass in the 'name' keyword argument to be used for name\n    mangling of such entries.\n    "
    __class__ = UtilityCodeBase
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        "\n    Support for loading utility code from a file.\n\n    Code sections in the file can be specified as follows:\n\n        ##### MyUtility.proto #####\n\n        [proto declarations]\n\n        ##### MyUtility.init #####\n\n        [code run at module initialization]\n\n        ##### MyUtility #####\n        #@requires: MyOtherUtility\n        #@substitute: naming\n\n        [definitions]\n\n    for prototypes and implementation respectively.  For non-python or\n    -cython files backslashes should be used instead.  5 to 30 comment\n    characters may be used on either side.\n\n    If the @cname decorator is not used and this is a CythonUtilityCode,\n    one should pass in the 'name' keyword argument to be used for name\n    mangling of such entries.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'Cython.Compiler.Code'
    def __str__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _add_utility(self, cls, utility, type, lines, begin_lineno, tags):
        pass
    
    _utility_cache = _mod_builtins.dict()
    def format_code(self, code_string, replace_empty_lines):
        '\n        Format a code section for output.\n        '
        pass
    
    def get_tree(self, **kwargs):
        pass
    
    is_cython_utility = False
    def load(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load utility code from a file specified by from_file (relative to\n        Cython/Utility) and name util_code_name.  If from_file is not given,\n        load it from the file util_code_name.*.  There should be only one\n        file matched by this pattern.\n        '
        pass
    
    def load_as_string(self, cls, util_code_name, from_file, **kwargs):
        '\n        Load a utility code as a string. Returns (proto, implementation)\n        '
        pass
    
    def load_cached(self, cls, utility_code_name, from_file, __cache):
        '\n        Calls .load(), but using a per-type cache based on utility name and file name.\n        '
        pass
    
    def load_utilities_from_file(self, cls, path):
        pass
    
    requires = None

__builtins__ = {}
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/Cython/Compiler/Code.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'Cython.Compiler.Code'
__package__ = 'Cython.Compiler'
__test__ = _mod_builtins.dict()
basicsize_builtins_map = _mod_builtins.dict()
closing = _mod_contextlib.closing
defaultdict = _mod_collections.defaultdict
def funccontext_property(name):
    pass

def get_utility_dir():
    pass

def is_self_assignment(self, string, pos, endpos):
    'Matches zero or more characters at the beginning of the string.'
    pass

def modifier_output_mapper():
    'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
    pass

non_portable_builtins_map = _mod_builtins.dict()
partial = _mod_functools.partial
special_py_methods = _mod_builtins.set()
def sub_tempita(s, context, file, name):
    'Run tempita on string s with given context.'
    pass

uncachable_builtins = _mod_builtins.list()
