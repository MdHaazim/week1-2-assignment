# funtion to merge 2 dictionaries together
def merge_dicts(dict1, dict2):

    # copy contents of dict1 to dict3
    dict3 = dict1.copy()

    # update contents of dict3 with dict 2
    dict3.update(dict2)

    #return dict3
    return dict3

# initialise the dictionaries
dict1 = {'a': 10, 'b': 4, 'c': 4}
dict2 = {'b': 3, 'c': 1, 'd': 8}

# merge the dictionaries
merged_dict = merge_dicts(dict1, dict2)

# output the merged dictionary
print(merged_dict)
