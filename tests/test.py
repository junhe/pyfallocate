import unittest

from os import O_RDWR, O_CREAT
import os

from pyfallocate import fallocate


class Basic(unittest.TestCase):
    def test(self):
        fd = os.open("/tmp/myfile", O_RDWR|O_CREAT, 00666)
        os.write(fd, 'x'*4096)
        ret = fallocate(fd, 3, 0, 4096)
        os.close(fd)

        self.assertEqual(ret, 0)

if __name__ == '__main__':
    unittest.main()
