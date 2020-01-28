"""
magine you are building a compiler. Before running any code, the compiler must
check that the parentheses in the program are balanced. Every opening bracket
must have a corresponding closing bracket.
We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

"""


def validate_parenthesis(input_str):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    brackets_open = ['(', '{', '[']
    brackets_close = [')', '}', ']']
    l1 = []
    input_str = list(input_str)
    status = True

    if len(input_str) == 0:
        return status

    for bracket in input_str:
        if bracket in brackets_open:
            l1.append(bracket)
        elif bracket in brackets_close:
            if len(l1) > 0:
                if brackets.get(bracket) != l1.pop(-1):
                    status = False
                    return status
            else:
                status = False
                return status
        else:
            status = False

    return status


if __name__ == '__main__':
    user_input = input('Please enter input string')
    res = validate_parenthesis(user_input)
    print('Output - {}'.format(res))
