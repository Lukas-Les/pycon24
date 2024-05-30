from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int


p = Point(0, 10, 0)

match p:
    case Point(0, 0, 0):
        print("Origin")
    case Point(0, y, 0):
        print(f"{y} units along the Y axis")
    case Point(x, 0, 0):
        print(f"{x} units along the X axis")
    case Point(0, 0, z):
        print(f"{z} units along the Z axis")
    case Point(x, y, z):
        print(f"{x} {y} {z}")


p = Point(0, 10, 0)

match p:
    case Point(0, 0, 0):
        print("Origin")
    case Point(0, _, 0) | Point(_, 0, 0) | Point(0, 0, _):
        print("along the axis")
    case Point(x, y, z):
        print(f"{x} {y} {z}")
