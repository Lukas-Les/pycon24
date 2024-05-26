import inspect

from typing import Optional


def f(*args):
    """This text"""
    res = 0
    for x in args:
        res += x
    return res


print("Docstring:")
print(f.__doc__)
f.__doc__ = "This is a dynamically generated docstring"
print(f.__doc__)

print("Name:")
print(f.__name__)
f.__name__ = "adder"
print(f.__name__)

params = [
    inspect.Parameter("x", inspect.Parameter.POSITIONAL_OR_KEYWORD, default=0, annotation=Optional[float]),
    inspect.Parameter("y", inspect.Parameter.POSITIONAL_OR_KEYWORD, default=0, annotation=Optional[float]),
    inspect.Parameter("z", inspect.Parameter.POSITIONAL_OR_KEYWORD, default=0, annotation=Optional[float]),
]

f.signature = inspect.Signature(parameters=params, return_annotation=float)

print("Signature:")
print(inspect.signature(f))
print(f(1, 2, 3))
print(f(1, 2))