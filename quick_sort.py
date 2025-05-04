"""
Quick Sort Algorithm

This script implements the Quick Sort algorithm, a highly efficient and commonly used
divide-and-conquer sorting method. It works by selecting a 'pivot' element and partitioning
the array into sub-arrays of elements less than or equal to the pivot and those greater than it.
The sub-arrays are then recursively sorted.

Time Complexity:
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n^2)  (when the pivot selection is poor, e.g., already sorted list)

Space Complexity:
- O(log n) for recursive stack calls (in-place sorting)

Quick Sort is generally faster than Bubble Sort and is widely used in practice.
"""


def quick_sort(array):
    """
    Sorts a list of numbers in ascending order using the Quick Sort algorithm.

    Parameters:
        array (list): The list of numerical values to be sorted.
    """
    start = 0
    end = len(array) - 1
    _quick_sort(array, start, end)


def _quick_sort(array, start, end):
    """
    Recursively sorts subarrays defined by start and end indices.

    Parameters:
        array (list): The list to sort.
        start (int): Starting index of the subarray.
        end (int): Ending index of the subarray.
    """
    if start >= end:
        return

    # Partition the array and get the pivot boundary
    boundary = partition(array, start, end)

    # Recursively sort elements before and after partition
    _quick_sort(array, start, boundary - 1)
    _quick_sort(array, boundary + 1, end)


def partition(array, start, end):
    """
    Partitions the array into two parts around a pivot such that elements
    less than or equal to the pivot are on the left, and greater elements are on the right.

    Parameters:
        array (list): The list to partition.
        start (int): Starting index of the partition segment.
        end (int): Ending index of the partition segment.

    Returns:
        int: The index where the pivot ends up (partition boundary).
    """
    pivot = array[end]
    boundary = start - 1

    for i in range(start, end + 1):
        if array[i] <= pivot:
            boundary += 1
            array[boundary], array[i] = array[i], array[boundary]

    return boundary


def main():
    """
    Demonstrates the usage of the quick_sort function with a sample list.
    """
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    quick_sort(unsorted_numbers)
    print("Sorted list:", unsorted_numbers)


if __name__ == "__main__":
    main()
