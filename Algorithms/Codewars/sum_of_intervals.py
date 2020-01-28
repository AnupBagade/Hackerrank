"""
    Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

"""


def sum_of_intervals(x):
    result = dict()
    result[x[0][0]] = x[0][1]
    added = False
    sum = 0
    for val in x:
        a = val[0]
        b = val[1]

        for k, v in result.items():
            if k <= a and a <= v-1:
                if b >= v:
                    result[k] = b
                    added = True
                    break

        if not added:
            result[a] = b
        else:
            added = False

    for k, v in result.items():
        sum += v-k

    print(sum)


if __name__ == '__main__':
    # Test.assert_equals(sum_of_intervals([(1, 5)]), 4)
    # Test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
    # Test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
    # Test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
    sum_of_intervals([(1, 1147483640), (147483640, 87483640), (1147483643, 2147483647)])
