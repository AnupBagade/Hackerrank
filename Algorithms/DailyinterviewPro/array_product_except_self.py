"""
You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.
"""

import numpy as np

def array_product(num):
    res = []
    def get_product(n):
        np_list = np.array(n)
        np_list = np.prod(np_list)
        return np_list

    for i in range(len(num)):
        res.append(get_product(num[0:i]+num[i+1:]))

    return res
if __name__ == '__main__':
    nums = input('Please provide input list ')
    nums = list(map(int,nums.strip('[]').split(',')))
    res = array_product(nums)
    print('Result - {}'.format(res))