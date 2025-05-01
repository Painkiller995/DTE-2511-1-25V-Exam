"""
Selection Sort Algorithm

This script implements the Selection Sort algorithm, a simple in-place comparison-based
sorting method. It works by repeatedly selecting the smallest element from the unsorted
portion of the list and placing it at the beginning of the sorted portion.

Time Complexity:
- Best Case:    O(n^2)
- Average Case: O(n^2)
- Worst Case:   O(n^2)

Space Complexity:
- O(1), as it sorts the list in place.

Selection Sort is easy to understand but inefficient on large lists. It is primarily used
for educational purposes.
"""


def selection_sort(list_of_numbers):
    """
    Sorts a list of numbers in ascending order using the selection sort algorithm.

    Parameters:
        list_of_numbers (list): The list of numerical values to be sorted.
    """
    total_elements = len(list_of_numbers)
    for current_position in range(total_elements):
        index_of_smallest_value = current_position
        for candidate_index in range(current_position + 1, total_elements):
            if list_of_numbers[candidate_index] < list_of_numbers[index_of_smallest_value]:
                index_of_smallest_value = candidate_index
        # Swap the current element with the smallest found element
        list_of_numbers[current_position], list_of_numbers[index_of_smallest_value] = (
            list_of_numbers[index_of_smallest_value],
            list_of_numbers[current_position],
        )


def main():
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    selection_sort(unsorted_numbers)
    print("Sorted list:", unsorted_numbers)


if __name__ == "__main__":
    main()
