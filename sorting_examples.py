# 1. Sorting a list of integers
numbers = [5, 2, 9, 1]
numbers.sort()  # In-place sort
print("Sorted with sort():", numbers)

numbers = [5, 2, 9, 1]
print("Sorted with sorted():", sorted(numbers))

# 2. Sorting a list of floats
floats = [3.1, 2.4, 5.6, 1.0]
print("Floats sorted:", sorted(floats))

# 3. Sorting a list of strings
words = ["banana", "apple", "cherry"]
print("Strings sorted alphabetically:", sorted(words))

# 4. Sorting strings case-insensitively
words = ["Banana", "apple", "Cherry"]
print("Case-insensitive sort:", sorted(words, key=str.lower))

# 5. Sorting a list of tuples by second element
tuples = [(1, "b"), (3, "a"), (2, "c")]
print("Tuples sorted by 2nd element:", sorted(tuples, key=lambda x: x[1]))

# 6. Sorting a list of dictionaries by a key
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]
# Sort by age
sorted_people = sorted(people, key=lambda person: person["age"])
print("Dictionaries sorted by age:", sorted_people)

# 7. Sorting a string (produces a list of characters)
text = "dbca"
print("Sorted string characters:", sorted(text))

# 8. Sorting a set (converted to list first)
my_set = {5, 1, 3, 2}
print("Sorted set:", sorted(my_set))

# 9. Sorting in descending order
numbers = [3, 1, 4, 2]
print("Descending order:", sorted(numbers, reverse=True))

# 10. Sorting complex numbers by their magnitude
complex_numbers = [3 + 4j, 1 + 1j, 0 + 2j]
print("Sorted by magnitude:", sorted(complex_numbers, key=abs))
