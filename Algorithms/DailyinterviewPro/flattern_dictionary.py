"""
Given a nested dictionary, flatten the dictionary, where nested dictionary keys
can be represented through dot notation.

Example:
Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
"""


def flatten(dict_obj, parent=None, result_obj):
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            flatten(value, key)
        if parent:
            for k, v in result_obj.items():
                result_obj[parent+'.'+k] = v
                del result_obj[k]


if __name__ == '__main__':
    flatten({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}})
