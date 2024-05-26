class RGBDescriptor:
    def __init__(self, pos) -> None:
        self.pos = pos

    def __get__(self, color, _):
        p = self.pos
        return int(color.hex[p + 1: p + 3], 16)


class RGBColor:
    r = RGBDescriptor(0)
    g = RGBDescriptor(2)
    b = RGBDescriptor(4)

    def __init__(self, hex_color):
        self.hex = hex_color


red = RGBColor("#ff0000")
print(red.r)
print(red.g)
print(red.b)
