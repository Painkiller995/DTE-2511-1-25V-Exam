"""
Binary Search Implementation

This script implements the binary search algorithm to find the index of a target value in a sorted list.

How it works:
- Binary search divides the search space in half each iteration.
- It compares the target value to the middle element.
- If the target is equal to the middle, it returns the index.
- If the target is less, it searches the left half.
- If the target is greater, it searches the right half.
- This continues until the value is found or the range is empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        print(f"Searching in range [{start}:{end}], middle index = {mid}, middle value = {arr[mid]}")

        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{target} is greater than {arr[mid]}; searching right half")
            start = mid + 1
        else:
            print(f"{target} is less than {arr[mid]}; searching left half")
            end = mid - 1

    print(f"{target} not found in list. It can be inserted at index {start}")
    return -start - 1  # Insertion point encoded as negative value


# Example usage:
target_index = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 11)
print(f"Result index: {target_index}")
