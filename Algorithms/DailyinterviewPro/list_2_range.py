"""
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.
"""

def num_range(num):
    consecutive_start = False
    start = num[0]
    res = {}
    for i in range(len(num)-1):
        if not consecutive_start:
            start = num[i]
        temp_1 = num[i]
        temp_2 = num[i+1]
        if temp_1 == temp_2:
            res[start] = temp_2
        else:
            if temp_2 == temp_1 + 1:
                res[start] = temp_2
                consecutive_start = True
            else:
                if start == num[i]:
                    res[start] = start
                consecutive_start = False
    res = [str(i)+'->'+str(v) for i,v in res.items()]
    return res


if __name__ == '__main__':
    num = input('Please enter list of numbers ')
    num = list(map(int,num.strip('[]').split(',')))
    res = num_range(num)
    print('List of ranges - {}'.format(res))