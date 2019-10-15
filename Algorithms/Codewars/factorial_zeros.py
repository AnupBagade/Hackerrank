def count_zeros(n):
    res = 0
    num = n
    while num > 5:
        res += num // 5
        num = num // 5
        print(num)
    return res


if __name__ == '__main__':
    res = count_zeros(6)
    print(res)