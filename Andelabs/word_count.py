def word_count(a):
    if isinstance(a, str):
        a = a.split()


return "{} : {}".format(i, a.count(i))

print word_count("word count")

# a = "mine two"
# print (a).split()
# b = a.split()
# print b.count(i) for i in b
