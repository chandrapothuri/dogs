from dog import Dog
import stats as s

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
# and the standard deviation
 
doglist = []
dogages = []

with open('dogs.txt') as f:
    for line in f:
    dog = line.strip().split(',')
    doglist.append(Dog(dog[0], int(dog[1]), dog[2]))
    dogages.append(int(dog[1]))

avg_age = s.mean(dogages)
age_std_dev = s.variance(dogages)**(1 / 2)
print(doglist, avg_age, age_std_dev) 
