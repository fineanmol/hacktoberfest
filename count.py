list1 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'),
		('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]

# Counts the number of times 'Cat' appears in list1
print(list1.count(('Cat', 'Bat')))

# Count the number of times sublist
# '[1, 2]' appears in list1
print(list1.count([1, 2]))
