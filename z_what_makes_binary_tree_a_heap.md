# 🌳 What Makes a Binary Tree a Heap?

To qualify as a **heap**, a binary tree must meet **two essential properties**:

---

## ✅ 1. Heap Property

- A **min-heap** requires each node to be **less than or equal to** its children.
- A **max-heap** requires each node to be **greater than or equal to** its children.

This must hold **recursively** throughout the tree.

---

## ✅ 2. Complete Binary Tree

- The tree must be a **complete binary tree**:
  - All levels are **fully filled**, except possibly the **last level**.
  - The last level must be **filled from left to right**.

This structure allows for efficient array representation and predictable node relationships.

---

## ❗Example

```plaintext
       10
      /  \
     15   20
    / \
   30  40
```

- This is a **min-heap**:
  - It is a complete binary tree.
  - Every parent node is ≤ its children.

---

## ✅ Summary

A **binary tree is a heap** if:

1. It is a **complete binary tree**.
2. It satisfies the **heap property**:
   - **Min-heap**: Parent ≤ Children
   - **Max-heap**: Parent ≥ Children
