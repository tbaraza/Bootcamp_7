def data_type(x):
    """
    Takes in an argument x:
            - For an integer , return x ** 2
            - For a float, return x/2
            - For a string, returns "Hello " + x
            - For a boolean, return "boolean"
            - For a long, return squaroot of x
    """
    if isinstance(x, int):
        return x ** 2

    elif isinstance(x, float):
        return x / 2

    elif isinstance(x, str):
        return "Hello {}".format(x)

    elif isinstance(x, bool):
        return "boolean"

    elif isinstance(x, long):
        return "long"

    else:
        return "That'a not a primitive data type"


print data_type(24)
print data_type(25.67)
print data_type("Tonida")
print data_type(True)
print data_type(456 ** 456)
print data_type([2, 3])
