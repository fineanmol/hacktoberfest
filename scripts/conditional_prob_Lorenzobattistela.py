# Github: Lorenzobattistela
# REPRESENTATION OF PROBABILITY OF x CONDICIONED BY y
# References: Data Science from zero by Joel Grus

import enum, random

class Person(enum.Enum):
    MALE = 0
    FEMALE = 1
    
def random_person() -> Person:
    return random.choice([Person.MALE, Person.FEMALE])

both_females = 0
older_female = 0
either_female = 0

random.seed(0)

for _ in range(10000):
    younger = random_person()
    older = random_person()
    if older == Person.FEMALE:
        older_female += 1
    if older == Person.FEMALE and younger == Person.FEMALE:
        both_females += 1
    if older == Person.FEMALE or younger == Person.FEMALE:
        either_female += 1

print("P(both | older): ", both_females / older_female)
print("P(both | either): ", both_females / either_female)

