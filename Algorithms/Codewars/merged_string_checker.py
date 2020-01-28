'''
At a job interview, you are challenged to write an algorithm to check
if a given string, s, can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2
should be in the same order as in s.
The interviewer gives you the following example and tells you to
figure out the rest from the given test cases.

For example:
'codewars' is a merge from 'cdw' and 'oears':
    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
'''


def merged_string_checker(s, s1, s2):
    i = j = 0
    m = len(s1)
    n = len(s2)
    print(m)
    print(n)
    print(len(s))
    status = True
    if len(s) != len(s1) + len(s2):
        status = False
        return status

    for val in s:
        if i < m and s1[i] == val:
            i += 1
        elif j < n and s2[j] == val:
            j += 1
        else:
            status = False
            break
    return status


if __name__ == '__main__':
    # print(merged_string_checker('codewars', 'code', 'wars'))
    # print(merged_string_checker('codewars', 'cdw', 'oears'))
    # print(merged_string_checker('codewars', 'code', 'warss'))
    print(merged_string_checker(r"Can we merge it? Yes, we can!", 'a wemei es,wcan!', 'Cn erg t?Y e'))
