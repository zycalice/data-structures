

def binary_search(num_list, low, high, target):
    """
    binary search recursively
    :param num_list: a sorted list of numbers to search for
    :param low: starting index
    :param high: ending index
    :param target: the number to search for
    :return: the position index of the target number; -1 if not found
    """
    # base case
    if low > high:
        return -1

    # recursive case
    mid = (low + high) // 2

    if target < num_list[mid]:
        return binary_search(num_list, low, mid-1, target)

    if target > num_list[mid]:
        return binary_search(num_list, mid+1, high, target)

    return mid


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 5], 0, 3, 4))
    print(binary_search([1, 2, 3, 5], 0, 3, 5))
