"""
You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
"""
import ast

def two_sum(nums, target):
    buff_dict = {}
    n = len(nums)
    status = 'No match'
    for i in range(len(n)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]],i]
        else:
            buff_dict[target - nums[i]] = i

    return status

if __name__ == '__main__':
    user_input1 = ast.literal_eval(input('Please provide list input'))
    user_input1 = [int(i) for i in user_input1]
    user_input2 = int(input('Please provide target'))
    result = two_sum(user_input1, user_input2)
    print(result)
