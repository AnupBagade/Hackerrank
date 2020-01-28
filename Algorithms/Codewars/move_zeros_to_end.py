def move_zeros(array):
    original_array = array[:]
    num_items_moved = 0

    for index, item in enumerate(original_array):
        try:
            if int(item) == 0 and not (item is False):
                value = int(array.pop(index - num_items_moved))
                array.append(value)
                print(index, item)
                num_items_moved += 1
        except Exception as exception:
            print(str(exception))
            continue

    return array


if __name__ == '__main__':
    res = move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False,
                      0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9])
    print(res)
