def super_sum(*args):
    """
    Returns a sum of numbers.
    e.g
            super_sum() ==> "Please enter numbers"
            super_sum("string") ==> 0
            super_sum(1, 2, 3) ==> 6
            super_sum([1, 2, 3]) ==> 6
            super_sum([10], [20, 30]) ==> 60
    """
    total = 0
    if args:
        for x in args:
            if type(x) is list:
                total += sum(x)
            elif type(x) is str:
                return 0
            else:
                total += x
        return total
    return 0
