people = [
    ('joe', 56),
    ('jane', 18),
    ('migun', 16)
]


def super_sum(*args):
    return sum(args)


def hello_again(name, age):
    return "I am {} and {} years old".format(name, age)


def max_min(A):
    '''
    Returns max value - min value
    '''
    # return max(A) - max(A)
    max_, min_ = A[0], A[0]
    for i in A:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    return max_ - min_

print max_min([20, 30, 50])
