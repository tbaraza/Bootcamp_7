from person import Person
from kenyan import Kenyan

#class methods
# mixin
# instance variables vs class variables

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

# making age optional:
# set age=0
# in init use an if statement

k = Kenyan('Anita', 40)
k.probe(False)
print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()