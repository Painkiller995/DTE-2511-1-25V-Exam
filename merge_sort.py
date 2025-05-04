"""
Merge Sort Algorithm

This script implements the Merge Sort algorithm, a divide-and-conquer sorting method.
Merge Sort works by recursively dividing the list into two halves, sorting each half,
and then merging the sorted halves back together.

Time Complexity:
- Best Case:    O(n log n)
- Average Case: O(n log n)
- Worst Case:   O(n log n)

Space Complexity:
- O(n), as it requires additional memory for merging.

Merge Sort is highly efficient and is commonly used in sorting large datasets due to its
consistent O(n log n) performance.
"""


def merge_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the Merge Sort algorithm.

    Parameters:
        numbers (list): The list of numerical values to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(numbers) <= 1:
        return numbers

    # Split the list into two halves
    middle_index = len(numbers) // 2
    left_half = merge_sort(numbers[:middle_index])
    right_half = merge_sort(numbers[middle_index:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
        left (list): The first sorted sublist.
        right (list): The second sorted sublist.

    Returns:
        list: A merged sorted list.
    """
    sorted_list = []
    left_index, right_index = 0, 0

    # Merge elements from both lists in order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list


def main():
    """
    Demonstrates the usage of the merge_sort function with a sample list.
    """
    unsorted_numbers = [9, 7, 8, 5, 4, 6, 2, 3, 1]
    sorted_numbers = merge_sort(unsorted_numbers)
    print("Sorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
