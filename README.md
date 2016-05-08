# pyfallocate
pyfallocate allows Python script to call Linux fallocate(). 

## Install

pyfallocate relies on cffi, so you need to install cffi first by:

```
$ pip install cffi
```

Then copy pyfallocate/pyfallocate to the project where you want to use it. 

Then:

```
$ cd pyfallocate
$ python fallocate_build.py
```

Use:

For example:

```
from os import O_RDWR, O_CREAT
import os

from pyfallocate import fallocate

fd = os.open("/tmp/myfile", O_RDWR|O_CREAT, 00666)
os.write(fd, 'x' * 4096)
ret = fallocate(fd, 3, 0, 4096)
os.close(fd)
```

