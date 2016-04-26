def funky(a, b):
	"""
	takes two arguments and returns
	the sum of the respective data types giving out necessary
	message for data types that cannot be summed up
	"""

    if type(a) == dict and type(b) == dict:
        a.update(b)
        return a
    elif type(a) is int and type(b) is float or type(a) is float and type(b) is int:
        return a + b
    elif type(a) is not type(b):
        return "invalid summation of data types"
    else:
        return a + b

print([1, 2], {1: "me", 2: "you"})
print funky(1.777, 34)
print funky(34, 56)
print funky({1: "boy", 3: "you"}, {3: "girl"})
print funky("lion", 34)
print funky(2.3444, 45.7)
print funky("toni", "da")
print funky([1, 2], [5, 6])
print funky("toni", [3, 4, 5])
