my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Yura'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
a = my_dict.pop('Egor')
print(a)
print(my_dict)
my_set = {'Яблоко', 'Яблоко', 1, 1, 1, 'Яблоко', 'Яблоко', 42.314, 42.314, 42.314, 42.314}
print(my_set)
my_set.add(13)
my_set.update ({(5, 6, 1.6)})
my_set.remove(1)
print(my_set)
