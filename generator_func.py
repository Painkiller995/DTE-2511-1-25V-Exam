# Generator function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Yield the current value of count
        count += 1


# Create a generator object
counter = count_up_to(5)

# Iterate through the generator using a for loop
for number in counter:
    print(number)
