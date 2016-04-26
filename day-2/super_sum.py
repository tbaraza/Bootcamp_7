def super_sum(A):
    '''
    Takes in a list A, and:
            -Halves every even number
            -Doubles every odd number
    And returns the sum of all
    '''
    total = 0

    for i in A:
        if i % 2 == 0:
            total += (i / 2)
        else:
            total += 1 * 2

    return total


print super_sum([10, 20, 30])
