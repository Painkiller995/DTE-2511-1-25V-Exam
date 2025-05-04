"""
Timsort Algorithm (Simplified Educational Version)

This script implements a simplified version of the Timsort algorithm, which combines
Insertion Sort and Merge Sort. Timsort is used in Python's built-in sort functions
due to its excellent performance on real-world data.

Time Complexity:
- Best Case:    O(n)       (nearly sorted)
- Average Case: O(n log n)
- Worst Case:   O(n log n)

Space Complexity:
- O(n)

This version demonstrates the core idea of using Insertion Sort for small chunks
and Merge Sort to combine them.
"""

MIN_RUN = 32  # A common default used in actual Timsort implementations


def insertion_sort(arr, left, right):
    """
    Sorts a sublist in place using Insertion Sort.

    Parameters:
        arr (list): The full list.
        left (int): Start index of the sublist.
        right (int): End index of the sublist.
    """
    for i in range(left + 1, right + 1):
        current = arr[i]
        j = i - 1
        while j >= left and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Parameters:
        left (list): The left sorted sublist.
        right (list): The right sorted sublist.

    Returns:
        list: Merged sorted list.
    """
    result = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def tim_sort(arr):
    """
    Sorts a list using a simplified version of the Timsort algorithm.

    Parameters:
        arr (list): The list of numerical values to be sorted.

    Returns:
        list: A new sorted list.
    """
    n = len(arr)

    # Step 1: Sort small pieces with Insertion Sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge the sorted runs
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merged = merge(arr[left : mid + 1], arr[mid + 1 : right + 1])
                arr[left : left + len(merged)] = merged
        size *= 2

    return arr


def main():
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    sorted_numbers = tim_sort(unsorted_numbers[:])  # Use a copy to preserve original
    print("Sorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
