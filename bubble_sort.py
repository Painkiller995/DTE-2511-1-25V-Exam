"""
Bubble Sort Algorithm

This script implements the Bubble Sort algorithm, a simple in-place comparison-based
sorting method. It works by repeatedly stepping through the list, comparing adjacent
items and swapping them if they are in the wrong order. This process is repeated until
the list is sorted.

Time Complexity:
- Best Case:    O(n)     (when the list is already sorted)
- Average Case: O(n^2)
- Worst Case:   O(n^2)

Space Complexity:
- O(1), as it sorts the list in place.

Bubble Sort is easy to understand and implement, but it is inefficient on large datasets.
It is primarily used for educational purposes.
"""


def bubble_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters:
        numbers (list): The list of numerical values to be sorted.
    """
    total_elements = len(numbers)
    for pass_index in range(total_elements):
        did_swap = False
        for current_index in range(0, total_elements - pass_index - 1):
            left_element = numbers[current_index]
            right_element = numbers[current_index + 1]

            if left_element > right_element:
                # Swap the adjacent elements
                numbers[current_index], numbers[current_index + 1] = right_element, left_element
                did_swap = True

        # If no swaps occurred during the entire pass, the list is already sorted
        if not did_swap:
            break


def main():
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    bubble_sort(unsorted_numbers)
    print("Sorted list:", unsorted_numbers)


if __name__ == "__main__":
    main()
