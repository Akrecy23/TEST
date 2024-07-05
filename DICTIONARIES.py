my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)

values = my_dict.values()
print(values)

items = my_dict.items()
print(items)

age = my_dict.get('age')
print(age)  # Output: 30

# With a default value
middle_name = my_dict.get('middle_name', 'Not Provided')
print(middle_name)  # Output: Not Provided

new_info = {'age': 31, 'city': 'San Francisco'}
my_dict.update(new_info)
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'San Francisco'}

age = my_dict.pop('age') #if age is irrelevant, can just my_dict.pop('age')
print(age)  # Output: 31
print(my_dict)  # Output: {'name': 'John', 'city': 'San Francisco'}

# With a default value
middle_name = my_dict.pop('middle_name', 'Not Provided')
print(middle_name)  # Output: Not Provided