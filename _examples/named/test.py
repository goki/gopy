# Copyright 2015 The go-python Authors.  All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

## py2/py3 compat
from __future__ import print_function

import named

### test docs
print("doc(named): %r" % (named.__doc__,))
print("doc(named.Float): %r" % (named.Float.__doc__,))
print("doc(named.Float.Value): %r" % (named.Float.Value.__doc__,))

print("v = named.Float()")
v = named.Float()
print("v = %s" % (v,))
print("v.Value() = %s" % (v.Value(),))

print("x = named.X()")
x = named.X()
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XX()")
x = named.XX()
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XXX()")
x = named.XXX()
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XXXX()")
x = named.XXXX()
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

### test ctors

print("v = named.Float(42)")
v = named.Float(42)
print("v = %s" % (v,))
print("v.Value() = %s" % (v.Value(),))

print("v = named.Float(42.0)")
v = named.Float(42.0)
print("v = %s" % (v,))
print("v.Value() = %s" % (v.Value(),))

print("x = named.X(42)")
x = named.X(42)
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XX(42)")
x = named.XX(42)
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XXX(42)")
x = named.XXX(42)
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XXXX(42)")
x = named.XXXX(42)
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("x = named.XXXX(42.0)")
x = named.XXXX(42.0)
print("x = %s" % (x,))
print("x.Value() = %s" % (x.Value(),))

print("s = named.Str()")
s = named.Str()
print("s = %s" % (s,))
print("s.Value() = %r" % (s.Value(),))

print("s = named.Str('string')")
s = named.Str("string")
print("s = %s" % (s,))
print("s.Value() = %r" % (s.Value(),))
