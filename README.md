# pyfallocate
pyfallocate allows Python script to call Linux fallocate(). 
Works even with Raspberry's Raspbian forcing 64b offsets allowing more than 4GB allocated.
## Install

pyfallocate relies on cffi, so you need to install cffi first by:

```
$ sudo apt-get install libffi-dev # Just in case you don't have it
$ pip install cffi
```

Then copy pyfallocate/pyfallocate to the project where you want to use it. 

Then:

```
$ cd pyfallocate
$ python fallocate_build.py
```

## Use

For example:

```
from os import O_RDWR, O_CREAT
import os

from pyfallocate import fallocate

fd = os.open("/tmp/myfile", O_RDWR|O_CREAT, 00666)
os.write(fd, 'x' * 4096)
ret = fallocate(fd, 3, 0, 4096)
print 'fallocate() returned', ret
os.close(fd)
```

