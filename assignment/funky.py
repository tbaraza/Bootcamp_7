def funky(a, b):
    if type(a) == dict and type(b) == dict:
        a.update(b)
        return a
    elif type(a) is int and type(b) is float or type(a) is float and type(b) is int:
        return a + b
    elif type(a) is not type(b):
        return "invalid summation of data types"
    else:
        return a + b


print funky(1.777, 34)
print funky(34, 56)
print funky({1: "boy"}, {2: "girl"})
print funky("lion", 34)
print funky(2.3444, 45.7)
print funky("toni", "da")
