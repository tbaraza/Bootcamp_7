def find_missing(A, B):
	A = set(A)
	B = set(B)
	if A != B:
		b = list(B - A)
		return b[0]
	else:
		return 0
   

print find_missing([1, 2], [1, 2])
print find_missing([1, 2, 3], [1, 2, 3, 4])
print find_missing([4, 6, 8], [4, 6, 8, 10])
print find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])


def find_missing(A, B):
    if A == B:
        return 0

    if A != B:
        a = ''
        for i in A:
            if i not in B:
                a = i
        for j in B:
            if j not in A:
                a = j
    return a

print find_missing([1, 2], [1, 2])
print find_missing([1, 2, 3], [1, 2, 3, 4])
print find_missing([4, 6, 8, 10], [4, 6, 8])
print find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])

# def find_missing(first, second):
#     len_first = len(first)
#     len_second = len(second)
#     if len_first == len_second:
#         return 0
#     else:
#         for i in second:
#             if i not in first:
#                 return i