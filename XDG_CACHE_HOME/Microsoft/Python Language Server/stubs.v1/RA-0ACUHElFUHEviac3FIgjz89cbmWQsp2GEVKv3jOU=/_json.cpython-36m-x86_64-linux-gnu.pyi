import builtins as _mod_builtins

Encoder = _mod_builtins.type
Scanner = _mod_builtins.type
__doc__ = 'json speedups\n'
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/lib-dynload/_json.cpython-36m-x86_64-linux-gnu.so'
__name__ = '_json'
__package__ = ''
def encode_basestring(string):
    'encode_basestring(string) -> string\n\nReturn a JSON representation of a Python string'
    return ''

def encode_basestring_ascii(string):
    'encode_basestring_ascii(string) -> string\n\nReturn an ASCII-only JSON representation of a Python string'
    return ''

make_encoder = Encoder()
make_scanner = Scanner()
def scanstring(string, end, strict=True):
    'scanstring(string, end, strict=True) -> (string, end)\n\nScan the string s for a JSON string. End is the index of the\ncharacter in s after the quote that started the JSON string.\nUnescapes all valid JSON string escape sequences and raises ValueError\non attempt to decode an invalid string. If strict is False then literal\ncontrol characters are allowed in the string.\n\nReturns a tuple of the decoded string and the index of the character in s\nafter the end quote.'
    return tuple()

