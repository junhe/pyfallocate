from cffi import FFI
ffi = FFI()

ffi.set_source("_fallocate",
"""
#include <fcntl.h>
""",
               libraries=[])

ffi.cdef("""
// some declarations from the man page

typedef long long off_t;

int fallocate(int fd, int mode, off_t offset, off_t len);
""")

if __name__ == "__main__":
    ffi.compile()
