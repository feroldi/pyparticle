# pyparticle

`pyparticle` is a drop-in replacement for `pyspark` that runs much faster
for automated tests.

The problem with `pyspark` is that when you are executing test code,
it takes a long time (as in many seconds) to create data-frames and
run operations on them, because all that work is done through the JVM.
It's great for big data, but test code generally has small data, so it
doesn't need the power of distributed computing.  So, by reimplementing
`pyspark` with native Python code, we can completely sidestep JVM,
thus saving a lot of time on tests.

## How to use

The current way to use `pyparticle` is to dynamically replace the
`pyspark` module with it:

```python
import sys

sys.modules["pyspark"] = __import__("pyparticle")

import pyspark # Automatically imports pyparticle.
```

The above works because `pyparticle` strictly implements the same API as
`pyspark`'s, even the submodule paths. Do note that such replacement
needs to happen before any code tries to import `pyspark`.

If you use `pytest`, which is most probably, then you can just drop that
code snippet inside `tests/conftest.py`, and all your tests should start
using `pyparticle` by default.
