import builtins as _mod_builtins

BOLD = 2
EXTERNAL_STREAM = 1024
FAST_GLYPHS = 128
FIXED_SIZES = 2
FIXED_WIDTH = 4
class FT2Font(_mod_builtins.object):
    'FT2Font(ttffile)\n\nCreate a new FT2Font object\nThe following global font attributes are defined:\n  num_faces              number of faces in file\n  face_flags             face flags  (int type); see the ft2font constants\n  style_flags            style flags  (int type); see the ft2font constants\n  num_glyphs             number of glyphs in the face\n  family_name            face family name\n  style_name             face style name\n  num_fixed_sizes        number of bitmap in the face\n  scalable               face is scalable\n\nThe following are available, if scalable is true:\n  bbox                   face global bounding box (xmin, ymin, xmax, ymax)\n  units_per_EM           number of font units covered by the EM\n  ascender               ascender in 26.6 units\n  descender              descender in 26.6 units\n  height                 height in 26.6 units; used to compute a default\n                         line spacing (baseline-to-baseline distance)\n  max_advance_width      maximum horizontal cursor advance for all glyphs\n  max_advance_height     same for vertical layout\n  underline_position     vertical position of the underline bar\n  underline_thickness    vertical thickness of the underline\n  postscript_name        PostScript name of the font\n'
    __class__ = FT2Font
    def __init__(self, ttffile):
        'FT2Font(ttffile)\n\nCreate a new FT2Font object\nThe following global font attributes are defined:\n  num_faces              number of faces in file\n  face_flags             face flags  (int type); see the ft2font constants\n  style_flags            style flags  (int type); see the ft2font constants\n  num_glyphs             number of glyphs in the face\n  family_name            face family name\n  style_name             face style name\n  num_fixed_sizes        number of bitmap in the face\n  scalable               face is scalable\n\nThe following are available, if scalable is true:\n  bbox                   face global bounding box (xmin, ymin, xmax, ymax)\n  units_per_EM           number of font units covered by the EM\n  ascender               ascender in 26.6 units\n  descender              descender in 26.6 units\n  height                 height in 26.6 units; used to compute a default\n                         line spacing (baseline-to-baseline distance)\n  max_advance_width      maximum horizontal cursor advance for all glyphs\n  max_advance_height     same for vertical layout\n  underline_position     vertical position of the underline bar\n  underline_thickness    vertical thickness of the underline\n  postscript_name        PostScript name of the font\n'
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
    def ascender(self):
        pass
    
    @property
    def bbox(self):
        pass
    
    def clear(self):
        'clear()\n\nClear all the glyphs, reset for a new set_text'
        pass
    
    @property
    def descender(self):
        pass
    
    def draw_glyph_to_bitmap(self, bitmap, x, y, glyph):
        'draw_glyph_to_bitmap(bitmap, x, y, glyph)\n\nDraw a single glyph to the bitmap at pixel locations x,y\nNote it is your responsibility to set up the bitmap manually\nwith set_bitmap_size(w,h) before this call is made.\n\nIf you want automatic layout, use set_text in combinations with\ndraw_glyphs_to_bitmap.  This function is intended for people who\nwant to render individual glyphs at precise locations, eg, a\na glyph returned by load_char\n'
        pass
    
    def draw_glyphs_to_bitmap(self):
        'draw_glyphs_to_bitmap()\n\nDraw the glyphs that were loaded by set_text to the bitmap\nThe bitmap size will be automatically set to include the glyphs\n'
        pass
    
    @property
    def face_flags(self):
        pass
    
    @property
    def family_name(self):
        pass
    
    @property
    def fname(self):
        pass
    
    def get_bitmap_offset(self):
        'x, y = get_bitmap_offset()\n\nGet the offset in 26.6 subpixels for the bitmap if ink hangs left or below (0, 0).\nSince matplotlib only supports left-to-right text, y is always 0.\n'
        pass
    
    def get_char_index(self):
        'get_char_index()\n\nGiven a character code, returns a glyph index.\n'
        pass
    
    def get_charmap(self):
        'get_charmap()\n\nReturns a dictionary that maps the character codes of the selected charmap\n(Unicode by default) to their corresponding glyph indices.\n'
        pass
    
    def get_descent(self):
        'd = get_descent()\n\nGet the descent of the current string set by set_text in 26.6 subpixels.\nThe rotation of the string is accounted for.  To get the descent\nin pixels, divide this value by 64.\n'
        pass
    
    def get_glyph_name(self, index):
        'get_glyph_name(index)\n\nRetrieves the ASCII name of a given glyph in a face.\n'
        pass
    
    def get_image(self):
        'get_path()\n\nGet the path data from the currently loaded glyph as a tuple of vertices, codes.\n'
        pass
    
    def get_kerning(self):
        'dx = get_kerning(left, right, mode)\n\nGet the kerning between left char and right glyph indices\nmode is a kerning mode constant\n  KERNING_DEFAULT  - Return scaled and grid-fitted kerning distances\n  KERNING_UNFITTED - Return scaled but un-grid-fitted kerning distances\n  KERNING_UNSCALED - Return the kerning vector in original font units\n'
        pass
    
    def get_name_index(self, name):
        "get_name_index(name)\n\nReturns the glyph index of a given glyph name.\nThe glyph index 0 means `undefined character code'.\n"
        pass
    
    def get_num_glyphs(self):
        'get_num_glyphs()\n\nReturn the number of loaded glyphs\n'
        pass
    
    def get_path(self):
        'get_path()\n\nGet the path data from the currently loaded glyph as a tuple of vertices, codes.\n'
        pass
    
    def get_ps_font_info(self):
        'get_ps_font_info()\n\nReturn the information in the PS Font Info structure.\n'
        pass
    
    def get_sfnt(self, name):
        'get_sfnt(name)\n\nGet all values from the SFNT names table.  Result is a dictionary whosekey is the platform-ID, ISO-encoding-scheme, language-code, anddescription.\n'
        pass
    
    def get_sfnt_table(self, name):
        'get_sfnt_table(name)\n\nReturn one of the following SFNT tables: head, maxp, OS/2, hhea, vhea, post, or pclt.\n'
        pass
    
    def get_width_height(self):
        'w, h = get_width_height()\n\nGet the width and height in 26.6 subpixels of the current string set by set_text\nThe rotation of the string is accounted for.  To get width and height\nin pixels, divide these values by 64\n'
        pass
    
    def get_xys(self):
        'get_xys()\n\nGet the xy locations of the current glyphs\n'
        pass
    
    @property
    def height(self):
        pass
    
    def load_char(self, charcode, flags=LOAD_FORCE_AUTOHINT):
        'load_char(charcode, flags=LOAD_FORCE_AUTOHINT)\n\nLoad character with charcode in current fontfile and set glyph.\nThe flags argument can be a bitwise-or of the LOAD_XXX constants.\nReturn value is a Glyph object, with attributes\n  width          # glyph width\n  height         # glyph height\n  bbox           # the glyph bbox (xmin, ymin, xmax, ymax)\n  horiBearingX   # left side bearing in horizontal layouts\n  horiBearingY   # top side bearing in horizontal layouts\n  horiAdvance    # advance width for horizontal layout\n  vertBearingX   # left side bearing in vertical layouts\n  vertBearingY   # top side bearing in vertical layouts\n  vertAdvance    # advance height for vertical layout\n'
        pass
    
    def load_glyph(self, glyphindex, flags=LOAD_FORCE_AUTOHINT):
        'load_glyph(glyphindex, flags=LOAD_FORCE_AUTOHINT)\n\nLoad character with glyphindex in current fontfile and set glyph.\nThe flags argument can be a bitwise-or of the LOAD_XXX constants.\nReturn value is a Glyph object, with attributes\n  width          # glyph width\n  height         # glyph height\n  bbox           # the glyph bbox (xmin, ymin, xmax, ymax)\n  horiBearingX   # left side bearing in horizontal layouts\n  horiBearingY   # top side bearing in horizontal layouts\n  horiAdvance    # advance width for horizontal layout\n  vertBearingX   # left side bearing in vertical layouts\n  vertBearingY   # top side bearing in vertical layouts\n  vertAdvance    # advance height for vertical layout\n'
        pass
    
    @property
    def max_advance_height(self):
        pass
    
    @property
    def max_advance_width(self):
        pass
    
    @property
    def num_charmaps(self):
        pass
    
    @property
    def num_faces(self):
        pass
    
    @property
    def num_fixed_sizes(self):
        pass
    
    @property
    def num_glyphs(self):
        pass
    
    @property
    def postscript_name(self):
        pass
    
    @property
    def scalable(self):
        pass
    
    def select_charmap(self, i):
        'select_charmap(i)\n\nselect charmap i where i is one of the FT_Encoding number\n'
        pass
    
    def set_charmap(self, i):
        'set_charmap(i)\n\nMake the i-th charmap current\n'
        pass
    
    def set_size(self, ptsize, dpi):
        'set_size(ptsize, dpi)\n\nSet the point size and dpi of the text.\n'
        pass
    
    def set_text(self, s, angle):
        'set_text(s, angle)\n\nSet the text string and angle.\nYou must call this before draw_glyphs_to_bitmap\nA sequence of x,y positions is returned'
        pass
    
    @property
    def style_flags(self):
        pass
    
    @property
    def style_name(self):
        pass
    
    @property
    def underline_position(self):
        pass
    
    @property
    def underline_thickness(self):
        pass
    
    @property
    def units_per_EM(self):
        pass
    

class FT2Image(_mod_builtins.object):
    __class__ = FT2Image
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
    
    def as_array(self):
        'x = image.as_array()\n\nReturn the image buffer as a width x height numpy array of ubyte \n\n'
        pass
    
    def as_rgba_str(self):
        's = image.as_rgba_str()\n\nReturn the image buffer as a RGBA string\n\n'
        pass
    
    def as_str(self):
        's = image.as_str()\n\nReturn the image buffer as a string\n\n'
        pass
    
    def draw_rect(self, x0, y0, x1, y1):
        'draw_rect(x0, y0, x1, y1)\n\nDraw a rect to the image.\n\n'
        pass
    
    def draw_rect_filled(self, x0, y0, x1, y1):
        'draw_rect_filled(x0, y0, x1, y1)\n\nDraw a filled rect to the image.\n\n'
        pass
    
    def get_height(self):
        pass
    
    def get_width(self):
        pass
    

GLYPH_NAMES = 512
HORIZONTAL = 16
ITALIC = 1
KERNING = 64
KERNING_DEFAULT = 0
KERNING_UNFITTED = 1
KERNING_UNSCALED = 2
LOAD_CROP_BITMAP = 64
LOAD_DEFAULT = 0
LOAD_FORCE_AUTOHINT = 32
LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH = 512
LOAD_IGNORE_TRANSFORM = 2048
LOAD_LINEAR_DESIGN = 8192
LOAD_MONOCHROME = 4096
LOAD_NO_AUTOHINT = 32768
LOAD_NO_BITMAP = 8
LOAD_NO_HINTING = 2
LOAD_NO_RECURSE = 1024
LOAD_NO_SCALE = 1
LOAD_PEDANTIC = 128
LOAD_RENDER = 4
LOAD_TARGET_LCD = 196608
LOAD_TARGET_LCD_V = 262144
LOAD_TARGET_LIGHT = 65536
LOAD_TARGET_MONO = 131072
LOAD_TARGET_NORMAL = 0
LOAD_VERTICAL_LAYOUT = 16
MULTIPLE_MASTERS = 256
SCALABLE = 1
SFNT = 8
VERTICAL = 32
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/matplotlib/ft2font.cpython-36m-x86_64-linux-gnu.so'
__freetype_build_type__ = 'system'
__freetype_version__ = '2.9.1'
__name__ = 'matplotlib.ft2font'
__package__ = 'matplotlib'
