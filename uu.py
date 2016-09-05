def flatten_dict(a, result={}):
    if result is None:
        result = {}

    for x in a:
        if isinstance(x, dict):
            flatten_dict(x,result)
        else:
            result.add(x)
            return result
a=flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
print a