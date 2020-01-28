'''
Given a non-empty list of words, return the k most frequent words.
The output should be sorted from highest to lowest frequency,
and if two words have the same frequency, the word with lower
alphabetical order comes first. Input will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro",
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
'''


from collections import defaultdict


def frequent_word(s, k):
    s_set = set(s)
    count_dict = defaultdict(list)
    i = 0
    res = []
    for word in s_set:
        count_dict[s.count(word)].append(word)
    count_dict = dict(count_dict)

    while i < k:
        temp = sorted(count_dict[max(count_dict)])
        i += len(temp)
        res.extend(temp)
        del count_dict[max(count_dict)]
    return res


if __name__ == '__main__':
    print(frequent_word(["daily", "interview", "pro", "pro", "for", "daily",
                         "pro", "problems"], 2))
    print(frequent_word(["banana", "apple", "pro", "pro", 'pro', "for", "daily",
                         "apple", "banana"], 2))
    print(frequent_word(["daily", "interview", "pro", "pro", "for", "daily",
                         "pro", "problems"], 2))
