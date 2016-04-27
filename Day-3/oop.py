class Person:
    people_count = 0  # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people_count += 1

    def __repr__(self):
        return " <{}, {}>".format(self.name, self.age)

    def say_hello(self):
        return "Hello, I am {} and {} y/o".format(self.name, self.age)


p = Person('Likey', 29)
print p.name
print p.people_count
print p.say_hello()
p1 = Person('Jenty', 12)
print p.people_count
p2 = Person("Ken", 34)
print p2.people_count

a = [('Jane', 23),
     ('Jackie', 34),
     ("Manning", 12),
     ("linada", 89)
     ]

b = []
for name, age in a:
    person = Person(name, age)
    b.append(person)

print b

for person in b:
    print person.say_hello()
