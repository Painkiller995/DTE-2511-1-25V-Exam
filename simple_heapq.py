import heapq

# Step 1: Start with a regular list
numbers = [2, 5, 4, 3, 8, 5, 9, 6, 4, 3, 3, 6]
print("Original list:")
print(numbers)

# Step 2: Turn the list into a heap (in-place)
heapq.heapify(numbers)
print("\nList after heapify (min-heap):")
print(numbers)
# Note: It’s not sorted, but now numbers[0] is the smallest!

# Step 3: Push a new element into the heap
print("\nPushing 5 into the heap...")
heapq.heappush(numbers, 5)
print("Heap after pushing 5:")
print(numbers)

# Step 4: Pop the smallest element from the heap
print("\nPopping the smallest element...")
smallest = heapq.heappop(numbers)
print(f"Popped: {smallest}")
print("Heap after popping:")
print(numbers)
