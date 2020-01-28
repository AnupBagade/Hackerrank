"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""
import re


def pig_it(s):
    s_list = s.split(' ')
    res = []
    # print(s_list)
    for word in s_list:
        # print(word)
        if word.isalpha():
            print(word)
            chr_first = re.search(r'^[a-zA-Z]', word).group()
            print(chr_first)
            chs_remaining = re.sub(chr_first, '', word, 1)
            print(chs_remaining)
            res.append(chs_remaining + chr_first + 'ay')
        else:
            res.append(word)

    return ' '.join(res)


if __name__ == '__main__':
    # print(pig_it('Pig latin is cool'))
    # print(pig_it('This is my string !'))
    # print('Hic et nunc')
    print(pig_it('circenses'))
