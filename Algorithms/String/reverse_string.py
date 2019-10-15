"""
Reverse a string using recurssion
"""


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


if __name__ == '__main__':
    input_string = input('Please enter string to be reversed ')
    result = reverse_string(input_string)
    print('String reversed - {}'.format(result))