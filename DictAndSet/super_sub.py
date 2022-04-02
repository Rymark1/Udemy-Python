animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat'
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'birds is a subset of animals: {birds <= animals}')
print(f'birds is a proper subset of animals: {birds < animals}')
print(f'animals is a subset of birds: {animals.issubset(birds)}')
print(f'animals is a subset of birds: {animals <= birds}')
print(f'animals is a proper subset of birds: {animals < birds}')

# super_sub and subsets are not communicative.
print(f'animals is a superset of birds: {animals.issuperset(birds)}')
print(f'birds is a superset of animals: {birds.issuperset(animals)}')

print("*" * 80)

garden_birds = {'Robin', 'Swallow', 'Wren'}
print(birds == garden_birds)
print(garden_birds <= birds)
print(garden_birds < birds)
print("*" * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)

# Python doesn't have a disjoint method.
