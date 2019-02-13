```from dog import Dog

d1 = Dog('fido', 3, 'male')
d2 = Dog('sally', 5, 'female')
print('before', d1)
d1.eat()
print('after eating', d1)
d1.play()
print('after playing', d1)

# instructions
# read in dogs.txt
# create a dog for
# every entry
# add all dogs
# to a dogs array
# find the average age
# of these dogs
# and the standard deviation```

```class Dog:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = 5

    def __str__(self):
        return "{} is a {} dog, {} years old, weighs {} lbs".format(
            self.name, self.sex, self.age, self.weight
        )

    def __repr__(self):
        return self.__str__()

    def eat(self):
        self.weight += 2

    def play(self):
        self.weight -= 1```