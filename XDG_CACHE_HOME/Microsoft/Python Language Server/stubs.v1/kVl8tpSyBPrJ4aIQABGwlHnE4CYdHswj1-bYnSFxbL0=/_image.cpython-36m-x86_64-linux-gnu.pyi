BESSEL = 12
BICUBIC = 2
BILINEAR = 1
BLACKMAN = 16
CATROM = 10
GAUSSIAN = 11
HAMMING = 6
HANNING = 5
HERMITE = 7
KAISER = 8
LANCZOS = 15
MITCHELL = 13
NEAREST = 0
QUADRIC = 9
SINC = 14
SPLINE16 = 3
SPLINE36 = 4
__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/matplotlib/_image.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'matplotlib._image'
__package__ = 'matplotlib'
_n_interpolation = 17
def pcolor(x, y, data, rows, cols, bounds):
    'pcolor(x, y, data, rows, cols, bounds)\n\nGenerate a pseudo-color image from data on a non-uniform grid using\nnearest neighbour or linear interpolation.\nbounds = (x_min, x_max, y_min, y_max)\ninterpolation = NEAREST or BILINEAR \n'
    pass

def pcolor2(x, y, data, rows, cols, bounds, bg):
    'pcolor2(x, y, data, rows, cols, bounds, bg)\n\nGenerate a pseudo-color image from data on a non-uniform grid\nspecified by its cell boundaries.\nbounds = (x_left, x_right, y_bot, y_top)\nbg = ndarray of 4 uint8 representing background rgba\n'
    pass

def resample(input_array, output_array, matrix, interpolation=NEAREST, alpha=1.0, norm=False, radius=1):
    'resample(input_array, output_array, matrix, interpolation=NEAREST, alpha=1.0, norm=False, radius=1)\n\nResample input_array, blending it in-place into output_array, using an\naffine transformation.\n\nParameters\n----------\ninput_array : 2-d or 3-d Numpy array of float, double or uint8\n    If 2-d, the image is grayscale.  If 3-d, the image must be of size\n    4 in the last dimension and represents RGBA data.\n\noutput_array : 2-d or 3-d Numpy array of float, double or uint8\n    The dtype and number of dimensions must match `input_array`.\n\ntransform : matplotlib.transforms.Transform instance\n    The transformation from the input array to the output\n    array.\n\ninterpolation : int, optional\n    The interpolation method.  Must be one of the following constants\n    defined in this module:\n\n      NEAREST (default), BILINEAR, BICUBIC, SPLINE16, SPLINE36,\n      HANNING, HAMMING, HERMITE, KAISER, QUADRIC, CATROM, GAUSSIAN,\n      BESSEL, MITCHELL, SINC, LANCZOS, BLACKMAN\n\nresample : bool, optional\n    When `True`, use a full resampling method.  When `False`, only\n    resample when the output image is larger than the input image.\n\nalpha : float, optional\n    The level of transparency to apply.  1.0 is completely opaque.\n    0.0 is completely transparent.\n\nnorm : bool, optional\n    Whether to norm the interpolation function.  Default is `False`.\n\nradius: float, optional\n    The radius of the kernel, if method is SINC, LANCZOS or BLACKMAN.\n    Default is 1.\n'
    pass

