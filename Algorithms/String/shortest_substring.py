"""
Return the minimum length of substring having all characters of string.
Example:
    Input = 'abddcabcdab'
    output = 4 (abcd) (index - 5 to 8)
"""


def shortest_substring(s):
    unique_characters = set(s)
    substrings = {}
    small_substring = ''

    for i, character in enumerate(s):
        if character in unique_characters:
            substrings[character] = i
            if len(substrings) == len(unique_characters):
                temp = s[substrings[min(substrings, key=substrings.get)]: substrings[max(substrings, key=substrings.get)]+1]
                if len(temp) < len(small_substring) or len(small_substring) == 0:
                    small_substring = temp
    return len(small_substring)


if __name__ == '__main__':
    input_string = input('Enter string ')
    res = shortest_substring(input_string)
    print(res)