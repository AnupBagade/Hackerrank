"""
Longest substring without repeating characters.
Example: 'ABDEFGABEF' => 'ABDEFG' or 'BDEFGA' or 'DEFGAB' => length = 6
"""


def longest_substring(s):
    characters = set(s)
    char_count = {}
    sub_string = ''
    l = 0
    r = 0

    while r < len(s):
        if s[r] not in char_count:
            char_count[s[r]] = r
            r += 1
            if len(characters) == len(char_count):
                temp = s[char_count[min(char_count, key=char_count.get)]: char_count[max(char_count, key=char_count.get)]+1]
                if len(temp) > len(sub_string) or len(sub_string) == 0:
                    sub_string = temp
        else:
            char_count[s[r]] = r
            r += 1
            l += 1


    return sub_string

if __name__ == '__main__':
    input_string = input('Please enter the string ')
    result = longest_substring(input_string)
    print('Longest substring is {0} and length is {1}'.format(result, len(result)))