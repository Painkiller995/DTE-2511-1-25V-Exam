"""
Timsort Algorithm with In-Place Merge (Educational Version)

This version improves space efficiency by performing the merge step directly on the input list,
rather than creating new sublists.
"""

MIN_RUN = 32


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        current = arr[i]
        j = i - 1
        while j >= left and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def in_place_merge(arr, left, mid, right):
    """
    Merges two sorted subarrays of arr in-place.
    - First subarray: arr[left..mid]
    - Second subarray: arr[mid+1..right]
    """
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            i += 1
        else:
            # arr[j] should be before arr[i], so shift the subarray
            temp = arr[j]
            # Shift elements from arr[i] to arr[j-1] right by 1
            for k in range(j, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = temp

            # Update pointers
            i += 1
            mid += 1
            j += 1


def timsort(arr):
    n = len(arr)

    # Step 1: Sort small pieces with insertion sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge runs in place
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)

            if mid < right:
                in_place_merge(arr, left, mid, right)

        size *= 2

    return arr


def main():
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    timsort(unsorted_numbers)  # Sorting is done in place
    print("Sorted list:", unsorted_numbers)


if __name__ == "__main__":
    main()
