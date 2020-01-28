"""
You are given an array of integers. Return the length of the longest
consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive
 sequence 1, 2, 3, 4, and thus, you should return its length, 4.

def longest_consecutive(nums):
  # code.

print longest_consecutive([100, 4, 200, 1, 3, 2])
[1, 3, 6, 7, 5, 0, 4]
"""


def longest_consecutive(num):
    res = [0]
    cons_res = []
    status = False

    for val in num:
        if val - 1 in num:
            if val < max(res):
                continue

            if not status:
                cons_res.append(val)
                val = val - 1
                while val in num:
                    cons_res.append(val)
                    val = val - 1
                status = True

            if status and len(res) <= len(cons_res):
                res = cons_res[::]
                cons_res = []
                status = False

    return len(res)


if __name__ == '__main__':
    print(longest_consecutive([1, 3, 5, 7, 9]))
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive([1, 3, 6, 7, 5, 0, 4]))
    print(longest_consecutive([100, 99, 98]))
