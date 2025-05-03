"""
Insertion Sort Algorithm

This script implements the Insertion Sort algorithm, a simple and intuitive
comparison-based sorting technique. It builds the sorted list one element at a time
by repeatedly inserting the next unsorted element into the correct position
among the already sorted elements.

Time Complexity:
- Best Case:    O(n)     (when the list is already sorted)
- Average Case: O(n^2)
- Worst Case:   O(n^2)

Space Complexity:
- O(1), as it sorts the list in place.

Insertion Sort is efficient for small or nearly sorted datasets, and is commonly
used as part of more complex algorithms or for educational purposes.
"""


def insertion_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the Insertion Sort algorithm.

    Parameters:
        numbers (list): The list of numerical values to be sorted.
    """
    total_elements = len(numbers)
    for i in range(1, total_elements):
        current_value = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > current_value:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current_value


def main():
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    insertion_sort(unsorted_numbers)
    print("Sorted list:", unsorted_numbers)


if __name__ == "__main__":
    main()
