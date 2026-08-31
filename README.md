# Newton Practice

This repository contains a basic implementation of Newton's method for minimizing a one-dimensional function in Python.

The first and second derivatives are estimated using finite differences. The implementation does not use any external differentiation packages.

## Usage

```python
import newton

def test_function(x):
    return (x - 3) ** 2 + 5

minimum = newton.optimize(0, test_function)
print(minimum)
```

The result should be close to `3.0`.
