"""
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
"""


def search_unique_number(nums):
    buff_dict = {}
    for num in nums:
        if buff_dict.get(num,0) == 0:
            buff_dict[num] = 1
        else:
            del buff_dict[num]
    return list(buff_dict.keys())[0]



if __name__ == '__main__':
    userinput_nums = input('Please enter the list of numbers').strip('[]').split(',')
    userinput_nums = [int(val) for val in userinput_nums]
    result = search_unique_number(userinput_nums)
    print('Unique number in the list - {}'.format(result))