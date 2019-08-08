"""
https://www.hackerrank.com/challenges/electronics-shop/problem

"""
import os


def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort()
    res = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            total_amount = keyboards[i] + drives[j]
            if total_amount <= b and total_amount > res:
                res = total_amount
            elif total_amount > b:
                break

    if res == 0:
        return -1
    else:
        return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
