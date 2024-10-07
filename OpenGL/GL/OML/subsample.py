'''OpenGL extension OML.subsample

This module customises the behaviour of the 
OpenGL.raw.GL.OML.subsample to provide a more 
Python-friendly API

Overview (from the spec)
	
	Many video image formats and compression techniques utilize various
	component subsamplings, so it is necessary to provide a mechanism to
	specify the up- and down-sampling of components as pixel data is
	drawn from and read back to the client. Though subsampled components
	are normally associated with the video color space, YCrCb, use of
	subsampling in OpenGL does not imply a specific color space. Color
	space conversion may be performed using other extensions or core
	capabilities such as the color matrix.
	
	This extension defines two new pixel storage formats representing
	subsampled data on the client. It is loosely based on the
	SGIX_subsample extension, but specifies subsampling with the data
	format parameter rather than pixel packing parameters. It also
	adds support for CYA subsampled data.
	
	When pixel data is received from the client and an unpacking
	upsampling mode other than PIXEL_SUBSAMPLE_NONE_OML is specified,
	upsampling is performed via replication, unless otherwise specified
	by UNPACK_RESAMPLE_OML.
	
	Similarly, when pixel data is read back to the client and a packing
	downsampling mode other than PIXEL_SUBSAMPLE_NONE_OML is specified,
	downsampling is performed via simple component decimation (point
	sampling), unless otherwise specified by PACK_RESAMPLE_OML.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OML/subsample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.OML.subsample import *
from OpenGL.raw.GL.OML.subsample import _EXTENSION_NAME

def glInitSubsampleOML():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
from OpenGL import images as _i
_i.COMPONENT_COUNTS[ GL_FORMAT_SUBSAMPLE_24_24_OML ] = 1 # must be GL_UNSIGNED_INT_10_10_10_2
_i.COMPONENT_COUNTS[ GL_FORMAT_SUBSAMPLE_244_244_OML ] = 1 # must be GL_UNSIGNED_INT_10_10_10_2