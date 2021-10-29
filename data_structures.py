# Tuple
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))

# Dictionary
dictionary = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
del dictionary['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(dictionary)))
for name, address in dictionary.items():
    print('Contact {} at {}'.format(name, address))

# List
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])

# Set
countries = set(['brazil', 'russia', 'india'])
print("bri set: ", countries)
all_countries = countries.copy()
all_countries.add('china')
print("bric set: ", all_countries)
print("bric.issuperset(bri): ", all_countries.issuperset(countries))
countries.remove('russia')
print("bri & bric: ", countries & all_countries)