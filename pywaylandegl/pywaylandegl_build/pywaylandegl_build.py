from cffi import FFI
from os import path


HERE = path.dirname(path.realpath(__file__))
INCLUDE_FOLDER = path.join(HERE, 'include')

# ----------
# BUILD WRAPPER
# ----------
ffibuilder = FFI()

# prepare cdef
cdef = open(path.join(HERE, 'cdef', 'wayland-egl.cdef.h')).read()
ffibuilder.cdef(cdef)

# prepare source
source = '''
#include <wayland-egl.h>
'''

ffibuilder.set_source(
    '_pywaylandegl',
    source,
    libraries=['wayland-egl'],
    extra_compile_args=["-I"+INCLUDE_FOLDER]
)


if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
