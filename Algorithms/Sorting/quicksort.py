
class Quicksort:

    def __init__(self):
        pass

    def partition_index(self, input_list, st_index, en_index):
        pivot = input_list[en_index]
        pi_index = st_index
        for i in range(st_index,en_index):
            if input_list[i] <= pivot:
                input_list[i], input_list[pi_index] = input_list[pi_index], input_list[i]
                pi_index += 1
        input_list[pi_index], input_list[en_index] = input_list[en_index], input_list[pi_index]
        return pi_index

    def quicksort(self, inp_arr, start, end):
        if start < end:
            part_index = self.partition_index(inp_arr, start, end)
            self.quicksort(inp_arr, start, part_index-1)
            self.quicksort(inp_arr, part_index+1, end)

    def get_sorted(self, input_array):
        if len(input_array)>1:
            start = 0
            end = len(input_array) - 1
            self.quicksort(input_array, start, end)
            return input_array
        else:
            if len(input_array) == 1:
                return input_array
            else:
                return 'Invalid input.'

if __name__ == '__main__':
    sorting_obj = Quicksort()
    result = sorting_obj.get_sorted([8,6,1,2,4,3,9,7,5])
    print(result)
    result = sorting_obj.get_sorted([1])
    print(result)
    result = sorting_obj.get_sorted([])
    print(result)
