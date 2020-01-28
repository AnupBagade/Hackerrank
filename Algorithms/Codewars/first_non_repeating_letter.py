from collections import OrderedDict
import re


def first_non_repeating_letter(string):
    letter_dict = OrderedDict()
    string = re.sub(r'\s+', '', string)
    unique = False
    if len(string) == 0:
        return ''
    else:
        for value in string:
            if letter_dict.get(value, 0) == 0:
                letter_dict[value] = 1
            else:
                letter_dict[value] += 1

        for key, value in letter_dict.items():
            if key.isalpha():
                if key.isupper():
                    if value == 1 and letter_dict.get(key.lower(), 0) == 0:
                        unique = True
                        return key
                elif key.islower():
                    if value == 1 and letter_dict.get(key.upper(), 0) == 0:
                        unique = True
                        return key
            else:
                if value == 1:
                    unique = True
                    return key
        if not unique:
            return ''


if __name__ == '__main__':
    res = first_non_repeating_letter(r"""EQDWTzXhHOPgTnNq5.KEGgEO4giC:xYeGmnu
    ,gqG4KMRvD3D""")
    print(res)
