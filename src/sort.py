

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
    :param num_list: a list of numbers that needs to be sorted
    :param num_size: number of numbers in the list
    :param gap_values: integer, how much numbers to skip when comparing
    :return: sorted list
    """

    for g in gap_values:
        for i in (range(g)):  # if gap is 3, need to run start_idx 0,1,2
            insertion_sort_interleaved(num_list, num_size, i, g)
    return num_list


def partition(num_list, low_index, high_index):
    """
    Helper method for quick sort function
    :param num_list: a list of numbers that needs to be sorted
    :param low_index: low index of the list to be sorted
    :param high_index: high index of the list to be sorted
    :return: final high index value, which is the end index for the lower partition
    """
    # pick middle element
    midpoint = int(low_index + int(high_index - low_index)/2)
    pivot = num_list[midpoint]

    # could use done = False first, and set done = low_index >= high_index after the while loops
    while low_index < high_index:
        # increment low index while num_list[low_index] < pivot
        while num_list[low_index] < pivot:
            low_index += 1

        # decrement high index while num_list[high_index] > pivot
        while num_list[high_index] > pivot:
            high_index -= 1

        # if low_index is still smaller than high index after the above code
        # swap num_list[low_index] and num_list[high_index] bc they are at the wrong bucket
        if low_index < high_index:
            num_list[low_index], num_list[high_index] = num_list[high_index], num_list[low_index]

            # update low_index and high_index
            low_index += 1
            high_index -= 1

    return high_index


def quick_sort(num_list, low_index, high_index):
    """
    Quick sort method to sort a number list
    :param num_list: a list of numbers that needs to be sorted
    :param low_index: low index of the list to be sorted
    :param high_index: high index of the list to be sorted
    :return: a sorted list
    """

    # base case: if the partition size is 1 or zero elements, then the partition is already sorted
    if low_index >= high_index:
        return

    # save low_end_index, which is the high_index from previous partition
    low_end_index = partition(num_list, low_index, high_index)
    print(num_list)

    # recursively sort low partitions and high partitions
    quick_sort(num_list, low_index, low_end_index)
    quick_sort(num_list, low_end_index + 1, high_index)


def merge(num_list, left_first, left_last, right_last):
    merged_size = right_last - left_last + 1
    merged_nums = []

    left_pos = left_first
    right_pos = left_last + 1

    # Add smallest element from left or right partition to merged numbers
    while (left_pos <= left_last) and (right_pos <= right_last):
        if num_list[left_pos] < num_list[right_pos]:
            merged_nums.append(num_list[left_pos])
            left_pos += 1
        else:
            merged_nums.append(num_list[right_pos])
            right_pos += 1

    # If left partition is not empty, add remaining elements to merged numbers
    while left_pos <= left_last:
        merged_nums.append(num_list[left_pos])
        left_pos += 1

    # If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= right_last:
        merged_nums.append(num_list[right_pos])
        right_pos += 1

    # Copy merge numbers back to numbers
    for merge_pos in range(merged_size):
        num_list[left_first + merge_pos] = merged_nums[merge_pos]

    print(num_list)


def merge_sort(num_list, left_first, right_last):

    if left_first < right_last:
        left_last = int((left_first + right_last)/2)

        # recursively sort left and right partitions
        merge_sort(num_list, left_first, left_last)
        merge_sort(num_list, left_last + 1, right_last)

        # merge left and right partitions in sorted order
        merge(num_list, left_first, left_last, right_last)


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

    example_list1 = [10, 2, 78, 4, 45, 32, 7, 11]
    print()
    print("=== quick_sort test1 ===")
    quick_sort(example_list1, 0, 7)

    example_list2 = [6, 4, 7, 18, 8]
    print()
    print("=== quick_sort test2 ===")
    quick_sort(example_list2, 0, 4)

    import sys
    sys.setrecursionlimit(5000)

    example_list1 = [6, 4, 7, 18, 8]
    print()
    print("=== merge_sort test1 ===")
    merge_sort(example_list2, 0, 4)

    example_list2 = [8, 4, 7, 18, 8]
    print()
    print("=== merge_sort test2 ===")
    merge_sort(example_list2, 0, 4)
