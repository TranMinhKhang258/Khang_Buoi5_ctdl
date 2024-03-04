def max_value_key(my_dict):
    if len(my_dict) == 0:
        return None
    max_value = max(my_dict.values())
    for key, value in my_dict.items():
        if value == max_value:
            return key

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
