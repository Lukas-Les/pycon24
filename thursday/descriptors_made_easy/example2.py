class Dont:
    pass


class RODescriptor:
    def __set_name__(self, cls, attr_name):
        print("called __set_name__")
        self.attr_name = attr_name

    def __get__(self, obj, _):
        return getattr(
            obj,
            f"_{self.attr_name}"
        )

    def __set__(self, obj, value):
        raise Dont("STOP")


class Person:
    first = RODescriptor()
    last = RODescriptor()

    def __init__(self, first, last) -> None:
        self._first = first
        self._last = last


p = Person("J", "S")

print(p.first)

p.first = "A"

print(p.first)
