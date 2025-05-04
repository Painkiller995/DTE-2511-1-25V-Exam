
# Big-O Algorithm Complexity Cheat Sheet

This cheat sheet covers the space and time Big-O complexities of common algorithms used in Computer Science. It provides a quick reference for the best, average, and worst-case complexities for search and sorting algorithms.

---

## Big-O Complexity Chart

| Complexity Class | Description |
|------------------|-------------|
| O(1)             | Constant    |
| O(log n)         | Logarithmic |
| O(n)             | Linear      |
| O(n log n)       | Log-linear  |
| O(n²)            | Quadratic   |
| O(2ⁿ)            | Exponential |
| O(n!)            | Factorial   |

---

## Common Data Structure Operations

| Data Structure       | Access | Search | Insertion | Deletion | Space Complexity |
|----------------------|--------|--------|-----------|----------|------------------|
| Array                | O(1)   | O(n)   | O(n)      | O(n)     | O(n)             |
| Stack                | O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| Queue                | O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| Singly-Linked List   | O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| Doubly-Linked List   | O(n)   | O(n)   | O(1)      | O(1)     | O(n)             |
| Skip List            | O(log n)| O(log n)| O(log n) | O(log n) | O(n log n)       |
| Hash Table           | N/A    | O(1)   | O(1)      | O(1)     | O(n)             |
| Binary Search Tree   | O(log n)| O(log n)| O(log n) | O(log n) | O(n)             |
| Cartesian Tree       | N/A    | O(log n)| O(log n) | O(log n) | O(n)             |
| B-Tree               | O(log n)| O(log n)| O(log n) | O(log n) | O(n)             |
| Red-Black Tree       | O(log n)| O(log n)| O(log n) | O(log n) | O(n)             |
| Splay Tree           | N/A    | O(log n)| O(log n) | O(log n) | O(n)             |
| AVL Tree             | O(log n)| O(log n)| O(log n) | O(log n) | O(n)             |
| KD Tree              | O(log n)| O(log n)| O(log n) | O(log n) | O(n)             |

---

## Array Sorting Algorithms

| Algorithm       | Best Case | Average Case | Worst Case | Space Complexity |
|-----------------|-----------|--------------|------------|------------------|
| Quicksort       | O(n log n)| O(n log n)   | O(n²)      | O(log n)         |
| Mergesort       | O(n log n)| O(n log n)   | O(n log n) | O(n)             |
| Timsort         | O(n)      | O(n log n)   | O(n log n) | O(n)             |
| Heapsort        | O(n log n)| O(n log n)   | O(n log n) | O(1)             |
| Bubble Sort     | O(n)      | O(n²)        | O(n²)      | O(1)             |
| Insertion Sort  | O(n)      | O(n²)        | O(n²)      | O(1)             |
| Selection Sort  | O(n²)     | O(n²)        | O(n²)      | O(1)             |
| Tree Sort       | O(n log n)| O(n log n)   | O(n²)      | O(n)             |
| Shell Sort      | O(n log n)| O(n (log n)²)| O(n (log n)²)| O(1)           |
| Bucket Sort     | O(n + k)  | O(n + k)     | O(n²)      | O(n)             |
| Radix Sort      | O(nk)     | O(nk)        | O(nk)      | O(n + k)         |
| Counting Sort   | O(n + k)  | O(n + k)     | O(n + k)   | O(k)             |
| Cubesort        | O(n)      | O(n log n)   | O(n log n) | O(n)             |