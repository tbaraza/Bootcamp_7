def hello(name, age, class_=''):
    '''
    implementation of args and kwargs
    '''
    if class_ != '':
        return "I am {}, {} y/o and {} class".format(name, age, class_)
    return "I am {}. and I'm {}".format(name, age)


people = [
    ("jane", 23,),
    ("Tonida", 45, 'high'),
    ("Brian", 34, "high"),
    ("Omondi", 67,),
    ("Like", 34, "high")
]

# for name, age in people:
#     print hello(name, age)

for x in people:
    print hello(*x)
