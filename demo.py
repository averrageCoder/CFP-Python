# Write a function `merge_dicts` that takes two dictionaries
# as inputs and merges them into a single dictionary.
# If there are duplicate keys between the two dictionaries, the
# resultant dictionary's key should map to a list of the two
# values obtained from each dictionary.
#
# NOTE: Please do not use defaultdict. Your function should handle this.
#
# e.g. 1 & TC 1:
# _d1 = {1:2, 3:4, 'a':'b'}
# _d2 = {0:1, 4:4, 10:'a'}
# result = {1: 2, 3: 4, 'a': 'b', 0: 1, 4: 4, 10: 'a'}
#
# e.g. 2 & TC 2:
# _d1 = {1:2, 3:4, 10:5}
# _d2 = {3:1, 4:4, 10:'a'}
# result = {1: 2, 4: 4, 10: [5, 'a'], 3: [4, 1]}
#
# e.g. 3 & TC 3:
# _d1 = {1:2, 3:4, 'a':'b'}
# _d2 = {3:1, 4:4, 10:'a', 'a':[1,2,3]}
# result = {1: 2, 4: 4, 10: 'a', 'a': ['b', [1, 2, 3]], 3: [4, 1]}

def merge_dicts(dict1, dict2):
    result_dict = dict1
    for key, value in dict2.items():
        if key in result_dict:
            result_dict[key] = [result_dict[key], value]
        else:
            result_dict[key] = value
    return result_dict

_d1 = {1:2, 3:4, 10:5}
_d2 = {3:1, 4:4, 10:'a'}

print(merge_dicts(_d1, _d2))

_d1 = {1:2, 3:4, 'a':'b'}
_d2 = {3:1, 4:4, 10:'a', 'a':[1,2,3]}

print(merge_dicts(_d1, _d2))

_d1 = {1:2, 3:4, 'a':'b'}
_d2 = {0:1, 4:4, 10:'a'}

print(merge_dicts(_d1, _d2))