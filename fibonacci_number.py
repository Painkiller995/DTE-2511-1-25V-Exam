"""
Fibonacci Number Calculator

This script demonstrates two methods to compute the Fibonacci number at a given index:
1. Recursive approach
2. Iterative approach

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones:
    0, 1, 1, 2, 3, 5, 8, 13, ...

The sequence starts with 0 and 1. The nth Fibonacci number can be calculated either recursively or iteratively.
"""

import time


def fibonacci_recursive(index):
    """
    Calculate the Fibonacci number at the given index using recursion.

    Time Complexity: O(2^n)
    This approach is inefficient for large values of n due to repeated calculations.
    """
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fibonacci_recursive(index - 1) + fibonacci_recursive(index - 2)


def fibonacci_iterative(index):
    """
    Calculate the Fibonacci number at the given index using iteration.

    Time Complexity: O(n)
    This approach is efficient and avoids repeated calculations.
    """
    if index == 0:
        return 0
    if index == 1:
        return 1

    f0, f1 = 0, 1
    for _ in range(2, index + 1):
        f0, f1 = f1, f0 + f1
    return f1


def main():
    index = 30  # Recursive will be slow for large index

    # Time the recursive version
    start_time = time.time()
    result_recursive = fibonacci_recursive(index)
    end_time = time.time()
    recursive_time = end_time - start_time

    print(f"Recursive: Fibonacci number at index {index} is {result_recursive}")
    print(f"Time taken (recursive): {recursive_time:.6f} seconds")

    # Time the iterative version
    start_time = time.time()
    result_iterative = fibonacci_iterative(index)
    end_time = time.time()
    iterative_time = end_time - start_time

    print(f"Iterative: Fibonacci number at index {index} is {result_iterative}")
    print(f"Time taken (iterative): {iterative_time:.6f} seconds")


if __name__ == "__main__":
    main()
