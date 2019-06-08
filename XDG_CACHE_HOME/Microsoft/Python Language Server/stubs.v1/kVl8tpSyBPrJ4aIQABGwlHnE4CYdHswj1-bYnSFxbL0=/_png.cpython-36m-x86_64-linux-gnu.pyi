PNG_FILTER_AVG = 64
PNG_FILTER_NONE = 8
PNG_FILTER_PAETH = 128
PNG_FILTER_SUB = 16
PNG_FILTER_UP = 32
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/matplotlib/_png.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'matplotlib._png'
__package__ = 'matplotlib'
def read_png(file):
    'read_png(file)\n\nRead in a PNG file, converting values to floating-point doubles\nin the range (0, 1)\n\nAlias for read_png_float()\n\nParameters\n----------\nfile : str path or file-like object\n'
    pass

def read_png_float(file):
    'read_png_float(file)\n\nRead in a PNG file, converting values to floating-point doubles\nin the range (0, 1)\n\nParameters\n----------\nfile : str path or file-like object\n'
    pass

def read_png_int(file):
    'read_png_int(file)\n\nRead in a PNG file with original integer values.\n\nParameters\n----------\nfile : str path or file-like object\n'
    pass

def write_png(buffer, file, dpi=0, compression=6, filter=auto, metadata=None):
    "write_png(buffer, file, dpi=0, compression=6, filter=auto, metadata=None)\n\nParameters\n----------\nbuffer : numpy array of image data\n    Must be an MxNxD array of dtype uint8.\n    - if D is 1, the image is greyscale\n    - if D is 3, the image is RGB\n    - if D is 4, the image is RGBA\n\nfile : str path, file-like object or None\n    - If a str, must be a file path\n    - If a file-like object, must write bytes\n    - If None, a byte string containing the PNG data will be returned\n\ndpi : float\n    The dpi to store in the file metadata.\n\ncompression : int\n    The level of lossless zlib compression to apply.  0 indicates no\n    compression.  Values 1-9 indicate low/fast through high/slow\n    compression.  Default is 6.\n\nfilter : int\n    Filter to apply.  Must be one of the constants: PNG_FILTER_NONE,\n    PNG_FILTER_SUB, PNG_FILTER_UP, PNG_FILTER_AVG, PNG_FILTER_PAETH.\n    See the PNG standard for more information.\n    If not provided, libpng will try to automatically determine the\n    best filter on a line-by-line basis.\n\nmetadata : dictionary\n    The keyword-text pairs that are stored as comments in the image.\n    Keys must be shorter than 79 chars. The only supported encoding\n    for both keywords and values is Latin-1 (ISO 8859-1).\n    Examples given in the PNG Specification are:\n    - Title: Short (one line) title or caption for image\n    - Author: Name of image's creator\n    - Description: Description of image (possibly long)\n    - Copyright: Copyright notice\n    - Creation Time: Time of original image creation\n                     (usually RFC 1123 format, see below)\n    - Software: Software used to create the image\n    - Disclaimer: Legal disclaimer\n    - Warning: Warning of nature of content\n    - Source: Device used to create the image\n    - Comment: Miscellaneous comment; conversion\n               from other image format\n\n    For more details see the PNG specification:\n    https://www.w3.org/TR/2003/REC-PNG-20031110/#11keywords\n\nReturns\n-------\nbuffer : bytes or None\n    Byte string containing the PNG content if None was passed in for\n    file, otherwise None is returned.\n"
    pass

