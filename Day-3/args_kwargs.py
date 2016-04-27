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


def super_sum(*args):
    '''
    Takes in variable umber of items,
    and returns the sum.
    e.g. super_sum(10, 20) = 30
        super-sum(10, 20, 40) = 70
        super_sum91, 4, 5, 6, 7) = 23
    '''
    total = 0
    for i in args:
        total += i
    return total


print super_sum(12, 3, 5)
print super_sum(30)
print super_sum(10, 40, 50, 70, 30)


def hello_again(**kwargs):
    return " I am {}, and I am {}.".format(kwargs['name'], kwargs['age'])

print hello_again(name='joe', age=20)
print hello_again(age=20, name='Toni')

other_people = [
    {'name': "joe", 'age': 23},
    {'name': "Jenty", 'age': 34},
    {'name': "Rina", 'age': 29}

]
joe = {'name': 'Joe', 'age': 23}
print hello_again(**joe)

for k in other_people:
    print hello_again(**k)
