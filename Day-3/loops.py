a = [12, 3, 4, 6, 78, 56]

for i in a:
    print i

    # primitive reverse

i = len(a)
while i > 0:
    print a[i - 1]
    i -= 1

# edge cases
for x in range(len(a) - 1, -1, -1):
    print a[x]

b = [(2, 4), (5, 10), (6, 20), (50, 50)]
'''
x:2, y:4
'''
for n in b:
    print "x: {}, y: {}". format(n[0], n[1])

for x, y in b:
    print "x: {}, y: {}". format(x, y)


f = [(1, 20, 40), (10, 40), (4, 50, 10), (2, 4, 6, 7)]

for d in f:
    if len(d) > 2:
        print "x: {}, y: {}, z: {}". format(d[0], d[1], d[2])
    else:
        print " x: {}, y: {}". format(d[0], d[1])
