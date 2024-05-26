# currying
def plus(a):
    def add(b):
        return a + b
    return add


plus_1 = plus(1)(2)
print(plus_1)
