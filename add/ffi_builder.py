from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef("int add();")
ffibuilder.set_source("_add",
    """
    #include "add.h"
    """,
    sources=['add.c'],
    libraries=[])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
