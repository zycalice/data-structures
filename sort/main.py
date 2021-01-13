

def selection_sort(num_list):
    """
    Sort using selection sort algorithm; runtime is O(N^2)
    :param num_list: a list of numbers that needs to be sorted
    :return: a list of sorted numbers
    """

    # find index of the smallest remaining element
    for i in range(len(num_list) - 1):  # minus 1 bc there is no need to swap when only one element left
        print(i)
        index_smallest = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[index_smallest]:
                index_smallest = j

        # swap index i and index_smallest
        num_list[i], num_list[index_smallest] = num_list[index_smallest], num_list[i]
        print(num_list)
    return num_list


def insertion_sort(num_list):
    """
    Sort using insertion sort algorithm; runtime is typically O(N^2) for unsorted list, but O(N) for nearly sorted list
    :param num_list: a list of numbers that needs to be sorted
    :return: a list of sorted numbers
    """

    for i in range(1, len(num_list)):
        print(i)
        j = i
        while j > 0 and num_list[j - 1] > num_list[j]:
            # swap num_list[j - 1] and num_list[j]
            temp = num_list[j - 1]
            num_list[j - 1] = num_list[j]
            num_list[j] = temp
            j -= 1
        print(num_list)
    return num_list


def insertion_sort_interleaved(num_list, num_size, start_idx, gap):
    """
    This function will only sort interleaved lists based on index
    :param num_list: a list of numbers that needs to be sorted
    :param num_size: number of numbers in the list
    :param start_idx: starting index of the sort
    :param gap: number of gaps for the interleaved list
    :return: a list of numbers that is sorted on the interleaved list specified by start_idx and gap
    """

    for i in range(start_idx + gap, num_size):  # if start_idx + gap > num_size, this loop is never entered
        print("start_idx:", start_idx, ", gap:", gap, ", i:", i)
        j = i
        while j > 0 and num_list[j - gap] > num_list[j]:
            # swap num_list[j - gap] and num_list[j]
            temp = num_list[j - gap]
            num_list[j - gap] = num_list[j]
            num_list[j] = temp
            j -= 1
        print(num_list)
    return num_list


def shell_sort(num_list, num_size, gap_values):
    """
    Calls interleaved insertion sort
    Shell sort tends to perform well when choosing gap values in descending order.
    A common option is to choose powers of 2 minus 1, in descending order.
    Ex: For an array of size 100, gap values would be 63, 31, 15, 7, 3, and 1.
    Shell sort ends with a final gap value of 1, to finish with the regular insertion sort.
    :param num_list:
    :param num_size:
    :param gap_values:
    :return:
    """

    for g in gap_values:
        for i in (range(g)):  # if gap is 3, need to run start_idx 0,1,2
            insertion_sort_interleaved(num_list, num_size, i, g)
    return num_list


if __name__ == '__main__':
    example_list = [9, 1, 0, 3]
    print()
    print("=== selection sort ===")
    selection_example = selection_sort(example_list)

    example_list = [9, 1, 0, 3]
    print()
    print("=== insertion sort ===")
    insertion_example = insertion_sort(example_list)

    example_list = [9, 1, 0, 3]
    print()
    print("=== shell sort ===")
    shell_sort(example_list, len(example_list), [3, 1])
