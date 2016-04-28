def word_count(a):
	if isinstance(a, str):
		a = a.split()
		for i in a:
			n = ''
			n += "{} : {}".format(i, a.count(i))
	return n
print word_count("word count word book")

# a = "mine two"
# print (a).split()
# b = a.split()
# print b.count(i) for i in b
# a = a.split()
#     for i in a:
#     	if isinstance(i, a):return "{} : {}".format(i, a.count(i))
