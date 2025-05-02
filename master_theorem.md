# Master Theorem (Simplified)

The **Master Theorem** is a tool used in computer science to **quickly find the time complexity** of recursive algorithms, especially **divide-and-conquer** ones.

It helps solve recurrence relations of the form:

```
T(n) = a * T(n/b) + f(n)
```

Where:

* `n` is the size of the problem
* `a` is the number of subproblems
* `n/b` is the size of each subproblem
* `f(n)` is the extra work done outside the recursion (e.g., combining results)

## Cases of the Master Theorem

Let’s compare `f(n)` with `n^log_b(a)`:

### **Case 1: f(n) is smaller**

If:

```
f(n) = O(n^c), where c < log_b(a)
```

Then:

```
T(n) = Θ(n^log_b(a))
```

> Example: `T(n) = 2T(n/2) + n` → `a = 2`, `b = 2`, `f(n) = n`, and `log₂(2) = 1` → case 2.

### **Case 2: f(n) is the same**

If:

```
f(n) = Θ(n^log_b(a))
```

Then:

```
T(n) = Θ(n^log_b(a) * log n)
```

### **Case 3: f(n) is bigger**

If:

```
f(n) = Ω(n^c), where c > log_b(a) and regularity condition holds
```

Then:

```
T(n) = Θ(f(n))
```

---

## Example Problem

```
T(n) = 3T(n/2) + n^2
```

* a = 3
* b = 2
* f(n) = n²
* log₂(3) ≈ 1.58

Since `n²` grows faster than `n^1.58`, and regularity condition is satisfied ⇒ **Case 3**

**Result**:

```
T(n) = Θ(n²)
```