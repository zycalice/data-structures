
def binary_search(num_list, low, high, target):
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
    print(binary_search([1, 2, 3, 5], 0, 4, 4))
    print(binary_search([1, 2, 3, 5], 0, 4, 3))
